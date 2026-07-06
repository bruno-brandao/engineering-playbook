---
name: us-implementation-planner
description: >-
  Gera plano de implementação executável a partir de uma User Story — valida branch
  e alinhamento da KB, mapeia RNs para tarefas técnicas, antecipa riscos e impactos.
  Use quando o dev pedir plano de implementação, como implementar US, tarefas técnicas,
  ou análise de impacto antes de codar.
---

# US Implementation Planner

## Objetivo

Entregar ao desenvolvedor **tudo que precisa para executar a US**: plano por fases, tarefas técnicas, arquivos/nós KB prováveis, riscos e perguntas abertas — com consumo token-efficiente da KB (L0–L3) e fallback para código (L5).

Esta skill opera **após** sprint planning. Complementa [tech-lead-reviewer](../../delivery/tech-lead-reviewer/SKILL.md) (revisão prévia) com **plano de execução** grounded no código.

## Documentos de referência

* [us-guidelines.md](../../../product/us-guidelines.md)
* [us-template.md](../../../product/us-template.md)
* [project-context/README.md](../../../project-context/README.md)
* [agent-guidelines.md](../../../ai/agent-guidelines.md)
* [azure-devops-integration.md](../../../ai/azure-devops-integration.md)

## Responsabilidades

* **Etapa 0:** perguntar branch e validar KB (`scan verify`)
* Ler US (Azure DevOps MCP ou markdown fornecido)
* Carregar L0 `project-map.yaml` → L1 `repo-profile` → L2 `manifest` → L3 notas KB (máx. 8)
* Mapear RN → CA → tarefas técnicas
* Antecipar impactos via `integration-graph.md`
* Sinalizar lacunas, riscos e premissas
* Nunca inventar regras de negócio

---

## Etapa 0 obrigatória — Branch e validação (NÃO PULAR)

### 1. Perguntar a branch

**Antes de ler a US ou KB**, confirmar branch de implementação:

| Situação | Ação |
| --- | --- |
| Branch não informada | Perguntar: *"Em qual branch você vai implementar esta US?"* |
| Git detectável | Sugerir `git branch --show-current`, **confirmar** com dev |
| Multi-repo | Branch por repo ou mesma branch para todos |
| Branch no prompt | Confirmar brevemente |

### 2. Executar verify

Por repo candidato:

```bash
python project-context/scripts/scan.py verify --project {Projeto} --branch {branch} --repo {repo}
```

### 3. Interpretar vereditos

| Status | Ação |
| --- | --- |
| **aligned** | Prosseguir |
| **ref_stale** | **Bloquear** — pedir `scan sync` ou ressalva explícita |
| **branch_delta** | Alertar arquivos; oferecer `scan sync --branch` |
| **doc_ahead** | Alertar KB descreve código mais novo; recomendar merge/rebase |
| **divergent** | **Bloquear** — KB ahead + branch unique; L5 nos arquivos conflitantes |
| **branch_not_found** | Pedir correção |
| **not_indexed** | Pedir `scan init` ou `scan sync` |

### 4. Relatório de validação (sempre primeiro na saída)

Usar [examples/validation-report.md](examples/validation-report.md).

**Gate:** `ref_stale` ou `divergent` em repo crítico → **não gerar plano** até sync, merge/rebase ou confirmação *"prosseguir com ressalva"*.

---

## Fluxo de execução (após Etapa 0)

### Etapa 1 — Carregar US

* ID Azure DevOps ou path markdown (ex.: `product/drafts/US-147722-01.md`)
* Feature pai quando disponível
* Extrair: escopo, RNs, CAs, artefatos, observações

### Etapa 2 — L0 project-map

`project-context/projects/{projeto}/project-map.yaml`

Identificar repos `active` vs `legacy`. Alertar se US tocar repo legado.

### Etapa 3 — L1 repo-profiles

`.engineering/repo-profile.yaml` dos repos candidatos.

Keywords da US: entidades, rotinas, views, integrações (ex.: `Atualização Diária`, `DataDesativacao`, `VWImobilizadosSapGeralSIMA`).

Se `indexer_available: false` → declarar: *"Plano baseado em perfil + código (L5)"*.

### Etapa 4 — L2/L3 KB

1. Buscar `kb/manifest.json` por keywords (máx. 8 nós)
2. Expandir WikiLinks 1–2 hops
3. Citar origem: `[KB @ commit sha — branch]` vs `[Código @ branch]`

### Etapa 5 — integration-graph

`project-context/projects/{projeto}/integration-graph.md` — dependências cross-repo e externas.

### Etapa 6 — Gerar plano

Usar [examples/implementation-plan.md](examples/implementation-plan.md).

### Etapa 7 — Handoff

Plano pronto para execução. Sugerir `scan sync --branch` após implementação se KB ficou stale.

---

## Regras obrigatórias

1. **Etapa 0 sempre** — branch + verify antes da US
2. **Máximo 8 notas KB** por execução
3. **Não inventar RNs** — lacunas → premissas ou perguntas bloqueantes
4. **Azure DevOps somente leitura**
5. **Divergente/doc_ahead** — KB não é fonte primária para arquivos em conflito
6. **Marcar origem** de cada inferência técnica

---

## Recursos

| Recurso | Quando carregar |
| --- | --- |
| [checklist.md](checklist.md) | Antes de entregar plano |
| [examples/validation-report.md](examples/validation-report.md) | Etapa 0 |
| [examples/implementation-plan.md](examples/implementation-plan.md) | Saída final |
| [references/README.md](references/README.md) | Camadas L0–L5 |
