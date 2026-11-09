# AI Development Playbook — Contrato Operacional das Skills

**Identificador:** COP-01  
**Versão:** 1.1 — consolidação das decisões de implementação aprovadas  
**Status:** Proposta de consolidação v1.1 para conferência editorial; contrato v1.0 e decisões complementares aprovados  
**Abrangência:** Execução operacional da metodologia por agentes e skills, independentemente de plataforma  
**Referências principais:** PROD-02, PROD-04, DEV-04, DEV-05, DEV-06, DEV-09, DEV-10, DEV-11, DEV-12 e DEV-13.

---

## 1. Finalidade e autoridade

Este contrato define interfaces, etapas, estados, evidências e condições de transição comuns às skills do AI Development Playbook. É um **instrumento operacional subordinado** aos documentos normativos aprovados, e não uma fonte normativa concorrente. Em caso de divergência, prevalecem as normas aprovadas e as decisões específicas válidas do projeto, observada a hierarquia de instruções e as políticas da plataforma (DEV-12). Divergências deverão ser comunicadas, não resolvidas silenciosamente.

O contrato não autoriza, por si só, alteração de código, arquivos, dados, infraestrutura, instalação de ferramentas, commit, push, merge ou publicação. Sua adoção, implementação em skills e futuras revisões exigem as aprovações aplicáveis.

## 2. Vocabulário operacional

- **Solicitação:** entrada em linguagem natural apresentada pelo desenvolvedor.
- **Requisição unitária (REQ):** finalidade delimitada extraída de uma solicitação. Uma solicitação pode conter várias REQs; não dividir artificialmente uma única finalidade.
- **SPEC:** agrupamento funcional de jornadas e requisitos, sem substituir a hierarquia **Produto → Funcionalidade → Jornada → Etapas → Requisitos**.
- **SPEC principal:** funcionalidade responsável pela coordenação documental da REQ atual. Definida independentemente para cada REQ.
- **SPEC associada:** funcionalidade relacionada por dependência ou impacto; referencia a REQ e sua SPEC principal sem duplicar registros operacionais.
- **Regra canônica:** regra de negócio documentada em seu domínio funcional responsável.
- **Impacto:** consequência possível ou constatada sobre requisitos, jornadas, regras, código, dados, contratos ou outras SPECs.
- **Evidência:** registro verificável de uma inspeção, decisão, execução ou validação efetivamente realizada.

A convenção aprovada para novos projetos é `REQ-001`, `REQ-002`, etc., com identificadores sequenciais e únicos por projeto; registros preexistentes não devem ser renumerados.

## 3. Invariantes obrigatórias

1. Cada nova REQ deve ser interpretada, contextualizada e classificada por sua finalidade atual; nunca herda automaticamente a SPEC principal de outra REQ.
2. Uma REQ funcional possui **uma** SPEC principal e pode possuir zero ou mais SPECs associadas.
3. Os registros operacionais de uma REQ ficam na SPEC principal; SPECs associadas contêm referências cruzadas e documentação funcional própria atualizada quando aplicável.
4. A localização da documentação não determina a localização do código; as responsabilidades arquiteturais continuam regidas pelo Pilar Arquitetura.
5. A titularidade de uma regra de negócio permanece em sua localização canônica; referências não criam cópias independentes.
6. Impacto **previsto** não significa **implementado**; impacto **implementado** não significa **validado**.
7. Histórico funcional anterior não é apagado ou reescrito para ocultar mudanças posteriores.
8. Nenhuma skill presume aprovação de uma ação apenas porque a etapa anterior terminou.
9. Nenhuma skill declara testes, inspeções, alterações ou resultados que não foram realizados ou verificados.
10. Escopo e profundidade de análise são proporcionais a risco e relevância, conforme DEV-04, DEV-05 e DEV-06.

## 4. Entrada comum e identificação da solicitação

Ao receber uma solicitação, o agente deve identificar: objetivo declarado; resultado esperado; projeto e versão local da metodologia; estado conhecido; informações confirmadas, sugeridas e pendentes; restrições; permissões já concedidas; e eventuais limitações de acesso.

Se a solicitação contiver finalidades independentes, propor a decomposição em REQs distintas. A decomposição deve preservar as relações de dependência e evitar transformar etapas técnicas da mesma finalidade em requisições artificiais. Quando houver ambiguidade relevante, solicitar decisão antes de fixar a classificação.

Uma requisição não funcional ou de manutenção pode exigir tratamento específico conforme as normas aplicáveis; **não se deve inventar uma jornada funcional artificial**. O vínculo obrigatório com jornada aplica-se aos requisitos funcionais, conforme PROD-02.

## 5. Ciclo operacional de uma REQ

O fluxo lógico de uma REQ contém os seguintes marcos, aplicados conforme a natureza da tarefa:

1. **Interpretada:** finalidade e limites compreendidos; dúvidas impeditivas identificadas.
2. **Contextualizada:** versão, estado do projeto, decisões e histórico pertinente recuperados.
3. **Classificada:** SPEC principal proposta ou confirmada, SPECs associadas identificadas quando aplicável, com justificativa.
4. **Impactos analisados:** dependências, riscos, consequências e incertezas registradas.
5. **Especificada:** requisitos, regras, jornadas e critérios pertinentes definidos e aprovados quando exigidos.
6. **Planejada:** abordagem, tarefas, escopo autorizado, verificações e condições de reversão, quando pertinentes.
7. **Em execução:** alterações efetivas sob controle de escopo e autorizações.
8. **Em validação:** resultados e efeitos cruzados confrontados com critérios e evidências.
9. **Concluída:** condições de aceitação atendidas, registros necessários atualizados e estado comunicado.

Esses marcos **não constituem uma máquina de estados rígida universal**: uma REQ pode estar bloqueada, suspensa, parcialmente concluída ou encerrada com ressalvas, conforme DEV-10. Etapas podem ser simplificadas em tarefas de baixo risco, sem suprimir controles obrigatórios. A transição de um marco a outro exige verificar pré-condições e autorizações, e não apenas receber uma saída da skill anterior.

## 6. Registro operacional mínimo por REQ

Quando o projeto utiliza SPECs, manter na SPEC principal um registro rastreável, com campos proporcionais à tarefa:

| Campo | Conteúdo |
|---|---|
| Identificação | ID estável da REQ, título e origem da solicitação |
| Finalidade | Objetivo, resultado esperado e limites |
| Classificação | SPEC principal, SPECs associadas e justificativa |
| Contexto | Estado verificado, regras e REQs relacionadas |
| Produto | Jornadas, requisitos, regras e critérios aplicáveis |
| Impactos | Elementos afetados, natureza, estado, evidências e incertezas |
| Controle | Risco, decisões, autorizações e escopo aprovado |
| Execução | Plano, tarefas, alterações e referências ao Git, quando aplicável |
| Validação | Testes efetivos, resultados, pendências e evidências |
| Encerramento | Estado real, histórico, referências cruzadas e próximos passos |

**Não é obrigatório criar um arquivo para cada campo.** A organização física observará a seção 21 e respeitará o contexto existente. Não se criarão automaticamente planos, listas de tarefas ou modelos redundantes. Os controles mínimos permanecem obrigatórios independentemente do perfil documental.

## 7. Classificação funcional e vínculos entre SPECs

A SPEC principal é definida pela **finalidade da REQ atual**, e não pela primeira SPEC citada, pelo arquivo alterado ou pelo histórico de implementação. A classificação deve considerar a responsabilidade funcional vigente, jornadas e regras canônicas. Se não houver SPEC adequada, propor criação ou ajuste de organização, sujeitos à aprovação aplicável.

A SPEC associada deve permitir localizar a REQ causadora e sua SPEC principal, com identificação da relação. Ela não recebe cópia do plano, tarefas ou histórico operacional da REQ. Mudanças em sua descrição funcional vigente e histórico de evolução, quando cabíveis, são exceções documentais necessárias e não duplicação de execução.

## 8. Matriz de impactos e evolução de estado

Para cada impacto relevante, distinguir duas dimensões:

- **Natureza:** direto, indireto, potencial ou não identificado (DEV-04).
- **Estado de tratamento:** previsto, implementado, validado ou não confirmado (DEV-04).

Registrar, conforme aplicável: origem da REQ, elemento afetado, SPEC afetada, comportamento anterior, mudança esperada, natureza, estado, risco, verificação requerida e evidência. Não declarar impacto como validado sem evidência. Se um impacto previsto não se confirmar, registrar o resultado e sua justificativa, sem apresentá-lo como alteração funcional ocorrida.

## 9. Autorizações e limites

As skills devem distinguir claramente **analisar**, **propor**, **aprovar**, **executar**, **validar** e **publicar**. O agente pode investigar por leitura quando autorizado e disponível, mas não interpreta autorização de leitura como autorização de escrita. Classificação de risco, autorizações por escopo, exceções e operações sensíveis seguem DEV-05 e DEV-06.

Uma aprovação de especificação não é autorização implícita para implementar. Uma implementação concluída não é autorização implícita para commit, push, merge ou deploy. Mudanças fora do escopo exigem reavaliação e autorização quando aplicável.

## 10. Artefatos funcionais e histórico

Em projetos organizados por SPECs:

- `spec.md` representa o comportamento funcional **vigente** da funcionalidade, com referência à regra canônica de outro domínio quando necessário.
- `history.md` preserva a **evolução funcional** em registros aditivos, inclusive mudanças causadas por REQs de outras SPECs.
- Os registros operacionais da REQ atual ficam centralizados na SPEC principal.
- O Git permanece a fonte primária para mudanças no código; decisões arquiteturais e handoffs mantêm seus próprios registros apropriados.

Após implementação **e validação** de alteração funcional cruzada, atualizar os `history.md` das SPECs afetadas e ajustar seus `spec.md` quando necessário, dentro do escopo autorizado. Antes disso, manter impactos como previstos, implementados não validados ou pendentes, conforme evidências. Se o trabalho terminar sem atualização autorizada, registrar a pendência explicitamente.

## 11. Contrato entre skills

Toda skill deve receber ou recuperar informações suficientes para verificar o estado real da tarefa. Nenhuma skill deve confiar cegamente no status informado pela anterior; deve validar os pré-requisitos relevantes, consultar a documentação canônica e comunicar divergências.

A saída de cada skill deve informar, proporcionalmente: finalidade atendida; REQ(s) abrangida(s); SPEC principal e associadas quando aplicável; decisões e aprovações; artefatos criados ou alterados; verificações realizadas; impactos e pendências; próximo passo **recomendado**, sem dispará-lo automaticamente.

As skills podem compartilhar um contrato comum, mas não devem duplicar integralmente as normas nem manter definições concorrentes de estados, classificação ou rastreabilidade.

## 12. Responsabilidade de cada skill

| Skill | Responsabilidade | Limite de transição |
|---|---|---|
| `playbook-init` | Identificar instalação, ler documentos obrigatórios, preparar adaptadores conforme autorização e diagnosticar o projeto | Concluir a inicialização **não inicia** automaticamente `playbook-spec` |
| `playbook-spec` | Interpretar solicitação, decompor REQs, recuperar contexto funcional, classificar SPECs e especificar comportamentos | Não implementar nem presumir aprovação de requisitos |
| `playbook-plan` | Analisar impactos, riscos, dependências, escopo, tarefas e verificações | Não executar plano sem autorização aplicável |
| `playbook-implement` | Executar mudanças autorizadas, preservando escopo e estado do projeto | Não declarar validação ou publicação automaticamente |
| `playbook-review` | Verificar conformidade, critérios, testes, evidências e impactos cruzados | Não declarar testes não executados nem aprovar em nome do desenvolvedor |
| `playbook-handoff` | Registrar estado real, pendências, rastreabilidade e continuidade | Não transformar encerramento em autorização para novas operações |
| `playbook-audit` | Avaliar conformidade documental e operacional, identificar lacunas e recomendações | Não corrigir ou publicar automaticamente achados fora de escopo |

As responsabilidades acima integram o contrato operacional aprovado; detalhes de interface e integração com plataformas serão validados na implementação, sem alterar as competências normativas dos documentos aprovados.

## 13. Inicialização: fronteira explícita

A inicialização aplica DEV-08 e DEV-12: verificar a versão local instalada, ler integralmente os documentos obrigatórios na primeira inicialização, inspecionar o projeto conforme disponibilidade, preparar ou propor adaptadores e relatar limitações. A ausência de documento obrigatório impede declarar a inicialização concluída.

A conclusão ou aprovação de `playbook-init` **encerra somente a inicialização**. O agente pode recomendar `playbook-spec` como próximo passo, mas não a aciona automaticamente. Uma nova solicitação do desenvolvedor deverá indicar a finalidade subsequente; a execução respeitará as autorizações aplicáveis.

## 14. Especificação e planejamento

`playbook-spec` deve preservar o vínculo dos requisitos funcionais às jornadas e critérios de aceitação (PROD-02 e PROD-04), registrar informações confirmadas, sugeridas e pendentes e identificar ambiguidades. Antes de registrar nova REQ, deve pesquisar REQs potencialmente equivalentes ou sobrepostas, observando objetivo, escopo, estado e critérios de aceitação. A classificação da SPEC principal deve ser justificada por finalidade. Equivalência pode levar ao aproveitamento da REQ existente, sem ampliação silenciosa de escopo; finalidade independente exige REQ própria, ainda que relacionada a outra.

`playbook-plan` deve analisar consumidores, contratos, dados, integrações, jornadas e REQs anteriores pertinentes (DEV-04), classificar risco e delimitar escopo (DEV-05 e DEV-06). Deve verificar planejamento já aproveitável e definir documentação proporcional ao risco e à complexidade. A proposta de plano deve distinguir impactos previstos de alterações confirmadas e prever validações proporcionais.

## 15. Implementação e revisão

`playbook-implement` deve verificar autorização, estado real do repositório e se a capacidade solicitada já existe antes de escrever, evitar mudanças desnecessárias e reavaliar risco se descobrir efeitos novos. Deve registrar o que de fato mudou, sem confundir implementação com validação.

`playbook-review` deve confrontar critérios de aceitação e efeitos cruzados com evidências de testes, inspeções e verificações efetivamente executados. Falhas, testes indisponíveis e impactos não confirmados devem ser comunicados. Aprovação funcional humana, quando exigida, não pode ser substituída por autodeclaração do agente.

## 16. Encerramento, retomada e auditoria

`playbook-handoff` deve seguir DEV-10: informar concluído, concluído com ressalvas, parcialmente concluído, bloqueado ou não iniciado; registrar alterações, Git, testes, decisões, pendências e próxima ação. Em REQs entre SPECs, verificar referências cruzadas, estados de impacto e atualizações de `spec.md` e `history.md` pertinentes.

`playbook-audit` deve inspecionar conformidade com a versão instalada, inclusive duplicidades de REQs e de implementações, produzir achados rastreáveis, separar fatos de hipóteses e recomendar correções. Auditoria não é aprovação de publicação nem autorização de alteração. A retomada em outra sessão aplica DEV-09 e deve reconfrontar os registros com o estado atual do projeto.

## 17. Interrupções, divergências e exceções

Se houver documentos ausentes, divergências entre código e documentação, mudanças concorrentes, autorização insuficiente ou impactos desconhecidos relevantes, o agente deverá comunicar a limitação, indicar o que foi verificado e classificar o trabalho adequadamente. Não deve ocultar a divergência nem forçar conclusão.

Quando uma nova descoberta ampliar o escopo, propor reclassificação de risco, ajuste de plano ou nova REQ se houver finalidade independente. Não dividir artificialmente uma única REQ nem modificar SPECs afetadas fora do escopo autorizado.

## 18. Independência de plataforma e distribuição

O contrato deverá ser representado em formato portátil, consultável a partir da cópia local versionada do Playbook. `CLAUDE.md`, `AGENTS.md` e outros adaptadores devem apontar para a metodologia local e para o contrato operacional aprovado, sem duplicar integralmente suas regras. Não presumir que ferramentas, hooks ou mecanismos de execução de uma plataforma existem em outra.

A distribuição e atualização seguem DEV-12: versão aprovada, instalação local controlada, sem atualização automática. A adoção de ferramentas especializadas segue DEV-07 e sua orquestração segue DEV-13.

## 19. Cenários mínimos de teste de conformidade

| ID | Cenário | Resultado esperado |
|---|---|---|
| T-01 | Inicialização concluída e aprovada | Nenhum acionamento automático de `playbook-spec` |
| T-02 | Prompt contém duas finalidades independentes | Duas REQs classificadas independentemente, sem divisão artificial |
| T-03 | Nova REQ altera regra anteriormente implementada em outra SPEC | SPEC principal definida pela finalidade atual, sem herança histórica |
| T-04 | REQ em Financeiro muda vencimento de faturas criadas em Clientes | Registros operacionais em Financeiro; impacto e evolução funcional em Clientes após validação |
| T-05 | Impacto previsto não confirmado | Não declarar mudança implementada ou validada; registrar conclusão da investigação |
| T-06 | Código alterado, testes não executados | Estado de implementação separado de validação; pendência explícita |
| T-07 | Pedido de alteração fora do escopo | Reavaliação e autorização antes de executar |
| T-08 | Sessão interrompida com atualização de `history.md` pendente | Handoff com estado real, referência à SPEC e pendência documentada |
| T-09 | Agente novo assume REQ iniciada por outro | Recuperar contexto e verificar estado atual, sem presumir resultados anteriores |
| T-10 | Skill executada em plataforma sem recurso especializado | Alternativa compatível ou limitação comunicada, sem simular capacidade |
| T-11 | SPEC associada possui regra canônica própria | Referenciar regra, sem duplicá-la na SPEC principal |
| T-12 | Aprovação de especificação, sem autorização de implementação | Não iniciar mudanças no código |
| T-13 | Solicitação já coberta por REQ aberta, no mesmo escopo | Reutilizar a REQ e preservar controles, sem criar duplicata |
| T-14 | Solicitação parcialmente coberta por REQ aberta | Propor extensão autorizada ou nova REQ, sem alterar escopo silenciosamente |
| T-15 | Nova demanda independente semelhante a REQ concluída | Criar REQ própria, com referência à anterior |
| T-16 | REQ simples e de baixo risco | Registro único suficiente, sem `plan.md`/`tasks.md` artificiais |
| T-17 | REQ complexa com múltiplas dependências | Plano e tarefas separados quando justificados, com referências e evidências |
| T-18 | Autorização cobre especificação e planejamento, não implementação | Executar apenas etapas autorizadas; parar antes da implementação |

Os testes deverão ser executados e documentados antes de considerar as skills prontas para distribuição; esta tabela define expectativas, não evidências de testes já realizados.

## 20. Critérios de aceite do contrato

A proposta poderá ser aprovada quando:

1. Não contrariar nenhuma norma vigente nem redefinir responsabilidades dos três pilares.
2. Preservar a classificação independente de cada REQ e a centralização documental na SPEC principal.
3. Distinguir regras canônicas, registros operacionais e evolução funcional.
4. Diferenciar impacto previsto, implementado e validado.
5. Tornar explícitas autorizações e fronteiras entre skills.
6. Prever retomada, pendências, auditoria e validação proporcional.
7. Permanecer aplicável a Claude Code, Codex e outros agentes sem dependência obrigatória de fornecedor.
8. Ser aprovado pelo desenvolvedor antes de ser tratado como referência operacional vigente.

## 21. Convenções de implementação aprovadas

As convenções desta seção foram aprovadas pelo responsável pela metodologia após a aprovação do contrato v1.0. Integram a proposta de consolidação v1.1, sem substituir as normas dos três pilares.

### 21.1. Estrutura de diretórios e distribuição

Os projetos terão três diretórios distintos na raiz, respeitando maiúsculas e minúsculas conforme a convenção aprovada:

- `Specs/`: especificações funcionais, requisições, históricos funcionais e registros de transferência de sessões.
- `Skills/`: sete skills operacionais, cada uma com seu `SKILL.md` e arquivos auxiliares somente quando necessários.
- `docs/`: pacote normativo da metodologia, em `docs/playbook/`, incluindo `docs/playbook/operacional/COP-01.md`.

Adaptadores `AGENTS.md`, `CLAUDE.md` ou equivalentes ficam na raiz quando aplicáveis e apontam para a cópia normativa local. O diretório `docs/` não receberá os registros operacionais do produto. A localização canônica de `Skills/` não pressupõe que todos os agentes a descubram automaticamente; integrações específicas devem referenciar essa fonte sem manter cópias normativas divergentes.

### 21.2. Identificadores, propriedade e registros

Cada REQ formalizada receberá identificador estável e sequencial por projeto (`REQ-001`, `REQ-002`...), com verificação de unicidade e sem renumeração retroativa. A REQ fica vinculada à SPEC principal definida por sua finalidade atual. SPECs associadas mantêm referências cruzadas, não cópias de planejamento e tarefas. A identificação e classificação independentes não obrigam criar uma REQ nova se a demanda já estiver integralmente coberta por uma REQ existente.

### 21.3. Documentação progressiva

A documentação de uma REQ será proporcional à complexidade, risco, dependências e necessidade de rastreabilidade. Os perfis abaixo são **orientativos**, não limites rígidos:

| Perfil | Organização usual | Critério |
|---|---|---|
| Simples | `requests/REQ-xxx.md` | Um registro atende ao escopo, tarefas, autorizações, validação e encerramento |
| Intermediário | `requests/REQ-xxx/request.md` e `tasks.md` | Tarefas merecem acompanhamento próprio, mas não há justificativa para plano técnico separado |
| Complexo | `requests/REQ-xxx/request.md`, `plan.md` e `tasks.md` | Decisões técnicas, dependências, riscos ou estratégia exigem plano explícito |

A avaliação é contextual: alteração pequena pode ser de alto risco, e alteração extensa pode ser tecnicamente simples. A skill `playbook-plan` justifica os artefatos necessários; não cria arquivos vazios. Em todos os perfis, os registros operacionais continuam na SPEC principal, sem duplicação entre `request.md`, `plan.md` e `tasks.md`.

`spec.md` e `history.md` permanecem na raiz da SPEC, como referências de comportamento vigente e evolução funcional. Planos e tarefas de REQs distintas não serão acumulados indefinidamente em arquivos únicos na raiz da SPEC. Os arquivos de REQs encerradas permanecem consultáveis, sem exigência de leitura integral em toda sessão.

### 21.4. Verificação prévia de equivalência de requisições

Antes de registrar nova REQ, `playbook-spec` deverá pesquisar requisições existentes potencialmente equivalentes ou sobrepostas, comparando finalidade, escopo, critérios de aceitação, estado e evidências do comportamento vigente. A pesquisa será proporcional: localizar SPECs relevantes, examinar resumos e referências disponíveis e aprofundar apenas as candidatas. Não é obrigatória a leitura integral de todas as REQs do projeto.

- **Já atendida e validada:** indicar a implementação existente; não criar duplicata sem nova finalidade identificável.
- **Integralmente coberta por REQ aberta:** aproveitar o registro existente, respeitando escopo e autorizações.
- **Parcialmente coberta:** propor ampliação autorizada ou REQ independente, conforme finalidade e impactos.
- **Finalidade ou abrangência própria:** criar nova REQ e registrar relação com as anteriores quando relevante.

A ampliação de escopo não é automática. `playbook-plan` verifica planos e tarefas aproveitáveis; `playbook-implement` verifica capacidade já implementada; `playbook-audit` pode identificar duplicidades residuais. Um eventual índice resumido de REQs poderá ser avaliado na implementação, **sem obrigatoriedade de criação nesta versão** e sem se tornar fonte concorrente.

### 21.5. Validação, handoff e histórico

- Evidências de implementação e validação pertencem à REQ principal e podem apontar para artefatos externos verificáveis.
- `Specs/<SPEC>/spec.md` descreve comportamento funcional vigente; `history.md` preserva evolução funcional aditiva.
- Handoffs gerais de sessão ficam em `Specs/sessions/`, referenciando REQs sem duplicar seus registros.
- Git mantém o histórico de alterações de código e não substitui os registros funcionais.

### 21.6. Automação supervisionada

Consultas e análises permitidas podem ocorrer sem aprovação repetitiva. Etapas subsequentes podem ser executadas em sequência **somente quando abrangidas por autorização explícita e escopo definido**, após conferência de pré-requisitos. Ampliação de escopo, decisão pendente e operação sensível exigem autorização específica. Aprovação da inicialização não inicia `playbook-spec`; aprovação de especificação e planejamento não implica permissão para implementar. Ações como commit, push, merge e deploy observam suas autorizações próprias.

### 21.7. Exemplo de organização

```text
projeto/
├── Specs/
│   ├── SPEC-010-clientes/
│   │   ├── spec.md
│   │   ├── history.md
│   │   └── requests/
│   │       ├── REQ-001.md
│   │       ├── REQ-002/
│   │       │   ├── request.md
│   │       │   └── tasks.md
│   │       └── REQ-003/
│   │           ├── request.md
│   │           ├── plan.md
│   │           └── tasks.md
│   └── sessions/
├── Skills/
│   ├── playbook-init/SKILL.md
│   ├── playbook-spec/SKILL.md
│   ├── playbook-plan/SKILL.md
│   ├── playbook-implement/SKILL.md
│   ├── playbook-review/SKILL.md
│   ├── playbook-handoff/SKILL.md
│   └── playbook-audit/SKILL.md
├── docs/
│   └── playbook/
│       ├── produto/
│       ├── arquitetura/
│       ├── desenvolvimento/
│       └── operacional/COP-01.md
├── AGENTS.md           # Quando aplicável
├── CLAUDE.md           # Quando aplicável
└── src/
```

O exemplo não obriga criar SPECs ou REQs ilustrativas. O uso de `Specs/`, `Skills/` e `docs/` na raiz constitui a convenção aprovada para novos projetos; adaptações em projetos existentes devem respeitar o controle de mudanças.

## 22. Controle de versão e incorporação

Esta revisão consolida decisões operacionais aprovadas após o contrato v1.0: estrutura de diretórios, identificação de REQs, organização de skills, persistência, automação supervisionada, documentação progressiva e verificação de equivalência. A consolidação não implica execução de migrações em projetos existentes nem alteração automática dos documentos normativos.

**Estado do artefato:** consolidação v1.1 preparada para conferência e incorporação ao pacote versionado. O contrato v1.0 e as decisões aqui consolidadas já foram aprovados; a publicação do arquivo revisado e sua substituição na cópia oficial ainda dependem da etapa de incorporação.
