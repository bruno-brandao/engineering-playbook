# Agent Skills

Diretório canônico de skills do Engineering Playbook. Cada skill é uma pasta com `SKILL.md` no formato padrão Agent Skills (YAML frontmatter + instruções em Markdown).

As skills referenciam documentos do playbook (`product/`, `development/`, `qa/`, etc.) **sem duplicar conteúdo**. Guidelines e templates permanecem nas pastas de domínio; as skills contêm instruções operacionais, checklists e exemplos.

---

## Tipos de artefato

| Tipo | Onde fica | Objetivo |
| --- | --- | --- |
| Guideline | `product/`, `development/`, `qa/`, … | Regras e padrões do time |
| Template | `product/`, … | Estrutura de documento |
| Skill | `skills/` | Instruções para IA executar uma tarefa |
| Playbook | `playbooks/` | Processo passo a passo para pessoas |

---

## Estrutura por domínio

```text
skills
│
├── product
│   ├── requirements-analyst      ✅ disponível
│   ├── requirements-reviewer     ✅ disponível
│   └── refinement-facilitator    planejada
│
├── qa
│   ├── qa-test-designer            planejada
│   └── test-reviewer               planejada
│
├── architecture
│   ├── architecture-reviewer       planejada
│   └── adr-writer                  planejada
│
├── development
│   ├── pr-reviewer                 planejada
│   ├── code-reviewer               planejada
│   └── refactoring-advisor         planejada
│
└── delivery
    ├── tech-lead-reviewer          ✅ disponível
    ├── sprint-readiness-reviewer   ✅ disponível
    ├── us-estimator                ✅ disponível
    └── release-reviewer            planejada
```

---

## Estrutura de uma skill

```text
skills/<domínio>/<nome-da-skill>/
├── SKILL.md              # Obrigatório — instruções e fluxo
├── checklist.md          # Opcional — validação antes de entregar
├── references/           # Opcional — índice para documentos do playbook
├── examples/             # Opcional — exemplos de entrada/saída
└── scripts/              # Opcional — automações executáveis
```

---

## Skills disponíveis

| Domínio | Skill | Descrição |
| --- | --- | --- |
| product | [requirements-analyst](product/requirements-analyst/SKILL.md) | Transforma Features aprovadas em User Stories |
| product | [requirements-reviewer](product/requirements-reviewer/SKILL.md) | Revisa User Stories antes do backlog |
| delivery | [tech-lead-reviewer](delivery/tech-lead-reviewer/SKILL.md) | Revisão técnica de US e regras de negócio |
| delivery | [sprint-readiness-reviewer](delivery/sprint-readiness-reviewer/SKILL.md) | Valida prontidão para sprint; relatório consolidado por sprint ou lista de USs |
| delivery | [us-estimator](delivery/us-estimator/SKILL.md) | Pré-estimativa de US em horas |

---

## Integração por IDE

O conteúdo canônico fica em `skills/`. Para descoberta automática, copie ou vincule a skill para o caminho da IDE.

**Nota:** algumas IDEs exigem skills em pasta plana (sem subpastas de domínio). Nesse caso, vincule apenas a pasta da skill específica (ex.: `skills/product/requirements-analyst`).

### Cursor

| Escopo | Caminho |
| --- | --- |
| Projeto | `.cursor/skills/` |
| Global | `~/.cursor/skills/` |

```powershell
# Windows — a partir da raiz do projeto consumidor
New-Item -ItemType Directory -Force -Path ".cursor\skills"
New-Item -ItemType Junction -Path ".cursor\skills\requirements-analyst" -Target "caminho\para\engineering-playbook\skills\product\requirements-analyst"
```

```bash
# macOS / Linux
mkdir -p .cursor/skills
ln -s ../../caminho/para/engineering-playbook/skills/product/requirements-analyst .cursor/skills/requirements-analyst
```

### Claude Code

| Escopo | Caminho |
| --- | --- |
| Projeto | `.claude/skills/` |
| Global | `~/.claude/skills/` |

### Google Antigravity

| Escopo | Caminho |
| --- | --- |
| Projeto | `.agent/skills/` ou `.agents/skills/` |
| Global | `~/.gemini/antigravity/skills/` |

### Padrão aberto (Agent Skills)

| Escopo | Caminho |
| --- | --- |
| Projeto | `.agents/skills/` |
| Global | `~/.agents/skills/` |

---

## Uso em projetos de produto

1. Mantenha o Engineering Playbook acessível (clone, submodule ou workspace multi-root).
2. Vincule a skill no caminho da IDE.
3. Garanta que o agente consiga ler os documentos referenciados em `product/`, `development/`, etc.

### Azure DevOps (somente leitura)

Para ler Features e User Stories do Azure DevOps, configure o MCP conforme [ai/azure-devops-integration.md](../ai/azure-devops-integration.md). O agente **não deve escrever** no DevOps — apenas sugerir alterações ao usuário. Ver [ai/agent-guidelines.md](../ai/agent-guidelines.md).

**Analistas (sem Git):** ver [ai/analyst-onboarding.md](../ai/analyst-onboarding.md).

**Submodule (recomendado):**

```bash
git submodule add <url-do-engineering-playbook> docs/engineering-playbook
```

---

## Criar novas skills

1. Crie `skills/<domínio>/<nome-da-skill>/SKILL.md`.
2. Adicione `references/README.md` com links para o playbook — não copie guidelines.
3. Inclua `checklist.md` e `examples/` quando a qualidade da saída depender deles.
4. Registre a skill neste README.
5. Abra Pull Request.
