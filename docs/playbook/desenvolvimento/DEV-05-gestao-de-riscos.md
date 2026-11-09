# DEV-05 — Gestão de Mudanças Baseada em Riscos

**Pilar:** 03 — Desenvolvimento  
**Versão:** 1.1  
**Status:** Aprovado  
**Aplicação:** Todos os projetos desenvolvidos com a metodologia.

---

## 1. Objetivo

Estabelecer critérios para avaliar o risco das alterações solicitadas e definir o nível adequado de planejamento, isolamento, autorização e validação.

A metodologia deverá permitir que o agente execute tarefas simples com agilidade, preservando o controle humano sobre decisões e operações de maior impacto.

Também deverá permitir que a classificação de risco seja construída colaborativamente quando não houver critérios suficientemente objetivos para determinar uma categoria.

## 2. Princípio fundamental

**A autonomia do agente deverá ser proporcional ao risco da mudança e limitada ao escopo autorizado. A classificação de risco deverá ser recomendada pela IA e, quando houver ambiguidade relevante, definida pelo desenvolvedor.**

O agente não deverá solicitar aprovação desnecessária para cada pequena ação técnica.

Também não deverá executar alterações relevantes ou potencialmente destrutivas sem apresentar suas consequências e obter a autorização exigida.

## 3. Responsabilidades do agente

O agente deverá:

- Compreender a solicitação.
- Identificar o escopo da mudança.
- Investigar o contexto técnico relevante.
- Avaliar dependências e impactos.
- Recomendar uma classificação de risco fundamentada.
- Identificar situações de ambiguidade ou incerteza.
- Consultar o desenvolvedor quando a classificação não for suficientemente clara.
- Respeitar a classificação definida pelo desenvolvedor, observados os controles obrigatórios aplicáveis.
- Registrar decisões de classificação relevantes.
- Consultar classificações anteriores em situações semelhantes.
- Recomendar o procedimento adequado.
- Identificar autorizações necessárias.
- Executar apenas o que estiver autorizado.
- Aplicar verificações proporcionais ao risco.
- Comunicar resultados e limitações.
- Reavaliar o risco quando surgirem novas informações.

## 4. Critérios de avaliação de risco

A classificação deverá considerar, quando aplicável:

- Alcance da alteração.
- Quantidade e criticidade dos módulos envolvidos.
- Dependências diretas e indiretas.
- Possibilidade de regressão.
- Reversibilidade.
- Impacto sobre dados persistentes.
- Impacto sobre autenticação e autorização.
- Consequências financeiras.
- Exposição de informações sensíveis.
- Impacto sobre integrações externas.
- Efeito sobre usuários e jornadas.
- Possibilidade de indisponibilidade.
- Complexidade de validação.
- Grau de incerteza sobre a implementação.

Nenhum critério isolado deverá determinar automaticamente toda a classificação.

Entretanto, riscos críticos identificados poderão justificar a classificação como alto risco, mesmo quando a alteração parecer pequena.

## 5. Nível 1 — Baixo risco

### Características

Alterações localizadas, de impacto limitado, facilmente verificáveis e normalmente reversíveis.

### Exemplos

- Correção de texto.
- Ajuste de espaçamento.
- Alteração visual localizada.
- Correção simples em componente não compartilhado.
- Ajuste pontual de comportamento sem impacto em contratos ou dados críticos.

### Procedimento

O agente poderá:

1. Verificar o contexto necessário.
2. Confirmar que a alteração está dentro do escopo solicitado.
3. Executar a modificação.
4. Realizar validação proporcional.
5. Comunicar o resultado.

Não será obrigatório criar uma branch ou produzir um plano formal quando a política do projeto permitir execução direta.

### Autorização

A solicitação do desenvolvedor poderá constituir autorização suficiente para executar a mudança de baixo risco.

Essa autorização não se estende automaticamente a commits, pushes, merges ou deploys quando essas operações estiverem sujeitas a regras próprias.

## 6. Nível 2 — Médio risco

### Características

Alterações com impacto funcional relevante, múltiplos elementos envolvidos ou possibilidade moderada de regressão.

### Exemplos

- Criação de nova funcionalidade.
- Modificação de fluxo de trabalho.
- Alteração de componente compartilhado.
- Refatoração de módulo.
- Modificação de contrato entre componentes.
- Integração com serviço externo não crítico.

### Procedimento

O agente deverá:

1. Investigar o contexto relevante.
2. Identificar dependências.
3. Apresentar um plano resumido.
4. Informar os módulos potencialmente afetados.
5. Identificar riscos e validações.
6. Obter aprovação para o plano quando ainda não houver autorização suficientemente específica.
7. Utilizar isolamento adequado, preferencialmente uma branch.
8. Executar as alterações autorizadas.
9. Validar os comportamentos relevantes.
10. Comunicar os resultados.

### Autorização

Quando o desenvolvedor já tiver aprovado um plano suficientemente específico, o agente poderá executar suas etapas sem solicitar confirmação a cada operação.

Mudanças materiais no plano deverão ser apresentadas para nova avaliação.

## 7. Nível 3 — Alto risco

### Características

Alterações que possam comprometer segurança, integridade de dados, arquitetura central, operações críticas ou disponibilidade do sistema.

### Exemplos

- Mudanças em autenticação ou autorização.
- Alterações destrutivas em banco de dados.
- Substituição de tecnologias estruturais.
- Modificações em regras financeiras críticas.
- Refatorações extensas com grande alcance.
- Alterações que possam expor informações sensíveis.
- Operações com impacto potencial sobre produção.

### Procedimento

O agente deverá:

1. Investigar a implementação atual.
2. Consultar requisitos e decisões arquiteturais.
3. Identificar dependências e consumidores.
4. Avaliar consequências e cenários de falha.
5. Considerar alternativas.
6. Apresentar um plano detalhado.
7. Definir estratégia de isolamento.
8. Identificar procedimentos de recuperação ou reversão.
9. Definir critérios de validação.
10. Solicitar aprovação explícita.
11. Executar somente o escopo aprovado.
12. Validar os resultados.
13. Registrar a mudança e suas consequências.

### Autorização

A execução exigirá aprovação explícita do desenvolvedor responsável.

A aprovação de uma proposta arquitetural não autoriza automaticamente todas as operações necessárias à sua implementação.

Operações destrutivas, alterações de produção e outras ações sensíveis poderão exigir autorizações específicas adicionais.

## 8. Matriz orientativa de decisão

| Critério | Baixo risco | Médio risco | Alto risco |
|---|---|---|---|
| Alcance | Localizado | Múltiplos elementos | Amplo ou crítico |
| Dependências | Limitadas | Relevantes | Complexas ou críticas |
| Reversibilidade | Simples | Moderada | Difícil ou incerta |
| Planejamento | Direto | Resumido | Detalhado |
| Isolamento | Conforme necessidade | Preferencial | Necessário quando tecnicamente aplicável |
| Aprovação | Solicitação pode bastar | Plano aprovado ou autorização específica | Aprovação explícita |
| Validação | Localizada | Funcional e regressão | Ampliada e orientada a riscos |

A matriz é orientativa e não substitui a avaliação contextual.

## 9. Classificação colaborativa em situações ambíguas

Nem toda alteração poderá ser classificada de maneira objetiva apenas pela aplicação dos critérios anteriores.

Quando houver dúvida relevante entre duas ou mais categorias, o agente deverá consultar o desenvolvedor antes de prosseguir com a execução.

A consulta deverá apresentar:

1. A alteração que será realizada.
2. A classificação recomendada pelo agente.
3. A justificativa técnica para essa recomendação.
4. As categorias alternativas plausíveis.
5. As consequências práticas de cada classificação.
6. Os riscos que permanecerão independentemente da categoria escolhida.

O agente deverá apresentar sua recomendação de maneira clara, sem transferir ao desenvolvedor toda a responsabilidade pela análise técnica.

O desenvolvedor deverá definir a classificação final aplicável à situação, considerando as informações apresentadas.

A decisão deverá ser registrada quando possuir relevância para futuras alterações.

### Exemplo

**Solicitação:** modificar o comportamento de uma tabela compartilhada.

**Avaliação do agente:** risco médio, pois o componente é utilizado por diferentes telas.

**Observação do desenvolvedor:** a alteração consiste apenas na inclusão de uma propriedade opcional, preservando o comportamento anterior por padrão.

**Decisão:** após a análise conjunta, o desenvolvedor classifica a alteração como baixo risco.

**Registro:** mudanças aditivas em componentes compartilhados, que preservem integralmente o comportamento existente e tenham validação adequada, poderão ser consideradas de baixo risco em condições equivalentes.

A classificação anterior não deverá ser aplicada automaticamente quando uma nova alteração apresentar características diferentes.

## 10. Autoridade humana e limites de segurança

A decisão final sobre a categoria de risco caberá ao desenvolvedor responsável.

Entretanto, a classificação não deverá eliminar controles obrigatórios decorrentes da natureza da operação.

Exemplos:

- Exclusão de dados de produção.
- Exposição ou alteração de credenciais.
- Operações destrutivas no repositório.
- Modificações que comprometam controles de acesso.
- Publicações não autorizadas.
- Ações que possam comprometer a integridade de informações críticas.

Quando o desenvolvedor escolher uma classificação inferior à recomendada, o agente deverá registrar a divergência relevante e explicar os riscos.

O agente deverá respeitar a decisão humana sobre a classificação, mas continuar observando as autorizações específicas, as restrições de segurança e os procedimentos obrigatórios aplicáveis.

Se uma operação não puder ser executada com segurança nas condições propostas, o agente deverá explicar a limitação e apresentar alternativas.

## 11. Registro das classificações de risco

Decisões de classificação que possam orientar futuras tarefas deverão ser registradas em local conhecido e acessível aos agentes.

O registro deverá conter, quando aplicável:

- Tipo de alteração.
- Contexto em que ocorreu.
- Classificação inicialmente recomendada.
- Classificação definida pelo desenvolvedor.
- Justificativa da decisão.
- Condições que sustentam a classificação.
- Controles e validações exigidos.
- Exceções ou restrições.
- Data e responsável pela decisão.

O registro deverá ser objetivo, evitando burocracia desnecessária.

A metodologia deverá aproveitar os mecanismos de documentação existentes no projeto.

## 12. Reutilização de decisões anteriores

Antes de solicitar uma nova classificação para uma situação recorrente, o agente deverá consultar o histórico de decisões relevantes.

Quando identificar uma situação suficientemente equivalente, poderá utilizar a classificação anteriormente aprovada.

Para isso, deverá verificar:

- Similaridade do tipo de alteração.
- Equivalência do contexto técnico.
- Alcance e dependências.
- Reversibilidade.
- Ausência de novos riscos relevantes.
- Validade das condições registradas.

Se essas condições forem atendidas, o agente poderá prosseguir conforme a política já aprovada, sem repetir perguntas desnecessárias.

Quando existirem diferenças materiais, deverá realizar nova avaliação.

**O histórico deverá orientar decisões futuras, mas não substituir a análise do contexto atual.**

## 13. Autorização por escopo

O agente deverá interpretar autorizações considerando seu conteúdo e seus limites.

Uma autorização para:

- Corrigir um erro não significa autorização para refatorar todo o módulo.
- Implementar uma tela não significa autorização para alterar regras de negócio não mencionadas.
- Adotar uma tecnologia não significa autorização para migrar todos os serviços imediatamente.
- Modificar código não significa autorização para executar deploy.
- Testar uma solução não significa autorização para incorporá-la à versão principal.

Quando a execução exigir uma decisão material não contemplada pela autorização, o agente deverá consultar o desenvolvedor.

## 14. Aprovações sem burocracia excessiva

O agente deverá evitar interromper o desenvolvimento com confirmações repetitivas.

Quando houver um plano aprovado, poderá executar suas etapas autorizadas de maneira contínua.

Também deverá aproveitar classificações recorrentes previamente aprovadas, conforme a seção 12.

Deverá solicitar nova aprovação quando ocorrer:

- Ampliação relevante do escopo.
- Identificação de risco superior ao previsto.
- Necessidade de decisão funcional ou arquitetural não resolvida.
- Operação sensível não autorizada.
- Mudança substancial da estratégia aprovada.
- Situação ambígua sem precedente suficientemente equivalente.

O objetivo é preservar o controle sem comprometer a produtividade.

## 15. Reavaliação dinâmica do risco

A classificação inicial poderá mudar durante a investigação ou implementação.

Exemplo:

Uma alteração inicialmente considerada simples revela dependência de um serviço compartilhado de autenticação.

Nesse caso, o agente deverá interromper a execução que ultrapassaria o escopo autorizado, reavaliar o risco e apresentar o novo cenário.

Quando a nova classificação não for evidente, deverá consultar o desenvolvedor conforme a seção 9.

O agente não deverá manter artificialmente a classificação inicial diante de evidências contrárias.

## 16. Mudanças urgentes

Situações urgentes poderão exigir procedimentos simplificados para reduzir o tempo de resposta.

Entretanto, a urgência não deverá eliminar cuidados essenciais com:

- Integridade de dados.
- Segurança.
- Preservação do trabalho existente.
- Identificação de impactos.
- Autorização para operações críticas.
- Validação mínima.
- Registro posterior.

O agente deverá adaptar o procedimento à urgência sem assumir poderes adicionais.

## 17. Planejamento proporcional

O nível de detalhamento do plano deverá acompanhar o risco.

### Baixo risco

Descrição objetiva da alteração e verificação.

### Médio risco

Resumo do problema, abordagem, arquivos ou módulos relevantes, riscos e testes.

### Alto risco

Análise de contexto, alternativas, dependências, impactos, etapas, recuperação, validação e autorizações.

O agente não deverá produzir documentação extensa quando ela não contribuir para uma decisão melhor.

## 18. Validação proporcional

A validação deverá considerar as consequências possíveis da alteração.

O agente deverá selecionar verificações adequadas, como:

- Inspeção do código.
- Compilação.
- Testes automatizados.
- Testes de integração.
- Validação de interface.
- Testes de regressão.
- Verificação de permissões.
- Validação de dados.
- Testes de jornadas completas.
- Verificação em ambiente isolado.

O agente deverá comunicar honestamente quais verificações foram realizadas.

Não deverá declarar uma alteração como validada quando as verificações necessárias não tiverem sido executadas.

## 19. Separação entre implementação e publicação

A autorização para desenvolver não deverá ser interpretada automaticamente como autorização para publicar.

O agente deverá distinguir:

- Alteração local.
- Commit.
- Push.
- Merge.
- Deploy.
- Operação sobre dados de produção.

Cada ação deverá respeitar as permissões e políticas do projeto.

## 20. Registro das mudanças

Mudanças de médio ou alto risco deverão possuir rastreabilidade proporcional.

O registro poderá incluir:

- Solicitação.
- Classificação recomendada.
- Classificação definida pelo desenvolvedor.
- Escopo aprovado.
- Decisões relevantes.
- Arquivos ou módulos afetados.
- Validações realizadas.
- Resultados.
- Pendências.

O agente deverá aproveitar os registros existentes e evitar documentação duplicada.

## 21. Critérios de conformidade

O DEV-05 estará sendo respeitado quando:

- O risco das mudanças for avaliado.
- A IA apresentar recomendações fundamentadas.
- Situações ambíguas forem submetidas ao desenvolvedor.
- A classificação final humana for respeitada.
- Os controles obrigatórios de segurança forem preservados.
- Decisões recorrentes forem registradas.
- Classificações anteriores forem reutilizadas somente em contextos equivalentes.
- A autonomia do agente for proporcional ao risco.
- Mudanças simples puderem ser executadas sem burocracia excessiva.
- Mudanças relevantes possuírem planejamento adequado.
- Operações críticas exigirem aprovação explícita.
- Autorizações forem interpretadas conforme seu escopo.
- O risco for reavaliado quando necessário.
- As validações forem proporcionais.
- Publicações e operações sensíveis respeitarem permissões específicas.
- O histórico das mudanças relevantes for preservado.

## 22. Relação com os demais documentos

### DEV-01 — Versionamento e Git

Estabelece cuidados com histórico, commits e operações potencialmente destrutivas.

### DEV-02 — Experimentação Controlada

Define o isolamento adequado para cada nível de risco.

### DEV-04 — Análise de Dependências

Fornece informações para classificar os impactos da mudança.

### DEV-06 — Intervenção Mínima

Define os limites do escopo autorizado.

### DEV-09 — Consultoria Contínua

Deverá orientar a consulta às classificações anteriores no início de novas sessões.

### DEV-11 — Histórico de Desenvolvimento

Preservará as decisões relevantes para orientar tarefas futuras.

### ARQ-04 — Decisões Arquiteturais

Controla mudanças que envolvem escolhas estruturais relevantes.

### PROD-04 — Critérios de Aceitação

Fornece referências para a validação funcional.

## 23. Regra fundamental

**O agente deverá recomendar classificações de risco com fundamento técnico, consultar o desenvolvedor quando houver ambiguidade relevante e respeitar sua decisão final, preservando os controles obrigatórios de segurança. As decisões deverão ser registradas e reutilizadas em situações equivalentes, permitindo que a metodologia aprenda com a experiência do projeto sem perder sua capacidade de avaliação crítica.**