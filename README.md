# Engineering Playbook

Repositório destinado à documentação dos processos, padrões, convenções e boas práticas adotadas pelo time de Engenharia de Software.

O objetivo deste repositório é centralizar o conhecimento necessário para garantir consistência na forma como requisitos são definidos, soluções são desenvolvidas, testadas e entregues.

---

# Objetivos

* Padronizar processos de trabalho.
* Facilitar o onboarding de novos integrantes.
* Reduzir ambiguidades durante desenvolvimento e testes.
* Centralizar decisões e convenções adotadas pelo time.
* Manter histórico e rastreabilidade das práticas utilizadas.
* Evoluir continuamente a forma como o time entrega software.

---

# Estrutura

```text
engineering-playbook
│
├── README.md
│
├── product                 # Guidelines e templates de requisitos
├── development             # Padrões de código e arquitetura
├── qa                      # Estratégia e diretrizes de testes
├── devops                  # Release, deploy e ambientes
├── ai                      # Uso de IA no processo de engenharia
├── adr                     # Architecture Decision Records
├── playbooks               # Processos passo a passo para pessoas
└── skills                  # Instruções operacionais para agentes de IA
    ├── product
    │   ├── requirements-analyst
    │   └── requirements-reviewer
    └── delivery
        └── sprint-readiness-reviewer
```

Ver fluxo completo em [playbooks/PIPELINE.md](playbooks/PIPELINE.md).

## Tipos de artefato

| Tipo | Diretório | Objetivo |
| --- | --- | --- |
| Guideline | `product/`, `development/`, `qa/`, … | Regras e padrões do time |
| Template | `product/`, … | Estrutura de documento |
| Skill | `skills/` | Instruções para IA executar uma tarefa |
| Playbook | `playbooks/` | Processo passo a passo executado por pessoas |

---

# Product

Documentação relacionada à definição e decomposição de requisitos.

## Conteúdo

| Documento             | Objetivo                                           |
| --------------------- | -------------------------------------------------- |
| [feature-guidelines.md](product/feature-guidelines.md) | Padrões para criação de Features                   |
| [feature-template.md](product/feature-template.md) | Template oficial de Feature                     |
| [us-guidelines.md](product/us-guidelines.md) | Regras para criação e decomposição de User Stories |
| [us-template.md](product/us-template.md)        | Template oficial de User Story                     |

---

# Development

Documentação relacionada ao desenvolvimento de software.

## Conteúdo

| Documento                  | Objetivo                               |
| -------------------------- | -------------------------------------- |
| coding-standards.md        | Convenções e padrões de código         |
| architecture-guidelines.md | Diretrizes arquiteturais               |
| pull-request-guidelines.md | Processo de revisão de código          |
| branching-strategy.md      | Estratégia de branches e versionamento |

---

# QA

Documentação relacionada à qualidade de software.

## Conteúdo

| Documento             | Objetivo                            |
| --------------------- | ----------------------------------- |
| testing-guidelines.md | Diretrizes para testes              |
| test-strategy.md      | Estratégia de validação e cobertura |

---

# DevOps

Documentação relacionada à entrega e operação.

## Conteúdo

| Documento             | Objetivo                         |
| --------------------- | -------------------------------- |
| release-process.md    | Processo de release              |
| deployment-process.md | Processo de publicação           |
| environments.md       | Ambientes e suas características |

---

# AI

Documentação relacionada ao uso de Inteligência Artificial no processo de engenharia.

## Conteúdo

| Documento                  | Objetivo                             |
| -------------------------- | ------------------------------------ |
| [analyst-onboarding.md](ai/analyst-onboarding.md) | Guia para analistas usarem IA (Cursor, Claude, ChatGPT) sem Git |
| [agent-guidelines.md](ai/agent-guidelines.md) | Diretrizes para agentes (inclui política read-only no DevOps) |
| [azure-devops-integration.md](ai/azure-devops-integration.md) | Configuração MCP e uso com Features/US |
| prompt-guidelines.md       | Padrões para construção de prompts   |
| ai-assisted-development.md | Uso de IA no desenvolvimento         |

---

# Skills

Instruções operacionais para agentes de IA, organizadas por domínio e portáveis entre IDEs (Cursor, Claude Code, Antigravity).

| Recurso | Objetivo |
| --- | --- |
| [skills/README.md](skills/README.md) | Índice, estrutura e integração por IDE |
| [requirements-analyst](skills/product/requirements-analyst/SKILL.md) | Transformar Features aprovadas em User Stories |
| [requirements-reviewer](skills/product/requirements-reviewer/SKILL.md) | Revisar User Stories antes do backlog |
| [sprint-readiness-reviewer](skills/delivery/sprint-readiness-reviewer/SKILL.md) | Validar USs antes do sprint planning |
| [us-estimator](skills/delivery/us-estimator/SKILL.md) | Pré-estimar User Stories em horas |

---

# Playbooks

Processos cerimoniais e fluxos de trabalho conduzidos por pessoas. Ver [playbooks/README.md](playbooks/README.md) e [fluxo completo](playbooks/PIPELINE.md).

| Playbook | Objetivo |
| --- | --- |
| [product-discovery.md](playbooks/product-discovery.md) | Descoberta inicial do problema |
| [feature-refinement.md](playbooks/feature-refinement.md) | Refinar e aprovar Feature antes das User Stories |
| [sprint-planning.md](playbooks/sprint-planning.md) | Planejar sprint com USs prontas |

---

# ADR (Architecture Decision Records)

Diretório destinado ao registro de decisões arquiteturais relevantes.

Cada ADR deve registrar:

* Contexto da decisão;
* Problema a ser resolvido;
* Alternativas avaliadas;
* Decisão tomada;
* Consequências da decisão.

---

# Princípios

As definições contidas neste repositório seguem os seguintes princípios:

1. Simplicidade antes de complexidade.
2. Documentar apenas o necessário.
3. Priorizar clareza e objetividade.
4. Padronizar para reduzir ambiguidades.
5. Registrar decisões para preservar contexto.
6. Evoluir continuamente os processos.
7. Automatizar sempre que fizer sentido.

---

# Contribuição

Toda alteração nos processos ou padrões definidos neste repositório deve ser realizada através de Pull Request.

Mudanças relevantes devem conter:

* Motivação da alteração;
* Impactos esperados;
* Atualização dos documentos relacionados.

---

# Histórico

Este repositório é um artefato vivo e deve evoluir conforme a maturidade dos processos e necessidades do time.
