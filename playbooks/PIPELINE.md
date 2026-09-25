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
┌─────────────────────┐
│ project-scanner     │  DCP — scan repos, KB, sync-state
└──────────┬──────────┘     project-context/scripts/scan.py
           ▼
┌─────────────────────┐
│ us-implementation   │  DCP — plano de execução da US
│ planner             │     (branch verify + KB L0–L3)
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ qa-test-designer    │  Skill — estratégia e cenários rastreáveis
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ Desenvolvimento     │  Skills locais — verificação e testes
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ pre-pr-reviewer     │  Skill — gate e evidências antes do PR
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ code-reviewer       │  Skill + Devin Review + revisão humana
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ release-reviewer    │  Skill — prontidão e Go/No-Go humano
└─────────────────────┘
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
| Scan de repos / KB | CLI + Skill | [project-context](../project-context/README.md), [project-scanner](../skills/development/project-scanner/SKILL.md) |
| Plano de implementação | Skill | [us-implementation-planner](../skills/development/us-implementation-planner/SKILL.md) |
| Bootstrap de qualidade | Skill | [project-quality-bootstrap](../skills/development/project-quality-bootstrap/SKILL.md) |
| Plano de testes | Skill | [qa-test-designer](../skills/qa/qa-test-designer/SKILL.md) |
| Gate pré-PR | Skill | [pre-pr-reviewer](../skills/development/pre-pr-reviewer/SKILL.md) |
| Revisão de código | Skill + plataforma | [code-reviewer](../skills/development/code-reviewer/SKILL.md) + Devin Review |
| Prontidão de release | Skill | [release-reviewer](../skills/delivery/release-reviewer/SKILL.md) |

---

## Dev Context Platform (DCP)

Camada entre sprint planning e desenvolvimento. Documentação em [project-context/README.md](../project-context/README.md).

| Componente | Função |
| --- | --- |
| `scan init/sync/status/verify` | Scan determinístico, sync por branch de referência |
| `.engineering/` por repo | repo-profile, KB, sync-state |
| `project-map.yaml` | Mapa de repos (active / legacy / discontinued) |
| `integration-graph.md` | Dependências cross-repo |

**Piloto:** [AtivosCompraMobilizacao / US-147722](../project-context/projects/AtivosCompraMobilizacao/pilot/README.md)

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
| visual-regression (template local) | QA — evidências visuais específicas do projeto |
| migration-checklist (template local) | Development — segurança de migrations por stack |
| refinement-facilitator | Product — conduzir refinamento com IA |
| test-reviewer | QA — revisar implementação e cobertura dos testes |
| release-process (playbook) | Delivery — complementar o release-reviewer |
