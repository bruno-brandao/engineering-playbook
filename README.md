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
├── product
│   ├── feature-guidelines.md
│   ├── [us-guidelines.md](product/us-guidelines.md)
│   └── [us-template.md](product/us-template.md)
│
├── development
│   ├── coding-standards.md
│   ├── architecture-guidelines.md
│   ├── pull-request-guidelines.md
│   └── branching-strategy.md
│
├── qa
│   ├── testing-guidelines.md
│   └── test-strategy.md
│
├── devops
│   ├── release-process.md
│   ├── deployment-process.md
│   └── environments.md
│
├── ai
│   ├── prompt-guidelines.md
│   ├── ai-assisted-development.md
│   └── agent-guidelines.md
│
└── adr
    └── README.md
```

---

# Product

Documentação relacionada à definição e decomposição de requisitos.

## Conteúdo

| Documento             | Objetivo                                           |
| --------------------- | -------------------------------------------------- |
| feature-guidelines.md | Padrões para criação de Features                   |
| [us-guidelines.md](product/us-guidelines.md) | Regras para criação e decomposição de User Stories |
| us-template.md        | Template oficial de User Story                     |

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
| prompt-guidelines.md       | Padrões para construção de prompts   |
| ai-assisted-development.md | Uso de IA no desenvolvimento         |
| agent-guidelines.md        | Diretrizes para agentes e automações |

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
