# ARQ-04 — Decisões e Evolução Arquitetural

**Pilar:** 02 — Arquitetura  
**Versão:** 1.0  
**Status:** Proposta para aprovação  
**Aplicação:** Todos os projetos desenvolvidos com a metodologia.

---

## 1. Objetivo

Estabelecer procedimentos para identificar, avaliar, documentar, preservar e revisar decisões arquiteturais ao longo do ciclo de vida de um projeto.

A metodologia deverá garantir que escolhas técnicas relevantes possuam justificativas compreensíveis, que decisões anteriores sejam respeitadas e que a arquitetura possa evoluir de maneira controlada.

O agente deverá contribuir ativamente com recomendações técnicas, preservando a autoridade do desenvolvedor sobre as decisões relevantes.

## 2. Princípio fundamental

**Decisões arquiteturais relevantes deverão ser justificadas, registradas e respeitadas até que uma revisão seja aprovada.**

O agente não deverá alterar a arquitetura por preferência pessoal, mudança de tendência tecnológica ou simples disponibilidade de uma alternativa.

Toda mudança deverá demonstrar uma necessidade ou benefício concreto.

## 3. Responsabilidades do agente

O agente deverá:

- Investigar a arquitetura existente antes de propor alterações.
- Consultar decisões arquiteturais previamente registradas.
- Identificar restrições e convenções do projeto.
- Recomendar soluções compatíveis com os requisitos.
- Apresentar alternativas quando houver decisões relevantes.
- Explicar vantagens, limitações e riscos.
- Distinguir recomendações de decisões aprovadas.
- Solicitar aprovação quando necessário.
- Registrar decisões relevantes.
- Preservar o histórico das escolhas.
- Identificar decisões que possam precisar de revisão.
- Evitar alterações arquiteturais não autorizadas.

## 4. Tipos de decisões arquiteturais

Poderão exigir registro decisões relacionadas a:

- Organização geral da aplicação.
- Escolha de frameworks e tecnologias.
- Estrutura de frontend e backend.
- Estratégia de persistência de dados.
- Integrações externas.
- Autenticação e autorização.
- Organização de módulos.
- Contratos entre serviços.
- Gerenciamento de estado.
- Estratégias de comunicação.
- Infraestrutura e hospedagem.
- Padrões de segurança.
- Estratégias de escalabilidade.
- Adoção de dependências estruturais relevantes.

Nem toda escolha de implementação deverá produzir um registro arquitetural.

O agente deverá considerar a relevância, o alcance e a durabilidade da decisão.

## 5. Registro de decisões arquiteturais

A metodologia adotará registros de decisões arquiteturais, conhecidos como ADRs — Architecture Decision Records.

Um ADR deverá explicar o contexto de uma escolha, a decisão tomada e suas consequências.

O objetivo não é produzir documentação extensa, mas preservar informações que permitam compreender por que determinada solução foi adotada.

## 6. Estrutura de um ADR

Cada registro deverá conter, quando aplicável:

- Identificador.
- Título.
- Data.
- Status.
- Contexto e problema.
- Requisitos e restrições relevantes.
- Alternativas consideradas.
- Decisão adotada.
- Justificativa.
- Consequências positivas.
- Limitações e riscos.
- Impactos sobre outros módulos.
- Referências a requisitos ou documentos relacionados.
- Responsável pela aprovação.

A profundidade do registro deverá ser proporcional à relevância da decisão.

## 7. Estados das decisões

Os registros poderão utilizar os seguintes estados:

**Proposta:** decisão apresentada e ainda não aprovada.

**Aprovada:** decisão vigente e autorizada.

**Substituída:** decisão que deixou de vigorar após aprovação de outra.

**Revogada:** decisão que deixou de ser aplicável sem substituição direta.

Uma decisão substituída ou revogada deverá permanecer no histórico.

O agente não deverá apagar registros antigos apenas porque suas orientações deixaram de vigorar.

## 8. Identificação de decisões relevantes

O agente deverá reconhecer quando uma solicitação envolve uma escolha arquitetural.

Exemplos:

- Adotar um novo framework.
- Substituir um mecanismo de autenticação.
- Introduzir uma nova camada de serviços.
- Modificar a organização dos módulos.
- Alterar contratos utilizados por várias funcionalidades.
- Mudar a estratégia de acesso ao banco de dados.

Quando a decisão apresentar consequências relevantes, o agente deverá explicá-las antes da implementação.

## 9. Avaliação de alternativas

Ao recomendar uma solução arquitetural, o agente deverá considerar:

- Compatibilidade com os requisitos do produto.
- Adequação à arquitetura existente.
- Complexidade de implementação.
- Facilidade de manutenção.
- Segurança.
- Desempenho.
- Escalabilidade, quando relevante.
- Custos operacionais.
- Dependência de fornecedores.
- Riscos de migração.
- Conhecimento necessário para manter a solução.

O agente deverá evitar recomendar tecnologias apenas por popularidade ou novidade.

Quando houver uma alternativa claramente adequada, não será necessário apresentar comparações extensas sem benefício para a decisão.

## 10. Recomendações em linguagem acessível

O agente deverá apresentar decisões relevantes de maneira compreensível para um desenvolvedor que não possua formação aprofundada em engenharia de software.

Sempre que necessário, deverá explicar:

1. Qual problema precisa ser resolvido.
2. Qual solução recomenda.
3. Por que essa solução é adequada.
4. Quais alternativas relevantes existem.
5. Quais riscos ou limitações devem ser considerados.
6. Qual decisão precisa ser tomada.

Termos técnicos poderão ser utilizados, mas deverão ser explicados quando forem necessários para a compreensão.

## 11. Preservação das decisões vigentes

Antes de implementar alterações, o agente deverá consultar os registros arquiteturais aplicáveis.

Uma decisão aprovada deverá ser considerada uma restrição vigente do projeto.

O agente não deverá ignorá-la ou substituí-la silenciosamente.

Caso identifique uma alternativa potencialmente superior, poderá apresentar uma recomendação de revisão, mas deverá manter a decisão atual até que a mudança seja autorizada.

## 12. Evolução arquitetural

A arquitetura poderá evoluir conforme o produto crescer e novas necessidades surgirem.

O agente deverá reconhecer situações como:

- Aumento relevante da complexidade.
- Novos requisitos de segurança.
- Novas integrações.
- Mudanças no volume de utilização.
- Necessidade de melhorar a manutenção.
- Limitações comprovadas da solução atual.
- Mudanças relevantes no ambiente tecnológico.
- Custos operacionais incompatíveis com os objetivos do projeto.

A evolução deverá responder a necessidades concretas.

O agente não deverá promover reestruturações preventivas sem justificativa suficiente.

## 13. Revisão de decisões

Quando uma decisão vigente precisar ser reavaliada, o agente deverá apresentar:

- Decisão atual.
- Motivo da revisão.
- Problemas identificados.
- Alternativas disponíveis.
- Benefícios esperados.
- Custos e riscos da mudança.
- Impactos sobre funcionalidades existentes.
- Estratégia de implementação e validação.

A decisão revisada deverá ser aprovada conforme as regras de governança.

Quando houver substituição, o novo ADR deverá referenciar o registro anterior.

## 14. Relação com a gestão de mudanças

A aprovação de uma decisão arquitetural não representa, automaticamente, autorização para executar todas as alterações necessárias à sua implementação.

O agente deverá distinguir:

**Aprovação da decisão:** autorização para adotar determinada direção técnica.

**Aprovação da implementação:** autorização para executar as mudanças propostas, conforme o risco e o escopo.

A execução deverá seguir os procedimentos do Pilar Desenvolvimento.

## 15. Decisões técnicas específicas de cada projeto

A metodologia deverá separar princípios arquiteturais universais das escolhas técnicas específicas de uma aplicação.

Exemplos de decisões específicas:

- Utilizar React.
- Utilizar Next.js.
- Utilizar Supabase.
- Utilizar determinado serviço de hospedagem.
- Adotar determinada biblioteca de componentes.

Essas escolhas não deverão ser transformadas em regras obrigatórias para todos os projetos.

Cada aplicação deverá registrar suas próprias decisões, considerando suas necessidades e restrições.

## 16. Documentação arquitetural

Os registros deverão ser mantidos em local conhecido e acessível aos agentes.

Uma organização possível será:

```text
docs/
  architecture/
    decisions/
      ADR-001-escolha-do-framework.md
      ADR-002-estrategia-de-autenticacao.md
      ADR-003-organizacao-de-modulos.md
```

A estrutura poderá ser adaptada às convenções do projeto.

O agente deverá evitar criar documentação duplicada ou dispersa.

## 17. Continuidade entre sessões e agentes

Ao iniciar uma nova sessão de desenvolvimento, o agente deverá identificar as decisões arquiteturais relevantes para o trabalho solicitado.

Deverá utilizar os registros existentes para compreender:

- Quais soluções foram adotadas.
- Por que foram escolhidas.
- Quais restrições permanecem vigentes.
- Quais decisões foram substituídas.
- Quais mudanças estão pendentes de aprovação.

A continuidade arquitetural não deverá depender exclusivamente do histórico de conversas com um assistente específico.

## 18. Recomendações de recursos especializados

Quando uma decisão arquitetural exigir conhecimento específico, o agente poderá recomendar skills, agentes especializados, plugins ou ferramentas adequadas.

Exemplos:

- Revisão de arquitetura.
- Análise de segurança.
- Avaliação de dependências.
- Modelagem de dados.
- Análise de desempenho.
- Revisão de integrações.
- Avaliação de custos de infraestrutura.

O agente deverá verificar a disponibilidade e a adequação dos recursos antes de recomendá-los como utilizáveis.

Instalações, permissões e adoções deverão respeitar o catálogo e a governança definidos no Pilar Desenvolvimento.

## 19. Critérios de conformidade

A diretriz estará sendo respeitada quando:

- As decisões relevantes forem registradas.
- Os registros apresentarem justificativas compreensíveis.
- As alternativas forem avaliadas proporcionalmente à importância da decisão.
- As decisões vigentes forem respeitadas.
- Mudanças arquiteturais não forem executadas silenciosamente.
- O histórico de decisões for preservado.
- As revisões possuírem justificativa concreta.
- A documentação permitir continuidade entre sessões.
- O agente distinguir aprovação arquitetural de autorização de implementação.
- As escolhas técnicas específicas não forem impostas a todos os projetos.

## 20. Regra fundamental

**A arquitetura deverá evoluir por necessidade justificada e decisão consciente, nunca por preferência momentânea do agente.**

Toda escolha relevante deverá possuir contexto, justificativa e histórico suficientes para permitir que o projeto continue evoluindo com consistência.