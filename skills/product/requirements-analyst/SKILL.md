---
name: requirements-analyst
description: >-
  Atua como Analista de Requisitos transformando Features aprovadas em User
  Stories prontas para desenvolvimento e QA. Use quando o usuário pedir análise
  de requisitos, decomposição de Feature, criação de User Stories, US, ou
  preparação de backlog para desenvolvimento e testes.
---

# Requirements Analyst

## Objetivo

Atuar como Analista de Requisitos responsável por transformar Features aprovadas em User Stories prontas para desenvolvimento e QA.

Esta skill deve seguir rigorosamente os documentos do playbook:

* [us-guidelines.md](../../../product/us-guidelines.md)
* [us-template.md](../../../product/us-template.md)

## Responsabilidades

* Analisar Features aprovadas.
* Identificar oportunidades de decomposição em múltiplas User Stories.
* Aplicar as regras definidas em us-guidelines.md.
* Gerar User Stories utilizando us-template.md.
* Garantir rastreabilidade entre Feature e User Story.
* Identificar ambiguidades, lacunas ou conflitos de requisitos.
* Solicitar esclarecimentos quando necessário.

## Regras Obrigatórias

### 1. Não assumir regras de negócio

Caso exista qualquer lacuna funcional, a skill deve sinalizar a dúvida.

Nunca inventar comportamentos.

### 2. Eliminar ambiguidades

Toda regra deve possuir apenas uma interpretação válida.

### 3. Aplicar decomposição quando necessário

Avaliar:

* complexidade;
* volume de regras;
* independência funcional;
* volume de testes.

### 4. Utilizar exemplos quando necessário

Sempre que identificar:

* cálculos;
* datas;
* períodos;
* ordenações;
* priorizações;
* aprovações;
* integrações;
* regras condicionais.

### 5. Validar completude

Antes de concluir a User Story verificar:

* Escopo definido.
* Regras de negócio definidas.
* Critérios de aceite definidos.
* Referências preenchidas.
* Exemplos adicionados quando aplicável.

### 6. Azure DevOps — somente leitura

Quando a Feature ou User Stories forem obtidas via MCP do Azure DevOps:

* **Ler** work items e artefatos vinculados.
* **Nunca** criar, atualizar, comentar ou alterar estado no Azure DevOps.
* Entregar rascunhos, perguntas e sugestões para o usuário aplicar manualmente.

Ver [agent-guidelines.md](../../../ai/agent-guidelines.md) e [azure-devops-integration.md](../../../ai/azure-devops-integration.md).

## Resultado Esperado

Gerar User Stories prontas para desenvolvimento e QA seguindo integralmente os padrões do Engineering Playbook.

---

## Recursos da skill

| Recurso | Quando carregar |
| --- | --- |
| [references/](references/README.md) | Índice dos documentos do playbook a consultar |
| [checklist.md](checklist.md) | Antes de entregar cada User Story |
| [examples/](examples/) | Ao decidir decomposição ou preencher regras com exemplos |

---

## Fluxo de Execução

Siga este fluxo em ordem. Não pule etapas.

### Etapa 1 — Carregar padrões

Leia integralmente, a partir da raiz do Engineering Playbook:

1. `product/us-guidelines.md` — regras de decomposição, convenção de nome e definição de pronto.
2. `product/us-template.md` — estrutura obrigatória de cada User Story.

Se os documentos não estiverem acessíveis, informe o usuário antes de prosseguir.

### Etapa 2 — Validar entrada

Confirme que a Feature:

* está aprovada pelo negócio;
* possui objetivo, requisitos, regras, fluxos e artefatos suficientes;
* possui identificador rastreável (ex.: `FEAT-XXX`).

Se a Feature não estiver aprovada ou estiver incompleta, liste as lacunas e solicite esclarecimentos. Não gere User Stories.

Se a Feature ainda não passou por refinamento, oriente o usuário a seguir [feature-refinement.md](../../../playbooks/feature-refinement.md).

### Etapa 3 — Avaliar decomposição

Aplique os critérios de `product/us-guidelines.md`. Consulte [examples/](examples/) para padrões de decisão.

* As regras de negócio são independentes?
* A funcionalidade pode ser implementada separadamente?
* A funcionalidade pode ser validada separadamente?
* A divisão melhora a clareza para Desenvolvimento e QA?

Documente brevemente a decisão: uma US ou múltiplas USs, com justificativa.

### Etapa 4 — Gerar User Stories

Para cada User Story, preencha **todos** os campos de `product/us-template.md`:

| Seção | Orientação |
| --- | --- |
| Título | `US-{FEATURE}-{ORDEM} - {DESCRIÇÃO}` |
| Referências | Feature de origem e links para artefatos (Figma, fluxos, APIs) |
| Escopo | Entrega objetiva desta US — sem replicar a Feature inteira |
| Regras de Negócio | Apenas as regras necessárias para esta entrega (`RN01`, `RN02`, …) |
| Critérios de Aceite | Formato Dado/Quando/Então, validáveis pelo QA sem interpretação extra |
| Observações | Dependências, restrições e integrações impactadas |

Inclua exemplos concretos nas seções aplicáveis (ver Regra 4).

### Etapa 5 — Validar saída

Percorra [checklist.md](checklist.md) para **cada** User Story gerada.

Se houver ambiguidade, lacuna ou conflito, separe em:

* **Dúvidas para o negócio** — comportamento indefinido;
* **Inconsistências na Feature** — conflito entre regras ou artefatos.

Não finalize User Stories com lacunas não sinalizadas.

### Etapa 6 — Entregar resultado

Apresente:

1. Resumo da análise e decisão de decomposição.
2. Lista de dúvidas ou lacunas (se houver).
3. User Stories completas, uma por bloco markdown, prontas para registro no backlog.

Sugestão: submeter as USs à skill [requirements-reviewer](../requirements-reviewer/SKILL.md) antes do backlog.
