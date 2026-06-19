---
name: sprint-readiness-reviewer
description: >-
  Valida se User Stories estão prontas para entrar na sprint — revisão concluída,
  Feature aprovada, critérios de aceite completos. Use antes do sprint planning,
  quando o usuário perguntar se uma US está pronta para desenvolvimento, ou para
  analisar uma sprint inteira ou lista de USs e gerar relatório consolidado em MD.
---

# Sprint Readiness Reviewer

## Objetivo

Validar se uma ou mais User Stories atendem aos critérios de prontidão para serem incluídas na sprint.

Esta skill complementa o [requirements-reviewer](../product/requirements-reviewer/SKILL.md) e o [tech-lead-reviewer](tech-lead-reviewer/SKILL.md) com foco no **go/no-go** para planejamento.

Pode operar em dois modos:

| Modo | Entrada | Saída |
| --- | --- | --- |
| **Unitário** | Uma US | Veredito Pronta / Não pronta |
| **Consolidado** | Sprint ou lista de IDs de US | Relatório markdown na pasta [reports/](reports/README.md) |

## Documentos de referência

* [us-guidelines.md](../../../product/us-guidelines.md) — definição de pronto
* [feature-guidelines.md](../../../product/feature-guidelines.md) — Feature aprovada
* [sprint-planning.md](../../../playbooks/sprint-planning.md) — cerimônia de planejamento
* [agent-guidelines.md](../../../ai/agent-guidelines.md) — somente leitura no Azure DevOps
* [azure-devops-integration.md](../../../ai/azure-devops-integration.md) — org, projeto e MCP

## Responsabilidades

* Verificar prontidão da US para desenvolvimento e QA.
* Confirmar Feature de origem aprovada (quando dados disponíveis).
* Considerar parecer prévio do requirements-reviewer (quando fornecido).
* Emitir veredito **Pronta** ou **Não pronta** com bloqueios explícitos.
* **No modo consolidado:** expandir contexto por Feature, cruzar USs em sprints diferentes e gerar relatório final persistido em arquivo.

## Regras Obrigatórias

### 1. Não inventar aprovações

Se o status da Feature não for confirmado, registrar como pendência — não assumir aprovação.

### 2. Bloquear itens com lacunas

US com RN sem CA, Feature não aprovada ou achados bloqueantes do reviewer → **Não pronta**.

### 3. Somente leitura no Azure DevOps

Ler work items via MCP ou CLI; nunca alterar sprint, estado ou campos.

### 4. Não substituir estimativa humana

Esta skill valida **prontidão de requisitos**, não esforço ou capacidade do time.

### 5. Considerar contexto completo da Feature

USs da mesma Feature podem estar em sprints distintas. Ao analisar sprint ou lista de USs:

* Resolver a Feature pai de cada US do escopo.
* Buscar **todas** as USs filhas de cada Feature (independente da sprint).
* Usar USs fora do escopo como **contexto** — decomposição, dependências, lacunas de cobertura.
* Não emitir veredito de prontidão para USs de contexto; apenas referenciá-las no relatório.

### 6. Persistir relatório consolidado

No modo consolidado, **sempre** gravar o arquivo `.md` na pasta de relatórios (ver [Etapa 6](#etapa-6--gerar-relatório-consolidado)). Informar ao usuário o caminho completo do arquivo gerado.

## Resultado Esperado

* **Modo unitário:** veredito por US com bloqueios e recomendação para sprint planning.
* **Modo consolidado:** relatório markdown com links dos work items, resumo executivo, detalhamento por US, contexto por Feature e achados transversais.

---

## Recursos

| Recurso | Uso |
| --- | --- |
| [checklist.md](checklist.md) | Validação item a item |
| [examples/report-template.md](examples/report-template.md) | Estrutura do relatório consolidado |
| [reports/](reports/README.md) | Pasta de saída dos relatórios |
| [references/](references/README.md) | Links do playbook |

---

## Fluxo de Execução

### Etapa 1 — Carregar critérios

Leia [checklist.md](checklist.md) e `product/us-guidelines.md` (seção *Definição de Pronto*).

### Etapa 2 — Coletar entrada e definir escopo

Identifique o **modo** e monte o conjunto **escopo** (USs a avaliar com veredito):

| Entrada do usuário | Como resolver o escopo |
| --- | --- |
| Nome ou path da sprint (ex.: `Sprint 93`) | Listar USs alocadas à sprint no Azure DevOps |
| Lista de IDs (ex.: `147776, 147777`) | Buscar cada work item |
| US única | Modo unitário — escopo = 1 US |
| Sprint + IDs extras | União de ambos (sem duplicar) |

Registre também:

* Feature de origem (quando informada);
* Pareceres do requirements-reviewer e tech-lead-reviewer (se existirem);
* Caminho de saída do relatório (padrão: [reports/](reports/README.md)).

### Etapa 3 — Expandir contexto por Feature

Para **cada US do escopo**:

1. Obter Feature pai (`System.Parent` ou link hierárquico).
2. Ler a Feature (estado, RGs, escopo).
3. Listar **todas** as USs filhas da Feature (query por parent ou relações).

Classifique:

| Conjunto | Definição | Uso na análise |
| --- | --- | --- |
| **Escopo** | USs solicitadas pelo usuário | Veredito Pronta / Não pronta |
| **Contexto** | Outras USs da mesma Feature | Decomposição, dependências, cobertura |
| **Dependências externas** | Features ou USs referenciadas no texto | Riscos e bloqueios |

Montar mapa Feature → { USs escopo, USs contexto, sprint de cada US, estado }.

**Links dos work items** — use sempre URL completa:

```text
https://dev.azure.com/{organizacao}/{projeto}/_workitems/edit/{id}
```

Valores padrão deste playbook: `aguiabranca`, `AtivosCompraMobilizacao`.

### Etapa 4 — Validar prontidão

Percorra o [checklist.md](checklist.md) para **cada US do escopo**.

No modo consolidado, aplique também [requirements-reviewer](../../product/requirements-reviewer/SKILL.md) e [tech-lead-reviewer](tech-lead-reviewer/SKILL.md) de forma resumida quando não houver parecer prévio — registre achados no relatório.

Para USs de **contexto**, avalie apenas:

* Cobertura de decomposição da Feature;
* Dependências com USs do escopo;
* Inconsistências Feature ↔ US (estado, escopo, RGs).

### Etapa 5 — Emitir veredito (modo unitário)

```markdown
# Prontidão para Sprint — [{ID}]({URL})

## Veredito

[Pronta | Não pronta]

## Bloqueios

- [lista ou "Nenhum"]

## Contexto da Feature

- Feature: [{ID}]({URL}) — {estado}
- Outras USs da Feature: {lista com links e sprint, ou "Nenhuma"}

## Recomendação

[Incluir na sprint | Retornar ao analista | Aguardar revisão]
```

| Veredito | Condição |
| --- | --- |
| Pronta | Todos os itens obrigatórios do checklist atendidos |
| Não pronta | Qualquer bloqueio identificado |

### Etapa 6 — Gerar relatório consolidado

Quando o escopo tiver **duas ou mais USs** ou o usuário pedir análise de sprint/lista, gere o arquivo markdown.

1. Copie a estrutura de [examples/report-template.md](examples/report-template.md).
2. Preencha todas as seções — não omita *Contexto por Feature* nem *Achados transversais*.
3. Inclua link em **todo** ID de work item (Feature, US escopo, US contexto).
4. Salve em:

```text
skills/delivery/sprint-readiness-reviewer/reports/YYYY-MM-DD_{escopo-slug}_readiness.md
```

`{escopo-slug}`: minúsculas, hífens, sem acentos (ex.: `sprint-93`, `us-147776-147777`).

5. Informe ao usuário o caminho do arquivo e um resumo executivo na resposta do chat.

**Nome do escopo no título:** use sprint (`Sprint 93`) ou lista (`USs 147776, 147777`).

### Etapa 7 — Handoff

* **Pronta** → incluir no [sprint-planning](../../../playbooks/sprint-planning.md)
* **Não pronta** → [requirements-analyst](../../product/requirements-analyst/SKILL.md) ou [requirements-reviewer](../../product/requirements-reviewer/SKILL.md)
* **Relatório consolidado** → compartilhar com facilitador do sprint planning antes da cerimônia
