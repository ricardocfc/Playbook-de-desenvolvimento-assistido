# DEV-11 — Histórico de Desenvolvimento e Rastreabilidade das Decisões

**Pilar:** 03 — Desenvolvimento  
**Versão:** 1.1 — revisão proposta  
**Status:** Revisão normativa em validação — versão 1.0 preservada  
**Aplicação:** Todos os projetos desenvolvidos com a metodologia.

---

## 1. Objetivo

Estabelecer procedimentos para registrar, organizar, consultar e preservar o histórico relevante de desenvolvimento de um projeto.

O histórico deverá permitir compreender como o sistema evoluiu, quais decisões foram tomadas, por que determinadas abordagens foram escolhidas e quais consequências precisam ser consideradas em futuras intervenções.

A metodologia deverá preservar rastreabilidade sem produzir documentação redundante ou excessiva.

## 2. Princípio fundamental

**O projeto deverá preservar o conhecimento necessário para compreender suas decisões e sua evolução, sem depender exclusivamente da memória de agentes, conversas ou desenvolvedores individuais.**

O registro deverá ser proporcional à relevância do acontecimento.

## 3. Finalidades do histórico

O histórico deverá permitir:

- Recuperar decisões anteriores.
- Compreender alterações relevantes.
- Investigar regressões.
- Identificar requisitos relacionados.
- Consultar justificativas técnicas.
- Recuperar classificações de risco.
- Conhecer limitações existentes.
- Evitar repetição de análises.
- Facilitar a continuidade entre agentes.
- Apoiar manutenção e evolução.
- Identificar decisões substituídas.
- Preservar evidências relevantes de validação.

## 4. Tipos de registros

O projeto poderá preservar diferentes tipos de registros.

### Histórico de implementação

Mudanças relevantes realizadas no código e no comportamento do sistema.

### Decisões arquiteturais

Escolhas estruturais, alternativas e justificativas, conforme o ARQ-04.

### Decisões de produto

Alterações relevantes em jornadas, requisitos, regras de negócio e critérios de aceitação.

### Classificações de risco

Decisões e precedentes aprovados conforme o DEV-05.

### Registros de sessão

Informações de continuidade produzidas conforme o DEV-10.

### Registros de incidentes

Problemas relevantes, causas identificadas, correções e medidas preventivas.

### Decisões sobre ferramentas

Adoção, substituição, restrições ou descontinuação de recursos especializados, conforme o DEV-07.

Cada informação deverá ser mantida no registro mais adequado, evitando duplicação integral entre documentos.

## 5. O que merece registro permanente

O agente deverá priorizar acontecimentos que possam influenciar decisões futuras.

Exemplos:

- Implementação de funcionalidade relevante.
- Mudança de regra de negócio.
- Alteração de contrato compartilhado.
- Decisão arquitetural.
- Migração de dados.
- Correção de defeito crítico.
- Mudança de autenticação ou autorização.
- Alteração de integração externa.
- Adoção de ferramenta relevante.
- Classificação de risco recorrente.
- Descoberta de limitação importante.
- Substituição de abordagem anteriormente aprovada.

Pequenos ajustes sem consequências relevantes poderão permanecer documentados apenas no histórico do Git ou no registro de sessão.

## 6. O que não precisa ser registrado separadamente

O agente deverá evitar criar registros permanentes para:

- Cada comando executado.
- Cada arquivo consultado.
- Pequenas correções de formatação.
- Ajustes triviais sem impacto.
- Tentativas temporárias sem consequência.
- Informações já disponíveis integralmente em registros apropriados.

A ausência de um registro separado não deverá comprometer a rastreabilidade necessária.

## 7. Estrutura mínima de um registro

Um registro relevante deverá conter, conforme aplicável:

1. Identificação.
2. Data.
3. Tipo de acontecimento.
4. Contexto.
5. Problema ou necessidade.
6. Decisão ou alteração.
7. Justificativa.
8. Consequências.
9. Elementos afetados.
10. Referências relacionadas.
11. Estado atual.
12. Responsável pela decisão, quando pertinente.

O formato deverá ser simples e compreensível.

## 8. Identificadores e referências

Registros relevantes poderão receber identificadores estáveis.

Exemplos:

- `ADR-001` — Decisão arquitetural.
- `PR-RISCO-001` — Precedente de classificação de risco.
- `INC-001` — Incidente relevante.
- `MUD-001` — Mudança significativa.

Os identificadores deverão facilitar referências cruzadas.

O projeto não precisará adotar todas essas categorias se não houver necessidade.

## 9. Rastreabilidade entre produto e implementação

Sempre que aplicável, o agente deverá preservar a relação entre:

**Perfil de usuário → Jornada → Etapa → Requisito → Regra de negócio → Critério de aceitação → Implementação → Validação.**

Essa rastreabilidade deverá respeitar o PROD-02 e o PROD-04.

Uma alteração funcional relevante deverá permitir identificar os requisitos que a justificam.

A metodologia não deverá exigir que toda linha de código possua referência individual a um requisito.

## 10. Relação com o Git

O histórico do Git deverá ser utilizado como fonte primária para identificar alterações no código.

Os registros de desenvolvimento deverão complementar o Git, explicando informações que não estejam suficientemente representadas nos commits.

O agente deverá evitar duplicar listas extensas de arquivos ou alterações já facilmente consultáveis no repositório.

Quando útil, os registros poderão referenciar:

- Commits.
- Branches.
- Pull Requests.
- Issues.
- Releases.
- Versões.

As referências deverão ser verificáveis quando possível.

## 11. Registro de decisões

Decisões relevantes deverão preservar:

- Contexto.
- Alternativas consideradas.
- Escolha realizada.
- Justificativa.
- Consequências.
- Restrições.
- Estado da decisão.

O agente deverá distinguir:

**Proposta:** ainda não aprovada.

**Aprovada:** decisão válida.

**Substituída:** decisão anteriormente válida que foi superada.

**Revogada:** decisão que deixou de ser aplicável.

O histórico não deverá apagar decisões antigas apenas porque foram substituídas.

## 12. Registro de precedentes de risco

As classificações de risco aprovadas deverão ser preservadas conforme o DEV-05.

Cada precedente deverá informar:

- Situação analisada.
- Classificação recomendada.
- Classificação aprovada.
- Justificativa.
- Condições de aplicação.
- Controles necessários.
- Exceções.
- Responsável pela decisão.

O agente deverá consultar precedentes relevantes antes de solicitar novamente uma classificação ambígua.

### Exemplo

**PR-RISCO-001 — Alteração aditiva em componente compartilhado**

Classificação aprovada: baixo risco.

Aplicação: inclusão de propriedade opcional em componente de tabela compartilhado, preservando o comportamento anterior por padrão, sem alteração de contratos críticos e com validação dos consumidores relevantes.

A classificação deverá ser reavaliada quando essas condições não forem atendidas.

## 13. Registro de problemas e incidentes

Problemas relevantes poderão possuir registros específicos.

O registro deverá considerar:

- Sintoma.
- Impacto.
- Contexto.
- Causa identificada, quando conhecida.
- Correção realizada.
- Verificações.
- Medidas preventivas.
- Pendências.

O agente não deverá apresentar hipóteses como causas confirmadas.

## 14. Histórico de ferramentas especializadas

Quando uma ferramenta relevante for adotada, o projeto deverá preservar informações suficientes para compreender a decisão.

Poderá registrar:

- Nome e finalidade.
- Versão adotada.
- Fonte.
- Motivo da escolha.
- Alternativas consideradas.
- Permissões concedidas.
- Restrições.
- Avaliação de segurança realizada.
- Custos conhecidos.
- Estado de utilização.

Esse registro deverá complementar o catálogo definido no DEV-07.

## 15. Organização dos registros

O projeto deverá adotar uma organização simples e previsível.

Uma estrutura possível seria:

`docs/historico/`

`docs/decisoes/`

`docs/incidentes/`

`docs/riscos/`

Essa estrutura é ilustrativa.

O agente deverá respeitar as convenções existentes e não deverá criar diretórios desnecessários.

## 16. Fonte de verdade

Cada categoria de informação deverá possuir uma referência principal.

Exemplos:

- Código: repositório.
- Histórico de alterações: Git.
- Requisitos: documentação de produto.
- Decisões arquiteturais: registros de arquitetura.
- Precedentes de risco: registros de classificação.
- Estado da última sessão: registro de transferência.
- Recursos especializados: catálogo de ferramentas.

Quando informações forem referenciadas em diferentes documentos, deverá ser preferível utilizar links ou identificadores em vez de copiar integralmente seu conteúdo.

## 17. Atualização e manutenção

O agente deverá recomendar a atualização de registros quando:

- Uma decisão for modificada.
- Uma funcionalidade relevante evoluir.
- Uma limitação for resolvida.
- Uma ferramenta for substituída.
- Um risco deixar de existir.
- Um precedente perder validade.
- Um incidente for encerrado.

A atualização deverá preservar o histórico necessário para compreender a evolução.

## 18. Consulta contextual

O agente deverá consultar o histórico conforme a tarefa.

Exemplos:

- Alteração arquitetural: consultar ADRs relacionados.
- Mudança em componente compartilhado: consultar decisões e precedentes pertinentes.
- Correção de defeito recorrente: consultar incidentes anteriores.
- Alteração de requisito: consultar jornadas e decisões de produto.
- Adoção de ferramenta: consultar o catálogo e avaliações anteriores.

O agente não deverá carregar indiscriminadamente todo o histórico em cada sessão.

## 19. Divergências entre registros

Quando encontrar informações contraditórias, o agente deverá:

1. Identificar as fontes.
2. Verificar datas e estados.
3. Consultar evidências disponíveis.
4. Determinar se existe decisão posterior válida.
5. Apresentar ambiguidades não resolvidas.
6. Solicitar esclarecimento quando necessário.

Não deverá escolher silenciosamente uma informação apenas por estar em um documento mais recente.

## 20. Preservação de decisões humanas

Decisões aprovadas pelo desenvolvedor deverão ser registradas de forma fiel.

O agente não deverá reinterpretar uma decisão para ampliar seu alcance.

Também não deverá apresentar recomendações próprias como se fossem decisões humanas aprovadas.

Quando houver divergência entre a recomendação da IA e a escolha do desenvolvedor, o registro deverá preservar essa distinção quando relevante.

## 21. Independência de plataforma

Os registros deverão utilizar formatos acessíveis e portáveis sempre que possível.

O projeto não deverá depender exclusivamente de funcionalidades de memória de um assistente específico.

Ferramentas externas poderão complementar o histórico, desde que as informações necessárias à continuidade permaneçam acessíveis aos agentes autorizados.

## 22. Segurança dos registros

O histórico não deverá armazenar indevidamente:

- Senhas.
- Tokens.
- Chaves privadas.
- Segredos de integração.
- Dados pessoais desnecessários.
- Informações confidenciais sem proteção adequada.

Quando necessário, deverá referenciar o local seguro onde uma configuração é gerenciada, sem reproduzir seu conteúdo sensível.

## 23. Critérios de conformidade

O DEV-11 estará sendo respeitado quando:

- Decisões relevantes forem preservadas.
- O histórico permitir compreender a evolução do projeto.
- Registros forem proporcionais à importância.
- O Git for utilizado como referência para alterações de código.
- Requisitos e implementações possuírem rastreabilidade adequada.
- Precedentes de risco forem consultáveis.
- Decisões substituídas permanecerem identificáveis.
- Fontes de verdade forem claras.
- Informações duplicadas forem minimizadas.
- Registros contraditórios forem tratados adequadamente.
- Informações sensíveis forem protegidas.
- Diferentes agentes conseguirem recuperar o contexto necessário.

## 24. Relação com os demais documentos

### PROD-02 — Requisitos e Jornadas

Define a rastreabilidade funcional.

### PROD-04 — Critérios de Aceitação

Relaciona requisitos às evidências de validação.

### ARQ-04 — Decisões Arquiteturais

Define o registro e a evolução das escolhas estruturais.

### DEV-01 — Versionamento e Git

Preserva o histórico técnico das alterações de código.

### DEV-05 — Gestão de Mudanças

Define o registro e a reutilização de precedentes de risco.

### DEV-07 — Recursos Especializados

Define o catálogo e a avaliação de ferramentas.

### DEV-09 — Consultoria Contínua

Utiliza o histórico para recuperar contexto.

### DEV-10 — Encerramento de Sessão

Produz registros operacionais que alimentam a continuidade.

### DEV-12 — Instruções Permanentes

Orienta os agentes sobre onde consultar e atualizar os registros.

## 25. Histórico de evolução funcional entre SPECs

Nos projetos que adotarem a organização operacional por SPEC, o arquivo `spec.md` deverá representar o **comportamento funcional vigente** de sua funcionalidade. O arquivo `history.md` deverá preservar a **evolução funcional**, incluindo mudanças provocadas por requisições cuja SPEC principal seja diferente.

Cada requisição unitária terá uma única SPEC principal para centralizar sua especificação, planejamento, tarefas, validação e histórico operacional. As SPECs associadas deverão conter apenas referências de localização e os ajustes necessários para que sua descrição funcional permaneça correta. Isso não impede que o histórico funcional de uma SPEC afetada receba um registro de impacto proveniente de outra SPEC.

Quando uma nova requisição alterar comportamento definido anteriormente:

1. A nova requisição será registrada e executada em sua própria SPEC principal, definida independentemente conforme PROD-02.
2. A documentação da nova requisição identificará as requisições e SPECs anteriores afetadas e registrará os impactos previstos, conforme DEV-04.
3. Após a alteração ser efetivamente implementada e validada, o `history.md` de cada SPEC funcionalmente afetada receberá um registro **aditivo** de evolução, referenciando a nova requisição e sua SPEC principal.
4. O `spec.md` afetado será atualizado, quando necessário, para descrever o comportamento vigente ou referenciar a regra canônica em outra SPEC, sem duplicá-la.
5. O histórico anterior será preservado; não deverá ser reescrito para fazer parecer que a nova regra sempre esteve vigente.

Cada registro de evolução funcional deverá conter, conforme aplicável: identificador da requisição causadora; SPEC principal da requisição; funcionalidade e requisição anterior afetadas; comportamento anterior; comportamento vigente ou mudança esperada; natureza e estado do impacto; data ou versão; referências às decisões e às evidências de implementação e validação; e eventuais pendências.

**Impacto previsto** não equivale a alteração implementada. **Impacto implementado** não equivale a impacto validado. Enquanto a mudança não estiver validada, o agente não deverá apresentá-la como comportamento vigente confirmado; deverá explicitar o estado real e as incertezas.

A atualização de `spec.md` e `history.md` em SPECs afetadas integra a análise de escopo da nova requisição e depende da autorização aplicável, conforme DEV-05 e DEV-06. Não constitui uma segunda execução da requisição nem autoriza alterações técnicas fora do escopo.

O `history.md` é fonte de evolução funcional e de relações entre requisições; **não substitui** o Git como fonte primária do histórico de alterações de código, os registros de decisões arquiteturais nem o registro de transferência de sessão. Quando a estrutura por SPEC não estiver adotada, o agente deverá respeitar as convenções existentes e preservar esses mesmos princípios de fonte de verdade e rastreabilidade.

## 26. Regra fundamental

**O histórico de desenvolvimento deverá preservar decisões, mudanças e acontecimentos relevantes de maneira organizada, rastreável e proporcional, permitindo que qualquer agente autorizado compreenda a evolução do projeto e tome decisões fundamentadas sem depender exclusivamente da memória de conversas anteriores.**