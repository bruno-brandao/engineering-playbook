# Fluxo de Requisitos

Visão end-to-end do pipeline documentado neste repositório — da descoberta ao sprint planning.

---

## Pipeline

```text
┌─────────────────────┐
│ product-discovery   │  Playbook — entender problema
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ feature-refinement  │  Playbook — aprovar Feature com negócio
└──────────┬──────────┘
           ▼
┌─────────────────────┐     product/feature-guidelines.md
│ Feature aprovada    │     product/feature-template.md
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ requirements-analyst│  Skill — decompor em User Stories
└──────────┬──────────┘     product/us-guidelines.md
           ▼                product/us-template.md
┌─────────────────────┐
│ requirements-reviewer│ Skill — revisar qualidade das USs
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ tech-lead-reviewer  │  Skill — revisão técnica e RNs
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ sprint-readiness    │  Skill — validar prontidão para sprint
│ reviewer            │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ us-estimator        │  Skill — pré-estimativa em horas
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ sprint-planning     │  Playbook — comprometer sprint
└──────────┬──────────┘
           ▼
     Desenvolvimento + QA
```

---

## Artefatos por etapa

| Etapa | Tipo | Documento / Skill |
| --- | --- | --- |
| Descoberta | Playbook | [product-discovery.md](product-discovery.md) |
| Refinamento | Playbook | [feature-refinement.md](feature-refinement.md) |
| Feature | Guideline + Template | [feature-guidelines.md](../product/feature-guidelines.md), [feature-template.md](../product/feature-template.md) |
| User Story | Guideline + Template | [us-guidelines.md](../product/us-guidelines.md), [us-template.md](../product/us-template.md) |
| Decomposição | Skill | [requirements-analyst](../skills/product/requirements-analyst/SKILL.md) |
| Revisão funcional | Skill | [requirements-reviewer](../skills/product/requirements-reviewer/SKILL.md) |
| Revisão técnica | Skill | [tech-lead-reviewer](../skills/delivery/tech-lead-reviewer/SKILL.md) |
| Prontidão sprint | Skill | [sprint-readiness-reviewer](../skills/delivery/sprint-readiness-reviewer/SKILL.md) |
| Pré-estimativa | Skill | [us-estimator](../skills/delivery/us-estimator/SKILL.md) |
| Planejamento | Playbook | [sprint-planning.md](sprint-planning.md) |

---

## Azure DevOps

| Artefato ADO | Papel no pipeline |
| --- | --- |
| Epic / Iniciativa | Contexto de negócio (parent da Feature) |
| Feature | Aprovada antes da decomposição |
| User Story | Entrega de desenvolvimento e QA |
| Task | Decomposição técnica na sprint |

Integração somente leitura: [azure-devops-integration.md](../ai/azure-devops-integration.md)

**Distribuição para analistas:** [analyst-onboarding.md](../ai/analyst-onboarding.md)

---

## Próximas evoluções planejadas

| Item | Domínio |
| --- | --- |
| qa-test-designer | QA — gerar casos de teste a partir de USs |
| refinement-facilitator | Product — conduzir refinamento com IA |
| release-process (playbook) | Delivery — complementar devops |
