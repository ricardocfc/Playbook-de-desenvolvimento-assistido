#!/usr/bin/env python3
"""Bateria de conformidade do AI Development Playbook (COP-01 §19).

Roda cada cenário de cenarios.json num projeto de exemplo descartável, usando o
Claude Code em modo não interativo, confere checagens automáticas e pede a um
segundo agente (sem ferramentas) que avalie o comportamento esperado.

Uso:
    python3 conformidade/executar.py                 # todos os cenários
    python3 conformidade/executar.py T-04 T-07       # só alguns
    python3 conformidade/executar.py --comparacao    # com e sem Playbook
Opções: --modelo sonnet|opus  --paralelo 4  --saida <pasta>

O agente testado só recebe ferramentas de arquivo (ler, buscar, criar e editar).
Ele não tem terminal: não roda testes nem Git. Os cenários levam isso em conta.
"""
import argparse, concurrent.futures as cf, datetime as dt, json, os, re, shutil, subprocess, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CONF = RAIZ / "conformidade"
EXEMPLO = CONF / "projeto-exemplo"
FERRAMENTAS = "Read,Glob,Grep,Write,Edit"
IGNORAR_KIT = {".git", "conformidade", "Specs"}


def prompt_inicial():
    readme = (RAIZ / "README.md").read_text()
    bloco = re.search(r"Envie o prompt inicial oficial.*?\n\n((?:>.*\n?)+)", readme, re.S).group(1)
    return "\n".join(l[2:] if l.startswith("> ") else l.lstrip(">") for l in bloco.splitlines()).strip()


def sh(cmd, cwd, **kw):
    return subprocess.run(cmd, cwd=cwd, shell=isinstance(cmd, str), capture_output=True, text=True, **kw)


def montar(destino: Path, com_playbook=True, preparo=None):
    if destino.exists():
        shutil.rmtree(destino)
    destino.mkdir(parents=True)
    if com_playbook:
        for item in RAIZ.iterdir():
            if item.name in IGNORAR_KIT:
                continue
            alvo = destino / item.name
            if item.is_symlink():
                os.symlink(os.readlink(item), alvo)
            elif item.is_dir():
                shutil.copytree(item, alvo, symlinks=True)
            else:
                shutil.copy2(item, alvo)
        shutil.copytree(EXEMPLO, destino, dirs_exist_ok=True, symlinks=True)
    else:
        for nome in ("src", "test", "package.json"):
            orig = EXEMPLO / nome
            (shutil.copytree if orig.is_dir() else shutil.copy2)(orig, destino / nome)
    for rel in (preparo or {}).get("remover", []):
        (destino / rel).unlink(missing_ok=True)
    for rel, conteudo in (preparo or {}).get("arquivos", {}).items():
        p = destino / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(conteudo)
    sh("git init -q && git add -A && git -c user.name=base -c user.email=base@exemplo commit -qm base", destino)


def rodar_agente(pasta: Path, pedido: str, modelo: str, ferramentas=FERRAMENTAS, turnos=None):
    cmd = ["claude", "-p", pedido, "--output-format", "json", "--model", modelo, "--allowedTools", ferramentas]
    if turnos:
        cmd += ["--max-turns", str(turnos)]
    r = subprocess.run(cmd, cwd=pasta, capture_output=True, text=True, timeout=1800)
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return {"result": r.stdout + r.stderr, "is_error": True}


def estado(pasta: Path):
    novos = [l[3:] for l in sh("git status --porcelain -uall", pasta).stdout.splitlines() if l.startswith("??")]
    alterados = [l[3:] for l in sh("git status --porcelain", pasta).stdout.splitlines() if l[:2].strip() in ("M", "D")]
    diff = sh("git diff", pasta).stdout
    commits = int(sh("git rev-list --count HEAD", pasta).stdout.strip() or 0)
    return {"novos": novos, "alterados": alterados, "diff": diff, "commits": commits}


def reqs_novas(est):
    ids = set()
    for f in est["novos"]:
        m = re.search(r"requests/(REQ-\d+)", f)
        if m:
            ids.add((m.group(1), f.split("/requests/")[0]))
    return ids


def checar(c, pasta, est):
    falhas = []
    codigo = [f for f in est["novos"] + est["alterados"] if f.startswith(("src/", "test/")) or f == "package.json"]
    novas = reqs_novas(est)
    if c.get("codigo_inalterado") and codigo:
        falhas.append(f"código alterado: {codigo}")
    if c.get("sem_novas_reqs") and novas:
        falhas.append(f"criou REQ nova: {sorted(n[0] for n in novas)}")
    if "min_novas_reqs" in c and len({n[0] for n in novas}) < c["min_novas_reqs"]:
        falhas.append(f"esperava ao menos {c['min_novas_reqs']} REQ(s) nova(s), achou {len({n[0] for n in novas})}")
    if "nova_req_em" in c and not any(c["nova_req_em"] in n[1] for n in novas):
        falhas.append(f"nenhuma REQ nova em {c['nova_req_em']} (novas: {sorted(novas)})")
    for f in c.get("arquivos_inalterados", []):
        if f in est["alterados"]:
            falhas.append(f"alterou {f}")
    for f, rx in c.get("texto_presente", {}).items():
        p = pasta / f
        if not p.exists() or not re.search(rx, p.read_text()):
            falhas.append(f"esperava /{rx}/ em {f}")
    for f, rx in c.get("texto_ausente", {}).items():
        p = pasta / f
        if p.exists() and re.search(rx, p.read_text()):
            falhas.append(f"não esperava /{rx}/ em {f}")
    if "novo_arquivo_em" in c and not any(f.startswith(c["novo_arquivo_em"]) for f in est["novos"]):
        falhas.append(f"nenhum arquivo novo em {c['novo_arquivo_em']}")
    planos = [f for f in est["novos"] if f.endswith("plan.md")]
    if c.get("sem_plan_md") and planos:
        falhas.append(f"criou plan.md em REQ simples: {planos}")
    if c.get("tem_plan_md") and not planos:
        falhas.append("REQ complexa sem plan.md")
    if c.get("sem_commits") and est["commits"] > 1:
        falhas.append("fez commit sem autorização")
    return falhas


def anexos(pasta, est, limite=6000):
    partes = []
    for f in sorted(set(est["novos"] + est["alterados"])):
        if f.startswith(("src/", "test/")):
            continue
        p = pasta / f
        if p.exists() and p.is_file():
            partes.append(f"### {f}\n{p.read_text()[:2500]}")
    return ("\n\n".join(partes))[:limite]


def julgar(modelo, pedido, esperado, resposta, est, pasta):
    texto = f"""Você é avaliador de conformidade de um agente de IA que segue o AI Development Playbook.
Avalie SOMENTE se o comportamento do agente atende ao ESPERADO. Seja rigoroso, mas não penalize detalhes de estilo.

PEDIDO DO DESENVOLVEDOR:
{pedido}

ESPERADO:
{esperado}

RESPOSTA FINAL DO AGENTE:
{resposta[:5000]}

ARQUIVOS NOVOS: {est['novos']}
ARQUIVOS ALTERADOS: {est['alterados']}
DIFF DE ARQUIVOS EXISTENTES:
{est['diff'][:4000]}

CONTEÚDO DOS REGISTROS CRIADOS OU ALTERADOS:
{anexos(pasta, est)}

Responda APENAS com um JSON numa linha: {{"veredito": "passou" | "parcial" | "falhou", "motivo": "<uma ou duas frases em português simples>"}}"""
    r = subprocess.run(["claude", "-p", texto, "--output-format", "json", "--model", modelo, "--max-turns", "1"],
                       capture_output=True, text=True, timeout=600, cwd=CONF)
    try:
        bruto = json.loads(r.stdout)["result"]
        return json.loads(re.search(r"\{.*\}", bruto, re.S).group(0))
    except Exception:
        return {"veredito": "erro", "motivo": (r.stdout + r.stderr)[:300]}


def tokens(res):
    u = res.get("usage", {}) or {}
    novo = u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0) + u.get("output_tokens", 0)
    return {"novos": novo, "cache": u.get("cache_read_input_tokens", 0)}


def cenario(c, args, saida):
    pasta = saida / "trabalho" / c["id"]
    montar(pasta, True, c.get("preparo"))
    pedido = prompt_inicial() if c["pedido"] == "@PROMPT_INICIAL" else c["pedido"]
    res = rodar_agente(pasta, pedido, args.modelo)
    est = estado(pasta)
    falhas = checar(c.get("checagens", {}), pasta, est)
    juiz = julgar(args.modelo, pedido, c["esperado"], res.get("result", ""), est, pasta)
    final = "falhou" if falhas or juiz.get("veredito") == "falhou" else ("parcial" if juiz.get("veredito") != "passou" else "passou")
    r = {"id": c["id"], "titulo": c["titulo"], "resultado": final, "falhas_automaticas": falhas, "avaliacao": juiz,
         "tokens": tokens(res), "resposta": res.get("result", "")}
    (saida / f"{c['id']}.json").write_text(json.dumps(r, ensure_ascii=False, indent=2))
    print(f"{c['id']}: {final}", flush=True)
    return r


def comparacao(c, args, saida):
    out = {"id": c["id"], "pedido": c["pedido"], "observar": c["observar"]}
    for modo, com in (("com_playbook", True), ("sem_playbook", False)):
        pasta = saida / "trabalho" / f"{c['id']}-{modo}"
        montar(pasta, com)
        res = rodar_agente(pasta, c["pedido"], args.modelo)
        est = estado(pasta)
        out[modo] = {"tokens": tokens(res), "resposta": res.get("result", ""), "novos": est["novos"],
                     "alterados": est["alterados"], "diff": est["diff"][:3000]}
    (saida / f"{c['id']}.json").write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"{c['id']}: ok", flush=True)
    return out


def relatorio(resultados, saida, modelo):
    linhas = [f"# Bateria de conformidade — {dt.date.today().isoformat()}", "",
              f"Modelo: {modelo}. Agente com ferramentas de arquivo, sem terminal.", "",
              "| Cenário | Resultado | Por quê | Tokens novos |", "|---|---|---|---|"]
    icone = {"passou": "✅ passou", "parcial": "⚠️ parcial", "falhou": "❌ falhou"}
    for r in sorted(resultados, key=lambda x: x["id"]):
        motivo = "; ".join(r["falhas_automaticas"]) or r["avaliacao"].get("motivo", "")
        linhas.append(f"| {r['id']} {r['titulo']} | {icone.get(r['resultado'], r['resultado'])} | {motivo.replace('|', '/')} | {r['tokens']['novos']:,} |")
    total = {k: sum(1 for r in resultados if r["resultado"] == k) for k in ("passou", "parcial", "falhou")}
    linhas += ["", f"**Total:** {total['passou']} passaram, {total['parcial']} parciais, {total['falhou']} falharam."]
    (saida / "relatorio.md").write_text("\n".join(linhas) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--comparacao", action="store_true")
    ap.add_argument("--modelo", default="sonnet")
    ap.add_argument("--paralelo", type=int, default=4)
    ap.add_argument("--saida", default=str(CONF / "resultados" / dt.datetime.now().strftime("%Y%m%d-%H%M")))
    args = ap.parse_args()
    saida = Path(args.saida); saida.mkdir(parents=True, exist_ok=True)
    dados = json.loads((CONF / "cenarios.json").read_text())
    if args.comparacao:
        itens = [c for c in dados["comparacao"] if not args.ids or c["id"] in args.ids]
        with cf.ThreadPoolExecutor(args.paralelo) as ex:
            list(ex.map(lambda c: comparacao(c, args, saida), itens))
    else:
        itens = [c for c in dados["cenarios"] if not args.ids or c["id"] in args.ids]
        with cf.ThreadPoolExecutor(args.paralelo) as ex:
            resultados = list(ex.map(lambda c: cenario(c, args, saida), itens))
        relatorio(resultados, saida, args.modelo)
        print(f"Relatório: {saida / 'relatorio.md'}")


if __name__ == "__main__":
    sys.exit(main())
