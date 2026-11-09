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
5. **Preparar adaptadores.** Proponha (ou, se autorizado, crie) o adaptador do assistente em uso a partir dos modelos em `Skills/playbook-init/templates/` (`AGENTS.md`, `CLAUDE.md`). Se o projeto já tiver um desses arquivos, proponha a inclusão apenas do bloco do Playbook. O adaptador aponta para `docs/playbook/` e registra a versão; não copia as normas (DEV-12 §6, §9).
6. **Verificar a estrutura do projeto.** Confira `Specs/`, `Skills/`, `docs/playbook/`, `docs/decisoes/`, `docs/incidentes/`, `docs/riscos/` (COP-01 §21). Em projeto existente, não reorganize: proponha.
7. **Diagnóstico inicial (DEV-08), sem modificar código.** Cubra produto, arquitetura, desenvolvimento (Git, testes, build), segurança e documentação. Para projeto novo sem código, conduza a entrevista de descoberta do PROD-01.
8. **Classificar achados (DEV-08 §13):** bloqueadores, riscos relevantes, melhorias recomendadas, oportunidades futuras.

## Saída (relatório de inicialização, DEV-12 §18.5)

```markdown
## Inicialização — <projeto>
- Versão do Playbook: <versão do MANIFEST> | Documentos: <n encontrados>/<n obrigatórios> | Ausentes: <lista ou "nenhum">
- Assistente e ambiente: <assistente>; recursos indisponíveis: <lista>
- Regras fundamentais que vou seguir: <5 a 8 linhas>
- Classificação de risco: baixo / médio / alto conforme DEV-05
- Onde ficam requisitos, decisões e handoffs: Specs/, docs/decisoes/, Specs/sessions/
- Adaptadores: <existentes | propostos | criados com autorização>
- Diagnóstico: bloqueadores / riscos / melhorias / oportunidades
- Limitações desta análise: <lista>
- Estado: inicialização concluída | não concluída (motivo)
- Próximo passo recomendado: <normalmente playbook-spec para a primeira solicitação>
```

## Limites
- Concluir esta skill **não inicia** `playbook-spec` (COP-01 §13, teste T-01). Aguarde nova solicitação do desenvolvedor.
- Não substitua a cópia local por conteúdo remoto nem atualize a versão do Playbook por iniciativa própria (DEV-12 §18.1).
- O relatório demonstra a verificação inicial; não garante cumprimento futuro.

## Sessões posteriores
Não releia tudo. Use o adaptador, o MANIFEST e o último handoff em `Specs/sessions/` para recuperar contexto (DEV-09, DEV-12 §18.6).
