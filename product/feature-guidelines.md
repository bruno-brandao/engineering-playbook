# Feature Guidelines

Padrão para criação e manutenção de Features no Azure DevOps.

---

## Objetivo

Definir o conteúdo mínimo e as regras para que uma Feature seja compreendida pelo negócio, analisada pelo time e decomposta em User Stories.

---

## Conceitos

### Feature

Artefato funcional oficial, aprovado pelo negócio, que descreve **o que** deve ser entregue e **por quê**.

### Relação com User Story

| Feature | User Story |
| --- | --- |
| Visão de negócio e regras gerais | Entrega específica para desenvolvimento e QA |
| Regras Gerais (`RG01`, `RG02`, …) | Regras de Negócio (`RN01`, `RN02`, …) |
| Aprovada pelo negócio | Criada após aprovação da Feature |

As RNs da User Story devem derivar das RGs da Feature — não inventar regras na US que não existam na Feature.

---

## Princípios

* Toda Feature deve possuir identificador rastreável no Azure DevOps (ex.: `#146136`).
* Uma Feature só pode ser decomposta em User Stories após **aprovação formal** do negócio.
* Alterações relevantes após aprovação exigem nova rodada de refinamento (ver [feature-refinement.md](../playbooks/feature-refinement.md)).
* A Feature deve ser compreensível sem depender de conhecimento tácito do time.
* Protótipos, fluxos e documentos complementares devem ser referenciados por link ou imagem na descrição.
* Regras devem possuir apenas uma interpretação válida.

---

## Conteúdo obrigatório

Utilize o [feature-template.md](feature-template.md). A Feature deve conter:

| Seção | Conteúdo |
| --- | --- |
| Contexto | Situação atual e motivação da mudança |
| Objetivo | Resultado esperado para o negócio ou usuário |
| Escopo | Telas, módulos e campos impactados |
| Regras Gerais | Comportamentos e validações (`RG01`, `RG02`, …) |
| Aprovação | Registro de aprovação do negócio |

Opcional mas recomendado:

* Quem pode fazer (perfil/permissão);
* Protótipo ou imagem da tela;
* Integrações impactadas;
* Restrições conhecidas.

---

## Estados no Azure DevOps

O workflow pode variar por projeto. Estados típicos:

| Estado | Significado |
| --- | --- |
| Em elaboração / validação | Feature em construção — **não decompor em USs** |
| Feature Aprovada | Negócio aprovou — **pode decompor em USs** |
| Em andamento | Entrega em execução via User Stories |

Somente Features no estado **aprovado** devem ser entrada para [requirements-analyst](../skills/product/requirements-analyst/SKILL.md).

---

## Decomposição em User Stories

A decomposição segue os critérios de [us-guidelines.md](us-guidelines.md):

* Poucas regras e baixa complexidade → uma US;
* Fluxos independentes, integrações ou alto volume de testes → múltiplas USs.

O analista documenta a decisão de decomposição ao criar as USs.

---

## Responsabilidades

| Papel | Responsabilidade |
| --- | --- |
| Analista | Escrever a Feature, conduzir refinamento, obter aprovação |
| Negócio | Aprovar a Feature e validar a entrega final |
| Desenvolvimento | Sinalizar riscos técnicos durante o refinamento |
| QA | Antecipar cenários de teste durante o refinamento |

---

## Integração com IA

* Leitura de Features no Azure DevOps: [azure-devops-integration.md](../ai/azure-devops-integration.md)
* Decomposição assistida: skill [requirements-analyst](../skills/product/requirements-analyst/SKILL.md)
* Política somente leitura no DevOps: [agent-guidelines.md](../ai/agent-guidelines.md)
