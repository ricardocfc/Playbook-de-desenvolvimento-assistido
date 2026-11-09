---
name: playbook-init
description: Inicializa o AI Development Playbook em um projeto. Use na primeira sessão de um projeto novo ou incorporado, quando um agente novo assumir o projeto, ou quando o desenvolvedor pedir para "inicializar", "instalar" ou "diagnosticar" o projeto pelo Playbook. Lê a metodologia local, prepara adaptadores e faz o diagnóstico inicial sem alterar código.
---

# playbook-init — Inicialização e diagnóstico

Esta skill executa o COP-01 §13. As normas são a autoridade; este arquivo é um roteiro operacional. Em caso de divergência, prevalece o documento normativo, e a divergência deve ser comunicada.

## Fontes normativas
Esta é a única skill que lê as normas por inteiro, e só na primeira inicialização (DEV-12 §18.3). Nas sessões seguintes, as demais skills consultam apenas as seções necessárias.

- `docs/playbook/desenvolvimento/DEV-12-instrucoes-permanentes.md` (§18: inicialização; §5, §6, §9: adaptadores)
- `docs/playbook/desenvolvimento/DEV-08-diagnostico-inicial.md`
- `docs/playbook/operacional/COP-01-contrato-operacional.md`
- `docs/playbook/MANIFEST.md`

## Autorização
- Ler, inspecionar e diagnosticar: permitido.
- Criar ou alterar `AGENTS.md`, `CLAUDE.md` ou equivalente: **somente com autorização**. Sem ela, apresente o conteúdo proposto.
- Alterar código da aplicação, instalar dependências, commit, push: **proibido** nesta skill.

## Procedimento

1. **Verificar a instalação.** Abra `docs/playbook/MANIFEST.md`, identifique a versão e confira se cada documento obrigatório existe no caminho indicado.
2. **Leitura integral (primeira inicialização).** Leia por completo todos os documentos listados no MANIFEST. Se algum estiver ausente ou ilegível, registre a limitação e **não declare a inicialização concluída** (DEV-12 §18.3).
3. **Identificar o ambiente.** Qual assistente está em uso, quais recursos existem (terminal, Git, testes, acesso à rede, skills, subagentes) e quais não existem. Não presuma recursos de outra plataforma (COP-01 §18).
4. **Examinar instruções existentes.** Procure `AGENTS.md`, `CLAUDE.md` e equivalentes. Preserve conteúdo válido; não sobrescreva.
5. **Preparar adaptadores.** Proponha (ou, se autorizado, crie) o adaptador do assistente em uso a partir dos modelos em `.claude/skills/playbook-init/templates/` (`AGENTS.md`, `CLAUDE.md`). Se o projeto já tiver um desses arquivos, proponha a inclusão apenas do bloco do Playbook. O adaptador aponta para `docs/playbook/` e registra a versão; não copia as normas (DEV-12 §6, §9).
6. **Verificar a estrutura do projeto.** Confira `Specs/`, `.claude/skills/`, `docs/playbook/`, `docs/decisoes/`, `docs/incidentes/`, `docs/riscos/` (COP-01 §21). Em projeto existente, não reorganize: proponha.
7. **Diagnóstico inicial (DEV-08), sem modificar código.** Cubra produto, arquitetura, desenvolvimento (Git, testes, build), segurança e documentação. Para projeto novo sem código, conduza a entrevista de descoberta do PROD-01.
   - **Visão do produto no `README.md` da raiz.** Consolide a visão (PROD-01 §6) no `README.md` usando `templates/README.md`, com o estado "Rascunho" até o desenvolvedor aprovar. Se o `README.md` for o da distribuição do Playbook (título "AI Development Playbook"), substitua-o. Se for um README próprio do projeto, proponha a inclusão das seções que faltam sem apagar o que existe. Não crie `docs/produto/` para a visão: o `README.md` é o lugar único do contexto do produto.
8. **Classificar achados (DEV-08 §13):** bloqueadores, riscos relevantes, melhorias recomendadas, oportunidades futuras.

## Saída (relatório de inicialização, DEV-12 §18.5)

**Registro.** O bloco abaixo é o conteúdo mínimo que vai para os arquivos do projeto (REQ, sessão, relatório). Nele, identificadores e referências às normas são bem-vindos. **Não cole este bloco na conversa.**

```markdown
## Inicialização — <projeto>
- Versão do Playbook: <versão do MANIFEST> | Documentos: <n encontrados>/<n obrigatórios> | Ausentes: <lista ou "nenhum">
- Assistente e ambiente: <assistente>; recursos indisponíveis: <lista>
- Regras fundamentais que vou seguir: <5 a 8 linhas>
- Classificação de risco: baixo / médio / alto conforme DEV-05
- Onde ficam visão do produto, requisitos, decisões e handoffs: README.md, Specs/, docs/decisoes/, Specs/sessions/
- Adaptadores: <existentes | propostos | criados com autorização>
- Diagnóstico: bloqueadores / riscos / melhorias / oportunidades
- Limitações desta análise: <lista>
- Estado: inicialização concluída | não concluída (motivo)
- Próximo passo recomendado: <normalmente playbook-spec para a primeira solicitação>
```

**Resposta ao desenvolvedor.** Siga "Como falar com o desenvolvedor" no `AGENTS.md`: palavras comuns, sem códigos de documentos nem nomes de skills. Diga o que foi feito, o que você precisa dele e o que dá para fazer em seguida. Exemplo: "Já li as regras de trabalho e conferi o projeto. Agora quero entender a sua ideia: me conte ..."

## Limites
- Concluir esta skill **não inicia** `playbook-spec` (COP-01 §13, teste T-01). Aguarde nova solicitação do desenvolvedor.
- Não substitua a cópia local por conteúdo remoto nem atualize a versão do Playbook por iniciativa própria (DEV-12 §18.1).
- O relatório demonstra a verificação inicial; não garante cumprimento futuro.

Grave o relatório como primeiro registro de sessão em `Specs/sessions/AAAA-MM-DD-inicializacao.md`, se houver autorização para criar registros.

## Sessões posteriores
Não releia tudo. Use o adaptador, o MANIFEST e o último handoff em `Specs/sessions/` para recuperar contexto (DEV-09, DEV-12 §18.6).
