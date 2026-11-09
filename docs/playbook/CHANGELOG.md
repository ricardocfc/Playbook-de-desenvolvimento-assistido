# Changelog

## 1.0.0 — 2026-11-09

Primeira distribuição.

- Normas aprovadas: PROD-01 a PROD-04, ARQ-01 a ARQ-04, DEV-01 a DEV-13 e COP-01, organizadas em `docs/playbook/`.
- DEV-11 §15 e DEV-12 §20 alinhados à estrutura de pastas do COP-01 §21.
- Decisões, incidentes e riscos do projeto passam a ficar em `docs/decisoes/`, `docs/incidentes/` e `docs/riscos/`.
- Sete skills operacionais em `Skills/`, com modelos de SPEC, histórico, REQ, plano, tarefas, ADR e handoff.
- Adaptadores `AGENTS.md` e `CLAUDE.md`, e integração do Claude Code via `.claude/skills/`.
- Trilha curta para baixo risco (spec → implement em um único `REQ-NNN.md`) e trilha completa para médio e alto risco.
- Skills indicam a seção exata da norma a consultar e quando, em vez de listar documentos inteiros.

## 1.0.1 — 2026-11-09

- `playbook-spec`: regra para SPEC principal quando a regra afetada é canônica em outra SPEC (T-04).
- `playbook-review`: atualizar a tabela de impactos com o novo estado e a evidência (T-05).
- Modelos de REQ ganham o campo "REQs relacionadas" (T-15).
- Bateria de conformidade com os 18 cenários do COP-01 em `conformidade/`.

## 1.0.2 — 2026-11-09

Ajustes do primeiro piloto (Windows, download em ZIP).

- `.claude/skills/` passa a ser cópia real de `Skills/` em vez de links simbólicos, que viravam arquivos de texto no Windows e em downloads ZIP.
- `CHANGELOG.md` movido para `docs/playbook/`; `.gitignore` da bateria movido para `conformidade/`.
- README e `playbook-init` orientam a deixar de fora `README.md` da distribuição e `conformidade/`.
- `playbook-audit` confere se `.claude/skills/` está idêntica a `Skills/`.
- COP-01 §21: caminho real do arquivo (`COP-01-contrato-operacional.md`); §22: estado atualizado para aprovado e incorporado.
- DEV-06 §14: `PR-RISCO-001` deixa claro que é exemplo de precedente registrado no projeto.

## 1.0.3 — 2026-11-09

Comunicação em linguagem comum com o desenvolvedor.

- `AGENTS.md`: nova seção "Como falar com o desenvolvedor". O agente não cita códigos de normas, nomes de skills nem termos internos na conversa; essas referências ficam nos arquivos de registro.
- Todas as skills: a seção Saída separa o **registro** (vai para os arquivos, com referências às normas) da **resposta ao desenvolvedor** (palavras comuns, com exemplo).
- `playbook-init`: o relatório de inicialização é gravado em `Specs/sessions/` quando autorizado.
- Bateria de conformidade: checagem automática que reprova respostas com códigos de normas ou nomes de skills.
- Correções pendentes da 1.0.2: versão no MANIFEST, `CHANGELOG.md` da raiz removido e menções a links simbólicos trocadas por "cópia de `Skills/`".
