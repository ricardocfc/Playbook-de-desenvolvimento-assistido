# ARQ-03 — Responsabilidades, Coesão e Dependências

**Pilar:** 02 — Arquitetura  
**Versão:** 1.0  
**Status:** Proposta para aprovação  
**Aplicação:** Todos os projetos desenvolvidos com a metodologia.

---

## 1. Objetivo

Estabelecer princípios para distribuir responsabilidades entre componentes, funções, serviços e módulos, preservando a organização e a capacidade de evolução do sistema.

A metodologia deverá orientar o agente a produzir soluções compreensíveis, coesas e com dependências controladas, evitando que alterações localizadas provoquem impactos desnecessários em outras partes da aplicação.

## 2. Princípio fundamental

**Cada unidade de código deverá possuir uma responsabilidade clara, mantendo próximas as operações relacionadas e reduzindo dependências desnecessárias entre diferentes contextos.**

A aplicação desses princípios deverá ser proporcional à complexidade real do projeto.

O agente não deverá introduzir camadas, interfaces ou abstrações apenas para demonstrar conformidade com um padrão arquitetural.

## 3. Responsabilidades do agente

O agente deverá:

- Identificar a responsabilidade de cada módulo envolvido.
- Preservar os limites entre funcionalidades.
- Manter próximas as operações que pertencem ao mesmo contexto.
- Evitar concentração de responsabilidades independentes.
- Reduzir dependências desnecessárias.
- Identificar dependências circulares.
- Respeitar contratos entre módulos.
- Evitar acesso indevido às estruturas internas de outros contextos.
- Avaliar o impacto das mudanças propostas.
- Recomendar melhorias estruturais quando houver benefício concreto.
- Evitar refatorações não autorizadas fora do escopo solicitado.

## 4. Responsabilidade única

A metodologia adotará o princípio da responsabilidade única como orientação para organizar o código.

Cada componente, função, serviço ou módulo deverá possuir uma finalidade identificável e razões coerentes para sofrer alterações.

Exemplos:

- Um componente de apresentação deverá priorizar a exibição e a interação com informações.
- Um serviço de negócio deverá concentrar operações relacionadas à sua responsabilidade.
- Uma validação deverá verificar condições específicas.
- Um módulo funcional deverá concentrar comportamentos pertencentes ao seu contexto.

O agente deverá evitar misturar responsabilidades independentes quando isso prejudicar a compreensão, os testes ou a manutenção.

Entretanto, responsabilidade única não significa que cada arquivo deva conter apenas uma função ou executar uma única operação.

## 5. Alta coesão

Elementos relacionados à mesma responsabilidade deverão permanecer organizados de forma próxima e compreensível.

O agente deverá avaliar se as operações de um módulo contribuem para uma finalidade comum.

Exemplo:

Um módulo de manutenções poderá reunir operações de registro, acompanhamento, aprovação e consulta de histórico, desde que essas operações pertençam ao contexto funcional de manutenção.

A existência de diferentes operações não exige automaticamente a criação de módulos independentes.

O agente deverá evitar dividir excessivamente uma funcionalidade quando isso dificultar a compreensão de seu funcionamento.

## 6. Tamanho dos arquivos

O tamanho de um arquivo não deverá ser utilizado isoladamente como critério para determinar sua qualidade arquitetural.

Um arquivo extenso poderá ser adequado quando:

- Possuir responsabilidade claramente definida.
- Apresentar organização interna compreensível.
- Concentrar operações fortemente relacionadas.
- Permitir manutenção e testes adequados.
- Não reunir contextos independentes.

Da mesma forma, um arquivo pequeno poderá apresentar problemas quando possuir responsabilidades misturadas ou dependências inadequadas.

O agente deverá propor divisão de arquivos quando existir justificativa técnica concreta, e não apenas porque determinado limite de linhas foi ultrapassado.

## 7. Baixo acoplamento

Os módulos deverão depender uns dos outros apenas na medida necessária para cumprir suas responsabilidades.

O agente deverá buscar relações claras, previsíveis e controladas.

Deverá evitar:

- Dependências circulares.
- Acesso direto e desnecessário a detalhes internos de outros módulos.
- Alterações em cascata provocadas por dependências frágeis.
- Compartilhamento excessivo de estado.
- Contratos instáveis entre funcionalidades.
- Dependências criadas apenas por conveniência de implementação.

Baixo acoplamento não significa ausência de integração entre módulos.

Significa que essas integrações deverão ocorrer de maneira organizada.

## 8. Separação de contextos

Cada contexto funcional deverá preservar suas regras e responsabilidades.

Exemplos:

- Compras.
- Manutenções.
- Fornecedores.
- Financeiro.
- Usuários e permissões.

Quando uma jornada atravessar diferentes contextos, o agente deverá identificar como eles interagem.

A participação de vários módulos em uma mesma jornada não autoriza a mistura indiscriminada de suas responsabilidades.

## 9. Integridade contextual

O agente deverá respeitar os limites de responsabilidade dos contextos de negócio.

Quando uma funcionalidade precisar utilizar informações ou operações de outra, deverá preferir os mecanismos de integração e contratos aprovados para o projeto.

O agente não deverá reproduzir regras de negócio pertencentes a outro contexto apenas para evitar uma integração.

Também não deverá acessar estruturas internas de outro módulo quando existir uma interface adequada para a operação.

O objetivo é preservar a consistência das regras e evitar implementações divergentes.

## 10. Contratos entre módulos

Quando houver comunicação entre diferentes módulos, o agente deverá identificar os contratos utilizados.

Esses contratos poderão envolver:

- Funções públicas.
- Interfaces.
- Tipos compartilhados.
- Serviços.
- APIs.
- Eventos.
- Outros mecanismos previstos na arquitetura.

O agente deverá preservar a compatibilidade dos contratos existentes, salvo quando uma alteração tiver sido analisada e aprovada.

Mudanças que afetem consumidores deverão ser acompanhadas de análise de impacto e validação adequada.

## 11. Regras de negócio e interface

O agente deverá evitar concentrar regras de negócio críticas exclusivamente em componentes visuais.

A interface poderá apresentar informações, coletar dados e orientar interações, mas as regras que precisam ser respeitadas independentemente da interface deverão ser aplicadas nas camadas apropriadas.

Especialmente em operações envolvendo:

- Permissões.
- Aprovações.
- Estados de processos.
- Cálculos financeiros.
- Integridade dos registros.
- Validações obrigatórias.

A organização específica dependerá da arquitetura e das tecnologias aprovadas para o projeto.

## 12. Dependências circulares

O agente deverá evitar situações nas quais módulos dependam uns dos outros de maneira circular.

Exemplo inadequado:

O módulo Compras depende internamente de Manutenções, enquanto Manutenções também depende internamente de Compras, sem contratos ou limites claros.

Ao identificar dependências circulares, o agente deverá avaliar alternativas como:

- Revisão das responsabilidades.
- Definição de contratos.
- Extração de responsabilidades verdadeiramente compartilhadas.
- Introdução de mecanismos de integração adequados.

A solução escolhida deverá evitar complexidade desnecessária.

## 13. Estado e informações compartilhadas

O compartilhamento de estado entre módulos deverá ocorrer somente quando necessário.

O agente deverá avaliar:

- Quem é responsável pela informação.
- Quem pode modificá-la.
- Quem precisa consultá-la.
- Como as alterações são propagadas.
- Como a consistência é preservada.

O agente deverá evitar mecanismos globais de estado quando uma solução local for suficiente.

Também deverá evitar duplicar estados que precisem permanecer sincronizados sem um mecanismo confiável de atualização.

## 14. Avaliação de impacto arquitetural

Antes de executar alterações que afetem responsabilidades ou dependências, o agente deverá verificar:

1. Quais módulos serão envolvidos.
2. Quais responsabilidades serão modificadas.
3. Quais contratos poderão ser afetados.
4. Quais funcionalidades dependem desses contratos.
5. Se existem riscos de regressão.
6. Se a alteração exige refatoração.
7. Quais verificações serão necessárias.

A profundidade dessa análise deverá acompanhar o risco da mudança.

Alterações estruturais relevantes deverão seguir o processo de aprovação do Pilar Desenvolvimento.

## 15. Refatoração arquitetural

O agente poderá identificar oportunidades para melhorar a distribuição de responsabilidades.

Entretanto, não deverá realizar refatorações amplas apenas porque encontrou uma organização que considera preferível.

Uma proposta de refatoração deverá apresentar:

- Problema identificado.
- Consequências da estrutura atual.
- Benefício esperado.
- Alternativa proposta.
- Módulos afetados.
- Riscos envolvidos.
- Estratégia de validação.

O desenvolvedor deverá aprovar as mudanças quando exigido pelas regras de governança.

## 16. Proporcionalidade arquitetural

A metodologia deverá evitar tanto a ausência de organização quanto a complexidade excessiva.

O agente deverá considerar:

- Tamanho do projeto.
- Quantidade de funcionalidades.
- Número de integrações.
- Complexidade das regras de negócio.
- Frequência esperada de mudanças.
- Riscos envolvidos.
- Convenções das tecnologias utilizadas.

Uma aplicação simples não deverá receber uma arquitetura complexa sem justificativa.

Uma aplicação com regras críticas e múltiplos contextos poderá exigir separações e contratos mais rigorosos.

## 17. Critérios de conformidade

A diretriz estará sendo respeitada quando:

- Os módulos possuírem responsabilidades identificáveis.
- As operações relacionadas permanecerem organizadas de forma coesa.
- Os contextos funcionais estiverem preservados.
- As dependências forem compreensíveis e controladas.
- Não existirem dependências circulares injustificadas.
- Os contratos entre módulos forem respeitados.
- As regras de negócio estiverem nas camadas adequadas.
- A divisão de arquivos ocorrer por necessidade, não por limites arbitrários.
- Refatorações relevantes forem justificadas e autorizadas.
- A complexidade arquitetural for proporcional ao projeto.

## 18. Relação com os demais documentos

### PROD-02 — Requisitos, Jornadas e Regras de Negócio

Fornece os contextos e comportamentos que orientam a distribuição de responsabilidades.

### ARQ-01 — Organização por Funcionalidades

Define a organização geral dos módulos e arquivos.

### ARQ-02 — Componentes Compartilhados e Reutilização

Define como reutilizar implementações sem comprometer os limites de responsabilidade.

### ARQ-04 — Decisões e Evolução Arquitetural

Registra escolhas relevantes sobre responsabilidades, contratos e dependências.

### Pilar Desenvolvimento

Define os procedimentos para analisar impactos, implementar mudanças, executar testes e controlar refatorações.

## 19. Regra fundamental

**O agente deverá organizar o código de modo que cada contexto preserve suas responsabilidades, suas operações relacionadas permaneçam coesas e suas dependências sejam claras e controladas.**

A arquitetura deverá facilitar a evolução do sistema, sem impor complexidade que não produza benefício concreto.