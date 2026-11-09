# DEV-01 — Versionamento e Controle de Código com Git

**Pilar:** 03 — Desenvolvimento\
**Versão:** 1.0\
**Status:** Aprovado\
**Aplicação:** Todos os projetos desenvolvidos com a metodologia.

---

## 1. Objetivo

Estabelecer regras para utilização de controle de versão, preservando o histórico de desenvolvimento, a rastreabilidade das alterações e a possibilidade de recuperar estados anteriores do projeto.

A metodologia adotará o Git como ferramenta preferencial de versionamento, sem vincular seu funcionamento a uma plataforma específica de hospedagem de repositórios.

## 2. Princípio fundamental

**Alterações no código deverão ser rastreáveis e reversíveis sempre que tecnicamente possível.**

O agente deverá preservar o histórico do projeto e evitar operações que comprometam alterações existentes.

O controle de versão deverá contribuir para a segurança do desenvolvimento sem introduzir procedimentos desnecessariamente complexos.

## 3. Responsabilidades do agente

O agente deverá:

- Verificar se o projeto utiliza Git.
- Identificar o repositório e a branch atual.
- Consultar o estado dos arquivos antes de modificá-los.
- Identificar alterações preexistentes.
- Preservar modificações realizadas pelo desenvolvedor ou por outros agentes.
- Organizar alterações de maneira compreensível.
- Recomendar commits em momentos adequados.
- Utilizar mensagens de commit descritivas.
- Evitar operações destrutivas sem autorização.
- Informar o estado do versionamento ao encerrar o trabalho.

## 4. Diagnóstico inicial

Antes de iniciar uma tarefa que envolva alterações no código, o agente deverá verificar, quando possível:

- Se o diretório pertence a um repositório Git.
- Qual é a branch ativa.
- Se existem arquivos modificados.
- Se existem arquivos novos ainda não versionados.
- Se há alterações previamente preparadas para commit.
- Se existem conflitos de merge.
- Se o projeto possui convenções de versionamento.

A profundidade da análise deverá ser proporcional à tarefa.

O agente não deverá presumir que todas as alterações encontradas foram produzidas por ele.

## 5. Preservação das alterações existentes

Arquivos modificados antes do início da tarefa deverão ser tratados como trabalho preexistente.

O agente não deverá:

- Descartar alterações sem autorização.
- Sobrescrever trabalho não relacionado.
- Executar restaurações destrutivas indiscriminadas.
- Remover arquivos desconhecidos apenas para limpar o repositório.
- Incluir alterações de terceiros em commits sem avaliação.

Quando uma alteração preexistente interferir na tarefa, o agente deverá explicar a situação e propor um encaminhamento seguro.

## 6. Organização dos commits

Os commits deverão representar conjuntos coerentes de alterações.

Sempre que adequado, deverão estar relacionados a:

- Implementação de funcionalidade.
- Correção de defeito.
- Refatoração.
- Ajuste de documentação.
- Alteração de configuração.
- Atualização de testes.

O agente deverá evitar commits que misturem mudanças independentes sem justificativa.

Também deverá evitar fragmentação excessiva em commits sem significado próprio.

## 7. Mensagens de commit

As mensagens deverão permitir compreender a finalidade da alteração.

Exemplos:

- `feat: adiciona aprovação de manutenções`
- `fix: corrige validação de fornecedor`
- `refactor: reutiliza componente de tabela`
- `docs: registra decisão de autenticação`
- `test: adiciona testes do fluxo de compras`

O uso de Conventional Commits poderá ser adotado como convenção do projeto, mas não será obrigatório para toda aplicação.

O agente deverá respeitar o padrão aprovado para o repositório.

## 8. Autorização para commits

O agente deverá distinguir entre preparar alterações e registrá-las no histórico.

A execução automática de commits dependerá das permissões e das regras estabelecidas para o projeto.

Quando não houver autorização para commits automáticos, o agente deverá apresentar as alterações e solicitar confirmação.

A criação de um commit não representa, isoladamente, aprovação funcional da implementação.

## 9. Branches

O uso de branches deverá seguir a política de experimentação controlada definida no DEV-02.

O agente não deverá criar uma nova branch obrigatoriamente para toda alteração.

A necessidade deverá considerar:

- Risco.
- Alcance.
- Complexidade.
- Possibilidade de regressão.
- Existência de trabalho paralelo.
- Convenções do projeto.

Mudanças simples poderão seguir um fluxo mais direto quando isso estiver autorizado.

## 10. Operações de risco

Operações potencialmente destrutivas deverão exigir atenção especial.

Exemplos:

- `git reset --hard`
- `git clean -fd`
- Reescrita de histórico.
- Exclusão de branches com trabalho não integrado.
- Push forçado.
- Descarte de alterações locais.
- Substituição de histórico remoto.

O agente não deverá executar essas operações sem necessidade demonstrada e autorização explícita.

Antes de executá-las, deverá explicar o alcance, os riscos e as alternativas disponíveis.

## 11. Repositórios remotos

Quando o projeto utilizar repositório remoto, o agente deverá respeitar as configurações e permissões existentes.

Deverá distinguir:

- Alterações locais.
- Commits locais.
- Envio de commits ao repositório remoto.
- Integração de branches.
- Publicação da aplicação.

Essas ações não são equivalentes.

O agente não deverá presumir que autorização para modificar código também autoriza publicar alterações ou executar deploy.

## 12. Relação entre Git e implantação

O versionamento deverá permitir identificar qual versão do código foi utilizada em uma implantação.

Quando o projeto possuir integração contínua ou deploy automático, o agente deverá considerar as consequências de operações como push e merge.

A existência de deploy automático deverá ser identificada antes de ações capazes de disparar uma publicação.

A aprovação de código, a integração no repositório e a implantação em produção deverão ser tratadas como etapas distintas quando o fluxo do projeto assim exigir.

## 13. Segurança de informações

O agente deverá evitar incluir no repositório:

- Senhas.
- Tokens.
- Chaves privadas.
- Credenciais.
- Arquivos de ambiente contendo segredos.
- Dados pessoais ou confidenciais sem necessidade e autorização.

Deverá respeitar os arquivos de exclusão, como `.gitignore`, e as práticas de segurança adotadas.

Caso identifique um segredo potencialmente exposto, deverá comunicar o problema e recomendar medidas apropriadas.

A simples exclusão do arquivo não garante a remoção de informações já registradas no histórico.

## 14. Recuperação de versões

O Git deverá ser utilizado como mecanismo para recuperar estados anteriores do código quando necessário.

Entretanto, o agente deverá avaliar o impacto de qualquer reversão antes de executá-la.

Uma reversão poderá afetar alterações posteriores ou funcionalidades dependentes.

O agente deverá priorizar procedimentos que preservem o histórico e minimizem a perda de trabalho.

## 15. Rastreabilidade

Sempre que viável, as alterações deverão possuir vínculo com:

- Funcionalidade.
- Requisito.
- Jornada.
- Correção solicitada.
- Decisão arquitetural.
- Registro de desenvolvimento.

O objetivo é permitir compreender não apenas o que mudou, mas por que a mudança foi realizada.

Essa rastreabilidade deverá ser proporcional à complexidade e ao risco da alteração.

## 16. Encerramento da tarefa

Ao concluir uma tarefa, o agente deverá informar:

- Quais arquivos foram modificados.
- Quais alterações foram realizadas.
- Se houve commit.
- Qual branch foi utilizada.
- Se existem mudanças não registradas.
- Se houve envio ao repositório remoto.
- Se ocorreu alguma implantação.
- Quais pendências permanecem.

O relatório deverá ser objetivo e compreensível.

## 17. Critérios de conformidade

O DEV-01 estará sendo respeitado quando:

- O estado do repositório for verificado antes das alterações relevantes.
- O trabalho preexistente for preservado.
- Os commits forem coerentes e compreensíveis.
- As operações destrutivas forem controladas.
- As regras de branches forem respeitadas.
- O agente distinguir alterações locais, commits, push e deploy.
- Informações sensíveis não forem incluídas indevidamente.
- As alterações puderem ser rastreadas.
- O estado final do versionamento for comunicado.

## 18. Relação com os demais documentos

### DEV-02 — Experimentação Controlada

Define quando utilizar branches e como isolar alterações de maior risco.

### DEV-05 — Gestão de Mudanças

Determina os níveis de risco e as autorizações necessárias.

### DEV-06 — Intervenção Mínima

Define os limites da alteração e a análise de impacto.

### DEV-10 — Encerramento de Sessão

Consolida o estado do repositório e as pendências para continuidade.

### DEV-11 — Histórico de Desenvolvimento

Relaciona mudanças de código às decisões e atividades realizadas.

## 19. Regra fundamental

**O agente deverá preservar o histórico e o trabalho existente, mantendo as alterações rastreáveis e evitando operações de versionamento que possam causar perda de código ou publicação não autorizada.**
