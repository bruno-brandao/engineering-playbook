# Relatórios de prontidão para sprint

Pasta de saída dos relatórios gerados pela skill [sprint-readiness-reviewer](../SKILL.md).

## Quando usar

Gere um relatório ao final de uma análise de:

* **Sprint inteira** — todas as USs alocadas à sprint;
* **Lista de USs** — IDs informados pelo usuário (ex.: `147776, 147777`);
* **Mix** — sprint com exclusões ou USs adicionais fora da sprint.

## Convenção de arquivos

Salve na pasta `reports/` desta skill (caminho relativo ao Engineering Playbook):

```text
reports/YYYY-MM-DD_{escopo-slug}_readiness.md
```

| Parte | Exemplo |
| --- | --- |
| Data | `2026-06-17` |
| Escopo (slug) | `sprint-93`, `us-147776-147777`, `sprint-93-ipva` |
| Sufixo fixo | `_readiness.md` |

Exemplos:

* `reports/2026-06-17_sprint-93_readiness.md`
* `reports/2026-06-17_us-147776_readiness.md`

### Projetos consumidores

Se o playbook estiver como submodule ou o time preferir relatórios no repositório de produto, use:

```text
docs/sprint-readiness/YYYY-MM-DD_{escopo-slug}_readiness.md
```

Registre o caminho escolhido no prompt ou na configuração do projeto.

## Conteúdo

Use o template em [examples/report-template.md](../examples/report-template.md).

Todo work item citado deve incluir link clicável:

```text
https://dev.azure.com/{organizacao}/{projeto}/_workitems/edit/{id}
```

Para o projeto padrão deste playbook: `aguiabranca/AtivosCompraMobilizacao`.

## Versionamento

Relatórios são artefatos de trabalho locais. **Não commitar** no Engineering Playbook salvo quando o time quiser registrar um parecer oficial — nesse caso, prefira o repositório do produto ou wiki do Azure DevOps.
