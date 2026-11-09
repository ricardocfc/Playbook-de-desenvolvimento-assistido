---
name: playbook-review
description: Confronta a implementação de uma REQ com os critérios de aceitação, impactos cruzados e evidências de testes efetivamente executados, e classifica cada critério. Use depois de playbook-implement, ou quando o desenvolvedor pedir para revisar ou validar uma REQ. Não aprova em nome do desenvolvedor.
---

# playbook-review — Revisão e validação

Executa o COP-01 §8 e §15. As normas são a autoridade; este arquivo é um roteiro.

## Quando consultar as normas
Para baixo risco, este roteiro basta. Abra a norma só quando:
- Validar jornada completa, permissões, estados ou exceções → PROD-04 §7 a §10.
- Definir que evidência é suficiente → PROD-04 §13 e DEV-05 §18.
- Concluir uma funcionalidade inteira → PROD-04 §16.
- Houver impactos em outras SPECs → DEV-04 §20 e DEV-11 §25.

Caminhos: `docs/playbook/produto/` e `docs/playbook/desenvolvimento/`.

## Pré-requisitos (verifique, não presuma)
- Leia o diff real e o estado do repositório. O relato do `playbook-implement` não é evidência (COP-01 §11).
- Localize os critérios de aceitação da REQ e os impactos registrados.

## Proporcionalidade
- **Trilha curta:** verifique o que a alteração pode afetar (inspeção, build, testes existentes da área) e registre o resultado na seção Validação do próprio `REQ-NNN.md`, em poucas linhas. Os passos 3 e 4 abaixo só se aplicam se houver jornada ou impacto cruzado.
- **Trilha completa:** siga todos os passos.

## Procedimento
1. **Escopo:** compare o diff com o escopo autorizado. Alteração fora dele é achado, mesmo que pareça boa.
2. **Critérios de aceitação:** para cada um, execute ou inspecione a verificação prevista e classifique (PROD-04 §14):
   Não verificado, Aprovado, Reprovado, Bloqueado, Não aplicável.
3. **Jornadas, permissões, estados e exceções** cobertos pela REQ (PROD-04 §7 a §10).
4. **Impactos cruzados:** para cada impacto da REQ, decida o estado com base em evidência:
   - validado → há evidência concreta;
   - implementado não validado → mudou, mas falta verificação;
   - não confirmado → investigado e não se materializou; registre a conclusão sem apresentá-lo como mudança ocorrida (T-05).
5. **Evidências (PROD-04 §13):** critério, método, resultado, data, ambiente, limitações. Vincule a testes, logs ou PR quando possível.
6. **Registrar** os resultados na seção Validação da REQ.
7. **Apresentar ao desenvolvedor** em linguagem acessível (PROD-04 §15) e pedir a aprovação funcional quando exigida.

## Saída

```markdown
## Revisão — <REQ-NNN> <título>
- Escopo: <conforme / desvios>
- Critérios: <n Aprovados, n Reprovados, n Bloqueados, n Não verificados>
| Critério | Método | Resultado | Evidência |
|---|---|---|---|
- Impactos: <validados / implementados não validados / não confirmados>
- Testes não executados e motivo: <lista ou "nenhum">
- Falhas e pendências: <lista>
- Aprovação humana necessária: <sim/não, o quê>
- Próximo passo recomendado: <corrigir via playbook-implement | playbook-handoff>
```

## Limites
- Não declare testes não executados nem aprove em nome do desenvolvedor (COP-01 §12).
- Falta de ferramenta de teste não permite presumir que um critério passou (PROD-04 §13).
- Revisão não autoriza commit, merge ou deploy.
- Atualizar `spec.md` e `history.md` das SPECs afetadas acontece **após** validação, dentro do escopo autorizado (COP-01 §10). Se não houver autorização, registre como pendência.
