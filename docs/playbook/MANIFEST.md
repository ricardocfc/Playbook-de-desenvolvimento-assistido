# MANIFEST — AI Development Playbook

**Versão da distribuição:** 1.1.0  
**Status da distribuição:** Aprovada. Todos os documentos listados estão aprovados.  
**Fonte oficial:** repositório `ricardocfc/Playbook-de-desenvolvimento-assistido` no GitHub.  

Este arquivo identifica a versão instalada e os documentos **obrigatórios** desta distribuição, conforme DEV-12 (seções 3, 18.3 e 20). A ausência de qualquer documento listado impede declarar a inicialização concluída.

Uma nova versão publicada no repositório oficial **não altera automaticamente** a cópia local de um projeto.

## Documentos obrigatórios

| ID | Título | Versão | Status | Caminho |
|---|---|---|---|---|
| PROD-01 | Descoberta e Visão do Produto | 1.0 | Aprovado | `produto/PROD-01-descoberta-e-visao.md` |
| PROD-02 | Requisitos, Jornadas e Regras de Negócio | 1.1 | Aprovado | `produto/PROD-02-requisitos-jornadas-e-regras.md` |
| PROD-03 | Evolução Contínua do Produto | 1.1 | Aprovado | `produto/PROD-03-evolucao-continua.md` |
| PROD-04 | Critérios de Aceitação e Validação Funcional | 1.0 | Aprovado | `produto/PROD-04-criterios-de-aceitacao.md` |
| ARQ-01 | Organização por Funcionalidades | 1.0 | Aprovado | `arquitetura/ARQ-01-organizacao-por-funcionalidades.md` |
| ARQ-02 | Componentes Compartilhados e Reutilização de Código | 1.1 | Aprovado | `arquitetura/ARQ-02-componentes-compartilhados.md` |
| ARQ-03 | Responsabilidades, Coesão e Dependências | 1.0 | Aprovado | `arquitetura/ARQ-03-responsabilidades-e-dependencias.md` |
| ARQ-04 | Decisões e Evolução Arquitetural | 1.0 | Aprovado | `arquitetura/ARQ-04-decisoes-arquiteturais.md` |
| DEV-01 | Versionamento e Controle de Código com Git | 1.0 | Aprovado | `desenvolvimento/DEV-01-versionamento-git.md` |
| DEV-02 | Experimentação Controlada e Gerenciamento de Branches | 1.0 | Aprovado | `desenvolvimento/DEV-02-branches-e-experimentacao.md` |
| DEV-03 | Limpeza de Código e Funcionalidades Abandonadas | 1.0 | Aprovado | `desenvolvimento/DEV-03-limpeza-de-codigo.md` |
| DEV-04 | Análise de Dependências e Impactos Indiretos | 1.1 | Aprovado | `desenvolvimento/DEV-04-dependencias-e-impactos.md` |
| DEV-05 | Gestão de Mudanças Baseada em Riscos | 1.1 | Aprovado | `desenvolvimento/DEV-05-gestao-de-riscos.md` |
| DEV-06 | Intervenção Mínima e Controle do Escopo | 1.0 | Aprovado | `desenvolvimento/DEV-06-controle-de-escopo.md` |
| DEV-07 | Gestão de Skills, Plugins, Agentes e Ferramentas Especializadas | 1.1 | Aprovado | `desenvolvimento/DEV-07-recursos-especializados.md` |
| DEV-08 | Consultoria Inicial e Diagnóstico do Projeto | 1.0 | Aprovado | `desenvolvimento/DEV-08-diagnostico-inicial.md` |
| DEV-09 | Consultoria Contínua e Preparação de Sessões | 1.1 | Aprovado | `desenvolvimento/DEV-09-preparacao-de-sessoes.md` |
| DEV-10 | Encerramento de Sessão e Transferência de Contexto | 1.1 | Aprovado | `desenvolvimento/DEV-10-encerramento-de-sessao.md` |
| DEV-11 | Histórico de Desenvolvimento e Rastreabilidade das Decisões | 1.1 | Aprovado | `desenvolvimento/DEV-11-historico-e-rastreabilidade.md` |
| DEV-12 | Instruções Permanentes e Independência de Plataforma | 1.2 | Aprovado | `desenvolvimento/DEV-12-instrucoes-permanentes.md` |
| DEV-13 | Orquestração de Recursos Especializados | 1.0 | Aprovado | `desenvolvimento/DEV-13-orquestracao-de-recursos.md` |
| COP-01 | Contrato Operacional das Skills | 1.1 | Aprovado | `operacional/COP-01-contrato-operacional.md` |

Os caminhos são relativos a `docs/playbook/`.

## Convenções aprovadas complementares

- A estrutura de pastas dos projetos segue o COP-01, seção 21: `Specs/` para SPECs, REQs, histórico funcional e handoffs; `.claude/skills/` para as skills `playbook-*` (fonte única); `docs/playbook/` para esta cópia normativa.
- Decisões arquiteturais, incidentes e riscos do projeto ficam em `docs/decisoes/`, `docs/incidentes/` e `docs/riscos/`.

## Regra de versões

Quando houver mais de uma versão de um documento, vale a mais recente (por exemplo, 1.1 prevalece sobre 1.0). Versões anteriores não fazem parte da distribuição e permanecem consultáveis no histórico do repositório oficial.
