---
name: project-scanner
description: >-
  Inicializa e sincroniza a Dev Context Platform de um produto Azure DevOps —
  scan de repos, geração de repo-profile, KB e sync-state por branch de referência.
  Use quando o usuário pedir scan init, scan sync, scan status, mapear repos,
  atualizar documentação de engenharia, ou configurar project-map.
---

# Project Scanner

## Objetivo

Operar a **Dev Context Platform (DCP)** via CLI `scan`: mapear repos, gerar perfis arquiteturais (`.engineering/`), sincronizar KB incrementalmente na branch de referência e validar staleness.

Complementa [us-implementation-planner](us-implementation-planner/SKILL.md) — esta skill **prepara** o contexto; a outra **consome** para planos de US.

## Documentos de referência

* [project-context/README.md](../../../project-context/README.md) — estrutura e CLI
* [dcp-bootstrap](../dcp-bootstrap/SKILL.md) — **instalar deps e rodar scan** (use se Python ausente)
* [azure-devops-integration.md](../../../ai/azure-devops-integration.md) — ADO somente leitura
* [agent-guidelines.md](../../../ai/agent-guidelines.md)

## CLI

**Preferir wrapper com bootstrap automático:**

```powershell
.\project-context\scripts\dcp.ps1 init --project {Projeto} [--discover-ado]
.\project-context\scripts\dcp.ps1 sync --project {Projeto} [--repo {nome}] [--branch {branch}] [--force] [--dry-run]
.\project-context\scripts\dcp.ps1 status --project {Projeto}
.\project-context\scripts\dcp.ps1 verify --project {Projeto} --branch {branch} [--repo {nome}]
```

Se Python não estiver instalado, carregar [dcp-bootstrap](../dcp-bootstrap/SKILL.md) **antes** de executar.

Requisitos: Python 3.10+ (bootstrap instala via winget no Windows), `pip install -r project-context/scripts/requirements.txt`, git no PATH.

## Responsabilidades

* Criar ou validar `project-context/projects/{projeto}/project-map.yaml`
* Marcar repos como `active`, `legacy` ou `discontinued`
* Configurar `reference_branch` por repo
* Executar scan init (full) ou sync (incremental)
* Reportar staleness e recomendar sync quando KB atrás da ref branch
* Regenerar `integration-graph.md` central
* Respeitar `default_indexing.profile` no `project-map.yaml` (default: **standard**)
* Após mudar tier de indexação → `scan sync --force` para reindexar e limpar nós obsoletos

## Regras obrigatórias

### 1. Scan/indexer nunca usa LLM

Indexação é determinística (detectors + Roslyn/tree-sitter). Não inferir código via modelo.

### 2. Repos legados

Repos `legacy` / `discontinued` **não** sincronizam automaticamente — apenas com `--force`.

### 3. Branch de referência

Documentação reflete a `reference_branch` de cada repo, não o working tree local.

### 4. Azure DevOps — somente leitura

Listar repos via API/az CLI; nunca alterar work items ou pipelines.

---

## Fluxo de execução

### Etapa 1 — Validar project-map

1. Verificar `project-context/projects/{projeto}/project-map.yaml`
2. Se ausente: `scan init --discover-ado` ou copiar [template](../../../project-context/templates/project-map.yaml)
3. Confirmar `local_path` de cada repo ativo aponta para clone git válido

### Etapa 2 — Definir escopo

| Pedido do usuário | Comando |
| --- | --- |
| Primeiro setup | `scan init --project {P}` |
| Atualizar docs | `scan sync --project {P}` |
| Ver desatualização | `scan status --project {P}` |
| Feature branch | `scan sync --branch feature/...` |
| Simular | `scan sync --dry-run` |
| Forçar full | `scan sync --force` |

### Etapa 3 — Executar scan

1. Rodar comando apropriado via Shell
2. Interpretar saída JSON por repo
3. Se `skipped: status=legacy` → informar ao usuário

### Etapa 4 — Validar artefatos

Por repo escaneado, confirmar existência de:

```text
.engineering/
├── repo-profile.yaml
├── README.engineering.md
├── sync-state.json
└── kb/manifest.json   # se stack dotnet
```

### Etapa 5 — Reportar

```markdown
# Scan — {projeto}

## Resumo

| Repo | Commit | Nodes KB | Quality | Status |
| --- | --- | --- | --- | --- |
| {nome} | {sha12} | {n} | {score}/100 | OK / skipped |

## Staleness

{output de scan status}

## Próximo passo

- [us-implementation-planner](us-implementation-planner/SKILL.md) para analisar US
- `scan sync` se stale
```

### Etapa 6 — Marcar repos legados

Orientar edição manual em `project-map.yaml`:

```yaml
- name: repo-antigo
  status: legacy
  reference_branch: develop
  description: "Descontinuado para novas features"
```

---

## Recursos

| Recurso | Quando carregar |
| --- | --- |
| [checklist.md](checklist.md) | Antes de concluir scan |
| [references/README.md](references/README.md) | Schemas e templates |
