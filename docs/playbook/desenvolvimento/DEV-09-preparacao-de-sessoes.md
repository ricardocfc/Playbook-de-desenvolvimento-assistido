# DEV-09 — Consultoria Contínua e Preparação de Sessões

**Pilar:** 03 — Desenvolvimento  
**Versão:** 1.1  
**Status:** Aprovado  
**Aplicação:** Todas as sessões de desenvolvimento assistido por IA.

---

## 1. Objetivo

Estabelecer procedimentos para que agentes de IA recuperem o contexto de um projeto, compreendam seu estado atual e atuem continuamente como consultores técnicos durante o desenvolvimento.

A metodologia deverá permitir que diferentes agentes e sessões mantenham continuidade, respeitando decisões anteriores, alterações existentes e prioridades do projeto.

## 2. Princípio fundamental

**Toda nova sessão de desenvolvimento deverá começar com a recuperação do contexto relevante e a verificação do estado atual do projeto, em profundidade proporcional à tarefa.**

O agente não deverá presumir que seu conhecimento anterior continua atualizado.

Também não deverá repetir integralmente o diagnóstico inicial quando existirem registros suficientes para orientar o trabalho.

## 3. Diferença entre diagnóstico inicial e preparação de sessão

O DEV-08 estabelece o diagnóstico inicial de um projeto novo, desconhecido ou incorporado à metodologia.

O DEV-09 estabelece a preparação recorrente das sessões posteriores.

O diagnóstico inicial procura compreender o projeto de maneira abrangente.

A preparação de sessão procura identificar o que já foi decidido, o que mudou e o que precisa ser considerado para executar a tarefa atual.

Quando a documentação for insuficiente, o agente poderá complementar a preparação com procedimentos do DEV-08.

## 4. Fontes de contexto

O agente deverá consultar, conforme disponibilidade e relevância:

- Instruções permanentes do projeto.
- Documentos do Pilar Produto.
- Documentos do Pilar Arquitetura.
- Documentos do Pilar Desenvolvimento.
- Histórico de desenvolvimento.
- Registros de encerramento de sessões.
- Decisões arquiteturais.
- Classificações de risco aprovadas.
- Repositório de código.
- Estado do Git.
- Testes.
- Documentação técnica.
- Pendências registradas.
- Recursos especializados disponíveis.

O agente deverá distinguir informações documentadas de hipóteses ou lembranças não verificadas.

## 5. Ordem recomendada de preparação

Ao iniciar uma sessão, o agente deverá:

1. Identificar o projeto e a tarefa.
2. Consultar as instruções permanentes.
3. Recuperar o último estado conhecido.
4. Verificar o estado atual do repositório, quando acessível.
5. Identificar mudanças relevantes desde a sessão anterior.
6. Consultar requisitos e decisões relacionados.
7. Avaliar dependências e riscos da tarefa.
8. Identificar autorizações existentes e pendentes.
9. Considerar recursos especializados úteis.
10. Definir a abordagem adequada para prosseguir.

Essa sequência poderá ser simplificada conforme o contexto.

## 6. Verificação do repositório

Quando possuir acesso ao repositório, o agente deverá verificar, conforme necessário:

- Branch atual.
- Alterações não confirmadas.
- Arquivos novos ou removidos.
- Histórico recente de commits.
- Estado de sincronização conhecido.
- Existência de conflitos.
- Estrutura relevante para a tarefa.
- Scripts e testes disponíveis.

A inspeção deverá respeitar o DEV-01.

O agente não deverá descartar, sobrescrever ou incorporar alterações desconhecidas sem compreender sua origem e obter a autorização necessária.

## 7. Recuperação do histórico de desenvolvimento

O agente deverá consultar registros relevantes para compreender:

- O que foi implementado.
- Quais decisões foram tomadas.
- Quais alternativas foram rejeitadas.
- Quais problemas permanecem.
- Quais testes foram executados.
- Quais mudanças estão pendentes.
- Quais autorizações foram concedidas.
- Quais recomendações foram adiadas.

Deverá priorizar os registros relacionados à tarefa atual.

Não será necessário reconstruir todo o histórico do projeto em cada sessão.

## 8. Continuidade entre diferentes agentes

Quando um agente assumir trabalho iniciado por outro, deverá recuperar o contexto documentado.

Não deverá presumir que possui acesso ao raciocínio ou às informações não registradas pelo agente anterior.

Deverá verificar o estado real do código e confrontá-lo com os registros disponíveis.

Quando encontrar divergências, deverá investigá-las antes de prosseguir com mudanças potencialmente conflitantes.

## 9. Validade das decisões anteriores

O agente deverá respeitar decisões aprovadas enquanto permanecerem aplicáveis.

Entretanto, deverá considerar se houve mudanças relevantes em:

- Requisitos.
- Arquitetura.
- Dependências.
- Tecnologias.
- Ambientes.
- Riscos.
- Restrições.
- Prioridades do produto.

Quando identificar que uma decisão anterior pode estar desatualizada, deverá apresentar a questão ao desenvolvedor.

Não deverá revogar ou substituir silenciosamente decisões aprovadas.

## 10. Consulta aos precedentes de risco

Antes de classificar uma alteração ambígua, o agente deverá consultar as decisões anteriores de classificação de risco.

Quando encontrar precedente suficientemente equivalente, poderá reutilizá-lo conforme o DEV-05.

Deverá verificar se as condições que fundamentaram a decisão continuam presentes.

Quando houver diferenças materiais, deverá realizar nova avaliação e consultar o desenvolvedor quando necessário.

## 11. Avaliação da tarefa atual

Antes de iniciar alterações, o agente deverá compreender:

- Objetivo.
- Resultado esperado.
- Funcionalidade envolvida.
- Jornada ou requisito relacionado.
- Comportamento existente.
- Dependências relevantes.
- Possíveis impactos.
- Classificação de risco.
- Escopo autorizado.
- Critérios de aceitação.
- Verificações necessárias.

A profundidade dessa avaliação deverá seguir os princípios do DEV-04, DEV-05 e DEV-06.

## 12. Consultoria técnica contínua

O agente não deverá limitar sua atuação a executar instruções literalmente.

Durante o desenvolvimento, deverá identificar oportunidades relevantes de:

- Melhorar a organização do código.
- Reduzir riscos.
- Simplificar implementações.
- Melhorar a reutilização.
- Fortalecer testes.
- Corrigir inconsistências.
- Melhorar a segurança.
- Aperfeiçoar o desempenho.
- Melhorar a experiência dos usuários.
- Reduzir dependências desnecessárias.
- Aprimorar os processos de desenvolvimento.

As recomendações deverão ser fundamentadas e relacionadas ao contexto.

A identificação de uma oportunidade não autoriza automaticamente sua implementação.

## 13. Pesquisa contínua de recursos especializados

Quando identificar uma necessidade concreta, o agente deverá considerar se skills, plugins, agentes ou ferramentas especializadas podem melhorar o trabalho.

Deverá aplicar o DEV-07, incluindo:

- Consulta aos recursos existentes.
- Pesquisa externa quando pertinente e disponível.
- Comparação de alternativas.
- Avaliação de evidências de adoção e manutenção.
- Análise preventiva de segurança.
- Identificação de custos e permissões.
- Recomendação fundamentada.
- Solicitação das autorizações necessárias.

O agente não deverá realizar pesquisas extensas sobre ferramentas em toda sessão sem necessidade concreta.

## 14. Identificação de problemas não relacionados à tarefa

Durante a preparação ou execução, o agente poderá identificar problemas fora do escopo.

Deverá classificá-los conforme sua relevância e comunicar os que mereçam atenção.

Poderá recomendar sua inclusão em uma lista de melhorias ou pendências.

Não deverá interromper a tarefa principal por questões secundárias, salvo quando identificar um bloqueador ou risco crítico que justifique a interrupção.

## 15. Preparação proporcional ao risco

### Tarefas de baixo risco

A preparação poderá ser breve, concentrada no contexto diretamente relevante e no estado do repositório.

### Tarefas de médio risco

O agente deverá examinar requisitos, dependências, histórico e impactos pertinentes.

### Tarefas de alto risco

O agente deverá realizar preparação aprofundada, incluindo decisões anteriores, contratos, riscos, estratégias de validação e autorizações.

A classificação seguirá o DEV-05.

## 16. Autonomia durante a preparação

O agente poderá realizar investigações de leitura autorizadas, consultar documentação e elaborar recomendações.

Não deverá interpretar a preparação da sessão como autorização para:

- Alterar arquivos.
- Instalar ferramentas.
- Modificar configurações.
- Excluir dados.
- Realizar commits.
- Executar merges.
- Publicar alterações.
- Executar operações de produção.

Essas ações deverão respeitar as autorizações aplicáveis.

## 17. Comunicação inicial da sessão

Quando a preparação identificar informações relevantes, o agente deverá apresentar um resumo objetivo.

O resumo poderá incluir:

- Contexto recuperado.
- Estado do repositório.
- Último trabalho conhecido.
- Pendências relacionadas.
- Riscos identificados.
- Decisões que precisam ser confirmadas.
- Abordagem recomendada.

Para tarefas simples, a comunicação poderá ser incorporada diretamente à resposta de execução.

O agente deverá evitar relatórios repetitivos que não acrescentem valor.

## 18. Divergências entre documentação e código

Quando encontrar diferenças entre os registros e a implementação, o agente deverá:

1. Identificar a divergência.
2. Investigar as evidências disponíveis.
3. Avaliar suas consequências.
4. Determinar se a diferença afeta a tarefa.
5. Consultar o desenvolvedor quando necessário.
6. Recomendar atualização dos registros ou correção da implementação.

Não deverá presumir automaticamente que o código ou a documentação está correto.

## 19. Informações indisponíveis

Quando não tiver acesso a arquivos, repositórios, ferramentas ou registros necessários, o agente deverá informar a limitação.

Poderá solicitar acesso, arquivos ou esclarecimentos ao desenvolvedor.

Não deverá afirmar que verificou informações às quais não teve acesso.

Quando a ausência de informações não impedir a tarefa, poderá prosseguir com as ressalvas adequadas.

## 20. Atualização do contexto durante a sessão

A preparação inicial não deverá ser tratada como uma avaliação definitiva.

Quando surgirem novas informações, o agente deverá atualizar sua compreensão do projeto.

Isso inclui:

- Novos requisitos.
- Decisões do desenvolvedor.
- Mudanças de escopo.
- Dependências descobertas.
- Riscos identificados.
- Resultados de testes.
- Alterações de arquitetura.

Decisões relevantes deverão ser preservadas conforme os mecanismos de documentação do projeto.

## 21. Integração com o encerramento da sessão

O DEV-09 dependerá da qualidade dos registros produzidos ao final das sessões anteriores.

O DEV-10 deverá estabelecer como preservar:

- Trabalho realizado.
- Estado do repositório.
- Testes.
- Decisões.
- Pendências.
- Próximos passos.
- Alertas relevantes.

O agente deverá utilizar esses registros como referência para retomar o trabalho.

## 22. Critérios de conformidade

O DEV-09 estará sendo respeitado quando:

- Toda nova sessão recuperar o contexto relevante.
- O agente verificar o estado atual do projeto quando possível.
- Decisões anteriores forem consideradas.
- Precedentes de risco forem consultados quando aplicáveis.
- Alterações de outros desenvolvedores forem preservadas.
- O histórico for utilizado para evitar repetição desnecessária.
- A preparação for proporcional à tarefa.
- O agente atuar continuamente como consultor.
- Recursos especializados forem considerados quando pertinentes.
- Recomendações não forem executadas sem autorização.
- Limitações de acesso forem comunicadas.
- O contexto for atualizado durante a execução.
- A continuidade entre agentes for preservada.

## 23. Relação com os demais documentos

### DEV-01 — Versionamento e Git

Orienta a verificação do repositório e a preservação de alterações existentes.

### DEV-04 — Análise de Dependências

Orienta a identificação de impactos relevantes.

### DEV-05 — Gestão de Mudanças

Define classificação de risco, precedentes e autorizações.

### DEV-06 — Intervenção Mínima

Delimita o escopo de implementação.

### DEV-07 — Recursos Especializados

Orienta a descoberta e avaliação de ferramentas.

### DEV-08 — Diagnóstico Inicial

Estabelece a compreensão inicial do projeto.

### DEV-10 — Encerramento de Sessão

Define os registros utilizados para a retomada do trabalho.

### DEV-11 — Histórico de Desenvolvimento

Preserva acontecimentos e decisões relevantes.

### DEV-12 — Instruções Permanentes

Define as orientações que deverão ser recuperadas em todas as sessões.

## 24. Recuperação de contexto em requisições entre SPECs

Quando a tarefa envolver uma nova requisição unitária em projeto organizado por SPECs, a preparação da sessão deverá recuperar o contexto pertinente antes de confirmar sua classificação funcional, conforme PROD-02.

O agente deverá, de maneira proporcional ao escopo:

1. Consultar a SPEC aparentemente relacionada à solicitação e verificar suas referências cruzadas para outras SPECs.
2. Localizar os `spec.md` e `history.md` pertinentes, identificando o comportamento vigente, a evolução funcional e requisições anteriores relacionadas.
3. Verificar se a nova requisição possui finalidade e abrangência próprias, sem herdar automaticamente a SPEC principal de requisições anteriores.
4. Identificar dependências e impactos previstos que precisem ser analisados conforme DEV-04, inclusive em funcionalidades documentadas em outras SPECs.
5. Comunicar referências ausentes, divergências ou incertezas relevantes antes de prosseguir com uma classificação ou planejamento que delas dependa.

A consulta a uma SPEC associada não transfere a responsabilidade de execução para ela e não autoriza duplicar registros operacionais. A preparação não deverá alterar o histórico ou a especificação sem o escopo e a autorização aplicáveis, conforme DEV-11.

## 25. Regra fundamental

**Toda sessão deverá começar com a recuperação do contexto relevante e a verificação do estado atual do projeto. Durante o trabalho, o agente deverá atuar como consultor técnico proativo, respeitar decisões anteriores, identificar riscos e oportunidades e preservar a continuidade do desenvolvimento entre sessões e agentes.**