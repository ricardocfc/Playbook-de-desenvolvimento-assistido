---
name: playbook-spec
description: Interpreta uma solicitação do desenvolvedor, decompõe em requisições (REQ), verifica REQs equivalentes, classifica a SPEC principal e especifica requisitos e critérios de aceitação. Faz a triagem de risco que decide entre a trilha curta e a completa. Use quando chegar um pedido de funcionalidade, mudança ou correção que ainda não tem REQ registrada. Não implementa.
---

# playbook-spec — Interpretação e especificação

Executa o COP-01 §4, §7 e §14 e as seções 21.2 a 21.4. As normas são a autoridade; este arquivo é um roteiro.

## Quando consultar as normas
Para baixo risco, este roteiro basta. Abra a norma, na seção indicada, só quando a situação pedir:
- Pedido define produto novo ou funcionalidade sem SPEC → PROD-01 (entrevista de descoberta) e PROD-02 §3 a §12.
- Dúvida sobre SPEC principal ou associadas → PROD-02 §18 e COP-01 §7.
- Critérios de aceitação de jornada com vários perfis, permissões ou estados → PROD-04 §5 a §10.
- Possível REQ equivalente ou sobreposta → COP-01 §21.4.
- Risco médio ou alto → leia as seções acima antes de registrar.

Caminhos: `docs/playbook/produto/` e `docs/playbook/operacional/COP-01-contrato-operacional.md`.

## Autorização
- Ler, pesquisar e propor: permitido.
- Criar ou alterar arquivos em `Specs/`: conforme autorização do desenvolvedor. Sem ela, apresente o conteúdo proposto.
- Implementar, planejar execução, alterar código: **proibido** nesta skill.

## Procedimento

1. **Identificar a solicitação (COP-01 §4):** objetivo, resultado esperado, restrições, permissões já dadas, informações confirmadas, sugeridas e pendentes.
2. **Decompor em REQs.** Uma REQ por finalidade independente. Não divida etapas técnicas da mesma finalidade em REQs artificiais (T-02). Demanda não funcional ou de manutenção não ganha jornada inventada.
3. **Verificar equivalência antes de criar (COP-01 §21.4).** Procure em `Specs/*/spec.md`, `Specs/*/history.md` e `Specs/*/requests/` REQs com finalidade, escopo ou critérios parecidos. Aprofunde só nas candidatas.
   - Já atendida e validada → aponte a implementação; não crie duplicata.
   - Coberta por REQ aberta → reutilize a REQ (T-13).
   - Parcialmente coberta → proponha ampliação autorizada ou REQ nova; nunca amplie em silêncio (T-14).
   - Finalidade própria → REQ nova, com referência às anteriores (T-15).
4. **Classificar a SPEC principal pela finalidade atual**, não pela SPEC citada primeiro, pelo arquivo alterado ou pelo histórico (T-03). Identifique SPECs associadas e justifique. Se nenhuma SPEC servir, proponha criar `Specs/SPEC-NNN-nome/`.
   - **Regra canônica em outra SPEC (T-04):** quando a necessidade nasce num domínio (ex.: Financeiro quer mudar o vencimento) e a regra afetada é canônica em outra SPEC (ex.: Clientes), a SPEC principal é a do domínio que motivou a mudança. A SPEC dona da regra entra como associada: a regra continua canônica lá, e seu `spec.md`/`history.md` só é atualizado após validação. Não escolha a SPEC principal apenas por ser a dona da regra. Se não estiver claro qual domínio motivou o pedido, pergunte.
5. **Atribuir o ID.** Encontre o maior `REQ-NNN` existente em todo `Specs/` e use o seguinte. IDs são únicos no projeto e nunca renumerados.
6. **Especificar (PROD-02, PROD-04):** jornada e etapas afetadas, requisitos, regras de negócio (referencie a regra canônica de outra SPEC em vez de copiá-la, T-11), estados, exceções e critérios de aceitação verificáveis no formato Dado/Quando/Então.
7. **Classificar cada informação:** Confirmado, Sugerido, Pendente ou Descartado. Só requisito Confirmado segue para implementação.
8. **Triagem de risco e escolha da trilha (DEV-05 §4 e §5).** Faça uma classificação preliminar:
   - **Trilha curta:** baixo risco evidente (alteração localizada, reversível, sem dados críticos, autenticação, contratos ou componentes compartilhados). A REQ fica em um único `REQ-NNN.md`, com tarefas e critérios no próprio arquivo, e segue direto para `playbook-implement`, sem `playbook-plan`.
   - **Trilha completa:** risco médio ou alto, ou qualquer dúvida entre níveis. Segue para `playbook-plan`, que confirma o risco.
   Na dúvida, escolha a trilha completa. A triagem não dispensa as autorizações do projeto.
9. **Registrar.** Use `templates/req-simples.md` para começar. `playbook-plan` decide depois se a REQ vira pasta com `request.md`, `plan.md` e `tasks.md`. Em SPEC nova, use `templates/spec.md` e `templates/history.md`.
10. **SPECs associadas:** adicione apenas referência cruzada à REQ e à SPEC principal; não copie plano, tarefas nem registro operacional (COP-01 §7).

## Saída

```markdown
## Especificação — <REQ-NNN> <título>
- Finalidade: <objetivo e limites>
- Equivalência verificada: <REQs consultadas e conclusão>
- SPEC principal: <SPEC> (justificativa) | Associadas: <lista ou nenhuma>
- Requisitos: <confirmados / sugeridos / pendentes>
- Critérios de aceitação: <CA-01..>
- Artefatos criados ou alterados: <caminhos, ou "propostos, aguardando autorização">
- Decisões pendentes: <lista>
- Risco preliminar e trilha: <baixo → curta | médio/alto ou dúvida → completa> — <justificativa>
- Próximo passo recomendado: playbook-implement (trilha curta) | playbook-plan (trilha completa)
```

## Limites
- Não implemente nem presuma aprovação de requisitos (COP-01 §12).
- Aprovação da especificação **não autoriza** implementar (T-12).
- Ambiguidade relevante na classificação → pergunte antes de fixar.
