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
