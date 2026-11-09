# AI Development Playbook

Metodologia para desenvolver software com assistentes de IA de forma previsível, rastreável e independente de fornecedor. Este repositório é a **distribuição oficial**: contém as normas, as skills que as executam e a estrutura de pastas que todo projeto novo deve seguir.

Versão atual: veja [`docs/playbook/MANIFEST.md`](docs/playbook/MANIFEST.md).

## O que vem no pacote

```text
.
├── AGENTS.md              # instruções para qualquer assistente (Codex, Cursor, Copilot, Claude...)
├── CLAUDE.md              # adaptador do Claude Code (importa AGENTS.md)
├── .claude/skills/        # cópia de Skills/, para o Claude Code descobrir as skills
├── Skills/                # as 7 skills operacionais (fonte única)
│   ├── playbook-init/     # inicialização e diagnóstico
│   ├── playbook-spec/     # interpretação, REQs e especificação
│   ├── playbook-plan/     # impactos, risco e plano
│   ├── playbook-implement/# implementação sob controle de escopo
│   ├── playbook-review/   # validação contra critérios de aceitação
│   ├── playbook-handoff/  # encerramento e retomada de sessão
│   └── playbook-audit/    # auditoria de conformidade
├── Specs/                 # SPECs, REQs, histórico funcional e handoffs do projeto
│   └── sessions/
└── docs/
    ├── playbook/          # normas (cópia local da versão adotada)
    │   ├── produto/       # PROD-01 a PROD-04
    │   ├── arquitetura/   # ARQ-01 a ARQ-04
    │   ├── desenvolvimento/ # DEV-01 a DEV-13
    │   └── operacional/   # COP-01, contrato das skills
    ├── decisoes/          # ADRs do projeto
    ├── incidentes/
    └── riscos/
```

A estrutura segue o COP-01, seção 21. As normas são a autoridade; as skills são roteiros operacionais que apontam para elas.

## Fluxo

```text
playbook-init → playbook-spec → playbook-plan → playbook-implement → playbook-review → playbook-handoff
                                                                    playbook-audit a qualquer momento
```

Cada etapa exige autorização própria. Terminar uma skill **não** inicia a próxima: o agente recomenda o próximo passo e espera.

Há duas trilhas, conforme o risco (DEV-05):

- **Trilha curta** (baixo risco evidente): `playbook-spec` → `playbook-implement`, com tudo registrado em um único `REQ-NNN.md`. É o caminho da maioria das tarefas do dia a dia.
- **Trilha completa** (risco médio ou alto, ou dúvida): as cinco etapas, com `plan.md` e `tasks.md` quando se justificam.

## Consumo de tokens

- A leitura integral das normas (cerca de 39 mil palavras) acontece **uma vez**, no `playbook-init`.
- No dia a dia, o agente carrega o `AGENTS.md` e a skill da etapa (cerca de 500 palavras cada). As skills indicam a seção exata da norma a abrir, e só quando a situação pede.

## Começar um projeto novo

1. Crie o repositório do projeto a partir deste (botão **Use this template** no GitHub, ou copie todos os arquivos, inclusive as pastas ocultas `.claude/` e o `.gitattributes`).
2. Abra o projeto no seu assistente.
3. Envie o prompt inicial oficial (DEV-12 §18.2):

> Este projeto utiliza a metodologia AI Development Playbook, disponível na pasta `docs/playbook/`.
>
> Leia integralmente todos os documentos da metodologia, incluindo as instruções de inicialização, os três pilares (Produto, Arquitetura e Desenvolvimento), seus anexos e os arquivos de referência.
>
> Após concluir a leitura, assuma a responsabilidade de aplicar a metodologia neste projeto.
>
> Execute os procedimentos de inicialização previstos no Playbook, incluindo a identificação do ambiente, a preparação das instruções permanentes compatíveis com o assistente utilizado e o diagnóstico inicial do projeto.
>
> Não modifique o código da aplicação, não instale dependências e não execute operações sensíveis sem as autorizações previstas na metodologia.
>
> Ao finalizar a inicialização, apresente um resumo das regras fundamentais, das verificações realizadas, das limitações encontradas e dos próximos passos recomendados.
>
> A partir desse momento, conduza o desenvolvimento conforme o Playbook, consultando os documentos pertinentes a cada tarefa e preservando a continuidade entre sessões.

4. Preencha a seção "Contexto específico deste projeto" no `AGENTS.md` (stack, comandos de build e teste, convenções).

## Adotar em um projeto existente

Copie `docs/playbook/` e `Skills/` para o projeto. Não sobrescreva `AGENTS.md` ou `CLAUDE.md` existentes: peça ao agente para rodar o `playbook-init`, que propõe incluir apenas o bloco do Playbook (modelos em `Skills/playbook-init/templates/`). A migração da organização existente segue o controle de mudanças; nada é reorganizado automaticamente.

## Compatibilidade com assistentes

| Assistente | Como encontra as instruções e skills |
|---|---|
| Claude Code | `CLAUDE.md` importa `AGENTS.md`; skills descobertas em `.claude/skills/` (cópia de `Skills/`) |
| Assistentes que leem `AGENTS.md` | `AGENTS.md` lista cada skill e o caminho do `SKILL.md` a seguir |
| Outros | Aponte o arquivo de instruções do assistente para `AGENTS.md` |

Os arquivos `SKILL.md` usam o formato aberto de Agent Skills (cabeçalho com `name` e `description`). Mesmo um assistente sem suporte nativo a skills consegue segui-las lendo o arquivo indicado no `AGENTS.md`.

**`.claude/skills/`** é uma cópia de `Skills/` (funciona no Windows e em downloads ZIP). A fonte continua sendo `Skills/`: ao alterar uma skill, copie a pasta de novo para `.claude/skills/`.

## Atualizar a metodologia em um projeto

Cada projeto usa a cópia local da versão que adotou. Uma versão nova publicada aqui **não** altera projetos automaticamente (DEV-12 §14 a §16). Para atualizar, compare o `MANIFEST.md` do projeto com o desta distribuição, substitua `docs/playbook/` e `Skills/` em uma branch e registre a adoção como decisão em `docs/decisoes/`.

## Manutenção desta distribuição

- Antes de publicar uma versão, rode a [bateria de conformidade](conformidade/README.md), que testa os 18 cenários do COP-01 com um agente de verdade. A pasta `conformidade/` não precisa ir para os projetos.

- Toda mudança em norma ou skill entra por pull request e atualiza a versão no `MANIFEST.md` e o [`CHANGELOG.md`](docs/playbook/CHANGELOG.md).
- A versão mais alta de um documento substitui a anterior; versões antigas ficam no histórico do Git.
- Skills não duplicam regras: quando uma norma mudar, confira se o roteiro da skill correspondente continua coerente.
