# ARQ-02 — Componentes Compartilhados e Reutilização de Código

**Pilar:** 02 — Arquitetura\
**Versão:** 1.1\
**Status:** Proposta para aprovação\
**Aplicação:** Todos os projetos desenvolvidos com a metodologia.

---

## 1. Objetivo

Estabelecer critérios para identificar, reutilizar, criar e manter componentes, funções, serviços e outros recursos compartilhados entre diferentes funcionalidades.

A metodologia deverá evitar duplicações desnecessárias, preservar a consistência do sistema e impedir que a reutilização produza dependências excessivas ou abstrações difíceis de manter.

## 2. Princípio fundamental

**Antes de criar uma nova implementação, o agente deverá verificar se já existe no projeto um recurso adequado para atender à necessidade.**

A reutilização deverá ser orientada pela compatibilidade de responsabilidades e comportamentos, não apenas pela semelhança visual ou textual.

O agente não deverá duplicar código sem justificativa, nem criar abstrações compartilhadas sem benefício identificável.

## 3. Responsabilidades do agente

O agente deverá:

- Investigar componentes e serviços existentes antes de criar novos.
- Identificar implementações equivalentes ou semelhantes.
- Avaliar possibilidades de reutilização.
- Preservar a consistência visual e funcional.
- Evitar duplicação desnecessária.
- Reconhecer diferenças legítimas entre funcionalidades.
- Propor extração de componentes compartilhados quando apropriado.
- Avaliar impactos sobre os módulos consumidores.
- Respeitar os padrões arquiteturais do projeto.
- Comunicar riscos de alterações em recursos compartilhados.

## 4. Identificação de recursos existentes

Antes de implementar uma funcionalidade, o agente deverá procurar recursos relacionados à necessidade.

A análise poderá incluir:

- Componentes de interface.
- Hooks e funções reutilizáveis.
- Serviços.
- Validações.
- Tipos e contratos.
- Utilitários.
- Bibliotecas e dependências já instaladas.
- Componentes fornecidos pelo design system do projeto.

O agente deverá priorizar a utilização de recursos aprovados e compatíveis com a arquitetura existente.

A busca deverá ser proporcional à complexidade da alteração.

## 5. Critérios para reutilização

Um recurso existente poderá ser reutilizado quando:

- Sua responsabilidade for compatível com a necessidade.
- Seu comportamento atender aos requisitos.
- Sua utilização não introduzir dependências inadequadas.
- Sua interface permitir a adaptação necessária.
- A reutilização não comprometer outros consumidores.
- A solução permanecer compreensível e sustentável.

O agente não deverá reutilizar um componente apenas porque possui aparência semelhante.

Também não deverá criar uma implementação independente quando um recurso existente atender adequadamente à necessidade.

## 6. Princípio DRY

A metodologia adotará o princípio DRY — Don't Repeat Yourself — como orientação para evitar duplicação desnecessária de conhecimento e lógica.

O agente deverá identificar especialmente:

- Regras de negócio repetidas.
- Validações equivalentes.
- Cálculos duplicados.
- Componentes com comportamentos idênticos.
- Serviços que executam a mesma responsabilidade.
- Contratos ou definições inconsistentes.

Entretanto, a simples repetição de algumas linhas de código não exige automaticamente a criação de uma abstração.

O agente deverá considerar o contexto e a estabilidade da responsabilidade compartilhada.

## 7. Componentes compartilhados

Recursos utilizados por diferentes funcionalidades poderão ser organizados em áreas compartilhadas.

Exemplo:
```
src/
  shared/
    components/
      DataTable/
      ConfirmDialog/
      StatusBadge/
    hooks/
    utils/
```

A estrutura é ilustrativa e deverá respeitar as convenções do projeto.

Um componente compartilhado deverá possuir responsabilidade bem definida e evitar dependência direta de regras exclusivas de uma funcionalidade.

## 8. Componentes específicos de funcionalidades

Componentes utilizados exclusivamente por uma funcionalidade deverão permanecer, preferencialmente, dentro de seu módulo.

Exemplo:
```
src/
  features/
    manutencoes/
      components/
        MaintenanceForm/
        MaintenanceTimeline/
        MaintenanceApproval/
```

O agente não deverá mover componentes para áreas compartilhadas apenas por antecipar uma possível reutilização futura.

A extração deverá ocorrer quando existir justificativa concreta.

## 9. Reutilização e design system

Quando o projeto possuir um design system, o agente deverá utilizá-lo como referência para os componentes visuais.

Deverá preservar:

- Padrões de interface.
- Tipografia.
- Cores e tokens visuais.
- Espaçamentos.
- Estados dos componentes.
- Comportamentos de interação.
- Regras de acessibilidade.

O agente não deverá criar componentes paralelos que reproduzam recursos existentes no design system sem necessidade justificada.

### 9.1. Flexibilidade dos componentes compartilhados

Os componentes compartilhados deverão permitir configurações de apresentação e comportamento quando existirem necessidades legítimas entre diferentes telas ou funcionalidades.

A reutilização de um componente não deverá obrigar todas as suas instâncias a apresentarem dimensões, quantidades de registros ou comportamentos visuais idênticos.

O agente deverá distinguir:

- **Responsabilidade compartilhada:** aquilo que deve permanecer consistente entre as diferentes utilizações.
- **Configuração contextual:** aquilo que pode variar conforme as necessidades da tela.
- **Regra de negócio específica:** aquilo que pertence à funcionalidade e não deve ser incorporado indevidamente ao componente compartilhado.

#### Exemplo: componente de tabela

Um mesmo componente de tabela poderá permitir:

- Altura ajustável conforme o espaço disponível.
- Expansão para ocupar a área vertical livre da tela.
- Altura máxima configurável.
- Rolagem interna quando necessário.
- Quantidade de registros por página configurável.
- Diferentes densidades de apresentação.
- Comportamento responsivo conforme o dispositivo.

O agente deverá avaliar o espaço disponível na interface e evitar áreas vazias desnecessárias quando a expansão do componente melhorar a experiência de utilização.

Em telas com espaço vertical disponível, deverá considerar a expansão da tabela para aproveitar esse espaço.

Em telas com restrições de altura ou outros elementos relevantes, poderá utilizar uma tabela compacta com rolagem interna.

As configurações deverão preservar a consistência do design system, a acessibilidade e a usabilidade.

O agente não deverá criar uma nova implementação de tabela apenas para modificar sua altura ou seu comportamento de rolagem quando o componente compartilhado puder atender adequadamente à necessidade.

Entretanto, não deverá adicionar parâmetros excessivos ou comportamentos incompatíveis apenas para forçar a reutilização.

**Regra:** componentes compartilhados devem preservar a consistência funcional, permitindo adaptações contextuais justificadas.



## 10. Alterações em recursos compartilhados

Antes de modificar um recurso compartilhado, o agente deverá identificar seus consumidores.

A análise deverá considerar:

- Quais funcionalidades utilizam o recurso.
- Quais comportamentos poderão ser alterados.
- Se a mudança preserva compatibilidade.
- Se existem diferentes configurações ou variantes.
- Quais testes precisam ser executados.
- Se a alteração exige aprovação prévia.

Uma modificação pequena em um componente compartilhado poderá produzir impactos amplos.

Por isso, o risco deverá ser avaliado pelo alcance e pelas consequências da alteração, e não apenas pela quantidade de linhas modificadas.

## 11. Extração de recursos compartilhados

Quando identificar duplicações relevantes, o agente poderá propor a criação de um recurso compartilhado.

A proposta deverá indicar:

1. Quais implementações estão duplicadas.
2. Qual responsabilidade possuem em comum.
3. Quais diferenças precisam ser preservadas.
4. Qual recurso compartilhado será criado.
5. Quais módulos serão afetados.
6. Quais riscos existem.
7. Como a alteração será validada.

A extração não deverá ser executada automaticamente quando representar mudança relevante fora do escopo autorizado.

## 12. Prevenção de abstrações excessivas

O agente deverá evitar:

- Componentes com grande quantidade de parâmetros sem necessidade.
- Funções genéricas que concentram responsabilidades diferentes.
- Recursos compartilhados dependentes de regras de negócio específicas.
- Camadas adicionais sem benefício concreto.
- Generalizações baseadas apenas em possibilidades futuras.
- Refatorações que aumentem a complexidade sem melhorar a manutenção.

A reutilização deverá simplificar a arquitetura, não torná-la mais difícil de compreender.

## 13. Reutilização de bibliotecas externas

Antes de adicionar uma biblioteca, o agente deverá verificar:

- Se já existe uma dependência adequada no projeto.
- Se a necessidade pode ser atendida com recursos existentes.
- Se a biblioteca é compatível com o ambiente.
- Se acrescenta complexidade ou riscos desnecessários.
- Se sua manutenção e suas permissões são adequadas.
- Se existem custos ou restrições relevantes.

A inclusão de novas dependências deverá seguir as regras de gestão de mudanças do Pilar Desenvolvimento.

## 14. Limpeza de implementações substituídas

Quando uma implementação for substituída por um recurso compartilhado, o agente deverá identificar os elementos que deixaram de ser necessários.

Poderão existir:

- Componentes antigos.
- Funções duplicadas.
- Importações obsoletas.
- Dependências não utilizadas.
- Testes desatualizados.
- Documentação inconsistente.

A remoção deverá ocorrer somente após análise de dependências e validação, respeitando o escopo aprovado.

## 15. Critérios de conformidade

A diretriz estará sendo respeitada quando:

- O agente verificar recursos existentes antes de criar novos.
- Componentes compartilhados possuírem responsabilidades claras.
- Regras de negócio não forem duplicadas desnecessariamente.
- O design system for respeitado.
- As particularidades das funcionalidades forem preservadas.
- A reutilização não criar dependências inadequadas.
- Alterações compartilhadas forem acompanhadas de análise de impacto.
- Abstrações desnecessárias forem evitadas.
- Implementações substituídas forem tratadas de forma controlada.

## 16. Relação com os demais documentos

### ARQ-01 — Organização por Funcionalidades

Define onde os recursos específicos e compartilhados deverão ser organizados.

### ARQ-03 — Responsabilidades e Dependências

Estabelece os princípios de responsabilidade única, coesão e baixo acoplamento.

### ARQ-04 — Decisões e Evolução Arquitetural

Registra decisões relevantes sobre compartilhamento, dependências e padrões estruturais.

### Pilar Desenvolvimento

Define os procedimentos para avaliar riscos, executar refatorações, controlar mudanças e validar alterações.

## 17. Regra fundamental

**Reutilizar quando houver responsabilidade compartilhada real; manter separado quando as diferenças de contexto justificarem implementações independentes.**

O agente deverá buscar consistência e simplicidade, evitando tanto a duplicação desnecessária quanto a abstração excessiva.
