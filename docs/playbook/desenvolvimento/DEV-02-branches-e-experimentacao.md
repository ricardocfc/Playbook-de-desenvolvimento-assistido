# DEV-02 — Experimentação Controlada e Gerenciamento de Branches

**Pilar:** 03 — Desenvolvimento  
**Versão:** 1.0  
**Status:** Aprovado  
**Aplicação:** Todos os projetos desenvolvidos com a metodologia.

---

## 1. Objetivo

Estabelecer procedimentos para experimentar, desenvolver e validar alterações de código de maneira controlada, preservando versões estáveis e reduzindo riscos de regressão ou perda de trabalho.

A metodologia deverá utilizar branches e outros mecanismos de isolamento quando forem adequados ao risco e à complexidade da alteração.

## 2. Princípio fundamental

**O isolamento de uma alteração deverá ser proporcional ao seu risco, alcance e necessidade de experimentação.**

O agente não deverá criar branches desnecessárias para mudanças triviais.

Também não deverá executar experimentações relevantes diretamente sobre uma versão estável quando houver risco significativo de comprometer seu funcionamento.

## 3. Responsabilidades do agente

O agente deverá:

- Identificar a natureza da alteração solicitada.
- Avaliar seu risco e alcance.
- Verificar o estado atual do repositório.
- Identificar a branch ativa.
- Considerar alterações preexistentes.
- Recomendar o nível adequado de isolamento.
- Explicar quando uma branch for necessária.
- Preservar versões estáveis.
- Validar alterações antes de integrá-las.
- Evitar merges e publicações não autorizados.
- Registrar o resultado de experimentações relevantes.

## 4. Classificação inicial das alterações

A escolha do fluxo deverá considerar os níveis de risco definidos no DEV-05.

Como orientação inicial:

### Baixo risco

Exemplos:

- Correção de texto.
- Ajuste visual localizado.
- Pequena alteração de espaçamento.
- Correção simples sem impacto em contratos ou dados.

Poderá ser executada diretamente na branch de trabalho autorizada, inclusive na branch principal quando a política do projeto permitir.

O agente deverá realizar as verificações proporcionais à alteração.

### Médio risco

Exemplos:

- Implementação de nova funcionalidade.
- Alteração de comportamento relevante.
- Refatoração de componentes compartilhados.
- Modificação de fluxos envolvendo diferentes módulos.

Deverá, como padrão, utilizar uma branch de trabalho ou outro mecanismo de isolamento equivalente.

Exceções deverão ser justificadas e compatíveis com as regras do projeto.

### Alto risco

Exemplos:

- Alterações de autenticação ou autorização.
- Mudanças estruturais no banco de dados.
- Refatorações amplas.
- Substituição de tecnologias centrais.
- Modificações em regras financeiras críticas.
- Alterações com possibilidade relevante de perda de dados.

Deverá exigir análise prévia, isolamento adequado e aprovação explícita antes da execução.

A integração dependerá de validações compatíveis com o risco.

## 5. Diagnóstico antes da experimentação

Antes de criar uma branch ou modificar o código, o agente deverá verificar:

- Branch atual.
- Estado do repositório.
- Existência de alterações não registradas.
- Existência de trabalho paralelo.
- Convenções de branches.
- Possíveis consequências de mudanças de branch.
- Disponibilidade de um ponto de referência estável.

O agente não deverá descartar ou sobrescrever trabalho preexistente para preparar o ambiente.

## 6. Criação de branches

Quando uma branch for necessária, o agente deverá utilizar nomes descritivos e compatíveis com as convenções do projeto.

Exemplos:

- `feature/aprovacao-manutencao`
- `fix/validacao-fornecedor`
- `refactor/tabela-compartilhada`
- `experiment/nova-navegacao`

A nomenclatura é ilustrativa.

O agente deverá respeitar padrões existentes.

A criação de uma branch não autoriza automaticamente alterações fora do escopo solicitado.

## 7. Experimentações técnicas

O agente poderá recomendar experimentações quando existir incerteza relevante sobre uma solução.

Exemplos:

- Comparação entre duas abordagens de implementação.
- Avaliação de uma biblioteca.
- Teste de um componente alternativo.
- Investigação de desempenho.
- Prova de conceito para uma integração.

A experimentação deverá possuir objetivo e critérios de avaliação definidos.

O agente deverá distinguir código experimental de implementação aprovada.

## 8. Limites da experimentação

Antes de iniciar uma experimentação relevante, o agente deverá identificar:

- Objetivo.
- Hipótese ou dúvida a esclarecer.
- Escopo.
- Arquivos e módulos potencialmente afetados.
- Riscos.
- Critérios de sucesso.
- Forma de comparação.
- Procedimento de descarte ou integração.

O agente não deverá ampliar indefinidamente uma experimentação sem reavaliar seu propósito.

## 9. Validação antes da integração

Uma alteração isolada deverá ser verificada antes de sua integração.

A validação poderá incluir:

- Execução da aplicação.
- Testes automatizados.
- Testes de integração.
- Verificação de interface.
- Revisão de alterações.
- Verificação dos critérios de aceitação.
- Análise de regressões.

A profundidade deverá ser proporcional ao risco.

O agente deverá comunicar verificações não realizadas ou limitações do ambiente.

## 10. Integração de alterações

Antes de integrar uma branch, o agente deverá:

1. Confirmar que a implementação atende ao escopo aprovado.
2. Verificar o estado do repositório.
3. Identificar alterações relevantes na branch de destino.
4. Avaliar conflitos potenciais.
5. Executar as verificações exigidas.
6. Confirmar as autorizações necessárias.
7. Preservar a rastreabilidade da integração.

O agente não deverá realizar merge automaticamente quando essa ação exigir aprovação.

## 11. Conflitos de integração

Quando ocorrerem conflitos, o agente deverá analisar as alterações envolvidas.

Não deverá resolver conflitos descartando indiscriminadamente uma das versões.

Deverá identificar:

- Quais arquivos estão em conflito.
- Quais comportamentos foram modificados.
- Quais alterações precisam ser preservadas.
- Se a resolução exige decisão funcional ou arquitetural.
- Quais testes deverão ser repetidos.

Conflitos com consequências relevantes deverão ser apresentados ao desenvolvedor antes da resolução.

## 12. Descarte de experimentações

Uma experimentação poderá ser descartada quando:

- Não atingir seus objetivos.
- Produzir riscos incompatíveis com seus benefícios.
- Ser substituída por alternativa superior.
- Deixar de atender a uma necessidade do produto.

O descarte deverá preservar o trabalho não relacionado e respeitar as regras do DEV-01.

O agente não deverá excluir branches, arquivos ou registros com trabalho relevante sem verificar suas dependências e obter a autorização necessária.

## 13. Trabalho paralelo

Quando diferentes agentes ou desenvolvedores trabalharem simultaneamente, o agente deverá considerar possíveis interferências.

Deverá evitar:

- Sobrescrever alterações de outra pessoa ou agente.
- Modificar arquivos compartilhados sem coordenação.
- Integrar mudanças incompatíveis.
- Presumir que o repositório permaneceu inalterado.
- Executar operações destrutivas sobre trabalho paralelo.

Quando necessário, deverá recomendar branches ou ambientes de trabalho isolados.

## 14. Branches e ambientes de execução

Uma branch Git não representa, por si só, um ambiente de execução independente.

O agente deverá distinguir:

- Isolamento do histórico de código.
- Isolamento dos arquivos de trabalho.
- Isolamento de configurações.
- Isolamento de bancos de dados.
- Isolamento de serviços externos.
- Isolamento de ambientes de implantação.

Quando uma experimentação puder afetar dados ou serviços compartilhados, o agente deverá avaliar a necessidade de ambientes e recursos separados.

## 15. Relação com deploy

O agente deverá identificar se o repositório possui automações que executam builds ou publicações após pushes e merges.

Não deverá presumir que uma branch experimental está desconectada de ambientes externos.

Antes de ações capazes de disparar uma implantação, deverá considerar:

- Ambiente de destino.
- Consequências da publicação.
- Regras de aprovação.
- Necessidade de testes adicionais.
- Possibilidade de reversão.

O agente deverá respeitar a política de implantação do projeto.

## 16. Registro de experimentações relevantes

Experimentações com impacto significativo deverão possuir registro resumido contendo:

- Objetivo.
- Alternativas avaliadas.
- Resultado observado.
- Decisão tomada.
- Alterações incorporadas ou descartadas.
- Riscos ou pendências.

Quando a experimentação resultar em decisão arquitetural relevante, deverá ser produzido ou atualizado o ADR correspondente, conforme o ARQ-04.

## 17. Critérios de conformidade

O DEV-02 estará sendo respeitado quando:

- O isolamento das alterações for proporcional ao risco.
- Mudanças triviais não exigirem burocracia desnecessária.
- Alterações relevantes forem protegidas por mecanismos adequados.
- O estado do repositório for verificado.
- O trabalho preexistente for preservado.
- Experimentos possuírem objetivo e critérios de avaliação.
- As alterações forem validadas antes da integração.
- Merges e publicações respeitarem as autorizações.
- Conflitos forem resolvidos sem descarte indevido de trabalho.
- Os resultados relevantes forem registrados.

## 18. Relação com os demais documentos

### DEV-01 — Versionamento e Git

Define as regras gerais de preservação do histórico e controle das alterações.

### DEV-05 — Gestão de Mudanças

Estabelece a classificação de riscos e as aprovações necessárias.

### DEV-06 — Intervenção Mínima e Análise de Impacto

Define o alcance autorizado de cada alteração.

### DEV-10 — Encerramento de Sessão

Registra branches ativas, experimentações e pendências.

### ARQ-04 — Decisões e Evolução Arquitetural

Registra decisões técnicas relevantes decorrentes das experimentações.

## 19. Regra fundamental

**O agente deverá experimentar e desenvolver com liberdade proporcional ao risco, preservando o trabalho existente e integrando alterações somente após validação e autorização adequadas.**