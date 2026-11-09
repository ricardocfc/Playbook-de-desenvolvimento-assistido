# AI Development Playbook — cópia local

Esta pasta contém a cópia local da metodologia AI Development Playbook adotada pelo projeto. Ela é a **referência operacional** dos agentes de IA (DEV-12) e não deve ser editada para registrar informações do produto: requisitos, requisições e handoffs ficam em `Specs/`, na raiz do projeto.

A versão instalada e a lista de documentos obrigatórios estão em [MANIFEST.md](MANIFEST.md).

## Como os documentos se organizam

| Pasta | Conteúdo | Quando consultar |
|---|---|---|
| [produto/](produto/) | O que construir e como saber que está pronto | Ao descobrir, especificar, evoluir ou aceitar funcionalidades |
| [arquitetura/](arquitetura/) | Como organizar o código e registrar decisões técnicas | Ao planejar onde e como uma mudança será feita |
| [desenvolvimento/](desenvolvimento/) | Como o agente trabalha: Git, risco, escopo, sessões, histórico, ferramentas | Em toda sessão de trabalho |
| [operacional/](operacional/) | Contrato que transforma as normas em etapas executáveis pelas skills | Ao executar ou revisar qualquer skill `playbook-*` |

O contrato operacional (COP-01) é **subordinado** às normas dos três pilares. Em caso de divergência, prevalecem as normas.

## Índice

### Pilar 01 — Produto
- [PROD-01 — Descoberta e Visão do Produto](produto/PROD-01-descoberta-e-visao.md)
- [PROD-02 — Requisitos, Jornadas e Regras de Negócio](produto/PROD-02-requisitos-jornadas-e-regras.md)
- [PROD-03 — Evolução Contínua do Produto](produto/PROD-03-evolucao-continua.md)
- [PROD-04 — Critérios de Aceitação e Validação Funcional](produto/PROD-04-criterios-de-aceitacao.md)

### Pilar 02 — Arquitetura
- [ARQ-01 — Organização por Funcionalidades](arquitetura/ARQ-01-organizacao-por-funcionalidades.md)
- [ARQ-02 — Componentes Compartilhados e Reutilização de Código](arquitetura/ARQ-02-componentes-compartilhados.md)
- [ARQ-03 — Responsabilidades, Coesão e Dependências](arquitetura/ARQ-03-responsabilidades-e-dependencias.md)
- [ARQ-04 — Decisões e Evolução Arquitetural](arquitetura/ARQ-04-decisoes-arquiteturais.md)

### Pilar 03 — Desenvolvimento
- [DEV-01 — Versionamento e Controle de Código com Git](desenvolvimento/DEV-01-versionamento-git.md)
- [DEV-02 — Experimentação Controlada e Gerenciamento de Branches](desenvolvimento/DEV-02-branches-e-experimentacao.md)
- [DEV-03 — Limpeza de Código e Funcionalidades Abandonadas](desenvolvimento/DEV-03-limpeza-de-codigo.md)
- [DEV-04 — Análise de Dependências e Impactos Indiretos](desenvolvimento/DEV-04-dependencias-e-impactos.md)
- [DEV-05 — Gestão de Mudanças Baseada em Riscos](desenvolvimento/DEV-05-gestao-de-riscos.md)
- [DEV-06 — Intervenção Mínima e Controle do Escopo](desenvolvimento/DEV-06-controle-de-escopo.md)
- [DEV-07 — Gestão de Skills, Plugins, Agentes e Ferramentas Especializadas](desenvolvimento/DEV-07-recursos-especializados.md)
- [DEV-08 — Consultoria Inicial e Diagnóstico do Projeto](desenvolvimento/DEV-08-diagnostico-inicial.md)
- [DEV-09 — Consultoria Contínua e Preparação de Sessões](desenvolvimento/DEV-09-preparacao-de-sessoes.md)
- [DEV-10 — Encerramento de Sessão e Transferência de Contexto](desenvolvimento/DEV-10-encerramento-de-sessao.md)
- [DEV-11 — Histórico de Desenvolvimento e Rastreabilidade das Decisões](desenvolvimento/DEV-11-historico-e-rastreabilidade.md)
- [DEV-12 — Instruções Permanentes e Independência de Plataforma](desenvolvimento/DEV-12-instrucoes-permanentes.md)
- [DEV-13 — Orquestração de Recursos Especializados](desenvolvimento/DEV-13-orquestracao-de-recursos.md)

### Operacional
- [COP-01 — Contrato Operacional das Skills](operacional/COP-01-contrato-operacional.md)

## Fluxo resumido

```text
playbook-init ──► playbook-spec ──► playbook-plan ──► playbook-implement ──► playbook-review ──► playbook-handoff
   (DEV-08,12)     (PROD-02,04)     (DEV-04,05,06)        (DEV-01,02,06)        (PROD-04)           (DEV-10,11)

                                  playbook-audit (a qualquer momento)
```

Em baixo risco evidente, a trilha curta vai de `playbook-spec` direto para `playbook-implement`. Cada transição exige autorização própria. Concluir uma etapa não inicia a seguinte (COP-01, seções 9 e 21.6).
