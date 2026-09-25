---
name: release-reviewer
description: >-
  Consolida evidências técnicas e operacionais para avaliar prontidão de uma
  release. Use antes de Go/No-Go, publicação ou promoção de ambiente. Não executa
  deploy, não altera ambientes e não atualiza Azure DevOps.
---

# Release Reviewer

## Objetivo

Apoiar a decisão humana de Go/No-Go com um parecer rastreável sobre escopo, qualidade, dependências, rollout, rollback e operação.

## Entradas

* Escopo da release e itens incluídos;
* PRs/commits e aprovações;
* Resultados de CI, testes e [pre-pr-reviewer](../../development/pre-pr-reviewer/SKILL.md);
* Pareceres de [code-reviewer](../../development/code-reviewer/SKILL.md) ou Devin Review;
* Plano de deploy/rollback, migrations, flags e configurações;
* Evidências de observabilidade e suporte.

## Regras obrigatórias

1. Não executar deploy, promoção, rollback, migration ou alteração de ambiente.
2. Não criar release, aprovar pipeline ou alterar work items no Azure DevOps.
3. Não considerar “pipeline verde” como evidência suficiente para release.
4. Diferenciar evidência aprovada, não fornecida, não aplicável e falha.
5. Toda ressalva precisa de responsável, decisão e prazo/condição.
6. Ausência de rollback para mudança irreversível é bloqueante até decisão humana explícita.
7. A decisão final de Go/No-Go é humana.

## Recursos

| Recurso | Quando carregar |
| --- | --- |
| [checklist.md](checklist.md) | Durante a avaliação |
| [examples/release-report.md](examples/release-report.md) | Para formatar o parecer |

## Fluxo de execução

### Etapa 1 — Confirmar escopo

Listar versão/janela, itens, PRs, repos, ambientes e responsáveis. Identificar alteração fora do escopo aprovado ou dependência com versão divergente.

### Etapa 2 — Consolidar qualidade

Verificar:

* revisões e aprovações necessárias;
* CI e checks obrigatórios;
* testes por camada e regressão;
* defeitos conhecidos e aceite de risco;
* compatibilidade entre componentes.

Não reexecutar o gate pré-PR por padrão; usar evidências e solicitar reexecução quando estiverem obsoletas.

### Etapa 3 — Avaliar mudança operacional

Para cada componente, revisar:

* ordem e dependências de implantação;
* migrations e compatibilidade forward/backward;
* configuração, secrets e feature flags;
* rollout gradual ou janela;
* rollback e critério de acionamento;
* backups ou reconciliação quando aplicáveis.

### Etapa 4 — Avaliar operação e suporte

Confirmar métricas, logs, alertas, dashboards, smoke tests, responsáveis, comunicação e critérios de sucesso/falha pós-release.

### Etapa 5 — Emitir parecer

Usar [examples/release-report.md](examples/release-report.md).

| Veredito | Condição |
| --- | --- |
| Pronta | Evidências obrigatórias completas, sem bloqueios |
| Pronta com ressalvas | Riscos aceitos com responsável e condição documentados |
| Go/No-Go pendente | Decisão humana ou evidência externa ainda necessária |
| Não pronta | Falha, incompatibilidade ou controle crítico ausente |

### Etapa 6 — Handoff

Entregar parecer à pessoa responsável pelo Go/No-Go. Após decisão, a execução do deploy permanece no processo/pipeline autorizado, fora desta skill.

## Resultado esperado

Parecer de release conciso, com cobertura do escopo, evidências, bloqueios, riscos aceitos, rollback e decisão pendente.