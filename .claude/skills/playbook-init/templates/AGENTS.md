# Instruções para agentes de IA

<!-- playbook:inicio — bloco mantido pelo AI Development Playbook. Não duplique as normas aqui. -->

Este projeto segue o **AI Development Playbook**, versão registrada em `docs/playbook/MANIFEST.md`.
A cópia local em `docs/playbook/` é a referência normativa. Este arquivo só aponta para ela.

## Primeira sessão
Se o projeto ainda não foi inicializado (não há handoff em `Specs/sessions/`), execute `Skills/playbook-init/SKILL.md` antes de qualquer outra tarefa.

## Início de cada sessão
1. Confira a versão em `docs/playbook/MANIFEST.md`.
2. Leia o handoff mais recente em `Specs/sessions/` e as REQs citadas.
3. Verifique o estado atual do repositório antes de confiar nos registros.
4. Consulte os documentos do Playbook pertinentes à tarefa (não é preciso reler tudo).

## Fluxo de trabalho: skills
Leia e siga o `SKILL.md` correspondente quando a tarefa se encaixar:

| Situação | Skill |
|---|---|
| Inicializar ou diagnosticar o projeto | `Skills/playbook-init/SKILL.md` |
| Novo pedido sem REQ registrada | `Skills/playbook-spec/SKILL.md` |
| Analisar impacto, risco e planejar uma REQ | `Skills/playbook-plan/SKILL.md` |
| Implementar uma REQ autorizada | `Skills/playbook-implement/SKILL.md` |
| Validar uma REQ implementada | `Skills/playbook-review/SKILL.md` |
| Encerrar, pausar ou retomar uma sessão | `Skills/playbook-handoff/SKILL.md` |
| Auditar conformidade | `Skills/playbook-audit/SKILL.md` |

Terminar uma skill **não** dispara a próxima. Recomende o próximo passo e aguarde.

## Trilhas (proporcionais ao risco, DEV-05)
- **Curta (baixo risco evidente):** `playbook-spec` registra um `REQ-NNN.md` simples → `playbook-implement` → verificação resumida no próprio arquivo. Sem `playbook-plan`, sem arquivo de sessão se nada ficar pendente. Exemplos: texto, estilo, ajuste localizado em componente não compartilhado.
- **Completa (risco médio ou alto, ou dúvida):** spec → plan → implement → review → handoff.
- Se o risco subir no meio do caminho, pare e passe para a trilha completa.
- Nas duas trilhas valem: REQ registrada, escopo respeitado, nenhum teste declarado sem ter rodado, e commit/push/merge/deploy só com autorização.

## Leitura econômica
- O checklist de cada skill é suficiente para baixo risco. Abra uma norma só na seção que a skill indica, quando a situação pedir.
- Não releia `docs/playbook/` inteiro a cada sessão; a leitura integral acontece uma vez, no `playbook-init`.

## Onde as coisas ficam
- `Specs/SPEC-NNN-nome/spec.md`: comportamento vigente. `history.md`: evolução funcional (aditivo).
- `Specs/SPEC-NNN-nome/requests/`: registros das REQs (`REQ-NNN.md` ou `REQ-NNN/`).
- `Specs/sessions/`: handoffs de sessão.
- `docs/decisoes/`, `docs/incidentes/`, `docs/riscos/`: decisões arquiteturais, incidentes e riscos.
- `docs/playbook/`: metodologia. Não registre informações do produto aqui.

## Regras essenciais (DEV-12 §9)
- Não modifique arquivos fora do escopo autorizado.
- Não descarte alterações desconhecidas nem execute operações destrutivas sem autorização.
- Não presuma aprovação: especificação aprovada não autoriza implementar; implementação não autoriza commit, push, merge ou deploy.
- Não invente requisitos. Só requisito Confirmado vai para implementação.
- Não afirme testes não executados. Impacto previsto não é implementado; implementado não é validado.
- Não instale ferramentas sem avaliação e autorização (DEV-07). Não exponha credenciais.
- Classifique o risco de cada mudança (DEV-05) e mantenha a autonomia proporcional a ele.
- Registre decisões relevantes e o necessário para a continuidade entre sessões.
- Comunique divergências entre código, documentação e normas; não as resolva em silêncio.

## Contexto específico deste projeto
<!-- Preencha: stack, comandos de build e teste, convenção de commits, política de branches, autorizações permanentes. -->

<!-- playbook:fim -->
