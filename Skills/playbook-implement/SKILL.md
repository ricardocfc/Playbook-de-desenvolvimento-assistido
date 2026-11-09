---
name: playbook-implement
description: Executa as alterações autorizadas de uma REQ planejada, preservando escopo, trabalho existente e estado do repositório, e registra o que de fato mudou. Use quando o desenvolvedor autorizar a implementação de uma REQ. Não declara validação nem publica.
---

# playbook-implement — Implementação sob controle de escopo

Executa o COP-01 §9 e §15. As normas são a autoridade; este arquivo é um roteiro.

## Fontes normativas
- `docs/playbook/desenvolvimento/DEV-06-controle-de-escopo.md` (§9 a §14, §17, §18)
- `docs/playbook/desenvolvimento/DEV-01-versionamento-git.md` (§5 preservação, §6 a §8 commits, §10 operações de risco)
- `docs/playbook/desenvolvimento/DEV-02-branches-e-experimentacao.md`
- `docs/playbook/desenvolvimento/DEV-05-gestao-de-riscos.md` (§15 reavaliação, §19 implementação x publicação)
- `docs/playbook/arquitetura/` conforme a área tocada
- `docs/playbook/desenvolvimento/DEV-13-orquestracao-de-recursos.md` se delegar a subagentes

## Pré-requisitos (verifique, não presuma)
1. Existe autorização para implementar **esta** REQ, com escopo definido. Aprovação de especificação ou de plano sozinha não basta (T-12, T-18).
2. O estado real do repositório: branch atual, alterações não commitadas, divergências com o plano. Não descarte alterações desconhecidas (DEV-01 §5).
3. A capacidade pedida ainda não existe no código (COP-01 §15). Se existir, pare e informe.

## Procedimento
1. **Isolamento.** Risco médio ou alto: trabalhe em branch quando aplicável (DEV-02). Criar branch segue as regras do projeto.
2. **Executar só o escopo autorizado.** Siga `tasks.md` ou as tarefas da REQ. Intervenção mínima não significa solução incompleta (DEV-06 §6).
3. **Descobriu algo novo?** Pare a parte que ultrapassaria o escopo e:
   - alteração necessária para concluir a REQ → apresente e peça autorização (DEV-06 §9, T-07);
   - melhoria fora do escopo → registre como recomendação, não execute (DEV-06 §10);
   - risco maior que o previsto → reclassifique e consulte (DEV-05 §15);
   - finalidade independente → proponha nova REQ (COP-01 §17).
4. **Componentes compartilhados:** preserve o comportamento existente dos demais consumidores (DEV-06 §14, ARQ-02).
5. **Verificação técnica básica** do que você mudou (compila, testes existentes rodam). Isso não é a validação de aceitação, que é do `playbook-review`.
6. **Registrar o que de fato mudou** na REQ: arquivos, tarefas concluídas, desvios do plano, branch e commits. Atualize impactos de "previsto" para "implementado" **somente** quando a alteração existir.
7. **Commit:** apenas se houver autorização para commits nesta REQ ou no projeto (DEV-01 §8). Mensagem pela convenção do projeto.

## Saída

```markdown
## Implementação — <REQ-NNN> <título>
- Escopo executado: <tarefas concluídas> | Não executado: <tarefas e motivo>
- Arquivos alterados: <lista>
- Desvios do plano: <nenhum / lista com autorização>
- Impactos: <quais passaram de previsto para implementado>
- Verificação técnica feita: <comandos e resultado real> | Não feita: <motivo>
- Git: <branch, commits, ou "alterações locais não commitadas">
- Estado: implementado, **não validado**
- Recomendações fora do escopo: <lista>
- Próximo passo recomendado: playbook-review
```

## Limites
- Não declare validação nem publicação (COP-01 §12, T-06).
- Implementação concluída não autoriza commit, push, merge ou deploy (COP-01 §9).
- Não afirme testes que não rodou. Se um teste não pôde rodar, diga qual e por quê.
- Operações destrutivas no repositório ou em dados exigem autorização específica, independente do nível de risco (DEV-05 §10).
