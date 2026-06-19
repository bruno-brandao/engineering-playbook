---
name: tech-lead-reviewer
description: >-
  Revisa User Stories sob a ótica técnica — viabilidade de implementação,
  completude das regras de negócio para desenvolvimento, dependências,
  integrações, segurança e impacto arquitetural. Use quando o usuário pedir
  revisão técnica de US, parecer de tech lead, validação de regras para
  desenvolvimento, ou antes de estimar ou incluir no sprint.
---

# Tech Lead Reviewer

## Objetivo

Atuar como Tech Lead na revisão técnica de User Stories, validando se as **Regras de Negócio** e o escopo são implementáveis sem decisões implícitas, e se a US está tecnicamente pronta para desenvolvimento.

Esta skill complementa o [requirements-reviewer](../../product/requirements-reviewer/SKILL.md) (foco em qualidade funcional e template) com foco em **viabilidade técnica e implementação**.

## Documentos de referência

* [us-guidelines.md](../../../product/us-guidelines.md) — qualidade de RNs e RG06 (dev não deve adivinhar)
* [us-template.md](../../../product/us-template.md) — estrutura e seção Observações
* [technical-review-guidelines.md](references/technical-review-guidelines.md) — critérios técnicos da revisão
* [agent-guidelines.md](../../../ai/agent-guidelines.md) — somente leitura no Azure DevOps

## Responsabilidades

* Revisar RNs sob a ótica de implementação — cada regra deve ser traduzível em comportamento de sistema sem suposições.
* Avaliar viabilidade técnica do escopo declarado.
* Identificar lacunas técnicas (APIs, contratos, permissões, dados, integrações, migrações).
* Detectar decisões de arquitetura ou implementação deixadas implícitas para o desenvolvedor.
* Verificar dependências técnicas entre USs e com sistemas externos.
* Avaliar impactos em segurança, performance, observabilidade e dados sensíveis.
* Emitir parecer estruturado com achados classificados por severidade.
* Recomendar esclarecimentos ou ajustes sem alterar regras de negócio.

## Regras Obrigatórias

### 1. Não corrigir silenciosamente

Reportar achados. Não reescrever a User Story a menos que o usuário solicite explicitamente.

### 2. Não inventar regras de negócio

Sinalizar lacunas funcionais ou técnicas — não preencher com suposições de negócio.

### 3. Separar negócio de técnica

* Lacuna de **negócio** → retornar ao analista ou negócio.
* Lacuna **técnica** na especificação → registrar como achado e sugerir complemento na US (Observações ou RN).

### 4. Classificar achados

* **Bloqueante** — impede implementação segura ou correta; decisão crítica não documentada.
* **Importante** — alto risco de retrabalho, débito técnico ou interpretação divergente no time.
* **Sugestão** — melhoria de clareza técnica sem bloquear.

### 5. Considerar o conjunto

Ao revisar múltiplas USs da mesma Feature, avaliar ordem técnica, dependências e contratos entre entregas.

### 6. Usar contexto do código quando disponível

Se o repositório do produto estiver acessível, validar RNs contra padrões, modelos e integrações existentes. Sem acesso ao código, declarar premissas no parecer.

### 7. Azure DevOps — somente leitura

Ler work items via MCP; **nunca** criar, atualizar, comentar ou alterar estado.

Ver [azure-devops-integration.md](../../../ai/azure-devops-integration.md).

## Resultado Esperado

Parecer técnico com veredito, achados por RN/área técnica e recomendações objetivas. USs só são consideradas tecnicamente prontas quando não houver achados bloqueantes.

---

## Recursos

| Recurso | Quando carregar |
| --- | --- |
| [references/](references/README.md) | Índice e critérios técnicos |
| [checklist.md](checklist.md) | Durante a revisão de cada User Story |
| [examples/](examples/) | Formato do parecer de saída |

---

## Fluxo de Execução

### Etapa 1 — Carregar padrões

Leia:

1. `product/us-guidelines.md` (seções *Qualidade das Regras de Negócio* e RG06)
2. [technical-review-guidelines.md](references/technical-review-guidelines.md)
3. [checklist.md](checklist.md)

### Etapa 2 — Validar entrada

Confirme que recebeu:

* Uma ou mais User Stories para revisar;
* Feature de origem (recomendado);
* Parecer do [requirements-reviewer](../../product/requirements-reviewer/SKILL.md) (recomendado — não substitui esta revisão);
* Contexto do sistema ou repositório (opcional, melhora a revisão).

Se o parecer do requirements-reviewer indicar **Rejeitada** ou **Requer revisão**, registre que a revisão técnica é **provisória** até correção funcional.

### Etapa 3 — Revisar Regras de Negócio (implementabilidade)

Para cada RN (`RN01`, `RN02`, …), verifique:

* Comportamento traduzível em validação, persistência, integração ou UI sem ambiguidade técnica;
* Estados, transições e exceções documentados (erro, bloqueio, timeout, permissão negada);
* Dados de entrada e saída identificáveis (campos, formatos, limites);
* Regras condicionais com critérios objetivos — não genéricas (`us-guidelines.md` RG02);
* Exemplos presentes onde há cálculo, data, ordenação, aprovação ou integração;
* Nenhuma decisão de negócio deixada para o desenvolvedor (RG06).

Marque RNs com problema no parecer: `[RN03]`.

### Etapa 4 — Revisar escopo e entrega técnica

Avalie se o escopo declara **o que** será entregue tecnicamente:

* Endpoint, tela, job, evento ou componente identificável;
* Contratos de API ou referência a Swagger/OpenAPI quando aplicável;
* Artefatos técnicos referenciados (Figma, fluxo, documento de integração);
* Fronteiras claras — o que fica fora desta US.

### Etapa 5 — Revisar dimensões técnicas

Aplique [checklist.md](checklist.md) nas áreas:

* **Dados** — entidades impactadas, migrações, unicidade, histórico;
* **Integrações** — sistemas externos, idempotência, retry, fallback;
* **Segurança** — autenticação, autorização, dados sensíveis, auditoria;
* **Performance** — volume, paginação, limites, operações síncronas vs assíncronas;
* **Observabilidade** — logs, métricas ou rastreio quando falha impacta operação;
* **Dependências** — outras USs, features, ambientes ou feature flags.

### Etapa 6 — Revisar decomposição técnica (quando aplicável)

Se múltiplas USs da mesma Feature:

* Ordem técnica coerente com dependências (ex.: API antes de tela);
* Contratos entre USs definidos ou inferíveis;
* Risco de duplicação de lógica ou integração;
* Alguma US concentra complexidade técnica demais para uma sprint.

### Etapa 7 — Emitir parecer

Use o formato abaixo. Consulte [examples/](examples/).

```markdown
# Parecer Técnico — {US-ID ou conjunto}

## Veredito

[Aprovada tecnicamente | Aprovada com ressalvas | Requer esclarecimentos | Bloqueada tecnicamente]

## Resumo

[1–3 frases]

## Revisão por Regras de Negócio

| RN | Status | Observação |
| --- | --- | --- |
| RN01 | OK / Atenção / Bloqueio | [breve] |

## Achados

### Bloqueantes
- [RNxx | Área] Descrição — critério violado

### Importantes
- ...

### Sugestões
- ...

## Impacto técnico

| Área | Avaliação |
| --- | --- |
| Dados | [Baixo / Médio / Alto / N/A] |
| Integrações | ... |
| Segurança | ... |
| Complexidade | ... |

## Recomendações

1. Ação objetiva
2. ...

## Próximo passo

[Estimar | Sprint readiness | Retornar ao analista | Refinamento técnico]
```

**Vereditos:**

| Veredito | Condição |
| --- | --- |
| Aprovada tecnicamente | Nenhum achado bloqueante ou importante |
| Aprovada com ressalvas | Apenas sugestões |
| Requer esclarecimentos | Achados importantes, sem bloqueantes |
| Bloqueada tecnicamente | Um ou mais achados bloqueantes |

### Etapa 8 — Handoff

* **Aprovada tecnicamente / com ressalvas** → [us-estimator](../us-estimator/SKILL.md) e [sprint-readiness-reviewer](../sprint-readiness-reviewer/SKILL.md).
* **Requer esclarecimentos** → analista ou negócio (lacuna funcional) ou analista com complemento técnico em Observações.
* **Bloqueada tecnicamente** → retornar ao [requirements-analyst](../../product/requirements-analyst/SKILL.md) ou sessão de refinamento com desenvolvimento antes de estimar.
