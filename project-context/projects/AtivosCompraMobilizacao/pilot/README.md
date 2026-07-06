# Piloto — AtivosCompraMobilizacao / US-147722

Artefatos de referência da Dev Context Platform para o piloto SIMA + integração SAP.

## Conteúdo

| Arquivo | Descrição |
| --- | --- |
| [US-147722-01-plan.md](US-147722-01-plan.md) | Plano de implementação de referência |
| [manifest.json](manifest.json) | Manifest KB piloto (keywords para L2 search) |
| [kb-nodes/SIMA_AtualizacaoDiariaJob.md](kb-nodes/SIMA_AtualizacaoDiariaJob.md) | Nota KB exemplo |

## Como usar

1. Edite [../project-map.yaml](../project-map.yaml) com `local_path` dos clones git
2. Execute:

```bash
python project-context/scripts/scan.py init --project AtivosCompraMobilizacao --repo sima-backend
python project-context/scripts/scan.py verify --project AtivosCompraMobilizacao --branch main --repo sima-backend
```

3. Use a skill [us-implementation-planner](../../../skills/development/us-implementation-planner/SKILL.md) com US 147722

## US relacionada

- Draft: [product/drafts/US-147722-01.md](../../../product/drafts/US-147722-01.md)
- Feature ADO: [147722](https://dev.azure.com/aguiabranca/AtivosCompraMobilizacao/_workitems/edit/147722)
