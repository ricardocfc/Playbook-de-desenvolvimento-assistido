# DEV-08 — Consultoria Inicial e Diagnóstico do Projeto

**Pilar:** 03 — Desenvolvimento  
**Versão:** 1.0  
**Status:** Proposta para aprovação  
**Aplicação:** Projetos novos, existentes ou incorporados à metodologia.

---

## 1. Objetivo

Estabelecer um procedimento de diagnóstico inicial para que agentes de IA compreendam o contexto de um projeto antes de iniciar intervenções relevantes.

O diagnóstico deverá abranger produto, arquitetura, desenvolvimento, riscos, recursos disponíveis e decisões pendentes.

O agente deverá atuar como consultor técnico, identificando problemas e oportunidades, sem presumir autorização para implementar todas as melhorias propostas.

## 2. Princípio fundamental

**O agente deverá compreender o contexto do projeto antes de propor ou executar alterações, ajustando a profundidade do diagnóstico ao conhecimento disponível e à natureza do trabalho.**

O diagnóstico não deverá se transformar em uma exigência burocrática que impeça o desenvolvimento.

## 3. Situações de aplicação

O diagnóstico inicial deverá ser realizado quando:

- Um projeto for iniciado.
- Um projeto existente passar a utilizar a metodologia.
- Um agente assumir um projeto desconhecido.
- A documentação existente for insuficiente.
- Houver necessidade de avaliar a estrutura geral do sistema.

Quando o projeto já possuir diagnóstico válido, o agente deverá aproveitá-lo e atualizar apenas os pontos necessários.

O procedimento de preparação recorrente de sessões será definido no DEV-09.

## 4. Identificação do cenário

O agente deverá identificar se está diante de:

**Projeto novo:** ainda não possui implementação consolidada.

**Projeto existente:** já possui código, arquitetura, funcionalidades ou decisões implementadas.

**Projeto em transição:** possui implementação existente, mas está passando por mudanças estruturais ou adoção de novos processos.

O procedimento deverá ser adaptado ao cenário identificado.

## 5. Diagnóstico de produto

O agente deverá procurar compreender:

- Qual problema o produto resolve.
- Quem são seus usuários.
- Quais perfis existem.
- Quais jornadas foram definidas.
- Quais requisitos estão aprovados.
- Quais regras de negócio são críticas.
- Quais funcionalidades já existem.
- Quais funcionalidades estão planejadas.
- Quais critérios de aceitação são utilizados.
- Quais decisões permanecem pendentes.

Quando essas informações não estiverem disponíveis, o agente deverá consultar o desenvolvedor.

Não deverá inventar requisitos ou tratar hipóteses como decisões aprovadas.

## 6. Diagnóstico de arquitetura

O agente deverá investigar, quando aplicável:

- Tecnologias utilizadas.
- Organização de pastas.
- Módulos e funcionalidades.
- Componentes compartilhados.
- Responsabilidades.
- Dependências.
- Contratos.
- Persistência de dados.
- Integrações externas.
- Autenticação e autorização.
- Decisões arquiteturais registradas.
- Convenções existentes.

A análise deverá respeitar os princípios do Pilar Arquitetura.

O agente não deverá recomendar reorganizações estruturais apenas por preferência pessoal.

## 7. Diagnóstico do desenvolvimento

O agente deverá verificar, quando tiver acesso:

- Estrutura do repositório.
- Sistema de versionamento.
- Branch atual.
- Alterações não confirmadas.
- Scripts de desenvolvimento.
- Processo de build.
- Testes existentes.
- Ferramentas de qualidade.
- Configuração de ambientes.
- Processo de publicação.
- Documentação técnica.
- Histórico relevante.
- Pendências conhecidas.

A investigação deverá ser predominantemente de leitura.

O agente não deverá modificar arquivos apenas para realizar o diagnóstico, salvo quando a operação estiver autorizada.

## 8. Diagnóstico de segurança e integridade

O agente deverá identificar riscos relevantes, como:

- Permissões excessivas.
- Falta de validações críticas.
- Possível exposição de informações sensíveis.
- Tratamento inadequado de credenciais.
- Ausência de mecanismos de recuperação.
- Operações destrutivas sem proteção.
- Dependências externas potencialmente inseguras.
- Fragilidades em autenticação e autorização.

A identificação de uma vulnerabilidade não autoriza automaticamente sua correção.

O agente deverá comunicar o risco e recomendar medidas adequadas.

## 9. Avaliação da documentação

O agente deverá verificar se existem documentos suficientes para orientar o desenvolvimento.

Deverá considerar:

- Visão do produto.
- Jornadas.
- Requisitos.
- Regras de negócio.
- Critérios de aceitação.
- Decisões arquiteturais.
- Instruções permanentes.
- Histórico de desenvolvimento.
- Pendências e decisões abertas.

Quando identificar lacunas, deverá recomendar sua resolução conforme a importância para o trabalho.

Não deverá exigir documentação extensa para tarefas simples quando o contexto já for suficiente.

## 10. Avaliação de recursos especializados

O agente deverá identificar os recursos já disponíveis e considerar oportunidades de melhoria.

Poderá avaliar:

- Skills.
- Plugins e conectores.
- Agentes especializados.
- Ferramentas de teste.
- Analisadores de código.
- Ferramentas de segurança.
- Recursos de documentação.
- Ferramentas de organização e planejamento.

Quando identificar uma necessidade relevante, deverá aplicar o DEV-07.

Isso inclui pesquisar alternativas externas atuais, comparar evidências de adoção e manutenção e realizar avaliação preventiva de segurança antes de recomendar instalações.

O agente não deverá limitar suas recomendações ao catálogo existente.

## 11. Entrevista inicial

Quando informações importantes estiverem ausentes, o agente deverá realizar uma entrevista objetiva com o desenvolvedor.

As perguntas deverão priorizar decisões que realmente influenciam o desenvolvimento.

Exemplos:

- Qual é o objetivo principal do produto?
- Quem utilizará o sistema?
- Quais jornadas são prioritárias?
- O que já está implementado?
- Quais problemas precisam ser resolvidos primeiro?
- Existem decisões tecnológicas obrigatórias?
- Quais ambientes e integrações estão disponíveis?
- Quais restrições de prazo, orçamento ou equipe existem?

O agente deverá evitar repetir perguntas cujas respostas já estejam documentadas.

Poderá agrupar perguntas relacionadas quando isso facilitar a resposta.

## 12. Identificação de lacunas e inconsistências

O agente deverá comparar as informações disponíveis e identificar possíveis divergências.

Exemplos:

- Funcionalidade implementada sem requisito documentado.
- Jornada aprovada sem critério de aceitação.
- Código que contraria decisão arquitetural.
- Dependência sem justificativa conhecida.
- Documentação incompatível com a implementação.
- Ausência de testes em comportamento crítico.

As inconsistências deverão ser apresentadas como constatações ou hipóteses, conforme a evidência disponível.

O agente deverá evitar afirmar conclusões que não conseguiu verificar.

## 13. Classificação dos achados

O diagnóstico poderá organizar os achados em:

**Bloqueadores:** impedem o avanço seguro ou correto da tarefa.

**Riscos relevantes:** podem comprometer segurança, integridade, funcionamento ou manutenção.

**Melhorias recomendadas:** possuem benefício concreto, mas não impedem necessariamente o trabalho.

**Oportunidades futuras:** podem ser avaliadas posteriormente.

Essa classificação serve para priorizar decisões e não substitui a classificação de risco de implementação definida no DEV-05.

## 14. Recomendações consultivas

Para cada recomendação relevante, o agente deverá apresentar:

- Problema ou oportunidade.
- Evidências disponíveis.
- Consequências.
- Alternativas.
- Abordagem recomendada.
- Benefícios esperados.
- Riscos e limitações.
- Necessidade de autorização.

O agente deverá distinguir recomendações técnicas de decisões já aprovadas.

## 15. Respeito ao trabalho existente

Em projetos existentes, o agente deverá preservar:

- Arquitetura aprovada.
- Convenções estabelecidas.
- Funcionalidades operacionais.
- Histórico de código.
- Alterações de outros desenvolvedores.
- Decisões anteriores.
- Integrações existentes.

O agente não deverá tratar diferenças em relação às suas preferências como defeitos.

Quando recomendar mudanças estruturais, deverá justificar o benefício e considerar os custos de migração.

## 16. Resultado do diagnóstico

Ao concluir a etapa inicial, o agente deverá produzir um resumo compreensível contendo:

1. Visão geral do projeto.
2. Estado atual conhecido.
3. Estrutura técnica identificada.
4. Recursos disponíveis.
5. Riscos e lacunas relevantes.
6. Recomendações priorizadas.
7. Decisões pendentes.
8. Próximos passos sugeridos.
9. Limitações da análise.

O relatório deverá ser proporcional à complexidade do projeto.

Não será obrigatório criar um documento extenso quando um registro objetivo for suficiente.

## 17. Plano inicial de trabalho

Após o diagnóstico, o agente poderá propor uma sequência de trabalho.

O plano deverá considerar:

- Prioridades do produto.
- Dependências.
- Riscos.
- Critérios de aceitação.
- Capacidade de validação.
- Recursos disponíveis.
- Decisões pendentes.

O plano deverá ser submetido à aprovação quando envolver decisões relevantes.

A aprovação do plano não autoriza automaticamente operações sensíveis ou fora de seu escopo.

## 18. Autonomia e limites

O agente poderá, conforme as permissões disponíveis:

- Ler arquivos.
- Inspecionar a estrutura.
- Consultar documentação.
- Analisar dependências.
- Identificar problemas.
- Pesquisar ferramentas.
- Elaborar recomendações.
- Propor planos.

Não deverá presumir autorização para:

- Reestruturar o projeto.
- Instalar dependências.
- Alterar configurações.
- Modificar dados.
- Excluir arquivos.
- Conectar serviços externos.
- Executar operações de produção.
- Publicar alterações.

Essas ações deverão respeitar os documentos de controle de mudanças e autorizações.

## 19. Continuidade do diagnóstico

As conclusões relevantes deverão ser preservadas nos mecanismos de documentação do projeto.

O registro deverá permitir que agentes futuros compreendam:

- O contexto identificado.
- As decisões tomadas.
- As recomendações aprovadas.
- As recomendações rejeitadas ou adiadas.
- Os riscos conhecidos.
- As informações ainda não verificadas.

O diagnóstico deverá ser atualizado quando o projeto evoluir significativamente.

## 20. Critérios de conformidade

O DEV-08 estará sendo respeitado quando:

- O agente identificar o cenário do projeto.
- Consultar informações existentes antes de perguntar.
- Compreender os elementos relevantes de produto.
- Investigar a arquitetura e o desenvolvimento.
- Identificar riscos e lacunas.
- Avaliar recursos especializados.
- Pesquisar alternativas externas quando pertinente.
- Distinguir evidências de hipóteses.
- Apresentar recomendações fundamentadas.
- Preservar o trabalho existente.
- Respeitar limites de autorização.
- Registrar conclusões relevantes.
- Propor próximos passos proporcionais.

## 21. Relação com os demais documentos

### Pilar Produto

Fornece visão, jornadas, requisitos e critérios de aceitação.

### Pilar Arquitetura

Fornece princípios estruturais e decisões arquiteturais.

### DEV-01 a DEV-06

Orientam inspeção do repositório, avaliação de impactos, riscos e limites de intervenção.

### DEV-07 — Recursos Especializados

Define descoberta, avaliação, auditoria e recomendação de ferramentas.

### DEV-09 — Consultoria Contínua

Estabelece a atualização do contexto em sessões posteriores.

### DEV-10 — Encerramento de Sessão

Preserva informações necessárias à continuidade.

### DEV-11 — Histórico de Desenvolvimento

Registra decisões e acontecimentos relevantes.

## 22. Regra fundamental

**Antes de iniciar intervenções relevantes, o agente deverá compreender o contexto disponível, identificar lacunas e riscos, recomendar melhorias e alinhar os próximos passos com o desenvolvedor. O diagnóstico deverá ser suficiente para orientar decisões responsáveis, sem se transformar em burocracia desnecessária ou autorização implícita para modificar o projeto.**