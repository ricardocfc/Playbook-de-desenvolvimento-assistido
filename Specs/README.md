# Specs

Registros funcionais e operacionais do projeto (COP-01 §21).

```text
Specs/
├── SPEC-NNN-nome/          # uma pasta por funcionalidade
│   ├── spec.md             # comportamento vigente
│   ├── history.md          # evolução funcional, só aditiva
│   └── requests/
│       ├── REQ-001.md      # REQ simples: um arquivo
│       └── REQ-002/        # REQ intermediária ou complexa
│           ├── request.md
│           ├── plan.md     # só quando justificado
│           └── tasks.md
└── sessions/               # handoffs de sessão (AAAA-MM-DD-assunto.md)
```

- IDs de REQ são sequenciais e únicos no projeto inteiro (`REQ-001`, `REQ-002`...), nunca renumerados.
- Os registros de uma REQ ficam na sua SPEC principal. SPECs associadas recebem só referências.
- Modelos: `.claude/skills/playbook-spec/templates/`, `.claude/skills/playbook-plan/templates/`, `.claude/skills/playbook-handoff/templates/`.
- Não crie SPECs ou REQs de exemplo; elas nascem das solicitações reais.
