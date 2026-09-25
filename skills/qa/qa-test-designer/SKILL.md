---
name: qa-test-designer
description: >-
  Converte User Stories, regras de negócio e critérios de aceite em estratégia e
  cenários de teste rastreáveis. Use após o planejamento técnico, antes do
  desenvolvimento ou para preparar QA, sem assumir framework de automação.
---

# QA Test Designer

## Objetivo

Produzir um plano de testes executável e rastreável que cubra comportamento, riscos e integrações da entrega sem inventar regras de negócio ou impor tecnologia de teste.

Complementa [requirements-reviewer](../../product/requirements-reviewer/SKILL.md), [tech-lead-reviewer](../../delivery/tech-lead-reviewer/SKILL.md) e [us-implementation-planner](../../development/us-implementation-planner/SKILL.md).

## Entradas

* User Story, RNs e critérios de aceite;
* Feature de origem, quando disponível;
* Plano de implementação e impactos técnicos;
* Código, contratos e testes existentes, quando acessíveis;
* Skill local `test-generation`, quando existente.

## Regras obrigatórias

1. Não inventar comportamento ausente na US; registrar lacunas e perguntas.
2. Manter rastreabilidade explícita entre RN/CA, cenário e evidência.
3. Separar desenho de testes de implementação automatizada.
4. Escolher camadas por risco, não exigir E2E para todo cenário.
5. Identificar massas, mocks, integrações e ambientes sem usar dados reais sensíveis.
6. Azure DevOps é somente leitura; não criar casos ou atualizar work items.
7. Se a revisão funcional/técnica estiver bloqueada, marcar o plano como provisório.

## Recursos

| Recurso | Quando carregar |
| --- | --- |
| [checklist.md](checklist.md) | Durante o desenho e antes da entrega |
| [examples/test-plan.md](examples/test-plan.md) | Para formatar o plano final |

## Fluxo de execução

### Etapa 1 — Validar entradas

Confirmar escopo, RNs, CAs e resultado das revisões anteriores. Ausência de regra necessária para definir resultado esperado é bloqueante; ausência de detalhe técnico pode virar premissa explícita.

### Etapa 2 — Construir mapa de risco

Para cada comportamento, avaliar impacto e probabilidade em:

* negócio e cálculo;
* dados e histórico;
* autorização e dados sensíveis;
* integrações, timeout, retry e idempotência;
* concorrência, volume e performance;
* compatibilidade e regressão;
* observabilidade e recuperação.

### Etapa 3 — Definir cenários

Cobrir, quando aplicável:

* caminho feliz;
* validações e limites;
* erro e indisponibilidade;
* permissões;
* duplicidade/idempotência;
* estados e transições;
* regressões relacionadas.

Usar Dado/Quando/Então quando isso melhorar a testabilidade, sem reescrever a US silenciosamente.

### Etapa 4 — Escolher camada e evidência

| Camada | Uso |
| --- | --- |
| Unitário | Regras isoladas, cálculos e validações |
| Integração | Persistência, adapters, filas e serviços |
| Contrato | APIs/eventos entre sistemas |
| UI/E2E | Jornadas críticas e integração das camadas |
| Não funcional | Segurança, performance, acessibilidade e observabilidade |

Para cada cenário, definir evidência esperada: assertion, resposta, persistência, evento, log ou captura.

### Etapa 5 — Integrar contexto local

Se `.agents/skills/test-generation/SKILL.md` existir, usá-la para framework, estrutura, mocks e comandos. Se não existir, entregar o desenho agnóstico e recomendar [project-quality-bootstrap](../../development/project-quality-bootstrap/SKILL.md); não adivinhar ferramentas.

### Etapa 6 — Emitir plano

Usar [examples/test-plan.md](examples/test-plan.md). Classificar cenários em **Obrigatório**, **Recomendado** ou **Exploratório** e listar lacunas separadamente.

### Etapa 7 — Handoff

* Plano completo → desenvolvimento/QA e skill local `test-generation`.
* Lacunas funcionais → analista/negócio.
* Lacunas técnicas críticas → refinamento técnico.
* Após implementação e execução das verificações → [pre-pr-reviewer](../../development/pre-pr-reviewer/SKILL.md).

## Resultado esperado

Plano de testes rastreável, priorizado por risco e independente de framework, pronto para execução manual ou automação conforme os padrões locais.