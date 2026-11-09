# PROD-03 — Evolução Contínua do Produto

**Pilar:** 01 — Produto  
**Versão:** 1.1  
**Status:** Proposta revisada para aprovação  
**Aplicação:** Todos os projetos desenvolvidos com a metodologia.

---

## 1. Objetivo

Estabelecer um processo contínuo de acompanhamento, avaliação e evolução dos produtos desenvolvidos com auxílio de inteligência artificial.

A metodologia reconhece que a visão inicial de um produto pode ser incompleta e que novas necessidades, oportunidades e limitações serão descobertas durante o desenvolvimento e a utilização do sistema.

O agente deverá contribuir ativamente para essa evolução, preservando a coerência do produto, a qualidade do desenvolvimento e o controle decisório do desenvolvedor.

## 2. Princípio fundamental

**A visão inicial orienta o desenvolvimento, mas não limita permanentemente a evolução do produto.**

O agente deverá reconhecer oportunidades de melhoria e expansão, sem presumir que toda oportunidade identificada deva ser implementada.

A evolução deverá ser orientada pelo valor proporcionado aos usuários, pela coerência com a proposta do produto e pelas prioridades definidas pelo desenvolvedor.

O agente também deverá identificar quando recursos especializados podem aumentar a produtividade, reduzir riscos ou melhorar a qualidade do produto.

## 3. Responsabilidades do agente

O agente deverá:

- Acompanhar a evolução funcional do produto.
- Consultar a visão e as jornadas documentadas.
- Identificar novas necessidades e oportunidades.
- Reconhecer funcionalidades incompletas.
- Identificar jornadas que possam ser melhoradas.
- Sugerir funcionalidades complementares.
- Avaliar possíveis impactos sobre usuários e processos.
- Identificar conflitos com decisões anteriores.
- Apresentar alternativas e recomendações.
- **Identificar oportunidades de utilização de skills, plugins, agentes especializados e ferramentas complementares.**
- **Reavaliar os recursos disponíveis conforme o produto evolui.**
- Registrar decisões aprovadas, rejeitadas ou adiadas.

O agente não poderá modificar unilateralmente a visão do produto, introduzir novos requisitos funcionais ou instalar recursos externos sem aprovação.

## 4. Momentos de reavaliação

A evolução do produto deverá ser considerada em diferentes momentos.

### 4.1. Início de cada sessão

O agente deverá consultar o estado atual do produto e identificar mudanças relevantes desde a última sessão.

Deverá verificar:

- Funcionalidades recentemente implementadas.
- Jornadas criadas ou modificadas.
- Requisitos adicionados ou removidos.
- Decisões de produto ainda pendentes.
- Oportunidades identificadas anteriormente.
- Possíveis necessidades decorrentes das mudanças recentes.
- **Recursos especializados existentes e novas necessidades de especialização.**

A análise deverá ser proporcional à complexidade e às alterações ocorridas.

Não será necessário realizar uma revisão extensa quando não houver mudanças relevantes.

### 4.2. Criação de uma nova funcionalidade

Antes de especificar uma nova funcionalidade, o agente deverá avaliar:

- Sua relação com a visão do produto.
- Os perfis de usuário envolvidos.
- As jornadas existentes.
- A necessidade de novas jornadas.
- As dependências com funcionalidades existentes.
- Possíveis alternativas de solução.
- Eventuais impactos sobre a experiência dos usuários.
- **A existência de recursos especializados que possam contribuir para sua especificação, implementação ou validação.**

### 4.3. Alteração de uma funcionalidade existente

Quando uma funcionalidade for modificada, o agente deverá verificar se a alteração:

- Modifica alguma jornada.
- Introduz novos requisitos.
- Altera regras de negócio.
- Afeta outros perfis.
- Cria dependências funcionais.
- Torna algum comportamento anterior desnecessário.
- Exige conhecimentos ou ferramentas especializadas ainda não disponíveis.

As alterações aprovadas deverão ser refletidas na documentação correspondente.

### 4.4. Conclusão de um módulo

Ao concluir um módulo relevante, o agente deverá avaliar:

- Se as jornadas previstas foram atendidas.
- Se existem lacunas funcionais.
- Se surgiram oportunidades complementares.
- Se a implementação revelou novas necessidades.
- Se existem melhorias que devem ser consideradas futuramente.
- Se recursos especializados poderiam contribuir para melhorar a qualidade, os testes ou a manutenção do módulo.

Essa avaliação não deverá impedir o encerramento do módulo quando os critérios de aceitação estiverem satisfeitos.

### 4.5. Mudanças estratégicas

Quando o desenvolvedor modificar objetivos, público-alvo, proposta de valor ou modelo de negócio, o agente deverá recomendar uma revisão mais ampla da visão do produto e das capacidades especializadas necessárias.

## 5. Identificação de oportunidades

O agente poderá sugerir:

- Novas jornadas.
- Melhorias em jornadas existentes.
- Funcionalidades complementares.
- Simplificação de processos.
- Automatização de atividades.
- Integrações funcionais.
- Novos perfis de usuário.
- Melhorias de experiência.
- Possibilidades de expansão comercial.
- Recursos especializados que contribuam para essas oportunidades.

Cada sugestão deverá estar vinculada a uma necessidade, problema ou oportunidade identificável.

Sugestões não deverão ser apresentadas apenas porque determinada funcionalidade ou ferramenta é comum em sistemas semelhantes.

## 6. Classificação das oportunidades

As oportunidades deverão receber uma das seguintes situações:

**Identificada:** oportunidade registrada, ainda não avaliada.

**Em avaliação:** oportunidade em discussão.

**Aprovada:** desenvolvimento autorizado em princípio, sujeito ao planejamento.

**Adiada:** oportunidade válida, mas não prioritária.

**Descartada:** oportunidade rejeitada.

**Implementada:** oportunidade concluída e validada.

Uma oportunidade aprovada não será considerada automaticamente pronta para implementação.

Antes da execução, deverá passar pelo levantamento de jornadas e requisitos previsto no PROD-02 e pelos critérios de aceitação do PROD-04.

## 7. Priorização

O agente deverá ajudar o desenvolvedor a priorizar oportunidades considerando:

- Valor para os usuários.
- Relevância para a proposta do produto.
- Frequência da necessidade.
- Impacto operacional.
- Urgência.
- Dependências funcionais.
- Esforço estimado.
- Riscos e incertezas.

As estimativas deverão ser apresentadas como avaliações, não como certezas.

O agente poderá recomendar prioridades, mas a decisão final pertence ao desenvolvedor.

## 8. Gestão da visão do produto

A visão documentada no PROD-01 deverá permanecer como referência.

Entretanto, poderá ser revisada quando ocorrerem mudanças relevantes.

O agente deverá distinguir:

- Expansão coerente com a visão existente.
- Ajuste de prioridade.
- Alteração de jornada.
- Mudança de escopo.
- Mudança estratégica da proposta do produto.

Mudanças estratégicas deverão ser explicitamente aprovadas e registradas.

O agente não deverá alterar silenciosamente a finalidade original do produto.

## 9. Gestão das jornadas

Toda evolução funcional deverá respeitar a rastreabilidade estabelecida no PROD-02.

Quando uma nova oportunidade for aprovada, o agente deverá:

1. Identificar os perfis envolvidos.
2. Verificar se existem jornadas relacionadas.
3. Propor novas jornadas quando necessário.
4. Identificar requisitos afetados.
5. Verificar possíveis conflitos.
6. Atualizar a documentação após aprovação.

Não será permitido adicionar requisitos funcionais desvinculados de jornadas aprovadas.

## 10. Gestão de ideias abandonadas

O desenvolvedor poderá desistir de ideias ou funcionalidades em qualquer momento.

O agente deverá distinguir entre:

- Ideia ainda não implementada.
- Funcionalidade em desenvolvimento.
- Funcionalidade já integrada ao produto.
- Funcionalidade utilizada em produção.

Quando uma ideia for abandonada, deverá atualizar sua situação na documentação de produto.

Caso exista código associado, deverá encaminhar a alteração aos procedimentos de gestão de mudanças do Pilar Desenvolvimento.

O agente não deverá presumir que abandonar uma ideia autoriza excluir imediatamente seus arquivos, dados ou dependências.

## 11. Registro de oportunidades

O projeto deverá manter um registro de evolução contendo:

- Identificador.
- Descrição da oportunidade.
- Origem.
- Problema ou necessidade relacionada.
- Perfis potencialmente beneficiados.
- Jornadas envolvidas.
- Valor esperado.
- Prioridade.
- Situação.
- Decisão tomada.
- Justificativa.
- Data da última avaliação.

O registro deverá permitir recuperar oportunidades anteriormente discutidas sem depender exclusivamente do histórico das conversas com a IA.

## 12. Identificação e recomendação de recursos especializados

### 12.1. Objetivo

O agente deverá avaliar continuamente se o projeto poderá se beneficiar de conhecimentos, procedimentos, integrações ou capacidades especializadas.

Essa avaliação deverá considerar as necessidades reais do produto, sua arquitetura, suas funcionalidades e o estágio atual do desenvolvimento.

O objetivo é aumentar a produtividade, a qualidade técnica e a confiabilidade das implementações.

### 12.2. Categorias de recursos

O agente poderá recomendar:

**Skills:** conjuntos especializados de instruções, conhecimentos ou procedimentos que orientam o agente na execução de determinadas atividades.

**Plugins e conectores:** recursos que permitem integração com serviços, plataformas, ferramentas e fontes de informação externas.

**Agentes especializados:** agentes ou funções especializadas que podem assumir atividades específicas, como revisão de código, testes, arquitetura ou análise de segurança.

**Ferramentas complementares:** aplicações e utilitários que possam contribuir para o desenvolvimento, a validação ou a operação do produto.

A nomenclatura e a disponibilidade desses recursos poderão variar conforme a plataforma utilizada.

### 12.3. Identificação contextual

O agente deverá relacionar as necessidades do projeto às especialidades potencialmente úteis.

Exemplos:

- Desenvolvimento de interfaces: especialidades em UX, acessibilidade e design de interfaces.
- Integrações externas: ferramentas de documentação e validação de APIs.
- Sistemas com dados sensíveis: especialidades em segurança e proteção de dados.
- Aplicações com grande volume de usuários: especialidades em desempenho e escalabilidade.
- Sistemas com processos complexos: especialidades em testes funcionais e validação de regras de negócio.
- Aplicações comerciais: especialidades em SEO, análise de conversão ou experiência do usuário, quando relevantes.

Esses exemplos não representam uma lista obrigatória.

### 12.4. Pesquisa e verificação

Sempre que houver acesso a mecanismos de descoberta de recursos, o agente deverá consultar as opções disponíveis e avaliar sua adequação ao projeto.

O agente deverá distinguir claramente:

- Recursos que já estão disponíveis no ambiente.
- Recursos existentes, mas ainda não instalados.
- Recursos cuja disponibilidade não foi verificada.
- Capacidades que precisariam ser desenvolvidas especificamente para o projeto.

O agente não deverá inventar nomes, capacidades ou compatibilidades de ferramentas.

O conhecimento prévio do agente poderá orientar recomendações, mas informações sobre disponibilidade, manutenção, permissões e compatibilidade deverão ser verificadas quando relevantes.

### 12.5. Critérios de recomendação

Antes de recomendar um recurso, o agente deverá avaliar:

1. Qual problema ou necessidade ele atende.
2. Qual benefício concreto poderá proporcionar.
3. Se o recurso já está disponível.
4. Se existem alternativas mais simples.
5. Se sua utilização acrescenta complexidade desnecessária.
6. Quais permissões ou acessos exige.
7. Quais riscos técnicos ou de segurança apresenta.
8. Se existem custos adicionais.
9. Se há compatibilidade com o ambiente utilizado.

O agente deverá evitar recomendar recursos apenas por popularidade ou novidade.

### 12.6. Apresentação ao desenvolvedor

Uma recomendação deverá explicar, em linguagem acessível:

- Nome ou categoria do recurso.
- Finalidade.
- Problema que pretende resolver.
- Benefício esperado.
- Momento recomendado para utilização.
- Possíveis custos, riscos e limitações.
- Se exige instalação ou autorização.

Quando a indicação for apenas uma hipótese, o agente deverá deixar isso explícito.

### 12.7. Aprovação e utilização

A recomendação de um recurso não autoriza automaticamente sua instalação, configuração ou utilização.

O desenvolvedor deverá aprovar ações que envolvam instalação, novos acessos, permissões, custos ou mudanças relevantes no ambiente.

A gestão operacional desses recursos seguirá o procedimento DEV-07 — Catálogo de Recursos Especializados.

### 12.8. Reavaliação contínua

O agente deverá reavaliar a utilidade dos recursos conforme o produto evolui.

Poderá recomendar:

- Inclusão de novas especialidades.
- Utilização de recursos já disponíveis.
- Substituição de ferramentas inadequadas.
- Descontinuação de recursos que perderam utilidade.
- Redução de ferramentas redundantes.

A reavaliação deverá ser contextual e proporcional, evitando recomendações repetitivas.

## 13. Comunicação com o desenvolvedor

O agente deverá comunicar oportunidades e recomendações em linguagem natural.

Sempre que possível, deverá explicar:

1. O que identificou.
2. Por que considera relevante.
3. Quem seria beneficiado.
4. Qual mudança ou recurso sugere.
5. Quais impactos são esperados.
6. Se recomenda agir agora ou registrar para o futuro.

O agente deverá evitar interromper tarefas simples com sugestões extensas e não relacionadas.

Recomendações não urgentes poderão ser apresentadas no encerramento da sessão ou registradas para avaliação posterior.

## 14. Relação com os demais pilares

### Produto

O PROD-03 utiliza o PROD-01 como referência de visão e o PROD-02 como referência de jornadas e requisitos.

As funcionalidades aprovadas deverão receber critérios de aceitação conforme o PROD-04.

### Arquitetura

O agente deverá encaminhar oportunidades que envolvam mudanças técnicas relevantes para avaliação arquitetural.

A aprovação de uma oportunidade funcional não representa aprovação automática de uma solução técnica específica.

### Desenvolvimento

Mudanças aprovadas deverão seguir os procedimentos de planejamento, controle de escopo, versionamento, implementação e validação.

As recomendações de recursos especializados deverão seguir o DEV-07, enquanto sua reavaliação entre sessões será coordenada pelo DEV-09.

A análise de evolução não autoriza alterações diretas no código sem respeitar o processo de desenvolvimento.

## 15. Critérios de conformidade

O procedimento estará sendo respeitado quando:

- O agente considerar a evolução do produto nos momentos adequados.
- As sugestões estiverem vinculadas a necessidades identificáveis.
- O desenvolvedor mantiver controle sobre as decisões.
- As jornadas e os requisitos permanecerem atualizados.
- As oportunidades adiadas ou descartadas forem registradas.
- Mudanças relevantes na visão forem documentadas.
- O agente avaliar a necessidade de recursos especializados quando pertinente.
- As recomendações de skills e plugins forem justificadas.
- A disponibilidade e os riscos dos recursos forem considerados.
- Nenhum recurso externo for instalado sem a autorização necessária.
- A análise evolutiva não gerar burocracia desproporcional.
- Nenhuma oportunidade sugerida for implementada sem aprovação.

## 16. Regra fundamental

**O agente deve ajudar o produto a evoluir e identificar as melhores capacidades disponíveis para desenvolvê-lo, sem assumir o controle de sua direção.**

Sua responsabilidade é ampliar a capacidade de análise do desenvolvedor, identificar oportunidades, recomendar recursos especializados e preservar a coerência das decisões ao longo do tempo.