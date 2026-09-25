---
name: pre-pr-reviewer
description: >-
  Valida se uma alteração está pronta para abrir Pull Request, consolidando diff,
  rastreabilidade, testes e verificações locais. Use ao finalizar desenvolvimento
  ou antes de publicar uma branch. Não corrige código nem abre PR automaticamente.
---

# Pre-PR Reviewer

## Objetivo

Executar o gate local anterior ao Pull Request, reunindo evidências reproduzíveis sem substituir CI, code review ou aprovação humana.

## Entradas

* Diff atual e branch-base confirmada;
* US/plano de implementação, quando aplicáveis;
* Plano de testes do [qa-test-designer](../../qa/qa-test-designer/SKILL.md);
* `.agents/skills/local-verification/SKILL.md` do projeto;
* Resultados de testes e evidências existentes.

## Regras obrigatórias

1. Confirmar a branch-base antes de interpretar o diff.
2. Não adivinhar comandos. Usar `local-verification`; se ausente, recomendar [project-quality-bootstrap](../project-quality-bootstrap/SKILL.md).
3. Não corrigir código durante a revisão. Correção é uma etapa separada e explicitamente solicitada.
4. Não instalar dependências, executar migrations destrutivas ou acessar ambiente real sem autorização específica.
5. Não executar commit, push, abrir PR ou escrever no Azure DevOps.
6. Diferenciar falha, verificação não executada e item não aplicável.
7. Não declarar prontidão sem evidência dos checks obrigatórios do projeto.

## Recursos

| Recurso | Quando carregar |
| --- | --- |
| [checklist.md](checklist.md) | Durante o gate |
| [examples/pre-pr-report.md](examples/pre-pr-report.md) | Para formatar a saída |

## Fluxo de execução

### Etapa 1 — Delimitar a mudança

Confirmar branch-base, ler status/diff e resumir arquivos, componentes, dados, contratos e configurações impactados. Sinalizar arquivos inesperados, gerados ou sensíveis.

### Etapa 2 — Validar rastreabilidade

Quando houver US/plano:

* mapear alterações para tarefas, RNs e CAs;
* apontar escopo não implementado ou mudança sem requisito;
* verificar se riscos do plano receberam tratamento ou evidência.

Sem US, declarar o escopo usado para o gate.

### Etapa 3 — Carregar verificações locais

* Se `local-verification` existir, seguir seus pré-requisitos e comandos.
* Se não existir, não montar uma sequência genérica; executar somente comandos explicitamente fornecidos pelo usuário ou documentados no projeto e recomendar bootstrap.
* Reutilizar comandos da CI, evitando variações equivalentes sem necessidade.

### Etapa 4 — Avaliar testes e checks especiais

Usar o diff e o plano de testes para avaliar:

* cobertura de comportamentos alterados;
* testes de regressão;
* contratos e integrações;
* migrations, schema e rollback, quando aplicável;
* UI/visual, acessibilidade e console, quando aplicável;
* configuração, secrets e observabilidade.

Ausência de skill especializada não autoriza inventar procedimentos.

### Etapa 5 — Executar e registrar

Para cada comando autorizado, registrar comando exato, resultado e evidência. Não ocultar falhas nem substituir um check obrigatório por inspeção manual.

### Etapa 6 — Emitir gate

Usar [examples/pre-pr-report.md](examples/pre-pr-report.md).

| Veredito | Condição |
| --- | --- |
| Pronto | Checks obrigatórios aprovados, cobertura suficiente e sem bloqueios |
| Pronto com ressalvas | Sem falhas bloqueantes; evidências opcionais ou riscos aceitos pendentes |
| Não pronto | Falha obrigatória, escopo incompleto, evidência crítica ausente ou risco não tratado |

### Etapa 7 — Handoff

* **Pronto / com ressalvas aceitas** → [code-reviewer](../code-reviewer/SKILL.md), Devin Review e revisão humana.
* **Não pronto** → apresentar ações objetivas; corrigir apenas em nova etapa solicitada pelo usuário.

## Resultado esperado

Parecer pré-PR auditável, com escopo, comandos, resultados, lacunas e decisão clara.