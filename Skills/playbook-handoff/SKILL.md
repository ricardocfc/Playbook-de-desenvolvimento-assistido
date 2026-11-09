---
name: playbook-handoff
description: Encerra uma sessão ou etapa registrando o estado real do trabalho, alterações, Git, testes, decisões, pendências e próxima ação, e confere a rastreabilidade entre SPECs. Também orienta a retomada no início da sessão seguinte. Use ao final de uma sessão, ao pausar uma REQ, ao trocar de agente ou quando o desenvolvedor pedir "encerrar", "handoff" ou "retomar".
---

# playbook-handoff — Encerramento e retomada

Executa o COP-01 §16 e §21.5. As normas são a autoridade; este arquivo é um roteiro.

## Quando consultar as normas
Para baixo risco, este roteiro basta. Abra a norma só quando:
- Encerrar trabalho de risco médio ou alto, ou com problemas não resolvidos → DEV-10 §17 e §18.
- Houver REQs entre SPECs → DEV-10 §23 e DEV-11 §25.
- Retomar trabalho de outro agente ou com registros divergentes do código → DEV-09 §8, §18 e §24.

Caminhos: `docs/playbook/desenvolvimento/`.

## Autorização
- Ler e registrar o handoff em `Specs/sessions/`: conforme autorização do projeto para arquivos de registro.
- Commit, push ou qualquer nova operação: **não** decorrem do encerramento (COP-01 §12).

## Proporcionalidade
- **Trilha curta, concluída na mesma sessão:** basta preencher a seção Encerramento do `REQ-NNN.md`. Crie arquivo em `Specs/sessions/` só se a sessão terminar com algo pendente.
- **Trilha completa, trabalho pausado ou troca de agente:** siga o procedimento inteiro.

## Encerramento: procedimento
1. **Estado real de cada REQ tocada (DEV-10 §5):** concluído, concluído com ressalvas, parcialmente concluído, bloqueado ou não iniciado. O estado precisa bater com as evidências.
2. **Estado do repositório:** branch, commits feitos, alterações não commitadas, stash. Não descarte nada.
3. **Testes e validações:** o que rodou, resultado, o que não rodou e por quê.
4. **Decisões** tomadas na sessão e onde foram registradas.
5. **Rastreabilidade entre SPECs (DEV-10 §23):** para cada REQ com SPECs associadas, confira referências cruzadas, estado dos impactos e se `history.md` e `spec.md` foram atualizados após validação. Se não foram, registre a pendência explicitamente (T-08).
6. **Atualizar a REQ** com o estado e o encerramento.
7. **Gravar o handoff** em `Specs/sessions/AAAA-MM-DD-<assunto>.md` usando `templates/sessao.md`. O handoff referencia REQs; não copia seus registros (COP-01 §21.5). Em tarefa de baixo risco, um registro curto basta (DEV-10 §17).

## Retomada: procedimento (início da sessão seguinte ou agente novo)
1. Leia o adaptador (`AGENTS.md`/`CLAUDE.md`) e confira a versão em `docs/playbook/MANIFEST.md`.
2. Leia o handoff mais recente em `Specs/sessions/` e as REQs que ele cita.
3. **Reconfronte com o estado atual** do repositório: os registros podem estar desatualizados (DEV-09 §18, T-09). Não presuma resultados anteriores.
4. Recupere `spec.md`, `history.md` e decisões pertinentes à tarefa (DEV-09 §24).
5. Informe ao desenvolvedor o estado recuperado, divergências e a ação proposta, e aguarde autorização para operações que a exijam.

## Saída

**Registro.** O bloco abaixo é o conteúdo mínimo que vai para os arquivos do projeto (REQ, sessão, relatório). Nele, identificadores e referências às normas são bem-vindos. **Não cole este bloco na conversa.**

```markdown
## Encerramento — <data> <assunto>
- REQs: <REQ-NNN: estado real>
- Alterações: <resumo, arquivos>
- Git: <branch, commits, não commitado>
- Testes: <executados e resultado | não executados e motivo>
- Decisões: <lista e onde estão registradas>
- Rastreabilidade entre SPECs: <ok | pendências>
- Pendências e riscos: <lista>
- Autorizações necessárias para seguir: <lista>
- Próxima ação recomendada: <...>
- Registro: Specs/sessions/<arquivo>.md
```

**Resposta ao desenvolvedor.** Siga "Como falar com o desenvolvedor" no `AGENTS.md`: palavras comuns, sem códigos de documentos nem nomes de skills. Diga o que foi feito, o que você precisa dele e o que dá para fazer em seguida. Exemplo: "Salvei onde paramos e o que ficou pendente. Na próxima conversa é só pedir para continuar."

## Limites
- Não transforme encerramento em autorização para novas operações (COP-01 §12).
- O histórico da conversa não é a única fonte: o que importa para continuar precisa estar em arquivo (DEV-10 §15).
