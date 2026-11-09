# ARQ-01 — Organização por Funcionalidades

**Pilar:** 02 — Arquitetura\
**Versão:** 1.0\
**Status:** Aprovado\
**Aplicação:** Projetos de software desenvolvidos com a metodologia.

---

## 1. Objetivo

Estabelecer diretrizes para organizar o código-fonte de forma clara, modular e orientada às funcionalidades do produto.

A estrutura deverá facilitar a localização de arquivos, a manutenção, a reutilização de componentes e a evolução do sistema.

O agente deverá preservar a organização existente quando ela estiver coerente com os princípios arquiteturais aprovados.

## 2. Princípio fundamental

**O código deverá ser organizado prioritariamente por funcionalidades e contextos de negócio, e não exclusivamente por tipos técnicos de arquivos.**

Os arquivos relacionados a uma funcionalidade deverão permanecer próximos sempre que isso contribuir para a compreensão e manutenção do sistema.

Essa diretriz não determina uma estrutura universal de pastas. Sua aplicação deverá respeitar a linguagem, o framework, o tamanho do projeto e as convenções técnicas necessárias.

## 3. Organização por contexto funcional

Cada funcionalidade relevante deverá possuir um contexto identificável dentro da aplicação.

Exemplos:

- Usuários.
- Fornecedores.
- Compras.
- Manutenções.
- Reservas.
- Financeiro.

O agente deverá identificar os limites funcionais de cada módulo a partir das jornadas e dos requisitos documentados no Pilar Produto.

Uma funcionalidade poderá conter diferentes tipos de arquivos, incluindo componentes de interface, serviços, validações, tipos, testes e regras específicas.

## 4. Estrutura de referência

Uma estrutura ilustrativa poderá seguir o modelo:
```
src/
  features/
    manutencoes/
      components/
      services/
      hooks/
      types/
      validations/
      tests/

    compras/
      components/
      services/
      hooks/
      types/
      validations/
      tests/

    fornecedores/
      components/
      services/
      hooks/
      types/
      validations/
      tests/

  shared/
    components/
    hooks/
    utils/

  app/
```

Essa estrutura é uma referência conceitual.

O agente não deverá criar pastas vazias ou estruturas desnecessárias apenas para reproduzir o exemplo.

Frameworks que exigem diretórios específicos, como pastas de rotas, poderão mantê-los, desde que a lógica funcional permaneça organizada.

## 5. Separação entre funcionalidades

Cada módulo deverá concentrar os elementos específicos de sua responsabilidade.

O agente deverá evitar:

- Misturar regras de funcionalidades independentes.
- Criar arquivos genéricos que concentrem responsabilidades sem relação.
- Colocar lógica específica de um módulo em outro módulo.
- Duplicar implementações para evitar a organização correta das dependências.
- Criar dependências circulares entre funcionalidades.

Quando duas funcionalidades precisarem interagir, essa relação deverá ser explícita e organizada.

## 6. Relação com as jornadas de usuário

A organização funcional deverá considerar as jornadas documentadas no PROD-02.

Entretanto, uma jornada não corresponde necessariamente a um módulo de código.

Uma funcionalidade poderá atender várias jornadas e vários perfis.

Da mesma forma, uma jornada poderá atravessar diferentes módulos.

O agente deverá identificar os limites dos módulos considerando suas responsabilidades de negócio, e não criar automaticamente uma pasta para cada jornada.

## 7. Componentes compartilhados

Elementos utilizados por diferentes funcionalidades poderão ser organizados em áreas compartilhadas.

Exemplos:

- Componentes visuais reutilizáveis.
- Utilitários genéricos.
- Hooks reutilizáveis.
- Tipos e contratos comuns.
- Serviços de infraestrutura compartilhados.

O agente deverá verificar se já existe uma implementação adequada antes de criar outra.

A decisão de compartilhar um componente deverá considerar sua responsabilidade e sua estabilidade, e não apenas a semelhança visual ou textual.

As regras específicas de reutilização serão detalhadas no ARQ-02.

## 8. Organização interna dos módulos

O agente poderá utilizar subdivisões técnicas dentro de cada funcionalidade quando elas contribuírem para a clareza.

Exemplos:

- components: componentes de interface.
- services: operações e serviços específicos.
- hooks: comportamentos reutilizáveis no contexto da funcionalidade.
- types: definições de tipos.
- validations: validações.
- tests: testes.

Esses nomes não são obrigatórios.

O agente deverá seguir as convenções aprovadas para o projeto.

## 9. Crescimento proporcional

A organização deverá acompanhar a complexidade real da aplicação.

Funcionalidades pequenas poderão utilizar estruturas simples.

Funcionalidades maiores poderão exigir subdivisões adicionais.

O agente não deverá criar abstrações, camadas ou diretórios sem necessidade identificável.

A organização deverá ser suficientemente estruturada para permitir evolução, mas não excessivamente complexa para o estágio atual do produto.

## 10. Preservação da arquitetura existente

Antes de implementar uma nova funcionalidade, o agente deverá:

1. Inspecionar a estrutura atual.
2. Identificar o módulo responsável.
3. Verificar convenções existentes.
4. Localizar componentes e serviços reutilizáveis.
5. Avaliar dependências relevantes.
6. Propor mudanças estruturais somente quando necessárias.

O agente não deverá reorganizar pastas ou arquivos fora do escopo autorizado apenas por preferência arquitetural.

Mudanças estruturais relevantes deverão seguir a gestão de mudanças do Pilar Desenvolvimento.

## 11. Prevenção de estruturas inadequadas

O agente deverá identificar situações como:

- Funcionalidades independentes concentradas em um único módulo.
- Regras de negócio espalhadas por áreas sem responsabilidade definida.
- Componentes duplicados.
- Arquivos compartilhados contendo lógica exclusiva de uma funcionalidade.
- Dependências circulares.
- Diretórios genéricos utilizados como depósito de arquivos sem organização.

Ao identificar esses problemas, deverá explicar seus impactos e propor correções proporcionais.

A identificação de um problema não autoriza refatoração automática fora do escopo aprovado.

## 12. Critérios de conformidade

A diretriz estará sendo respeitada quando:

- As funcionalidades possuírem limites identificáveis.
- Os arquivos estiverem organizados de acordo com suas responsabilidades.
- A estrutura permitir localizar e compreender o código com facilidade.
- Os componentes compartilhados estiverem em locais apropriados.
- As dependências entre módulos forem compreensíveis.
- A organização respeitar as convenções do projeto.
- Não existirem estruturas desnecessariamente complexas.
- Alterações estruturais relevantes forem justificadas e aprovadas.

## 13. Relação com os demais documentos

### PROD-02 — Jornadas e Requisitos

Fornece os contextos funcionais que ajudam a identificar os limites dos módulos.

### ARQ-02 — Componentes e Reutilização

Define critérios para reutilizar implementações e organizar recursos compartilhados.

### ARQ-03 — Responsabilidades e Dependências

Define como manter módulos coesos, com responsabilidades claras e dependências controladas.

### ARQ-04 — Decisões e Evolução Arquitetural

Registra escolhas estruturais relevantes e suas justificativas.

### Pilar Desenvolvimento

Estabelece como executar mudanças na estrutura do projeto, avaliar impactos, controlar versões e validar alterações.

## 14. Regra fundamental

**Cada funcionalidade deverá possuir uma organização coerente com sua responsabilidade de negócio, preservando a clareza, a modularidade e a capacidade de evolução do sistema.**

O agente deverá privilegiar estruturas compreensíveis, evitar complexidade desnecessária e respeitar a arquitetura aprovada para o projeto.
