# PROD-04 — Critérios de Aceitação e Validação Funcional

**Pilar:** 01 — Produto  
**Versão:** 1.0  
**Status:** Proposta para aprovação  
**Aplicação:** Todos os projetos desenvolvidos com a metodologia.

---

## 1. Objetivo

Estabelecer critérios objetivos para determinar se uma funcionalidade implementada atende aos requisitos, às regras de negócio e às jornadas de usuário previamente aprovadas.

A metodologia deverá permitir que o desenvolvedor compreenda o que precisa ser verificado, mesmo sem conhecimento aprofundado de programação.

Os critérios de aceitação deverão ser definidos antes da implementação e utilizados como referência para a validação funcional.

## 2. Princípio fundamental

**Uma funcionalidade somente poderá ser considerada concluída quando atender aos critérios de aceitação aprovados.**

A ausência de erros aparentes ou a execução bem-sucedida do código não representa, isoladamente, a conclusão funcional.

O agente deverá demonstrar que os comportamentos implementados correspondem aos requisitos e às jornadas documentadas.

## 3. Responsabilidades do agente

O agente deverá:

- Consultar as jornadas e os requisitos aprovados.
- Identificar os comportamentos que precisam ser validados.
- Propor critérios de aceitação objetivos.
- Considerar fluxos principais e alternativos.
- Identificar regras de negócio que exigem validação.
- Definir resultados esperados.
- Relacionar critérios aos requisitos correspondentes.
- Recomendar formas adequadas de verificação.
- Executar as verificações disponíveis e autorizadas.
- Informar os resultados de maneira compreensível.
- Identificar falhas e pendências.
- Solicitar validação do desenvolvedor quando necessário.

O agente não deverá declarar uma funcionalidade concluída sem evidências suficientes.

## 4. Origem dos critérios de aceitação

Os critérios deverão ser derivados dos elementos aprovados no PROD-02:

- Jornadas.
- Etapas das jornadas.
- Requisitos funcionais.
- Regras de negócio.
- Estados e transições.
- Permissões dos perfis.
- Fluxos alternativos e exceções.

Cada critério deverá possuir vínculo com pelo menos um requisito ou regra de negócio.

Quando um critério estiver associado a uma jornada, essa relação também deverá ser preservada.

## 5. Estrutura dos critérios

Cada critério de aceitação deverá conter:

- Identificador único.
- Requisito relacionado.
- Jornada relacionada, quando aplicável.
- Perfil de usuário envolvido.
- Condições iniciais.
- Ação ou evento.
- Resultado esperado.
- Restrições relevantes.
- Forma prevista de verificação.
- Situação da validação.

Os critérios deverão utilizar linguagem clara, observável e verificável.

Expressões subjetivas, como "a tela deve funcionar bem" ou "o sistema deve ser rápido", não deverão ser aceitas sem parâmetros que permitam avaliação.

## 6. Formato de descrição

Sempre que adequado, os critérios poderão utilizar a estrutura:

**Dado que:** descreve as condições iniciais.

**Quando:** descreve a ação ou evento.

**Então:** descreve o resultado esperado.

Exemplo:

Dado que existe uma manutenção aguardando aprovação,

Quando o síndico aprovar sua conclusão,

Então o sistema deverá registrar a aprovação e atualizar o estado da manutenção para concluída.

Esse formato é recomendado, mas não obrigatório quando outra representação oferecer maior clareza.

## 7. Validação das jornadas

O agente deverá considerar a jornada como uma sequência de atividades, e não apenas como um conjunto de ações independentes.

A validação deverá verificar:

- Se o usuário consegue iniciar a jornada.
- Se as etapas podem ser executadas na ordem esperada.
- Se as informações necessárias estão disponíveis.
- Se as regras de negócio são respeitadas.
- Se as transições de responsabilidade funcionam.
- Se o resultado final corresponde ao objetivo da jornada.

Uma jornada poderá conter requisitos individualmente corretos e ainda apresentar falhas no fluxo completo.

Por isso, a validação integrada da jornada deverá complementar a verificação individual dos requisitos.

## 8. Validação de permissões

Quando diferentes perfis participarem de uma funcionalidade, o agente deverá verificar:

- Quais ações cada perfil pode executar.
- Quais informações pode consultar.
- Quais registros pode modificar.
- Quais decisões exigem autorização específica.
- Quais ações devem ser bloqueadas.

O sistema deverá impedir operações não autorizadas, inclusive quando tentadas fora da interface visual.

A validação de permissões deverá considerar os mecanismos de autorização efetivamente implementados, e não apenas a presença ou ausência de botões.

## 9. Validação de estados e transições

Quando a funcionalidade possuir estados, deverão ser estabelecidos critérios para verificar:

- Estado inicial.
- Transições permitidas.
- Transições proibidas.
- Perfil autorizado para cada transição.
- Condições obrigatórias.
- Consequências da mudança de estado.

O agente deverá verificar que o sistema não permite transições incompatíveis com as regras de negócio.

## 10. Fluxos alternativos e exceções

Os critérios deverão contemplar os principais comportamentos alternativos identificados no PROD-02.

Exemplos:

- Tentativa de concluir um registro incompleto.
- Rejeição de uma aprovação.
- Envio de informações inválidas.
- Tentativa de executar uma ação sem permissão.
- Falha em uma integração externa.
- Tentativa de repetir uma operação já concluída.

A profundidade da validação deverá ser proporcional à relevância e ao risco de cada situação.

## 11. Formas de verificação

O agente deverá recomendar a forma mais adequada de verificar cada critério.

Poderão ser utilizados:

**Testes automatizados:** verificações executadas por ferramentas de teste.

**Testes de integração:** verificações da interação entre componentes e serviços.

**Testes de interface:** simulações de ações realizadas pelos usuários.

**Testes manuais:** procedimentos executados pelo desenvolvedor ou por usuários responsáveis.

**Inspeção de registros e evidências:** análise de resultados, logs ou informações persistidas.

A escolha deverá considerar a arquitetura do projeto, as ferramentas disponíveis e os riscos envolvidos.

A definição técnica dos testes e sua execução deverão seguir os procedimentos do Pilar Desenvolvimento.

## 12. Recomendações de recursos especializados

O agente deverá avaliar se existem skills, agentes especializados, plugins ou ferramentas que possam melhorar a definição ou a verificação dos critérios de aceitação.

Poderá recomendar recursos relacionados a:

- Testes automatizados.
- Testes de interface.
- Validação de acessibilidade.
- Testes de integração.
- Verificação de segurança.
- Análise de cobertura de testes.
- Validação de desempenho.

As recomendações deverão ser justificadas e seguir as regras de avaliação e aprovação do DEV-07.

O agente não deverá afirmar que utilizou um recurso sem efetivamente tê-lo utilizado.

## 13. Evidências de validação

A conclusão de uma funcionalidade deverá ser acompanhada de evidências proporcionais ao seu risco.

O registro deverá indicar:

- Critérios verificados.
- Método utilizado.
- Resultado obtido.
- Data da verificação.
- Ambiente em que foi realizada.
- Limitações da verificação.
- Pendências identificadas.

Sempre que possível, as evidências deverão ser vinculadas aos testes ou registros correspondentes.

A ausência de uma ferramenta de testes não autoriza o agente a presumir que os critérios foram atendidos.

## 14. Classificação dos resultados

Cada critério deverá receber uma das seguintes situações:

**Não verificado:** ainda não foi avaliado.

**Aprovado:** comportamento verificado e compatível com o resultado esperado.

**Reprovado:** comportamento diferente do esperado.

**Bloqueado:** não foi possível realizar a verificação por alguma dependência ou impedimento.

**Não aplicável:** critério que deixou de ser pertinente após mudança aprovada no escopo.

Critérios reprovados ou bloqueados deverão permanecer identificados até sua resolução ou decisão formal.

## 15. Validação pelo desenvolvedor

O agente deverá apresentar os resultados em linguagem acessível.

A comunicação deverá indicar:

1. O que foi implementado.
2. Quais jornadas foram atendidas.
3. Quais comportamentos foram verificados.
4. Quais testes foram realizados.
5. Quais resultados foram obtidos.
6. Quais limitações permanecem.
7. Se existem decisões pendentes.

A aprovação do desenvolvedor deverá ser solicitada conforme o risco, o impacto e as regras de governança do Pilar Desenvolvimento.

A aprovação humana não substitui automaticamente as verificações técnicas necessárias.

## 16. Critérios de conclusão de uma funcionalidade

Uma funcionalidade poderá ser considerada concluída quando:

- Seus requisitos estiverem aprovados.
- Os critérios de aceitação estiverem definidos.
- Os comportamentos esperados tiverem sido implementados.
- Os critérios obrigatórios tiverem sido verificados com resultado satisfatório.
- As jornadas envolvidas tiverem sido validadas.
- Não existirem falhas impeditivas conhecidas.
- As evidências relevantes estiverem registradas.
- As aprovações exigidas tiverem sido obtidas.
- A documentação estiver atualizada.

Pendências não impeditivas poderão ser registradas para tratamento posterior, desde que essa decisão seja explícita e compatível com o risco.

## 17. Mudanças nos critérios de aceitação

Quando um requisito ou uma jornada for alterado, o agente deverá revisar os critérios correspondentes.

Critérios não deverão ser modificados apenas para fazer uma implementação incorreta parecer aprovada.

Qualquer mudança que altere o comportamento esperado deverá ser justificada e aprovada conforme o processo de gestão de mudanças.

## 18. Relação com os demais documentos

### PROD-01 — Descoberta e Visão

Define os objetivos gerais que orientam o produto.

### PROD-02 — Requisitos, Jornadas e Regras de Negócio

Fornece a origem e a rastreabilidade dos critérios de aceitação.

### PROD-03 — Evolução Contínua

Identifica oportunidades e mudanças que podem exigir revisão dos critérios.

### Pilar Arquitetura

Define as soluções técnicas e os atributos de qualidade necessários para atender aos requisitos.

### Pilar Desenvolvimento

Define os procedimentos de implementação, testes, revisão, controle de mudanças e registro das evidências.

## 19. Critérios de conformidade

O PROD-04 estará sendo respeitado quando:

- Os critérios forem definidos antes da implementação.
- Os critérios estiverem vinculados aos requisitos.
- As jornadas forem verificadas de maneira integrada.
- As permissões e regras relevantes forem testadas.
- Os resultados forem documentados.
- O agente não declarar sucesso sem evidências.
- As limitações forem comunicadas.
- O desenvolvedor compreender o que foi validado.
- As mudanças nos critérios forem controladas.

## 20. Regra fundamental

**Uma funcionalidade não está concluída porque o código foi escrito. Está concluída quando os comportamentos aprovados foram demonstrados, verificados e aceitos conforme as regras da metodologia.**