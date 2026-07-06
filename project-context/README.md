# Dev Context Platform — project-context

Camada de contexto de projeto do Engineering Playbook: scan de repos, base de conhecimento (KB) e mapas cross-repo.

## Estrutura

```text
project-context/
├── schemas/          # JSON Schema dos artefatos
├── templates/        # Templates para project-map, repo-profile, KB
├── scripts/          # CLI `scan` (Python)
│   ├── scan.py
│   ├── detectors/
│   └── indexers/
└── projects/         # Mapas por produto Azure DevOps
    └── {projeto}/
        ├── project-map.yaml
        ├── scan-state.json
        └── integration-graph.md
```

## CLI

**Recomendado:** use o wrapper `dcp.ps1` / `dcp.sh` — faz bootstrap automático se Python/venv ausentes.

```powershell
# Windows — a partir da raiz do engineering-playbook
.\project-context\scripts\dcp.ps1 status --project AtivosCompraMobilizacao
.\project-context\scripts\dcp.ps1 init --project AtivosCompraMobilizacao
.\project-context\scripts\dcp.ps1 verify --project AtivosCompraMobilizacao --repo sima-backend --branch main
.\project-context\scripts\dcp.ps1 vault-link --project AtivosCompraMobilizacao
```

```bash
# macOS / Linux
./project-context/scripts/dcp.sh sync --project AtivosCompraMobilizacao
```

Setup manual (primeira vez ou CI): [bootstrap.ps1](scripts/bootstrap.ps1) / [bootstrap.sh](scripts/bootstrap.sh).

Skill de setup para agentes: [dcp-bootstrap](../../skills/development/dcp-bootstrap/SKILL.md).

Requisitos: Python 3.10+ (instalado pelo bootstrap via winget no Windows), git no PATH. Opcional: `az` CLI, .NET 8 SDK (Roslyn).

### Vault Obsidian

Após `sync`, monte um vault local com symlinks para repos que já têm KB indexada (lê `scan-state.json` + `.engineering/kb/`):

```powershell
.\project-context\scripts\dcp.ps1 vault-link --project AtivosCompraMobilizacao
# Abrir no Obsidian: project-context/projects/AtivosCompraMobilizacao/vault/
```

Opções: `--dry-run`, `--force` (recriar links), `--copy` (sem symlinks — útil no Windows sem Modo Desenvolvedor), `--output {pasta}`.

## Indexação KB (tiers)

Perfil configurável em `project-map.yaml` via `default_indexing.profile` (default: **standard**).

| Perfil | O que indexa |
| --- | --- |
| `minimal` | Controllers, Repositories, Handlers, Jobs, Clients |
| `standard` | minimal + Services, Validators, Mappers, entidades em `Domain/`/`Entities/`/`Models/` |
| `full` | standard + demais classes C# |

Exclusões automáticas: `Migrations`, `*Dto.cs`, `*Request.cs`, `*Options.cs`, etc.

Após mudar o perfil, rode `dcp sync --force` para reindexar e limpar nós obsoletos.

```yaml
default_indexing:
  profile: standard
repos:
  - name: service-mobilizacaofrota
    indexing:
      profile: standard  # override opcional por repo
```

## Artefatos por repositório de produto

Cada repo de produto recebe `.engineering/` (versionado com o código):

```text
.engineering/
├── repo-profile.yaml
├── README.engineering.md
├── sync-state.json
└── kb/
    ├── manifest.json
    └── nodes/
```

## Skills relacionadas

- [project-scanner](../skills/development/project-scanner/SKILL.md)
- [us-implementation-planner](../skills/development/us-implementation-planner/SKILL.md)
