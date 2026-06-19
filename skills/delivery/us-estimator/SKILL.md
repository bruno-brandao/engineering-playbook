---
name: us-estimator
description: >-
  Estima esforço de User Stories em horas com decomposição por atividade,
  premissas e nível de confiança. Use quando o usuário pedir estimativa de US,
  sizing em horas, esforço de desenvolvimento, ou pré-estimativa antes do sprint
  planning.
---

# US Estimator

## Objetivo

Produzir **pré-estimativas em horas** de User Stories para apoiar planejamento e priorização — sem substituir a validação do time de desenvolvimento.

Esta skill complementa [requirements-reviewer](../product/requirements-reviewer/SKILL.md) e [tech-lead-reviewer](tech-lead-reviewer/SKILL.md), e antecede [sprint-planning](../../../playbooks/sprint-planning.md).

## Documentos de referência

* [us-guidelines.md](../../../product/us-guidelines.md) — definição de pronto
* [us-template.md](../../../product/us-template.md) — escopo e critérios de aceite
* [estimation-guidelines.md](references/estimation-guidelines.md) — faixas e atividades padrão

## Responsabilidades

* Analisar escopo, regras de negócio e critérios de aceite da US.
* Decompor o esforço em atividades estimáveis.
* Entregar estimativa em **horas** com faixa (mínimo–máximo) quando houver incerteza.
* Registrar premissas, riscos e dependências que impactam o esforço.
* Classificar confiança da estimativa (Alta, Média, Baixa).
* Sinalizar USs incompletas e impacto na precisão.

## Regras Obrigatórias

### 1. Não inventar escopo

Estimar apenas o que está na US (e Feature de origem, se fornecida). Lacunas → premissa explícita ou confiança **Baixa**.

### 2. Pré-estimativa, não compromisso

Toda saída deve deixar claro: *"Estimativa preliminar — validar com o time de desenvolvimento"*.

### 3. Sempre em horas

Unidade padrão: **horas (h)**. Não converter para story points salvo pedido explícito.

### 4. Faixa quando incerto

* Confiança **Alta** → valor único ou faixa estreita (ex.: 8h ou 6–8h).
* Confiança **Média** → faixa de ~30% (ex.: 12–16h).
* Confiança **Baixa** → faixa ampla + listar o que falta para refinar.

### 5. Decompor antes de totalizar

Nunca entregar apenas um número sem breakdown por atividade (ver [estimation-guidelines.md](references/estimation-guidelines.md)).

### 6. Sugerir divisão quando excessivo

Se total **> 40h** ou **> 5 dias úteis** de uma pessoa, avaliar se a US deve ser dividida (critérios de `us-guidelines.md`).

### 7. Azure DevOps — somente leitura

Ler work items via MCP; **nunca** gravar estimativa no DevOps. Entregar texto para o usuário aplicar.

Ver [agent-guidelines.md](../../../ai/agent-guidelines.md).

## Resultado Esperado

Relatório de estimativa estruturado, pronto para discussão no sprint planning ou registro manual no Azure DevOps.

---

## Recursos

| Recurso | Quando carregar |
| --- | --- |
| [references/estimation-guidelines.md](references/estimation-guidelines.md) | Faixas, atividades e heurísticas |
| [checklist.md](checklist.md) | Antes de entregar a estimativa |
| [examples/](examples/) | Formato de saída |

---

## Fluxo de Execução

### Etapa 1 — Validar entrada

Confirme que recebeu a US (texto ou ID via DevOps). Opcional: Feature de origem.

Avalie prontidão (resumo):

| Condição | Impacto na estimativa |
| --- | --- |
| Escopo + RN + CA definidos | Pode estimar com confiança Média ou Alta |
| Lacunas ou ambiguidades | Confiança Baixa; listar o que falta |
| Parecer do reviewer desfavorável | Sinalizar que estimativa é provisória |
| Parecer do tech-lead-reviewer desfavorável | Confiança Baixa; listar bloqueios técnicos |

### Etapa 2 — Identificar tipo de entrega

Classifique a US para calibrar esforço:

| Tipo | Indicadores |
| --- | --- |
| UI simples | Tela, campos, validações locais |
| CRUD / cadastro | Formulário, persistência, listagem |
| Relatório / exportação | Geração de arquivo, filtros |
| Importação | Upload, validação, persistência em lote |
| Integração | Sistema externo, API, de/para |
| Regra de negócio densa | Muitas RNs, cálculos, fluxos condicionais |
| Misto | Combinação dos acima |

Uma US pode ter múltiplos tipos — decompor por tipo.

### Etapa 3 — Decompor em atividades

Estime cada linha em horas (consulte [estimation-guidelines.md](references/estimation-guidelines.md)):

| Atividade | O que inclui |
| --- | --- |
| Refinamento técnico | Alinhamento, dúvidas, desenho rápido |
| Backend | API, regras, persistência, jobs |
| Frontend | Telas, componentes, UX |
| Integração | Chamadas externas, mapeamentos |
| Testes dev | Unitários, integração automatizada |
| Testes QA | Casos manuais a partir dos CAs |
| Ajustes / review | Code review, correções |
| Outros | Migração, feature flag, documentação |

Inclua apenas atividades **aplicáveis** à US.

### Etapa 4 — Calibrar com heurísticas

Ajuste com base em:

* Quantidade de **RNs** e **CAs**;
* Presença de **integração** ou **importação/exportação**;
* **Campos obrigatórios** e validações complexas;
* Dependência de **outras USs** ou times.

### Etapa 5 — Montar relatório

Use o template abaixo. Veja [examples/](examples/).

### Etapa 6 — Recomendar próximo passo

* US pronta + confiança Alta/Média → levar ao [sprint-planning](../../../playbooks/sprint-planning.md).
* US incompleta → [requirements-analyst](../product/requirements-analyst/SKILL.md) ou reviewer.
* US grande demais → sugerir decomposição.

---

## Template de saída

```markdown
# Estimativa — US-{ID} — {Título}

> Pré-estimativa em horas. Validar com o time de desenvolvimento antes de comprometer na sprint.

## Resumo

| Campo | Valor |
| --- | --- |
| Total estimado | {X}h (faixa: {min}–{max}h) |
| Confiança | {Alta \| Média \| Baixa} |
| Tipo principal | {UI \| CRUD \| Import/Export \| Integração \| Misto} |

## Premissas

- {premissa 1}
- {premissa 2}

## Decomposição (horas)

| Atividade | Horas | Observação |
| --- | --- | --- |
| Refinamento técnico | | |
| Backend | | |
| Frontend | | |
| Integração | | |
| Testes (dev) | | |
| Testes (QA) | | |
| Ajustes / review | | |
| **Total** | **{X}** | |

## Riscos que podem aumentar esforço

- {risco} — impacto estimado: +{N}h

## Lacunas que impedem estimativa precisa

- {lacuna} — ou "Nenhuma"

## Recomendação

{Incluir na sprint \| Refinar US antes \| Dividir em múltiplas USs}
```
