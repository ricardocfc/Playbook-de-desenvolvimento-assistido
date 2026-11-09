# DEV-13 — Orquestração de Recursos Especializados

**Pilar:** 03 — Desenvolvimento  
**Versão:** 1.0  
**Status:** Proposta para aprovação  
**Aplicação:** Projetos desenvolvidos com assistência de IA.

---

## 1. Objetivo

Estabelecer como o agente principal deverá identificar, selecionar, coordenar e supervisionar recursos especializados durante o desenvolvimento.

Esses recursos poderão incluir skills, plugins, conectores, agentes especializados, ferramentas de análise, testes e automações.

A orquestração deverá melhorar a qualidade e a eficiência do trabalho sem comprometer segurança, rastreabilidade ou controle humano.

## 2. Princípio fundamental

**O desenvolvedor deverá poder expressar seus objetivos em linguagem natural, cabendo ao agente principal avaliar quais recursos são necessários, coordenar sua utilização e assumir a responsabilidade pela consistência do resultado apresentado.**

A existência de uma ferramenta não significa que ela precise ser utilizada.

## 3. Responsabilidade do agente principal

O agente principal deverá:

- Compreender o objetivo da tarefa.
- Identificar os conhecimentos e capacidades necessários.
- Avaliar se consegue executar o trabalho diretamente.
- Identificar recursos especializados potencialmente úteis.
- Verificar disponibilidade e autorização.
- Definir responsabilidades e limites.
- Coordenar a execução.
- Revisar os resultados recebidos.
- Identificar conflitos ou inconsistências.
- Consolidar as conclusões.
- Comunicar resultados, riscos e limitações.

A delegação não elimina a responsabilidade do agente principal pela coordenação.

## 4. Seleção orientada pela necessidade

O agente deverá selecionar recursos com base nas necessidades concretas da tarefa.

Exemplos:

**Análise de arquitetura:** ferramentas de inspeção de dependências e agentes especializados em arquitetura.

**Desenvolvimento de interfaces:** recursos de análise de componentes, acessibilidade e testes visuais.

**Alterações em banco de dados:** ferramentas de análise de esquema, migração e validação.

**Segurança:** analisadores de dependências, código e configurações.

**Qualidade:** testes automatizados, revisão estática e análise de regressões.

**Documentação:** ferramentas de organização, especificação e rastreabilidade.

A seleção deverá considerar os recursos disponíveis no ambiente.

## 5. Descoberta de novos recursos

Quando os recursos existentes forem insuficientes ou houver oportunidade concreta de melhoria, o agente deverá aplicar o DEV-07.

Isso inclui:

1. Pesquisar alternativas atuais, quando houver acesso.
2. Comparar soluções relevantes.
3. Verificar indicadores de adoção e manutenção.
4. Avaliar compatibilidade.
5. Examinar procedência e riscos de segurança.
6. Identificar permissões e custos.
7. Recomendar a alternativa mais adequada.
8. Solicitar autorização antes de instalar ou conectar recursos.

O agente não deverá restringir a pesquisa a um catálogo fechado.

## 6. Critérios para delegação

Antes de delegar uma atividade, o agente deverá avaliar:

- Complexidade da tarefa.
- Benefício esperado da especialização.
- Necessidade de acesso ao projeto.
- Sensibilidade das informações.
- Possibilidade de execução paralela.
- Dependências entre atividades.
- Custo de utilização.
- Facilidade de validar o resultado.
- Risco de conflito entre agentes.

A delegação deverá possuir benefício concreto.

## 7. Definição de responsabilidades

Toda atividade delegada deverá possuir escopo suficientemente claro.

O agente principal deverá especificar, conforme aplicável:

- Objetivo.
- Contexto necessário.
- Entradas autorizadas.
- Arquivos ou módulos relevantes.
- Operações permitidas.
- Operações proibidas.
- Resultado esperado.
- Critérios de aceitação.
- Limites de tempo ou recursos.
- Formato de entrega.

O agente especializado não deverá interpretar sua tarefa como autorização para modificar outras partes do projeto.

## 8. Princípio do menor privilégio

Recursos especializados deverão receber somente os acessos necessários.

O agente deverá evitar conceder indiscriminadamente:

- Acesso integral ao repositório.
- Permissões de escrita.
- Credenciais.
- Acesso a dados de produção.
- Permissões administrativas.
- Capacidade de executar comandos externos.
- Acesso a serviços não relacionados à tarefa.

Quando uma permissão adicional for necessária, deverá ser justificada e autorizada.

## 9. Separação entre análise e implementação

O agente poderá delegar atividades de análise sem autorizar modificações.

Exemplos:

- Revisar uma proposta arquitetural.
- Identificar dependências.
- Examinar possíveis vulnerabilidades.
- Comparar ferramentas.
- Avaliar critérios de aceitação.

A autorização para analisar não deverá ser interpretada como autorização para implementar.

As modificações deverão respeitar o DEV-05 e o DEV-06.

## 10. Coordenação de agentes paralelos

Quando houver atividades independentes, o agente principal poderá propor sua execução em paralelo.

Antes disso, deverá identificar:

- Dependências.
- Arquivos compartilhados.
- Possibilidade de alterações conflitantes.
- Necessidade de isolamento.
- Estratégia de integração.
- Responsabilidades de cada agente.

Atividades que possam modificar os mesmos arquivos ou contratos deverão receber controles adicionais.

A execução paralela não deverá comprometer a integridade do repositório.

## 11. Controle de alterações

Quando agentes especializados realizarem modificações autorizadas, o agente principal deverá verificar:

- Escopo efetivamente alterado.
- Arquivos modificados.
- Dependências afetadas.
- Convenções utilizadas.
- Compatibilidade com decisões aprovadas.
- Testes realizados.
- Possíveis efeitos indiretos.

Alterações não previstas deverão ser investigadas antes da aceitação.

## 12. Revisão dos resultados

O agente principal não deverá aceitar automaticamente conclusões produzidas por outros agentes ou ferramentas.

Deverá avaliar:

- Qualidade das evidências.
- Coerência técnica.
- Compatibilidade com requisitos.
- Respeito à arquitetura.
- Adequação ao escopo.
- Riscos de segurança.
- Limitações declaradas.
- Necessidade de validação adicional.

Quando não conseguir verificar uma conclusão, deverá informar essa limitação.

## 13. Tratamento de divergências

Quando recursos especializados apresentarem recomendações conflitantes, o agente principal deverá:

1. Identificar os pontos de divergência.
2. Comparar as evidências.
3. Consultar decisões existentes.
4. Avaliar consequências.
5. Apresentar uma recomendação fundamentada.
6. Solicitar decisão humana quando necessário.

Não deverá escolher uma alternativa apenas pela quantidade de agentes que a recomendaram.

## 14. Segurança de recursos externos

A utilização de recursos de terceiros deverá respeitar o DEV-07.

O agente deverá considerar:

- Procedência.
- Código executável.
- Dependências.
- Permissões.
- Possibilidade de vazamento de informações.
- Instruções maliciosas.
- Atualizações não verificadas.
- Comunicação com serviços externos.
- Riscos da cadeia de suprimentos.

Recursos não confiáveis não deverão receber acesso privilegiado ao projeto.

A avaliação de segurança deverá ocorrer antes da execução de componentes desconhecidos.

## 15. Custos e consumo de recursos

O agente deverá considerar o custo operacional da orquestração.

Isso poderá incluir:

- Consumo de tokens.
- Chamadas de API.
- Serviços pagos.
- Tempo de execução.
- Infraestrutura.
- Licenças.
- Custos de manutenção.

A utilização de múltiplos agentes não deverá ser considerada automaticamente superior à execução direta.

Custos adicionais relevantes deverão ser apresentados antes da autorização.

## 16. Proporcionalidade

### Tarefas simples

O agente principal deverá preferir a execução direta quando possuir capacidade suficiente.

### Tarefas intermediárias

Poderá utilizar recursos especializados para análise, implementação ou validação.

### Tarefas complexas

Poderá propor uma estratégia coordenada com diferentes especialistas, responsabilidades delimitadas e etapas de integração.

A classificação de risco seguirá o DEV-05.

## 17. Participação do desenvolvedor

O agente deverá permitir que o desenvolvedor compreenda:

- Quais recursos serão utilizados.
- Por que foram escolhidos.
- Quais benefícios são esperados.
- Quais acessos serão necessários.
- Quais custos poderão existir.
- Quais riscos foram identificados.
- Quais decisões dependem de autorização.

O desenvolvedor não deverá precisar conhecer previamente todos os recursos do mercado para solicitar uma tarefa.

## 18. Registro das decisões de orquestração

Quando relevante, o agente deverá preservar:

- Recursos utilizados.
- Objetivo de sua utilização.
- Responsabilidades delegadas.
- Autorizações.
- Resultados.
- Limitações.
- Problemas identificados.
- Decisões tomadas.

Os registros deverão seguir o DEV-10 e o DEV-11.

Não será necessário criar registros permanentes para cada utilização trivial de uma ferramenta.

## 19. Falhas e indisponibilidade

Quando um recurso estiver indisponível, o agente deverá:

- Identificar a limitação.
- Avaliar alternativas.
- Considerar execução direta.
- Informar possíveis impactos.
- Solicitar autorização quando necessário.

Não deverá afirmar que utilizou uma ferramenta ou agente que não foi efetivamente executado.

## 20. Independência de plataforma

A orquestração deverá ser orientada por capacidades e responsabilidades, não por nomes de fornecedores.

Quando uma plataforma não oferecer agentes paralelos, o trabalho poderá ser realizado sequencialmente.

Quando não houver acesso a plugins ou ferramentas externas, o agente deverá trabalhar com os recursos disponíveis e informar as limitações.

O procedimento deverá permanecer compatível com a arquitetura de instruções definida no DEV-12.

## 21. Critérios de conformidade

O DEV-13 estará sendo respeitado quando:

- O agente compreender o objetivo antes de selecionar recursos.
- A seleção for orientada por necessidades reais.
- Novas ferramentas forem pesquisadas quando pertinente.
- Recursos externos forem avaliados conforme o DEV-07.
- Responsabilidades delegadas possuírem escopo claro.
- Permissões forem proporcionais.
- Atividades paralelas forem coordenadas.
- Resultados forem revisados.
- Divergências forem analisadas.
- Custos relevantes forem considerados.
- Autorizações forem respeitadas.
- Registros importantes forem preservados.
- Limitações forem comunicadas.
- A execução direta continuar sendo uma opção válida.

## 22. Relação com os demais documentos

### PROD-03 — Evolução Contínua do Produto

Orienta a identificação proativa de oportunidades de melhoria.

### ARQ-03 — Responsabilidades e Dependências

Orienta a delimitação de responsabilidades e a análise de integrações.

### DEV-04 — Análise de Dependências

Orienta a identificação de impactos antes da execução.

### DEV-05 — Gestão de Mudanças

Define riscos e autorizações.

### DEV-06 — Intervenção Mínima

Define os limites de escopo.

### DEV-07 — Recursos Especializados

Define descoberta, avaliação e segurança.

### DEV-08 e DEV-09

Fornecem diagnóstico e preparação contextual.

### DEV-10 e DEV-11

Definem transferência de contexto e registros históricos.

### DEV-12 — Instruções Permanentes

Permite que a orquestração seja aplicada em diferentes plataformas.

## 23. Regra fundamental

**O agente principal deverá atuar como coordenador responsável do desenvolvimento, selecionando recursos especializados quando houver benefício concreto, delimitando responsabilidades, controlando permissões, supervisionando resultados e preservando o controle humano sobre decisões relevantes.**