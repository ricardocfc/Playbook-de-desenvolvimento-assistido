# DEV-04 — Análise de Dependências e Impactos Indiretos

**Pilar:** 03 — Desenvolvimento  
**Versão:** 1.1 — revisão proposta  
**Status:** Revisão normativa em validação — versão 1.0 preservada  
**Aplicação:** Todos os projetos desenvolvidos com a metodologia.

---

## 1. Objetivo

Estabelecer procedimentos para identificar dependências entre arquivos, componentes, funções, serviços, módulos, dados e integrações antes da execução de alterações relevantes.

A metodologia deverá reduzir o risco de regressões, mudanças inesperadas e comprometimento de funcionalidades que não fazem parte diretamente da solicitação.

## 2. Princípio fundamental

**Antes de modificar um elemento, o agente deverá avaliar quem depende dele e quais comportamentos poderão ser afetados.**

A profundidade da análise deverá ser proporcional ao risco, ao alcance e à natureza da alteração.

O agente não deverá executar investigações extensas para mudanças triviais quando não houver indícios de impacto relevante.

## 3. Responsabilidades do agente

O agente deverá:

- Identificar os elementos diretamente envolvidos na solicitação.
- Investigar seus consumidores e dependências.
- Reconhecer recursos compartilhados.
- Avaliar impactos diretos e indiretos.
- Identificar contratos e interfaces relevantes.
- Considerar efeitos sobre dados e integrações.
- Identificar possíveis regressões.
- Recomendar verificações proporcionais ao risco.
- Comunicar impactos relevantes antes da implementação.
- Registrar limitações da análise.
- Evitar modificações desnecessárias fora do escopo autorizado.

## 4. Identificação do ponto de alteração

Antes de implementar uma mudança, o agente deverá identificar:

- Qual comportamento precisa ser alterado.
- Qual funcionalidade é responsável por ele.
- Quais arquivos implementam esse comportamento.
- Quais regras de negócio estão envolvidas.
- Quais componentes ou serviços são utilizados.
- Quais contratos podem ser afetados.

O agente deverá evitar modificar o primeiro arquivo aparentemente relacionado sem compreender sua função.

## 5. Dependências diretas

São relações explícitas entre elementos do sistema.

Exemplos:

- Importação de componentes.
- Chamada de funções.
- Utilização de serviços.
- Consumo de APIs.
- Referências a tipos e interfaces.
- Dependências entre módulos.
- Consultas a estruturas de dados.

O agente deverá identificar os consumidores diretos relevantes antes de modificar um recurso compartilhado.

## 6. Dependências indiretas

São relações nas quais uma alteração poderá produzir consequências em elementos que não utilizam diretamente o código modificado.

Exemplo:

Uma mudança no cálculo de despesas poderá alterar valores utilizados pelo rateio condominial, que posteriormente influenciam a geração de cobranças e relatórios financeiros.

O agente deverá considerar cadeias de dependências quando houver possibilidade relevante de propagação de efeitos.

A análise deverá priorizar caminhos de impacto plausíveis, evitando exploração ilimitada de relações sem relevância para a tarefa.

## 7. Dependências compartilhadas

Recursos utilizados por diferentes funcionalidades deverão receber atenção especial.

Exemplos:

- Componentes de interface.
- Serviços de autenticação.
- Funções de cálculo.
- Validadores.
- Utilitários.
- Modelos de dados.
- Bibliotecas.
- Configurações globais.

O agente deverá identificar os principais consumidores e avaliar se a alteração preserva os comportamentos esperados.

## 8. Contratos entre módulos

Quando uma mudança afetar contratos utilizados por outros componentes, o agente deverá verificar:

- Entradas esperadas.
- Saídas produzidas.
- Tipos de dados.
- Tratamento de erros.
- Compatibilidade.
- Comportamentos assumidos pelos consumidores.

Alterações de contrato deverão ser avaliadas conforme seu impacto.

O agente não deverá presumir que uma mudança é segura apenas porque o código compila.

## 9. Dependências de dados

O agente deverá considerar relações entre:

- Tabelas.
- Colunas.
- Consultas.
- Restrições.
- Migrações.
- Políticas de acesso.
- Procedimentos armazenados.
- Eventos e rotinas automatizadas.
- Relatórios.
- Integrações.

Alterações em estruturas persistentes poderão exigir análise específica de compatibilidade e preservação dos dados.

O agente não deverá executar mudanças destrutivas sem autorização explícita.

## 10. Dependências externas

O agente deverá identificar quando a funcionalidade depende de serviços externos.

Exemplos:

- Serviços de autenticação.
- Gateways de pagamento.
- Serviços de mensagens.
- APIs de terceiros.
- Armazenamento em nuvem.
- Provedores de infraestrutura.

A análise deverá considerar contratos, credenciais, limites, falhas, disponibilidade e possíveis efeitos sobre processos relacionados.

O agente deverá distinguir dependências comprovadas de hipóteses que ainda precisam ser verificadas.

## 11. Dependências dinâmicas ou pouco evidentes

Nem todas as relações poderão ser identificadas por importações ou buscas textuais.

O agente deverá considerar, quando relevante:

- Carregamento dinâmico.
- Convenções de rotas.
- Registro automático de módulos.
- Configurações.
- Injeção de dependências.
- Eventos.
- Referências por identificadores.
- Execução indireta de scripts.
- Recursos utilizados por serviços externos.

A ausência de referências explícitas não deverá ser interpretada automaticamente como ausência de dependências.

## 12. Impacto sobre jornadas e requisitos

A análise técnica deverá considerar os elementos funcionais definidos no Pilar Produto.

Quando uma alteração puder afetar diferentes jornadas, o agente deverá identificar:

- Quais perfis poderão ser impactados.
- Quais jornadas utilizam o comportamento.
- Quais requisitos poderão sofrer alteração.
- Quais regras de negócio precisam ser preservadas.
- Quais critérios de aceitação deverão ser verificados.

O objetivo é conectar a análise de dependências técnicas aos comportamentos esperados pelos usuários.

## 13. Classificação dos impactos

O agente deverá distinguir:

### Impacto direto

Consequência sobre o elemento que será modificado ou sobre seus consumidores imediatos.

### Impacto indireto

Consequência propagada por dependências intermediárias.

### Impacto potencial

Consequência plausível que ainda não foi confirmada.

### Impacto não identificado

Situação em que a análise realizada não encontrou evidências de efeito relevante.

A ausência de impacto identificado não deverá ser apresentada como garantia absoluta de inexistência de riscos.

## 14. Profundidade proporcional da análise

A análise deverá acompanhar a natureza da alteração.

### Mudanças de baixo risco

Verificação localizada dos elementos diretamente envolvidos.

### Mudanças de médio risco

Investigação dos consumidores relevantes, contratos, regras de negócio e possíveis regressões.

### Mudanças de alto risco

Análise ampliada de dependências, dados, integrações, jornadas afetadas, compatibilidade, recuperação e validações necessárias.

A classificação formal de risco seguirá o DEV-05.

## 15. Comunicação dos impactos

Quando a análise identificar consequências relevantes, o agente deverá apresentar ao desenvolvedor:

1. O que será alterado.
2. Onde a alteração será realizada.
3. Quais elementos dependem do recurso.
4. Quais funcionalidades poderão ser afetadas.
5. Quais riscos foram identificados.
6. Quais verificações serão necessárias.
7. Se existe necessidade de autorização adicional.

A comunicação deverá ser objetiva e compreensível.

## 16. Limites da análise

O agente deverá reconhecer que análises estáticas, buscas e inspeções podem não revelar todas as dependências.

Quando existirem limitações relevantes, deverá informá-las.

Não deverá declarar ausência de riscos com base apenas em inspeção superficial.

Quando necessário, deverá complementar a análise com testes, execução da aplicação ou ferramentas especializadas.

## 17. Recomendações de recursos especializados

O agente poderá recomendar skills, ferramentas ou agentes especializados para:

- Análise de dependências.
- Identificação de código não utilizado.
- Inspeção de contratos.
- Análise de impacto.
- Testes de regressão.
- Verificação de segurança.
- Análise de migrações.

As recomendações deverão ser justificadas e seguir as regras de disponibilidade, permissões e aprovação estabelecidas no DEV-07.

## 18. Critérios de conformidade

O DEV-04 estará sendo respeitado quando:

- O ponto de alteração for identificado corretamente.
- Os consumidores relevantes forem investigados.
- Dependências diretas e indiretas forem consideradas.
- Contratos compartilhados forem avaliados.
- Impactos sobre dados e integrações forem identificados quando aplicável.
- Jornadas e requisitos potencialmente afetados forem considerados.
- A análise for proporcional ao risco.
- Limitações forem comunicadas.
- As verificações forem compatíveis com os impactos.
- O agente não ampliar indevidamente o escopo da implementação.

## 19. Relação com os demais documentos

### PROD-02 — Jornadas e Requisitos

Fornece as relações funcionais que permitem identificar impactos sobre usuários e processos.

### PROD-04 — Critérios de Aceitação

Fornece os comportamentos que deverão continuar sendo atendidos após a alteração.

### ARQ-02 — Componentes Compartilhados

Identifica recursos reutilizados por diferentes funcionalidades.

### ARQ-03 — Responsabilidades e Dependências

Define os princípios arquiteturais para controlar as relações entre módulos.

### DEV-03 — Limpeza de Código

Utiliza a análise de dependências antes de remover implementações.

### DEV-05 — Gestão de Mudanças

Define os níveis de risco e a profundidade das verificações.

### DEV-06 — Intervenção Mínima e Análise de Impacto

Utiliza os resultados da análise para delimitar o escopo autorizado da implementação.

## 20. Impactos entre requisições e SPECs

A análise de uma nova requisição deverá considerar não apenas dependências técnicas, mas também comportamentos e regras previamente definidos por outras requisições, inclusive quando documentados em SPECs diferentes.

O agente deverá:

1. Identificar a SPEC principal e as SPECs associadas da requisição atual, conforme o PROD-02.
2. Consultar referências cruzadas, requisitos vigentes e registros históricos pertinentes, sem presumir que a classificação de uma requisição anterior se aplica à atual.
3. Identificar quais requisições, jornadas, regras, critérios de aceitação e comportamentos anteriores poderão ser afetados.
4. Registrar, na documentação da nova requisição, os **impactos previstos**, indicando sua origem, alcance, incertezas e verificações necessárias.
5. Reavaliar os impactos durante a implementação e a validação, sem apresentar como efetiva uma mudança ainda não executada ou comprovada.
6. Após implementação e validação, encaminhar a atualização rastreável dos `history.md` das SPECs afetadas e os ajustes mínimos necessários em seus `spec.md`, conforme DEV-11 e o escopo autorizado.

A **natureza do impacto** (direto, indireto, potencial ou não identificado), definida na seção 13, é distinta do **estado de tratamento do impacto** (previsto, implementado, validado ou não confirmado). Essas dimensões não deverão ser confundidas. Um impacto implementado não será considerado validado sem evidência apropriada, conforme PROD-04.

A necessidade de atualizar uma SPEC associada para preservar a coerência documental não autoriza executar nela uma segunda implementação da mesma requisição. Se a análise revelar finalidades independentes, o agente deverá propor a decomposição e a classificação de requisições distintas antes de ampliar o escopo.

## 21. Regra fundamental

**O agente deverá compreender as dependências relevantes antes de alterar o código, identificando os possíveis efeitos sobre funcionalidades, dados, contratos e jornadas, sem transformar toda mudança em uma investigação desproporcional.**