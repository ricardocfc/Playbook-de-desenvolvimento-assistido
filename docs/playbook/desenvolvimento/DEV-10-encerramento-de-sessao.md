# DEV-10 — Encerramento de Sessão e Transferência de Contexto

**Pilar:** 03 — Desenvolvimento  
**Versão:** 1.1 — revisão pontual proposta  
**Status:** Revisão pontual em validação — versão anterior preservada  
**Aplicação:** Todas as sessões de desenvolvimento assistido por IA.

---

## 1. Objetivo

Estabelecer procedimentos para encerrar sessões de desenvolvimento de maneira organizada, preservando informações necessárias à continuidade do projeto.

O documento deverá permitir que outro agente ou desenvolvedor compreenda o trabalho realizado, o estado atual da implementação e os próximos passos, sem depender exclusivamente do histórico da conversa anterior.

## 2. Princípio fundamental

**Toda sessão de desenvolvimento deverá preservar as informações relevantes para que o trabalho possa ser retomado com segurança, independentemente do agente ou da plataforma utilizada.**

O encerramento deverá ser proporcional à complexidade da sessão.

O agente não deverá produzir documentação extensa quando um registro objetivo for suficiente.

## 3. Responsabilidades do agente

Ao encerrar uma sessão, o agente deverá:

- Identificar o trabalho realizado.
- Verificar o estado da implementação.
- Identificar arquivos modificados.
- Verificar o estado do Git, quando acessível.
- Registrar testes e validações.
- Preservar decisões relevantes.
- Identificar pendências.
- Registrar riscos e limitações.
- Informar operações ainda não executadas.
- Recomendar os próximos passos.
- Produzir um resumo compreensível para o desenvolvedor.
- Atualizar os registros persistentes pertinentes, quando autorizado.

## 4. Quando realizar o encerramento

O procedimento deverá ser aplicado quando:

- Uma tarefa for concluída.
- O desenvolvedor solicitar o encerramento.
- Uma sessão for interrompida de maneira planejada.
- Houver transferência de trabalho para outro agente.
- Uma etapa relevante de implementação for concluída.
- O agente identificar necessidade de preservar contexto antes de uma mudança de abordagem.

Quando o encerramento for inesperado, o próximo agente deverá reconstruir o contexto disponível conforme o DEV-09.

O agente não deverá presumir que conseguirá executar ações depois que a sessão tiver sido encerrada.

## 5. Estado da tarefa

O agente deverá identificar a situação do trabalho:

**Concluído:** implementação finalizada e critérios aplicáveis atendidos.

**Concluído com ressalvas:** implementação realizada, mas existem verificações ou limitações pendentes.

**Parcialmente concluído:** parte do trabalho foi implementada.

**Bloqueado:** existe impedimento que exige informação, autorização ou recurso adicional.

**Não iniciado:** a tarefa foi analisada, mas não houve implementação.

O estado informado deverá corresponder às evidências disponíveis.

## 6. Registro das alterações

O agente deverá registrar, conforme relevância:

- Funcionalidades implementadas.
- Defeitos corrigidos.
- Comportamentos modificados.
- Arquivos criados.
- Arquivos alterados.
- Arquivos removidos.
- Testes adicionados ou atualizados.
- Documentação modificada.
- Configurações alteradas.

O registro deverá destacar as alterações que possam influenciar futuras tarefas.

Não será necessário descrever cada linha modificada quando o histórico de código já permitir essa consulta.

## 7. Estado do repositório

Quando houver acesso ao Git, o agente deverá verificar e comunicar:

- Branch atual.
- Alterações não confirmadas.
- Commits realizados.
- Existência de arquivos novos.
- Estado de sincronização conhecido.
- Operações pendentes.
- Possíveis conflitos.

O agente deverá distinguir claramente:

- Código modificado.
- Código registrado em commit.
- Código enviado ao repositório remoto.
- Código integrado à branch principal.
- Código publicado em ambiente de execução.

Nenhuma dessas etapas deverá ser presumida a partir da realização de outra.

## 8. Preservação de trabalho não concluído

Quando uma tarefa permanecer incompleta, o agente deverá registrar:

1. O que já foi realizado.
2. O que falta implementar.
3. Quais arquivos estão envolvidos.
4. Quais decisões foram tomadas.
5. Quais problemas foram encontrados.
6. Quais testes ainda precisam ser executados.
7. Qual é a próxima ação recomendada.

O registro deverá permitir a retomada sem necessidade de repetir investigações já documentadas.

O agente não deverá realizar commits, pushes ou outras operações apenas para encerrar a sessão, salvo quando autorizado pelas políticas do projeto.

## 9. Registro de testes e validações

O agente deverá informar quais verificações foram efetivamente executadas.

Poderá registrar:

- Compilação.
- Testes automatizados.
- Testes de integração.
- Testes de interface.
- Testes de regressão.
- Verificações de permissões.
- Validação de dados.
- Testes de jornadas.
- Revisão de código.

Para cada verificação relevante, deverá indicar o resultado.

Quando um teste não puder ser executado, deverá registrar a limitação.

O agente não deverá declarar testes como aprovados sem evidências de execução.

## 10. Decisões tomadas

O encerramento deverá preservar decisões relevantes, como:

- Alterações de abordagem.
- Escolhas técnicas.
- Ajustes de requisitos.
- Mudanças de escopo.
- Classificações de risco.
- Autorizações.
- Restrições.
- Alternativas rejeitadas.
- Decisões adiadas.

As decisões deverão ser registradas nos mecanismos adequados, evitando duplicidade desnecessária.

Decisões arquiteturais relevantes deverão seguir o ARQ-04.

Classificações de risco recorrentes deverão seguir o DEV-05.

## 11. Riscos e limitações

O agente deverá registrar riscos que permaneçam relevantes para a continuidade.

Exemplos:

- Dependência ainda não analisada.
- Comportamento sem validação.
- Alteração com possibilidade de regressão.
- Integração indisponível.
- Ambiente de testes incompleto.
- Incompatibilidade identificada.
- Problema de segurança pendente.
- Divergência entre código e documentação.

O registro deverá distinguir riscos confirmados de hipóteses.

## 12. Pendências

As pendências deverão ser apresentadas de maneira objetiva.

Cada pendência relevante deverá indicar, quando aplicável:

- O que precisa ser feito.
- Por que permanece pendente.
- Qual elemento do projeto está envolvido.
- Se existe dependência de decisão humana.
- Se existe impedimento técnico.
- Qual é a prioridade recomendada.

O agente deverá evitar listas extensas de pendências sem relação com o trabalho realizado.

## 13. Próximos passos

O agente deverá recomendar a próxima sequência lógica de trabalho.

As recomendações deverão considerar:

- Estado atual.
- Dependências.
- Riscos.
- Critérios de aceitação.
- Autorizações.
- Prioridades conhecidas.

O agente não deverá apresentar decisões ainda não aprovadas como etapas obrigatórias.

## 14. Registro de transferência de contexto

Quando houver necessidade de continuidade, o agente deverá produzir um registro de transferência de contexto.

O registro poderá conter:

### Identificação

- Projeto.
- Data ou referência da sessão.
- Tarefa.
- Estado.

### Trabalho realizado

- Resumo das alterações.
- Arquivos ou módulos envolvidos.
- Decisões relevantes.

### Estado técnico

- Branch.
- Commits.
- Alterações pendentes.
- Testes realizados.
- Limitações.

### Continuidade

- Pendências.
- Riscos.
- Autorizações necessárias.
- Próxima ação recomendada.

A estrutura poderá ser simplificada conforme a complexidade da tarefa.

## 15. Persistência dos registros

Informações necessárias à continuidade deverão ser preservadas em mecanismos acessíveis às futuras sessões e aos agentes autorizados.

Poderão ser utilizados:

- Documentos do projeto.
- Arquivos de histórico.
- Registros de tarefas.
- Sistemas de gestão.
- Documentação técnica.
- Registros de decisões.

O histórico da conversa poderá complementar esses registros, mas não deverá ser sua única fonte.

O agente deverá respeitar as políticas de autorização para criar ou modificar arquivos persistentes.

## 16. Independência de plataforma

O procedimento deverá funcionar com diferentes assistentes e ambientes de desenvolvimento.

O registro de transferência não deverá depender de funcionalidades exclusivas de um fornecedor.

Quando uma plataforma oferecer recursos específicos de continuidade, eles poderão complementar os registros universais do projeto.

## 17. Encerramento proporcional ao risco

### Baixo risco

Resumo breve da alteração, validação e estado final.

### Médio risco

Registro das mudanças, dependências relevantes, testes, decisões e pendências.

### Alto risco

Registro detalhado do estado técnico, autorizações, impactos, validações, riscos residuais e procedimentos de continuidade.

A classificação deverá seguir o DEV-05.

## 18. Encerramento com problemas não resolvidos

O agente poderá encerrar uma sessão mesmo quando existirem problemas pendentes.

Entretanto, deverá comunicar claramente:

- O que não foi concluído.
- Quais verificações faltam.
- Quais riscos permanecem.
- Se o sistema pode estar em estado intermediário.
- Quais cuidados deverão ser observados antes da retomada.

Não deverá apresentar uma implementação parcial como concluída.

## 19. Comunicação ao desenvolvedor

O agente deverá fornecer um resumo final compreensível.

A comunicação deverá priorizar:

1. Resultado alcançado.
2. Alterações relevantes.
3. Verificações realizadas.
4. Estado do repositório.
5. Pendências.
6. Próximo passo recomendado.

Informações técnicas adicionais poderão ser incluídas quando necessárias.

O objetivo é permitir que o desenvolvedor compreenda a situação sem precisar interpretar todos os arquivos modificados.

## 20. Integração com a próxima sessão

O registro de encerramento deverá servir como uma das fontes prioritárias para a preparação definida no DEV-09.

O próximo agente deverá verificar se as informações continuam compatíveis com o estado real do projeto.

O registro de encerramento não substitui a inspeção do repositório.

## 21. Critérios de conformidade

O DEV-10 estará sendo respeitado quando:

- O estado da tarefa for comunicado corretamente.
- Alterações relevantes forem identificadas.
- O estado do Git for registrado quando acessível.
- Commits, pushes, merges e deploys forem distinguidos.
- Testes executados forem informados com precisão.
- Decisões relevantes forem preservadas.
- Riscos e limitações forem comunicados.
- Pendências forem identificadas.
- Próximos passos forem recomendados.
- Informações necessárias à continuidade forem persistidas quando autorizado.
- O registro for proporcional ao trabalho.
- Outro agente puder retomar a tarefa com segurança.

## 22. Relação com os demais documentos

### DEV-01 — Versionamento e Git

Define as operações e os cuidados com o repositório.

### DEV-05 — Gestão de Mudanças

Orienta o detalhamento do encerramento conforme o risco.

### DEV-06 — Intervenção Mínima

Permite verificar se a implementação permaneceu no escopo autorizado.

### DEV-09 — Consultoria Contínua

Utiliza os registros de encerramento para preparar sessões futuras.

### DEV-11 — Histórico de Desenvolvimento

Define a organização permanente dos registros e decisões.

### DEV-12 — Instruções Permanentes

Garante que os procedimentos de encerramento sejam conhecidos pelos agentes.

## 23. Verificação de rastreabilidade e consistência entre SPECs no encerramento

Quando a tarefa envolver uma requisição unitária em projeto organizado por SPECs, o encerramento deverá verificar, conforme o estado real do trabalho e o escopo autorizado:

1. Se a requisição e seus registros operacionais permanecem centralizados em sua SPEC principal, conforme PROD-02.
2. Se as SPECs associadas possuem as referências de localização necessárias, sem duplicação de planejamento, tarefas ou histórico operacional.
3. Se os impactos previstos, implementados e validados estão diferenciados e sustentados por evidências, conforme DEV-04 e PROD-04.
4. Se alterações funcionais efetivamente implementadas e validadas foram registradas de forma aditiva nos `history.md` das SPECs afetadas, com referência à requisição causadora e à sua SPEC principal, conforme DEV-11.
5. Se os `spec.md` afetados descrevem o comportamento vigente ou referenciam a regra canônica, sem reproduzir regras contraditórias.
6. Se eventuais atualizações documentais não executadas foram identificadas como pendências, com justificativa, responsável ou próximo passo quando aplicável.

O agente não deverá declarar uma alteração como validada sem evidência, nem apresentar documentação pendente como concluída. O registro de transferência deverá permitir que o próximo agente localize a SPEC principal e compreenda o estado dos impactos cruzados. A verificação de encerramento não constitui autorização para realizar mudanças fora do escopo.

## 24. Regra fundamental

**Ao concluir ou interromper uma sessão, o agente deverá preservar um registro fiel e proporcional do trabalho realizado, do estado técnico, das decisões, das validações e das pendências, permitindo que qualquer agente autorizado retome o desenvolvimento sem depender da memória da sessão anterior.**