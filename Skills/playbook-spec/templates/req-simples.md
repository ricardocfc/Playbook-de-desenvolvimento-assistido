# REQ-NNN — <Título>

> Perfil **simples**: um único registro cobre escopo, tarefas, autorizações, validação e encerramento (COP-01 §21.3).
> Se a REQ crescer, `playbook-plan` converte em `requests/REQ-NNN/request.md` (+ `tasks.md`, + `plan.md`) sem duplicar conteúdo.

| Campo | Valor |
|---|---|
| Estado | Interpretada |
| Origem | <solicitação do desenvolvedor, data> |
| SPEC principal | <SPEC-NNN> — <justificativa pela finalidade> |
| SPECs associadas | <nenhuma / SPEC-XXX (relação)> |
| REQs relacionadas | <REQ-XXX (relação: depende de / estende / semelhante a) ou nenhuma> |
| Risco (DEV-05) | <baixo / médio / alto> — <justificativa> |

Estados possíveis (COP-01 §5): Interpretada, Contextualizada, Classificada, Impactos analisados, Especificada, Planejada, Em execução, Em validação, Concluída; ou Bloqueada, Suspensa, Parcialmente concluída, Concluída com ressalvas.

## Finalidade
<Objetivo, resultado esperado e limites. O que **não** faz parte.>

## Contexto
- REQs relacionadas e verificação de equivalência: <REQ-XXX: conclusão>
- Regras e decisões aplicáveis: <...>

## Produto
- Jornadas/etapas: <...>
- Requisitos: <RF-xx (Confirmado/Sugerido/Pendente)>
- Critérios de aceitação: <CA-xx>

## Impactos
| Elemento | SPEC | Natureza | Estado | Evidência |
|---|---|---|---|---|
| <...> | <...> | direto / indireto / potencial / não identificado | previsto / implementado / validado / não confirmado | <...> |

## Controle
- Escopo autorizado: <...>
- Autorizações obtidas: <quem, quando, para quê>
- Autorizações pendentes: <commit, push, merge, deploy...>

## Tarefas
- [ ] <tarefa>

## Validação
| Critério | Método | Resultado | Data | Ambiente | Limitações |
|---|---|---|---|---|---|
| CA-01 | <...> | Não verificado / Aprovado / Reprovado / Bloqueado / Não aplicável | | | |

## Encerramento
- Estado real: <...>
- `history.md` e `spec.md` atualizados: <sim / pendente (motivo)>
- Git: <branch, commits, PR>
- Próximo passo: <...>
