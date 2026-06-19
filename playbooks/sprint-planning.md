# Sprint Planning

Playbook para planejar a sprint com User Stories prontas para desenvolvimento.

---

## Objetivo

Selecionar e comprometer o conjunto de User Stories que o time executará na sprint, com escopo claro e capacidade alinhada.

---

## Pré-requisitos

| Item | Descrição |
| --- | --- |
| USs revisadas | Parecer favorável do [requirements-reviewer](../skills/product/requirements-reviewer/SKILL.md) ou revisão manual equivalente |
| Feature aprovada | Toda US vinculada a Feature no estado aprovado |
| Backlog priorizado | Product Owner ou analista definiu ordem de prioridade |
| Capacidade conhecida | Disponibilidade do time para a sprint |

---

## Papéis

| Papel | Responsabilidade |
| --- | --- |
| **Facilitador (SM / líder técnico)** | Conduz a cerimônia e registra compromisso |
| **Time de desenvolvimento** | Estima, questiona escopo e assume entregas |
| **QA** | Valida testabilidade e antecipa cenários |
| **Analista / PO** | Esclarece requisitos e prioriza |

---

## Entradas

* Backlog de User Stories priorizado;
* Resultado da sprint anterior (carry-over, se houver);
* Capacidade do time (pessoas × dias × férias/ausências);
* Pareceres de revisão de requisitos (quando existirem).

---

## Saídas

* Sprint backlog definido no Azure DevOps;
* USs atribuídas à sprint com responsáveis (quando aplicável);
* Tasks de implementação criadas ou planejadas;
* Riscos e dependências registrados.

---

## Passos

### 1. Revisar capacidade (10 min)

* Quantos desenvolvedores e QA disponíveis?
* Há feriados, férias ou compromissos fixos?
* Existe meta de velocity ou apenas compromisso por item?

### 2. Validar prontidão das USs (15 min)

Para cada US candidata, confirmar:

- [ ] Feature de origem aprovada
- [ ] Revisão de requisitos concluída (sem achados bloqueantes)
- [ ] Escopo, RNs e CAs definidos
- [ ] Dependências identificadas

USs não prontas **não entram** na sprint. Retornar ao analista ou agendar refinamento.

Opcional: usar a skill [sprint-readiness-reviewer](../skills/delivery/sprint-readiness-reviewer/SKILL.md) para validação assistida. Para a sprint inteira ou uma lista de USs, a skill pode gerar um **relatório consolidado** (markdown com links dos work items) em `skills/delivery/sprint-readiness-reviewer/reports/`, incluindo contexto das Features e USs irmãs em outras sprints.

Para USs sem estimativa do time, o analista pode solicitar pré-estimativa com [us-estimator](../skills/delivery/us-estimator/SKILL.md) antes da cerimônia. O desenvolvimento **valida** as horas no planning.

### 3. Apresentar e esclarecer USs (30–45 min)

Para cada US selecionada:

* Ler escopo e regras principais;
* Esclarecer dúvidas com analista/PO;
* Identificar tasks técnicas (backend, frontend, integração, testes);
* Registrar riscos.

### 4. Estimar e comprometer (20–30 min)

* Estimar esforço (story points, horas ou t-shirt — conforme prática do time);
* Verificar se o conjunto cabe na capacidade;
* Ajustar escopo se necessário (remover US ou reduzir escopo com acordo).

### 5. Finalizar sprint no Azure DevOps (10 min)

* Mover USs para a sprint;
* Criar ou vincular tasks filhas;
* Atribuir responsáveis quando definido;
* Registrar meta da sprint (opcional).

### 6. Encerramento (5 min)

* Resumir compromisso da sprint;
* Destacar dependências externas;
* Combinar canal para dúvidas durante a execução.

---

## Critérios de conclusão

1. Sprint backlog definido com USs prontas para desenvolvimento.
2. Time alinhado sobre escopo e prioridade.
3. Capacidade respeitada ou desvio justificado e acordado.
4. USs sem revisão ou com achados bloqueantes **não** incluídas.

---

## Integração com Azure DevOps

Leitura de backlog e sprint via MCP conforme [azure-devops-integration.md](../ai/azure-devops-integration.md). Alterações no sprint são feitas **pelo time** — agentes de IA apenas sugerem.

---

## Próxima etapa

Execução da sprint → desenvolvimento e testes conforme USs e CAs definidos.
