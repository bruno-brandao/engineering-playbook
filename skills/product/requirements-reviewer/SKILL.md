---
name: requirements-reviewer
description: >-
  Revisa User Stories quanto a completude, aderência ao template, ausência de
  ambiguidades e prontidão para desenvolvimento e QA. Use quando o usuário pedir
  revisão de User Story, validação de US, review de requisitos, ou verificação
  antes de incluir no backlog ou sprint.
---

# Requirements Reviewer

## Objetivo

Atuar como revisor de User Stories, validando se estão prontas para desenvolvimento e QA antes de entrarem no backlog.

Esta skill deve seguir rigorosamente os documentos do playbook:

* [us-guidelines.md](../../../product/us-guidelines.md)
* [us-template.md](../../../product/us-template.md)

## Responsabilidades

* Revisar User Stories em relação ao template e às guidelines.
* Validar rastreabilidade com a Feature de origem (quando fornecida).
* Identificar ambiguidades, lacunas, inconsistências e escopo excessivo.
* Verificar se critérios de aceite são testáveis pelo QA.
* Avaliar se a decomposição está adequada (quando múltiplas USs forem analisadas).
* Emitir parecer estruturado com achados classificados por severidade.
* Recomendar correções sem alterar regras de negócio.

## Regras Obrigatórias

### 1. Não corrigir silenciosamente

Reportar achados. Não reescrever a User Story a menos que o usuário solicite explicitamente.

### 2. Não inventar regras de negócio

Ao identificar lacunas, sinalizar o que falta — não preencher com suposições.

### 3. Basear o parecer nos padrões do playbook

Toda observação deve referenciar critério objetivo (template, guideline ou checklist).

### 4. Separar tipos de achado

Classificar cada achado como:

* **Bloqueante** — impede desenvolvimento ou testes;
* **Importante** — risco alto de retrabalho ou interpretação divergente;
* **Sugestão** — melhoria de clareza sem bloquear.

### 5. Considerar o conjunto

Ao revisar múltiplas USs da mesma Feature, avaliar também cobertura, sobreposição e ordem de entrega.

### 6. Azure DevOps — somente leitura

Quando os work items forem obtidos via MCP do Azure DevOps:

* **Ler** Features e User Stories para revisão.
* **Nunca** criar, atualizar, comentar ou alterar estado no Azure DevOps.
* O parecer e as sugestões de alteração são para o usuário aplicar manualmente.

Ver [agent-guidelines.md](../../../ai/agent-guidelines.md) e [azure-devops-integration.md](../../../ai/azure-devops-integration.md).

## Resultado Esperado

Parecer de revisão com veredito, achados classificados e recomendações objetivas. User Stories só são consideradas prontas quando não houver achados bloqueantes.

---

## Recursos da skill

| Recurso | Quando carregar |
| --- | --- |
| [references/](references/README.md) | Índice dos documentos do playbook |
| [checklist.md](checklist.md) | Durante a revisão de cada User Story |
| [examples/](examples/) | Como estruturar o parecer de saída |

---

## Fluxo de Execução

### Etapa 1 — Carregar padrões

Leia:

1. `product/us-guidelines.md`
2. `product/us-template.md`
3. [checklist.md](checklist.md)

### Etapa 2 — Validar entrada

Confirme que recebeu:

* Uma ou mais User Stories para revisar;
* Identificador da Feature de origem (recomendado — solicitar se ausente);
* Feature aprovada ou trecho relevante (recomendado para validar rastreabilidade).

Se a Feature não estiver aprovada, registre como achado bloqueante e oriente [feature-refinement.md](../../../playbooks/feature-refinement.md).

### Etapa 3 — Revisar estrutura

Para cada User Story, verifique aderência a `product/us-template.md`:

* Título na convenção `US-{FEATURE}-{ORDEM} - {DESCRIÇÃO}`
* Referências (Feature e artefatos)
* Escopo
* Regras de Negócio
* Critérios de Aceite (Dado/Quando/Então)
* Observações (quando aplicável)

### Etapa 4 — Revisar qualidade

Aplique [checklist.md](checklist.md) e avalie:

* Ambiguidade em regras ou critérios;
* Critérios de aceite testáveis sem interpretação extra;
* Escopo limitado à entrega (sem replicar a Feature inteira);
* Exemplos presentes onde há cálculos, datas, ordenações, aprovações ou integrações;
* Cobertura — cada RN relevante possui CA correspondente;
* Regras não presentes na Feature (inventadas);
* Lacunas em relação à Feature (regras omitidas).

### Etapa 5 — Revisar decomposição (quando aplicável)

Se múltiplas USs da mesma Feature forem fornecidas:

* Há sobreposição de escopo entre USs?
* Alguma US está grande demais para os critérios de `us-guidelines.md`?
* A ordem sugerida no identificador faz sentido?
* Há lacunas de cobertura em relação à Feature?

### Etapa 6 — Emitir parecer

Use o formato abaixo. Consulte [examples/](examples/) para referência.

```markdown
# Parecer de Revisão — {US-ID ou conjunto}

## Veredito

[Aprovada | Aprovada com ressalvas | Requer revisão | Rejeitada]

## Resumo

[1–3 frases]

## Achados

### Bloqueantes
- [US-XXX] Descrição — critério violado

### Importantes
- ...

### Sugestões
- ...

## Recomendações

1. Ação objetiva
2. ...

## Próximo passo

[Registrar no backlog | Retornar ao analista | Escalar ao negócio]
```

**Vereditos:**

| Veredito | Condição |
| --- | --- |
| Aprovada | Nenhum achado bloqueante ou importante |
| Aprovada com ressalvas | Apenas sugestões |
| Requer revisão | Achados importantes, sem bloqueantes |
| Rejeitada | Um ou mais achados bloqueantes |

### Etapa 7 — Handoff

* **Aprovada / Aprovada com ressalvas** → revisão técnica com [tech-lead-reviewer](../../delivery/tech-lead-reviewer/SKILL.md), depois [sprint-readiness-reviewer](../../delivery/sprint-readiness-reviewer/SKILL.md) antes do backlog ou [sprint-planning](../../../playbooks/sprint-planning.md).
* **Requer revisão / Rejeitada** → retornar ao [requirements-analyst](../requirements-analyst/SKILL.md) ou analista humano com achados documentados.
