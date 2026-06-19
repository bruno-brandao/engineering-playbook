# Playbooks

Processos passo a passo executados por **pessoas** — cerimônias, rituais e fluxos de trabalho do time.

---

## Diferença entre artefatos

| Artefato | Audiência | Conteúdo típico |
| --- | --- | --- |
| **Guideline** (`product/`, `qa/`, …) | Time inteiro | Regras, padrões, convenções |
| **Template** (`product/`, …) | Quem produz o documento | Estrutura fixa de um artefato |
| **Skill** (`skills/`) | Agente de IA | Instruções operacionais para executar uma tarefa |
| **Playbook** (`playbooks/`) | Facilitadores e participantes | Sequência de atividades, papéis, entradas e saídas |

Um playbook pode **referenciar** guidelines, templates e skills, mas descreve *como conduzir* o processo — não substitui as regras nem as instruções para IA.

---

## Playbooks

| Playbook | Status | Objetivo |
| --- | --- | --- |
| [feature-refinement.md](feature-refinement.md) | Disponível | Refinar Feature com negócio antes da decomposição em USs |
| [product-discovery.md](product-discovery.md) | Disponível | Conduzir descoberta e entendimento do problema |
| [sprint-planning.md](sprint-planning.md) | Disponível | Planejar sprint com base em USs prontas |
| [PIPELINE.md](PIPELINE.md) | Disponível | Visão end-to-end do fluxo de requisitos |
| release-process.md | Planejado | Conduzir release (complementa `devops/release-process.md`) |
| incident-management.md | Planejado | Resposta e comunicação em incidentes |

Contribuições devem seguir o padrão: objetivo, pré-requisitos, papéis, passos, entradas/saídas e critérios de conclusão.
