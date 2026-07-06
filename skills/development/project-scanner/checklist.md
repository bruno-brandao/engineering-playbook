# Checklist — Project Scanner

## Pré-scan

- [ ] `project-map.yaml` existe e lista repos corretos
- [ ] `local_path` ou clone git acessível para repos `active`
- [ ] `reference_branch` definida por repo
- [ ] Repos legados marcados com `status: legacy` ou `discontinued`

## Execução

- [ ] Comando correto (init / sync / status / verify)
- [ ] `--dry-run` usado quando usuário pediu simulação
- [ ] `--force` apenas quando explicitamente solicitado

## Pós-scan

- [ ] `.engineering/repo-profile.yaml` gerado por repo ativo
- [ ] `sync-state.json` com `indexed_commit_sha` preenchido
- [ ] `scan-state.json` central atualizado
- [ ] `integration-graph.md` regenerado
- [ ] Staleness reportado ao usuário

## Bloqueios

Reportar se:

* Repo ativo sem caminho local configurado
* Branch de referência inexistente no remoto
* Scan falhou por ausência de git/dotnet (Roslyn opcional)
