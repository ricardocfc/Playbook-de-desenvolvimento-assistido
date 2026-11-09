---
name: playbook-plan
description: Analisa impactos, dependências e risco de uma REQ já especificada, define o escopo autorizado, as tarefas, as verificações e a documentação proporcional. Use depois de playbook-spec e antes de qualquer implementação de risco médio ou alto. Não executa o plano.
---

# playbook-plan — Impactos, risco e planejamento

Executa o COP-01 §8, §9, §14 e §21.3. As normas são a autoridade; este arquivo é um roteiro.

## Quando consultar as normas
Esta skill só roda na trilha completa (risco médio ou alto), então consulte de forma dirigida:
- Classificação de risco com dúvida entre níveis → DEV-05 §4, §8 e §9.
- Precedente de risco aplicável → DEV-05 §12.
- Análise de impactos → DEV-04 §4 a §12; profundidade pelo §14; impactos entre SPECs pelo §20.
- Contrato de implementação → DEV-06 §7 e §8.
- Mudança em estrutura, componente compartilhado ou decisão arquitetural → ARQ-01 a ARQ-04, na seção do tema.
- Estratégia de branch → DEV-02 §6 a §9.
- Risco alto → leia DEV-05 §7 inteiro antes de propor o plano.

Caminhos: `docs/playbook/desenvolvimento/` e `docs/playbook/arquitetura/`.

## Quando esta skill é dispensada
Na **trilha curta** (baixo risco evidente, definido pelo `playbook-spec`), não rode esta skill: a REQ simples já contém escopo, tarefas e critérios. Se durante a implementação o risco subir, a REQ volta para cá (DEV-05 §15).

## Pré-requisitos (verifique, não presuma)
- A REQ existe em `Specs/<SPEC>/requests/` e seus requisitos estão Confirmados ou as pendências estão explícitas.
- Releia o estado real do repositório; a saída de `playbook-spec` não é prova do estado atual (COP-01 §11).

## Autorização
- Analisar e propor: permitido.
- Gravar o plano em `Specs/`: conforme autorização.
- Executar qualquer parte do plano: **proibido** nesta skill.

## Procedimento

1. **Precedentes de risco.** Consulte `docs/decisoes/precedentes-de-risco.md`, se existir. Use um precedente só se o contexto for equivalente (DEV-05 §12).
2. **Analisar impactos (DEV-04).** Ponto de alteração, consumidores, contratos, dados, integrações externas, jornadas e REQs anteriores. Profundidade proporcional ao risco.
3. **Classificar cada impacto em duas dimensões (COP-01 §8):**
   - natureza: direto, indireto, potencial, não identificado;
   - estado: previsto (é o estado de todo impacto nesta fase).
   "Não identificado" não é garantia de ausência de risco.
4. **Classificar o risco (DEV-05):** baixo, médio ou alto, com justificativa pelos critérios do §4. Se houver dúvida real entre níveis, pergunte ao desenvolvedor apresentando recomendação, alternativas e consequências (§9).
5. **Escopo (DEV-06):** o que pode ser modificado, o que deve ser preservado, o que fica fora. Melhorias fora do escopo viram recomendação, não tarefa.
6. **Escolher a documentação proporcional (COP-01 §21.3)** e justificar:
   - Simples → mantém `requests/REQ-NNN.md`;
   - Intermediário → `requests/REQ-NNN/request.md` + `tasks.md`;
   - Complexo → `request.md` + `plan.md` + `tasks.md`.
   Não crie arquivos vazios nem planos artificiais (T-16). Use os modelos em `templates/`.
7. **Planejar (DEV-05 §17):** abordagem, tarefas, isolamento (branch quando médio ou alto), verificações por critério de aceitação, recuperação ou reversão (alto risco), autorizações necessárias.
8. **Decisão arquitetural?** Se a mudança exige uma, proponha um ADR em `docs/decisoes/` com `templates/adr.md` (estado: Proposta).
9. **Contrato de implementação (DEV-06 §7)** para risco médio ou alto: apresente-o e peça aprovação.

## Saída

```markdown
## Plano — <REQ-NNN> <título>
- Risco: <nível> — <justificativa> | Precedente usado: <nenhum / referência>
- Impactos previstos: <tabela resumida: elemento, SPEC, natureza>
- Escopo autorizado proposto: modificar <...>; preservar <...>; fora do escopo <...>
- Documentação: <simples / intermediária / complexa> — <motivo>
- Tarefas: <lista curta>
- Verificações: <por critério de aceitação>
- Reversão: <quando aplicável>
- Autorizações necessárias: <aprovar plano; branch; commit; ...>
- Próximo passo recomendado: playbook-implement, **após aprovação**
```

## Limites
- Não execute o plano sem autorização aplicável (COP-01 §12, T-18).
- Aprovar o plano não autoriza commit, push, merge ou deploy (DEV-05 §13).
- Se a análise revelar finalidade independente, proponha nova REQ em vez de inflar esta (COP-01 §17).
