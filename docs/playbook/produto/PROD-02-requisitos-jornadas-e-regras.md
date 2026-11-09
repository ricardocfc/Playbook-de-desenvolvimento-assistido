# PROD-02 — Requisitos, Jornadas e Regras de Negócio

**Pilar:** 01 — Produto  
**Versão:** 1.1  
**Status:** Aprovado  
**Aplicação:** Todos os projetos desenvolvidos com a metodologia.

---

## 1. Objetivo

Estabelecer um processo padronizado para identificar, organizar, documentar e validar os requisitos de um sistema a partir das jornadas de seus usuários.

Todo requisito funcional deverá estar vinculado a pelo menos uma jornada e aos perfis de usuário envolvidos.

A metodologia deverá assegurar que nenhuma funcionalidade seja implementada sem uma finalidade identificável dentro da experiência ou do processo operacional de seus usuários.

## 2. Princípio fundamental

**O desenvolvimento funcional será orientado por jornadas de usuário.**

O agente não deverá começar pela criação de telas, formulários, tabelas ou componentes.

Primeiro, deverá compreender:

1. Quem utilizará a funcionalidade.
2. Qual objetivo esse usuário pretende alcançar.
3. Quais atividades precisará executar.
4. Como o sistema deverá responder a essas atividades.
5. Quais condições determinam o sucesso da jornada.

Somente depois deverão ser identificados os requisitos funcionais necessários.

## 3. Hierarquia dos elementos

A organização dos requisitos seguirá esta estrutura conceitual:

**Produto → Funcionalidade → Jornada → Etapas → Requisitos**

Essa estrutura representa a organização principal da documentação, mas não impede relacionamentos entre diferentes funcionalidades e jornadas.

Uma funcionalidade poderá reunir jornadas de vários perfis.

Uma jornada poderá envolver múltiplos perfis, especialmente quando existir transferência de responsabilidade.

Um requisito poderá atender a várias jornadas, mantendo um único identificador.

Toda jornada deverá identificar seus participantes e suas responsabilidades.

## 4. Identificação dos perfis de usuário

Antes de detalhar as jornadas, o agente deverá identificar os perfis que interagem com o produto.

Para cada perfil, registrar:

- Identificador único.
- Nome do perfil.
- Descrição.
- Objetivos.
- Responsabilidades.
- Funcionalidades utilizadas.
- Limitações e permissões conhecidas.

Os perfis representam responsabilidades funcionais, não necessariamente cargos ou contas individuais.

O agente não deverá presumir que perfis diferentes possuem as mesmas permissões.

## 5. Mapeamento das jornadas

Cada jornada deverá representar um processo ou objetivo identificável na utilização do sistema.

Para cada jornada, registrar:

- Identificador único.
- Nome.
- Funcionalidade relacionada.
- Perfil ou perfis participantes.
- Objetivo.
- Evento que inicia a jornada.
- Condições necessárias para iniciá-la.
- Sequência principal de atividades.
- Resultado esperado.
- Condição de encerramento.
- Exceções e caminhos alternativos.
- Relação com outras jornadas.

O agente deverá descrever inicialmente as atividades em linguagem de negócio, evitando antecipar decisões sobre telas, componentes ou tecnologias.

## 6. Jornadas com múltiplos usuários

Quando uma funcionalidade envolver diferentes perfis, o agente deverá identificar as jornadas correspondentes e os pontos de interação entre elas.

Deverá esclarecer:

- Quem inicia o processo.
- Quem registra informações.
- Quem consulta os registros.
- Quem possui autoridade para aprovar ou rejeitar ações.
- Quem pode modificar o estado do processo.
- Quando a responsabilidade passa de um usuário para outro.
- Qual evento encerra o processo.

As transições de responsabilidade deverão ser documentadas explicitamente.

Uma atividade concluída por determinado usuário não implica necessariamente a conclusão definitiva do processo.

## 7. Identificação dos requisitos funcionais

Os requisitos deverão ser derivados das jornadas.

Cada requisito funcional deverá possuir:

- Identificador único.
- Descrição objetiva.
- Jornada ou jornadas relacionadas.
- Etapa da jornada atendida.
- Perfis envolvidos.
- Comportamento esperado do sistema.
- Condições de execução.
- Regras de negócio aplicáveis.
- Resultado esperado.
- Critérios de aceitação associados.
- Situação de aprovação.

Um requisito não poderá ser aprovado para implementação se sua finalidade dentro das jornadas não estiver identificada.

## 8. Requisitos compartilhados

Quando um requisito atender a mais de uma jornada, o agente deverá registrar os vínculos correspondentes.

Não deverá duplicar requisitos apenas porque são utilizados por perfis diferentes.

Entretanto, deverá distinguir comportamentos ou permissões diferentes quando necessário.

Exemplo:

A consulta a um registro de manutenção poderá ser utilizada pelo funcionário e pelo síndico.

Caso os perfis possuam permissões diferentes, essas diferenças deverão ser explicitadas nas regras de negócio.

## 9. Regras de negócio

As regras de negócio estabelecem condições, restrições e decisões que governam o funcionamento do produto.

Cada regra deverá possuir:

- Identificador.
- Descrição.
- Requisitos relacionados.
- Jornadas impactadas.
- Condições de aplicação.
- Exceções.
- Origem da decisão.
- Situação de aprovação.

O agente deverá investigar regras relacionadas a:

- Permissões.
- Validações.
- Aprovações.
- Restrições.
- Cálculos.
- Mudanças de estado.
- Prazos.
- Dependências entre processos.

As regras não deverão ser presumidas quando dependerem de decisões do desenvolvedor.

## 10. Estados e transições

Quando uma funcionalidade possuir etapas de processamento, o agente deverá identificar os estados relevantes.

Exemplo ilustrativo:

**Manutenção iniciada → Em execução → Aguardando aprovação → Concluída**

Para cada transição, registrar:

- Estado de origem.
- Evento que provoca a mudança.
- Perfil autorizado.
- Condições necessárias.
- Estado de destino.
- Consequências da transição.

Estados e transições deverão refletir as jornadas aprovadas.

## 11. Exceções e fluxos alternativos

O agente deverá investigar situações em que a jornada não segue seu fluxo principal.

Exemplos:

- Informações obrigatórias ausentes.
- Aprovação rejeitada.
- Processo cancelado.
- Usuário sem permissão.
- Registro duplicado.
- Falha em serviço externo.
- Tentativa de executar uma ação em estado incompatível.

As exceções identificadas deverão ser apresentadas ao desenvolvedor para validação.

O agente não poderá criar comportamentos de negócio relevantes sem aprovação.

## 12. Requisitos não funcionais

Requisitos de segurança, desempenho, disponibilidade, acessibilidade e outras qualidades técnicas deverão ser documentados.

Esses requisitos poderão estar relacionados a várias jornadas ou ao produto como um todo.

Não será obrigatório criar jornadas artificiais para justificar requisitos transversais.

Entretanto, deverá existir uma justificativa documentada para sua inclusão.

A definição das soluções técnicas para atendê-los pertence ao Pilar Arquitetura.

## 13. Classificação das informações

Todas as informações relevantes deverão ser classificadas como:

- **Confirmado:** aprovado pelo desenvolvedor.
- **Sugerido:** proposto pelo agente, aguardando decisão.
- **Pendente:** necessita de esclarecimento.
- **Descartado:** avaliado e rejeitado.

Somente requisitos confirmados poderão seguir para implementação.

Requisitos pendentes poderão permanecer documentados, desde que não sejam tratados como decisões aprovadas.

## 14. Matriz de rastreabilidade

O agente deverá manter uma matriz relacionando:

**Perfil → Jornada → Etapa → Requisito → Regra de negócio → Critério de aceitação**

A matriz deverá permitir identificar:

- Quais requisitos atendem cada jornada.
- Quais jornadas dependem de determinado requisito.
- Quais perfis serão afetados por uma alteração.
- Quais regras de negócio governam cada comportamento.
- Quais critérios permitem verificar o funcionamento esperado.

Na etapa de desenvolvimento, essa rastreabilidade deverá ser estendida às tarefas e aos testes.

## 15. Análise de completude

Antes de encaminhar os requisitos para planejamento técnico, o agente deverá verificar:

1. Todas as jornadas possuem objetivos identificáveis?
2. Todas as jornadas possuem perfis participantes?
3. As etapas principais estão documentadas?
4. Existem transferências de responsabilidade não esclarecidas?
5. Todos os requisitos funcionais estão vinculados a jornadas?
6. Existem requisitos duplicados ou contraditórios?
7. As regras de negócio relevantes foram identificadas?
8. Os fluxos alternativos importantes foram considerados?
9. Existem decisões pendentes que impedem a implementação?
10. Os critérios de aceitação estão definidos ou encaminhados para detalhamento no PROD-04?

## 16. Gestão de alterações

Quando uma jornada for modificada, o agente deverá identificar os requisitos e regras de negócio afetados.

Quando um requisito for modificado ou removido, deverá verificar quais jornadas dependem dele.

Não será permitido remover silenciosamente um requisito utilizado por outras jornadas.

Alterações deverão preservar a rastreabilidade e seguir os procedimentos de gestão de mudanças do Pilar Desenvolvimento.

## 17. Critérios de conclusão

O levantamento será considerado suficientemente completo quando:

- Os perfis envolvidos estiverem identificados.
- As jornadas necessárias ao escopo estiverem documentadas.
- Os requisitos funcionais estiverem vinculados às jornadas.
- As principais regras de negócio estiverem definidas.
- Os fluxos alternativos relevantes estiverem considerados.
- As dependências entre jornadas estiverem claras.
- Não existirem pendências críticas para o escopo que será implementado.
- O desenvolvedor tiver aprovado os requisitos.

Não será necessário mapear antecipadamente todas as jornadas futuras do produto.

## 18. Requisições unitárias e vinculação entre SPECs

Uma **requisição unitária** representa uma finalidade delimitada identificada durante a interpretação de uma solicitação do desenvolvedor. Um prompt poderá originar uma ou mais requisições unitárias. A decomposição não deverá produzir artificialmente implementações independentes quando existir uma única finalidade funcional.

Toda nova requisição unitária deverá passar pelo fluxo padrão de interpretação, recuperação do contexto, verificação do estado atual do sistema, identificação de escopo, classificação funcional e análise de impactos, independentemente da classificação de requisições anteriores.

Para requisições funcionais, o agente deverá identificar uma **SPEC principal**, correspondente à funcionalidade que coordena a requisição, e, quando aplicável, **SPECs associadas**. A classificação deverá considerar a finalidade da requisição atual e as responsabilidades funcionais existentes, não simplesmente herdar a SPEC principal de uma requisição histórica.

A SPEC representa um agrupamento funcional de jornadas e requisitos, preservando a hierarquia **Produto → Funcionalidade → Jornada → Etapas → Requisitos**. A requisição é a unidade de mudança, e não um nível substitutivo dessa hierarquia. Uma SPEC poderá acolher diversas requisições ao longo de sua evolução.

Quando a requisição envolver mais de uma SPEC:

- A especificação e os registros operacionais da requisição deverão permanecer centralizados na SPEC principal.
- As SPECs associadas deverão manter referências de localização para a requisição e sua SPEC principal, sem duplicar planejamento, tarefas, critérios ou histórico operacional.
- Cada regra funcional deverá possuir uma localização canônica; referências cruzadas não transferem a titularidade das regras entre domínios.
- A centralização documental não determina a localização física do código nem modifica as responsabilidades estabelecidas pelo Pilar Arquitetura.

Uma nova requisição que afete uma funcionalidade anterior deverá ser classificada de maneira independente. A relação histórica deverá ser considerada na análise de impactos, mas não determinará automaticamente sua SPEC principal.

A classificação proposta e suas dependências deverão ser verificadas antes do planejamento; ambiguidades relevantes deverão ser apresentadas ao desenvolvedor. As atualizações seguirão as autorizações e os limites de escopo definidos no Pilar Desenvolvimento.

## 19. Regra fundamental

**Nenhum requisito funcional poderá ser implementado sem vínculo com uma jornada de usuário aprovada.**

O agente deverá preservar a relação entre a necessidade do usuário, o comportamento esperado do sistema e as regras de negócio que governam sua execução.

A implementação técnica deverá servir às jornadas aprovadas, e não determinar artificialmente quais jornadas existirão.