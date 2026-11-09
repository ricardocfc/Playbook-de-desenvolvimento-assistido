---
name: playbook-audit
description: Avalia a conformidade documental e operacional do projeto com a versão instalada do Playbook, encontra lacunas, duplicidades de REQs e de implementações e inconsistências entre código e documentação, e recomenda correções. Use quando o desenvolvedor pedir auditoria, revisão de conformidade ou "verificar se o projeto segue o Playbook". Não corrige nada sozinha.
---

# playbook-audit — Auditoria de conformidade

Executa o COP-01 §16 e §17. As normas são a autoridade; este arquivo é um roteiro.

## Quando consultar as normas
A auditoria é a exceção: para cada achado, confirme a regra na norma antes de registrá-lo. Comece por:
- `docs/playbook/MANIFEST.md` (versão e documentos obrigatórios).
- COP-01 §3 (invariantes), §19 (cenários de teste) e §21 (convenções).
- DEV-12 §19 e §21 (conformidade), DEV-11 (histórico).
Abra os demais documentos apenas para os temas do recorte auditado.

## Autorização
- Ler e inspecionar: permitido.
- Gravar o relatório: conforme autorização.
- Corrigir achados, alterar código ou documentos, publicar: **proibido** sem autorização específica (COP-01 §12).

## Procedimento
1. **Definir o recorte** com o desenvolvedor: projeto inteiro, uma SPEC, uma REQ ou um período.
2. **Instalação:** versão no MANIFEST, documentos obrigatórios presentes, adaptadores apontando para a cópia local sem duplicar normas.
3. **Estrutura (COP-01 §21):** `Specs/`, `Skills/`, `docs/playbook/`; registros operacionais fora de `docs/`.
4. **REQs:** IDs únicos e sequenciais; uma SPEC principal por REQ com justificativa; SPECs associadas com referência e sem cópia de plano; estados coerentes com evidências.
5. **Duplicidades (COP-01 §21.4):** REQs equivalentes ou sobrepostas; funcionalidades implementadas duas vezes.
6. **Evidências:** impactos marcados como validados sem evidência; critérios Aprovados sem método; testes declarados que não aparecem.
7. **Histórico:** `history.md` aditivo, sem reescrita; `spec.md` coerente com o código atual; pendências registradas.
8. **Código x documentação:** divergências relevantes (DEV-09 §18).
9. **Cenários T-01 a T-18 (COP-01 §19)**, quando o recorte for a conformidade das próprias skills.

Separe sempre **fato verificado** de **hipótese**. Cada achado precisa apontar onde foi observado.

## Saída

**Registro.** O bloco abaixo é o conteúdo mínimo que vai para os arquivos do projeto (REQ, sessão, relatório). Nele, identificadores e referências às normas são bem-vindos. **Não cole este bloco na conversa.**

```markdown
## Auditoria — <recorte> — <data>
- Versão do Playbook: <...>
| # | Achado | Tipo (fato/hipótese) | Onde | Regra | Severidade | Recomendação |
|---|---|---|---|---|---|---|
- Severidade: bloqueador / risco relevante / melhoria / oportunidade (DEV-08 §13)
- Limitações da auditoria: <o que não foi possível verificar>
- Próximo passo recomendado: <decisões que o desenvolvedor precisa tomar>
```

**Resposta ao desenvolvedor.** Siga "Como falar com o desenvolvedor" no `AGENTS.md`: palavras comuns, sem códigos de documentos nem nomes de skills. Diga o que foi feito, o que você precisa dele e o que dá para fazer em seguida. Exemplo: "Encontrei 5 pontos: 2 importantes (...) e 3 melhorias. Quer que eu corrija algum?"

## Limites
- Auditoria não é aprovação de publicação nem autorização de alteração (COP-01 §16).
- Não corrija achados fora do escopo, mesmo os simples.
