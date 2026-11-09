# DEV-06 — Intervenção Mínima e Controle do Escopo de Implementação

**Pilar:** 03 — Desenvolvimento  
**Versão:** 1.0  
**Status:** Proposta para aprovação  
**Aplicação:** Todos os projetos desenvolvidos com a metodologia.

---

## 1. Objetivo

Estabelecer procedimentos para delimitar o alcance das intervenções realizadas pelos agentes de IA, garantindo que as modificações sejam necessárias, justificadas e compatíveis com a solicitação aprovada.

A metodologia deverá permitir investigações técnicas abrangentes sem autorizar automaticamente alterações em todos os elementos analisados.

Também deverá preservar a capacidade consultiva do agente, permitindo identificar e recomendar melhorias fora do escopo sem executá-las indevidamente.

## 2. Princípio fundamental

**O agente deverá investigar tudo o que for necessário para compreender a tarefa, mas modificar apenas o que for necessário e autorizado para executá-la corretamente.**

A intervenção mínima não significa produzir a menor quantidade possível de linhas de código.

Significa evitar alterações desnecessárias, preservar comportamentos existentes e limitar o alcance da implementação ao objetivo aprovado.

## 3. Responsabilidades do agente

O agente deverá:

- Compreender a solicitação e o resultado esperado.
- Identificar a funcionalidade responsável pelo comportamento.
- Consultar requisitos, jornadas e decisões relevantes.
- Investigar os arquivos e módulos necessários.
- Avaliar dependências e impactos.
- Delimitar o escopo de implementação.
- Distinguir elementos analisados de elementos modificados.
- Justificar alterações adicionais necessárias.
- Preservar comportamentos não relacionados.
- Evitar refatorações oportunistas não autorizadas.
- Recomendar melhorias identificadas fora do escopo.
- Reavaliar o escopo quando surgirem novas informações.
- Comunicar o resultado efetivamente implementado.

## 4. Escopo de análise

O escopo de análise compreende os elementos que o agente precisa examinar para compreender o problema e suas consequências.

Poderá incluir:

- Arquivos diretamente relacionados.
- Componentes compartilhados.
- Serviços.
- Regras de negócio.
- Contratos.
- Modelos de dados.
- Testes.
- Configurações.
- Integrações.
- Documentação.
- Jornadas e requisitos relacionados.

A análise poderá ultrapassar o módulo diretamente mencionado na solicitação quando isso for necessário para identificar dependências e riscos.

**A consulta a um arquivo não representa autorização para modificá-lo.**

## 5. Escopo de modificação

O escopo de modificação compreende os elementos que precisam ser alterados para entregar o resultado autorizado.

O agente deverá identificar:

- Comportamentos que serão modificados.
- Arquivos diretamente envolvidos.
- Dependências que precisam ser ajustadas.
- Testes que precisam ser criados ou atualizados.
- Documentação que precisa acompanhar a alteração.
- Elementos que deverão permanecer inalterados.

A delimitação deverá ser proporcional ao risco e à complexidade da tarefa.

## 6. Intervenção mínima não significa solução incompleta

O agente não deverá utilizar o princípio da intervenção mínima como justificativa para implementar soluções frágeis ou incompletas.

Quando a correção adequada exigir mudanças em mais de um arquivo ou módulo, essas alterações deverão ser consideradas.

Exemplo:

Uma correção em uma regra de negócio pode exigir atualização do serviço responsável, de seus testes e de um contrato utilizado pela interface.

Modificar somente um arquivo, deixando os demais inconsistentes, não representa uma intervenção adequada.

O objetivo é realizar **todas as alterações necessárias, mas nenhuma alteração desnecessária**.

## 7. Contrato de implementação

Para alterações de médio ou alto risco, o agente deverá estabelecer um contrato de implementação antes de executar mudanças relevantes.

Esse contrato representa o entendimento compartilhado entre agente e desenvolvedor sobre o trabalho autorizado.

Deverá conter, conforme aplicável:

1. Objetivo da solicitação.
2. Resultado esperado.
3. Funcionalidades e jornadas envolvidas.
4. Escopo autorizado.
5. Elementos que poderão ser modificados.
6. Elementos que deverão ser preservados.
7. Dependências e riscos identificados.
8. Estratégia de implementação.
9. Critérios de aceitação.
10. Verificações previstas.
11. Limites de autonomia.
12. Decisões pendentes.

O contrato poderá ser apresentado em linguagem natural, sem necessidade de formulário ou documento separado quando um resumo na própria sessão for suficiente.

## 8. Contrato proporcional ao risco

### Baixo risco

A solicitação do desenvolvedor e o contexto disponível poderão ser suficientes para definir o escopo.

O agente poderá executar diretamente quando houver autorização e clareza adequadas.

### Médio risco

O agente deverá apresentar um resumo da implementação, identificando os principais elementos envolvidos e as validações previstas.

Quando necessário, deverá obter aprovação antes da execução.

### Alto risco

O contrato deverá apresentar maior detalhamento, incluindo impactos, riscos, alternativas relevantes, procedimentos de recuperação e autorizações específicas.

A classificação seguirá o DEV-05, incluindo suas regras de decisão colaborativa e precedentes contextuais.

## 9. Alterações necessárias descobertas durante a execução

Durante a implementação, o agente poderá descobrir que o objetivo aprovado exige alterações não previstas inicialmente.

Nessa situação, deverá avaliar:

- Se a alteração adicional é indispensável.
- Se permanece dentro do objetivo autorizado.
- Se modifica contratos ou comportamentos existentes.
- Se amplia o risco.
- Se afeta funcionalidades não previstas.
- Se exige uma nova decisão funcional ou arquitetural.

Ajustes técnicos complementares de baixo risco, diretamente necessários e compatíveis com o escopo aprovado, poderão ser executados quando as permissões do projeto permitirem.

Ampliações materiais de escopo ou risco deverão ser apresentadas ao desenvolvedor antes da execução.

## 10. Melhorias identificadas fora do escopo

O agente poderá identificar oportunidades durante a investigação, como:

- Código duplicado.
- Componentes que poderiam ser reutilizados.
- Problemas de organização.
- Dependências desnecessárias.
- Falhas de validação.
- Melhorias de desempenho.
- Oportunidades de simplificação.
- Problemas de interface.
- Possíveis riscos de segurança.

O agente deverá distinguir essas descobertas da tarefa principal.

Poderá recomendar melhorias, explicando seus benefícios e sua prioridade.

Não deverá incorporá-las automaticamente quando não forem necessárias para cumprir o objetivo aprovado.

## 11. Tratamento de problemas críticos identificados

Se o agente identificar um problema crítico fora do escopo, deverá comunicar sua existência e suas possíveis consequências.

Quando houver risco imediato de perda de dados, exposição de informações ou comprometimento da segurança, deverá priorizar o alerta e recomendar medidas de contenção adequadas.

A identificação do problema não autoriza automaticamente intervenções destrutivas ou alterações em produção.

O agente deverá respeitar os controles e as autorizações aplicáveis.

## 12. Preservação de comportamentos existentes

O agente deverá considerar os comportamentos que não devem mudar.

Isso inclui:

- Regras de negócio existentes.
- Permissões.
- Contratos.
- Comportamentos de componentes compartilhados.
- Fluxos de navegação.
- Estados e transições.
- Integrações.
- Persistência de dados.
- Convenções de interface.

Quando uma alteração puder afetar esses comportamentos, deverá aplicar as verificações adequadas.

## 13. Refatorações durante outras tarefas

O agente não deverá transformar uma correção localizada em uma refatoração ampla apenas por considerar a estrutura atual pouco elegante.

Refatorações poderão ser realizadas quando:

- Forem necessárias para executar corretamente a tarefa.
- Estiverem explicitamente incluídas no escopo aprovado.
- Representarem ajustes complementares pequenos, diretamente relacionados e de baixo risco.
- Forem aprovadas após recomendação do agente.

Refatorações estruturais relevantes deverão seguir o DEV-05 e, quando aplicável, o ARQ-04.

## 14. Alterações em componentes compartilhados

Quando a tarefa envolver um componente compartilhado, o agente deverá considerar todos os consumidores relevantes.

Deverá preferir soluções que preservem o comportamento existente e permitam configuração contextual quando isso atender ao problema.

Exemplo:

A inclusão de uma propriedade opcional de altura em um componente de tabela poderá permitir diferentes comportamentos de layout sem alterar o funcionamento das telas existentes.

Quando as condições forem equivalentes às estabelecidas no precedente PR-RISCO-001, a alteração poderá ser classificada como baixo risco, conforme o DEV-05.

Essa classificação não elimina a necessidade de validar os consumidores relevantes.

## 15. Relação com a análise de dependências

A análise de dependências definida no DEV-04 deverá orientar a delimitação do escopo.

O agente deverá distinguir:

**Elementos diretamente modificados:** arquivos ou recursos que receberão alterações.

**Elementos indiretamente afetados:** recursos que poderão apresentar mudanças de comportamento em consequência da implementação.

**Elementos apenas analisados:** recursos consultados para compreender dependências e impactos, mas que não precisam ser modificados.

Essa distinção deverá orientar tanto o planejamento quanto a comunicação final.

## 16. Controle de mudanças no escopo

O agente deverá reavaliar o contrato de implementação quando ocorrer:

- Descoberta de dependência crítica.
- Necessidade de alterar comportamento não previsto.
- Ampliação relevante dos arquivos envolvidos.
- Identificação de risco superior.
- Necessidade de modificar dados persistentes.
- Mudança da abordagem técnica aprovada.
- Descoberta de incompatibilidade com requisito ou decisão arquitetural.

Quando a alteração ultrapassar os limites autorizados, o agente deverá consultar o desenvolvedor.

A aprovação de um novo escopo deverá ser registrada de maneira proporcional à sua relevância.

## 17. Verificação das alterações realizadas

Ao concluir a implementação, o agente deverá comparar o resultado com o escopo autorizado.

Deverá verificar:

- Se o objetivo foi atendido.
- Se todas as alterações são justificáveis.
- Se houve modificação não relacionada.
- Se comportamentos existentes foram preservados.
- Se os testes necessários foram executados.
- Se a documentação precisa ser atualizada.
- Se existem pendências.

O agente deverá evitar declarar conclusão quando a implementação não atender aos critérios de aceitação.

## 18. Comunicação final

O agente deverá apresentar, de maneira proporcional à tarefa:

- O que foi implementado.
- Quais arquivos ou módulos foram modificados.
- Quais comportamentos foram alterados.
- Quais dependências relevantes foram verificadas.
- Quais testes foram realizados.
- Quais verificações não puderam ser realizadas.
- Se houve ampliação autorizada do escopo.
- Quais oportunidades adicionais foram identificadas.
- Quais pendências permanecem.

A comunicação deverá permitir que o desenvolvedor compreenda o resultado sem precisar interpretar todo o código.

## 19. Critérios de conformidade

O DEV-06 estará sendo respeitado quando:

- O objetivo da solicitação estiver compreendido.
- O escopo de análise for distinguido do escopo de modificação.
- As alterações forem necessárias e justificadas.
- A implementação não for artificialmente limitada a poucos arquivos.
- Mudanças relevantes possuírem contrato de implementação proporcional.
- O trabalho permanecer dentro dos limites autorizados.
- Melhorias externas ao escopo forem recomendadas sem execução indevida.
- Refatorações oportunistas forem controladas.
- Comportamentos existentes forem preservados.
- Ampliações materiais forem submetidas à aprovação.
- O resultado for validado e comunicado.

## 20. Relação com os demais documentos

### PROD-02 — Requisitos, Jornadas e Regras de Negócio

Define os comportamentos e processos que delimitam o objetivo funcional.

### PROD-04 — Critérios de Aceitação

Estabelece os resultados que deverão ser demonstrados.

### ARQ-02 — Componentes Compartilhados

Orienta alterações que envolvam recursos reutilizados por diferentes funcionalidades.

### ARQ-03 — Responsabilidades e Dependências

Define os limites arquiteturais e as responsabilidades dos módulos.

### DEV-01 — Versionamento e Git

Preserva a rastreabilidade das modificações.

### DEV-04 — Análise de Dependências

Fornece a base para identificar os elementos envolvidos e os impactos indiretos.

### DEV-05 — Gestão de Mudanças

Define o nível de risco, a autonomia e as autorizações necessárias.

### DEV-10 — Encerramento de Sessão

Consolida o resultado, as alterações e as pendências.

## 21. Regra fundamental

**O agente deverá investigar com profundidade suficiente para compreender o problema, executar todas as alterações necessárias para resolvê-lo corretamente e evitar modificações que não contribuam para o objetivo autorizado. Melhorias adicionais deverão ser recomendadas, não implementadas silenciosamente.**