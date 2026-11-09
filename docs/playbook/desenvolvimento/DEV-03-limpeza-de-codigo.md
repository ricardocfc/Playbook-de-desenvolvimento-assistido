# DEV-03 — Limpeza de Código e Funcionalidades Abandonadas

**Pilar:** 03 — Desenvolvimento  
**Versão:** 1.0  
**Status:** Proposta para aprovação  
**Aplicação:** Todos os projetos desenvolvidos com a metodologia.

---

## 1. Objetivo

Estabelecer procedimentos para identificar e tratar implementações abandonadas, código obsoleto, arquivos desnecessários e resíduos produzidos durante o desenvolvimento.

A metodologia deverá preservar a organização do projeto sem permitir exclusões precipitadas ou alterações que comprometam funcionalidades existentes.

## 2. Princípio fundamental

**Código aparentemente desnecessário não deverá ser removido sem verificação de suas dependências, finalidade e impacto.**

O agente deverá distinguir recursos efetivamente obsoletos daqueles que continuam necessários, mesmo quando não possuem utilização evidente.

A limpeza deverá ser proporcional ao escopo autorizado e ao risco da alteração.

## 3. Responsabilidades do agente

O agente deverá:

- Identificar implementações potencialmente abandonadas.
- Investigar a finalidade dos arquivos envolvidos.
- Verificar referências e dependências.
- Considerar usos indiretos ou dinâmicos.
- Identificar recursos compartilhados.
- Avaliar impactos da remoção.
- Recomendar limpeza quando apropriado.
- Preservar código e dados relevantes.
- Solicitar aprovação quando necessário.
- Validar o funcionamento após a remoção.
- Registrar alterações relevantes.

## 4. Situações que podem exigir limpeza

A necessidade de limpeza poderá surgir quando:

- Uma funcionalidade for cancelada.
- Uma experimentação for descartada.
- Um componente for substituído.
- Uma refatoração eliminar implementações anteriores.
- Uma dependência deixar de ser utilizada.
- Um arquivo se tornar obsoleto.
- Uma solução temporária for substituída.
- Uma funcionalidade for removida do produto.

O agente deverá avaliar cada situação considerando o estado real do projeto.

## 5. Classificação dos elementos identificados

Antes de propor remoções, o agente deverá classificar os elementos encontrados.

### Em uso

Recurso utilizado por uma ou mais funcionalidades.

Não deverá ser removido.

### Potencialmente obsoleto

Recurso sem utilização identificada, mas cuja finalidade ou dependências ainda precisam ser investigadas.

Não deverá ser removido automaticamente.

### Obsoleto confirmado

Recurso cuja finalidade deixou de existir e cuja remoção foi considerada segura após análise adequada.

Poderá ser removido conforme as regras de autorização.

### Compartilhado

Recurso utilizado por diferentes funcionalidades ou contextos.

Sua remoção exigirá avaliação de todos os consumidores relevantes.

### Indeterminado

Recurso cuja utilização não pôde ser confirmada nem descartada com segurança.

Deverá ser preservado até que existam informações suficientes para decidir.

## 6. Análise de dependências

Antes de excluir um elemento, o agente deverá investigar:

- Importações diretas.
- Referências entre módulos.
- Chamadas de funções.
- Utilização de componentes.
- Rotas.
- Configurações.
- Testes.
- Scripts.
- Dependências externas.
- Referências dinâmicas.
- Possíveis consumidores indiretos.

A ausência de referências encontradas por busca textual não será considerada prova suficiente de que um recurso está inutilizado.

Quando a análise não for conclusiva, o agente deverá comunicar a incerteza.

## 7. Funcionalidades abandonadas

Quando o desenvolvedor decidir abandonar uma funcionalidade, o agente deverá identificar em que estágio ela se encontra.

### Ideia não implementada

Deverá ser atualizada a documentação de produto, sem necessidade de limpeza de código.

### Implementação experimental

Deverá ser avaliado o descarte da experimentação, preservando alterações não relacionadas.

### Implementação parcialmente integrada

Deverão ser identificados arquivos, dependências e alterações compartilhadas antes da remoção.

### Funcionalidade integrada ou publicada

A remoção deverá considerar consumidores existentes, dados persistidos, integrações, compatibilidade e possíveis efeitos sobre usuários.

Quanto maior o estágio de integração, maior deverá ser o cuidado com a remoção.

## 8. Limpeza após substituição de componentes

Quando um componente for substituído, o agente deverá verificar se a implementação anterior continua sendo utilizada.

A análise deverá considerar:

- Outras telas consumidoras.
- Variantes do componente.
- Importações.
- Estilos associados.
- Testes.
- Documentação.
- Recursos auxiliares.

O agente não deverá remover um componente compartilhado apenas porque uma das telas deixou de utilizá-lo.

## 9. Dependências não utilizadas

Quando uma biblioteca ou pacote aparentemente deixar de ser necessário, o agente deverá verificar se ainda existe utilização direta ou indireta.

A remoção deverá considerar:

- Código-fonte.
- Scripts.
- Configurações.
- Ferramentas de build.
- Testes.
- Processos de desenvolvimento.
- Dependências de execução.

O agente deverá evitar remover pacotes apenas porque não aparecem nas importações convencionais.

## 10. Código temporário

O agente deverá evitar deixar no projeto resíduos de experimentações e depuração.

Exemplos:

- Logs temporários desnecessários.
- Arquivos de teste improvisados.
- Implementações provisórias substituídas.
- Código comentado sem finalidade.
- Configurações temporárias.
- Dados fictícios utilizados apenas durante testes.

Entretanto, deverá distinguir recursos temporários de ferramentas permanentes de diagnóstico, observabilidade ou testes.

A remoção deverá ocorrer apenas quando sua finalidade estiver esclarecida.

## 11. Dados e estruturas persistentes

A limpeza de código não autoriza automaticamente a exclusão de dados, tabelas, registros ou estruturas persistentes.

Alterações em bancos de dados deverão receber avaliação específica.

O agente deverá considerar:

- Existência de dados reais.
- Dependências entre tabelas.
- Migrações.
- Integridade referencial.
- Compatibilidade com versões existentes.
- Possibilidade de recuperação.
- Necessidade de backup.
- Impactos sobre usuários e integrações.

Operações destrutivas sobre dados deverão exigir autorização explícita e seguir as regras de risco do DEV-05.

## 12. Proposta de limpeza

Quando identificar uma oportunidade relevante de limpeza, o agente deverá apresentar:

1. Elementos identificados.
2. Motivo pelo qual parecem desnecessários.
3. Evidências de obsolescência.
4. Dependências verificadas.
5. Riscos conhecidos.
6. Arquivos ou recursos que serão removidos.
7. Validações previstas.
8. Necessidade de aprovação.

A proposta deverá ser compreensível e proporcional ao impacto.

## 13. Execução controlada

Uma limpeza autorizada deverá seguir, quando aplicável, a sequência:

1. Confirmar o escopo aprovado.
2. Verificar o estado do Git.
3. Preservar alterações preexistentes.
4. Identificar dependências relevantes.
5. Remover os elementos autorizados.
6. Atualizar referências e configurações.
7. Executar verificações adequadas.
8. Inspecionar o resultado.
9. Registrar as alterações.
10. Comunicar pendências ou limitações.

O agente não deverá ampliar o escopo da limpeza sem reavaliar os riscos e as autorizações.

## 14. Validação após a remoção

A validação deverá considerar as funcionalidades potencialmente afetadas.

Poderão ser utilizados:

- Verificação de compilação.
- Testes automatizados.
- Testes de integração.
- Testes de interface.
- Inspeção de rotas.
- Verificação de dependências.
- Execução de jornadas relevantes.

O agente deverá informar quais verificações foram executadas e quais não puderam ser realizadas.

## 15. Limpeza oportunista

Durante uma tarefa, o agente poderá identificar código obsoleto fora do escopo solicitado.

Nesses casos, deverá avaliar a relevância da descoberta.

Problemas pequenos e diretamente relacionados à alteração poderão ser tratados quando estiverem dentro do escopo autorizado e apresentarem risco baixo.

Limpezas independentes ou de maior alcance deverão ser registradas como oportunidades e submetidas à aprovação apropriada.

O agente não deverá transformar uma correção simples em uma refatoração extensa.

## 16. Preservação do histórico

A remoção de código não deverá eliminar indevidamente o histórico das decisões e alterações.

O Git deverá preservar a rastreabilidade das modificações.

Quando uma remoção resultar de decisão relevante, o agente deverá atualizar os registros correspondentes.

Documentos de produto e arquitetura deverão refletir o estado vigente, preservando o histórico necessário para compreender decisões anteriores.

## 17. Critérios de conformidade

O DEV-03 estará sendo respeitado quando:

- Recursos potencialmente obsoletos forem investigados antes da remoção.
- Dependências diretas e indiretas forem consideradas.
- Recursos compartilhados forem preservados quando ainda necessários.
- Funcionalidades abandonadas forem tratadas conforme seu estágio.
- Dados persistentes receberem proteção específica.
- Limpezas relevantes forem justificadas.
- O escopo autorizado for respeitado.
- As remoções forem validadas.
- O histórico permanecer rastreável.
- Incertezas e limitações forem comunicadas.

## 18. Relação com os demais documentos

### PROD-03 — Evolução Contínua

Registra decisões de abandono, substituição ou alteração de funcionalidades.

### ARQ-01 — Organização por Funcionalidades

Define a organização dos recursos que poderão ser afetados pela limpeza.

### ARQ-02 — Componentes Compartilhados

Orienta a identificação de consumidores e implementações reutilizáveis.

### DEV-01 — Versionamento e Git

Preserva o histórico e permite recuperar alterações.

### DEV-02 — Experimentação Controlada

Define como descartar experimentações e branches de forma segura.

### DEV-04 — Análise de Dependências

Estabelece procedimentos para identificar impactos diretos e indiretos.

### DEV-05 — Gestão de Mudanças

Define os níveis de risco e as aprovações necessárias.

### DEV-06 — Intervenção Mínima

Impede que a limpeza ultrapasse desnecessariamente o escopo autorizado.

## 19. Regra fundamental

**O agente deverá manter o projeto livre de implementações comprovadamente desnecessárias, mas nunca deverá sacrificar a segurança, a rastreabilidade ou a integridade do sistema em nome da limpeza do código.**