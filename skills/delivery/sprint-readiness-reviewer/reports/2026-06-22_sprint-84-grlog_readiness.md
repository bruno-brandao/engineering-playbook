# Relatório de Prontidão para Sprint — Sprint 84 GRLog

**Data:** 2026-06-22  
**Projeto:** [Vix - GRLog](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog)  
**Time:** Vix - GRLog Team  
**Sprint:** Sprint 84 (15/06/2026 – 30/06/2026)  
**Escopo analisado:** Sprint 84 — todas as User Stories alocadas  
**Gerado por:** sprint-readiness-reviewer

---

## Resumo executivo

| Métrica | Valor |
| --- | --- |
| USs no escopo | 9 |
| **Prontas** | **0** |
| **Não prontas** | **9** |
| Features envolvidas | 7 |
| Features aprovadas | 7 |
| Features com pendência | 0 |
| Features na sprint sem US no escopo | 1 ([147137](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147137)) |
| USs de contexto (outras sprints) | 1 ([148087](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148087)) |

**Recomendação geral:** **Adiar execução plena no sprint planning** — nenhuma US atende integralmente ao checklist de prontidão. Incluir na sprint apenas itens operacionais (bugs/tasks) e USs após refinamento. Priorizar fechamento de [147345](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147345), decomposição de [110227](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/110227) e [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146), e remoção ou especificação de [148075](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148075) / [148152](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148152).

**Parecer prévio considerado:** análise de requisitos (guideline) e parecer item a item de [110227](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/110227), [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146), [147345](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147345). Revisão técnica (tech-lead-reviewer): **não realizada**.

---

## Contexto por Feature

> USs da mesma Feature podem estar distribuídas em sprints diferentes. Esta seção consolida o panorama completo da Feature.

### Feature [143425](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/143425) — Controle de Receita — Integração com o fluxo da medição

| Campo | Valor |
| --- | --- |
| Estado | Feature Aprovada |
| USs no escopo desta análise | [110227](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/110227) |
| USs da mesma Feature em outras sprints | Nenhuma |
| USs da mesma Feature sem sprint | Nenhuma |

**Cobertura da Feature**

- RGs da Feature cobertas pelas USs do escopo: **parcial** — única US concentra rotina, CUT OFF, consolidação e memória de cálculo
- Lacunas de decomposição: **sim** — complexidade exige múltiplas USs (guideline de decomposição)
- Dependências: [110227](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/110227) depende de UI/campos de [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146) e parametrização de [147345](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147345)

---

### Feature [144922](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/144922) — Melhorias na Tela Controle de Receitas

| Campo | Valor |
| --- | --- |
| Estado | Feature Aprovada |
| USs no escopo desta análise | [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146) |
| USs da mesma Feature em outras sprints | Nenhuma |
| USs da mesma Feature sem sprint | Nenhuma |

**Cobertura da Feature**

- RGs da Feature cobertas pelas USs do escopo: **parcial** — US única agrega layout, permissões, aba espelhada, recálculo, inconsistências e memória de cálculo
- Lacunas de decomposição: **sim**
- Dependências: referenciada por [147348](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147348); precede [147345](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147345) e [110227](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/110227)

---

### Feature [145543](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145543) — Apponta — Pré-Carregamento Automático

| Campo | Valor |
| --- | --- |
| Estado | Feature Aprovada |
| USs no escopo desta análise | [145541](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145541) |
| USs da mesma Feature em outras sprints | Nenhuma |
| USs da mesma Feature sem sprint | Nenhuma |

**Cobertura da Feature**

- RGs da Feature cobertas pelas USs do escopo: **sim** (escopo alinhado, ~58% da Feature)
- Lacunas de decomposição: **não**
- Dependências: nenhuma crítica identificada

---

### Feature [146808](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/146808) — Carga única de Parametrizações

| Campo | Valor |
| --- | --- |
| Estado | Feature Aprovada |
| USs no escopo desta análise | [147345](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147345) |
| USs da mesma Feature em outras sprints | Nenhuma |
| USs da mesma Feature sem sprint | Nenhuma |

**Cobertura da Feature**

- RGs da Feature cobertas pelas USs do escopo: **parcial** — lacunas RG06 abertas (“validar com equipe”)
- Lacunas de decomposição: **não** (US única adequada se requisitos fechados)
- Dependências: depende de campos definidos em [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146)

---

### Feature [146830](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/146830) — Importação de Valores Faturados

| Campo | Valor |
| --- | --- |
| Estado | Feature Aprovada |
| USs no escopo desta análise | [147348](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147348) |
| USs da mesma Feature em outras sprints | Nenhuma |
| USs da mesma Feature sem sprint | Nenhuma |

**Cobertura da Feature**

- RGs da Feature cobertas pelas USs do escopo: **sim** (~57,5% da Feature)
- Lacunas de decomposição: **não**
- Dependências: [147348](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147348) → [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146); alimenta [147943](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147943)

---

### Feature [147420](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147420) — Contrato — Dados Financeiro e Histórico Faturamento

| Campo | Valor |
| --- | --- |
| Estado | Feature Aprovada |
| USs no escopo desta análise | [147943](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147943) |
| USs da mesma Feature em outras sprints | Nenhuma |
| USs da mesma Feature sem sprint | Nenhuma |

**Cobertura da Feature**

- RGs da Feature cobertas pelas USs do escopo: **parcial** (~39% — entrega parcial da Feature)
- Lacunas de decomposição: **avaliar** — três áreas funcionais na mesma US
- Dependências: [147943](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147943) → [147348](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147348)

---

### Feature [147496](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147496) — Tabela de Preços — Cadastro de Tributação

| Campo | Valor |
| --- | --- |
| Estado | Feature Aprovada |
| USs no escopo desta análise | [147969](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147969) |
| USs da mesma Feature em outras sprints | Nenhuma |
| USs da mesma Feature sem sprint | Nenhuma |

**Cobertura da Feature**

- RGs da Feature cobertas pelas USs do escopo: **parcial** — lacuna RG06 na auditoria
- Lacunas de decomposição: **avaliar** — duas telas (Tabela de Preços + Operação)
- Dependências: nenhuma crítica entre Features

---

### Feature [147137](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147137) — CNPJ Alfanumérico *(na sprint, fora do escopo de US)*

| Campo | Valor |
| --- | --- |
| Estado | Feature Aprovada |
| USs no escopo desta análise | Nenhuma |
| USs da mesma Feature em outras sprints | [148087](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148087) — Sprint 83 — Teste QA aprovado |
| USs da mesma Feature sem sprint | Nenhuma |

**Cobertura da Feature**

- Feature alocada na Sprint 84, mas trabalho de execução está na US [148087](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148087) (Sprint 83, QA aprovado)
- Risco: Feature aparece na sprint atual sem US correspondente — possível item residual ou alocação incorreta

---

## Detalhamento por User Story (escopo)

### [110227](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/110227) — Integração Medição → Controle de Receitas

| Campo | Valor |
| --- | --- |
| Sprint | Sprint 84 |
| Feature pai | [143425](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/143425) — Feature Aprovada |
| Escopo desta análise | Sim |

#### Veredito

**Não pronta**

#### Checklist resumido

| Área | Status |
| --- | --- |
| Feature aprovada | ✅ |
| Estrutura US (escopo, RN, CA) | ❌ — escopo presente; RNs narrativas sem numeração; **sem CA Dado/Quando/Então** |
| Revisão de requisitos | ❌ Requer revisão |
| Revisão técnica | Não realizada |
| Cobertura RN ↔ CA | ❌ — CAs formais ausentes |

#### Bloqueios

- Parecer requirements-reviewer = **Requer revisão**
- US sem critérios de aceite em formato Dado/Quando/Então (checklist — definição de pronto)
- Decomposição insuficiente — rotina batch + CUT OFF + consolidação + memória de cálculo (RG06 / decomposição)
- Lacunas RG06: fluxo “processamento de medição” vs edição manual indefinido
- Revisão técnica não realizada

#### Achados importantes

- Replica ~118% do conteúdo da Feature 143425
- Termos genéricos “conforme parametrizações/detalhado” (RG02)
- Cálculos CUT OFF sem exemplos numéricos (RG04)

#### Recomendação

Retornar ao analista — decompor, formalizar CAs e fechar lacunas antes do sprint planning.

---

### [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146) — Melhorias na Tela Controle de Receitas

| Campo | Valor |
| --- | --- |
| Sprint | Sprint 84 |
| Feature pai | [144922](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/144922) — Feature Aprovada |
| Escopo desta análise | Sim |

#### Veredito

**Não pronta**

#### Checklist resumido

| Área | Status |
| --- | --- |
| Feature aprovada | ✅ |
| Estrutura US (escopo, RN, CA) | ❌ — sem CA Dado/Quando/Então formal |
| Revisão de requisitos | ❌ Requer revisão |
| Revisão técnica | Não realizada |
| Cobertura RN ↔ CA | ❌ |

#### Bloqueios

- Parecer requirements-reviewer = **Requer revisão**
- US sem critérios de aceite Dado/Quando/Então
- Decomposição insuficiente — 6+ entregas independentes na mesma US
- “Por Importação de Receita (será descrito posteriormente)” — lacuna funcional (RG06)
- Revisão técnica não realizada

#### Achados importantes

- Replica ~82% da Feature; link Figma presente ✅
- Condição de edição ambígua (status Liberado vs Aberto)
- Possível conflito de fórmulas de cálculo com [110227](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/110227)

#### Recomendação

Retornar ao analista — decompor e alinhar cálculos com [110227](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/110227). **Deve preceder** [147345](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147345) e [110227](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/110227).

---

### [145541](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145541) — Apponta — Pré-Carregamento Automático

| Campo | Valor |
| --- | --- |
| Sprint | Sprint 84 |
| Feature pai | [145543](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145543) — Feature Aprovada |
| Escopo desta análise | Sim |

#### Veredito

**Não pronta**

#### Checklist resumido

| Área | Status |
| --- | --- |
| Feature aprovada | ✅ |
| Estrutura US (escopo, RN, CA) | ❌ — regras narrativas OK; **sem CA Dado/Quando/Então** |
| Revisão de requisitos | ⚠️ Aprovada com ressalvas |
| Revisão técnica | Não realizada |
| Cobertura RN ↔ CA | ❌ |

#### Bloqueios

- US sem critérios de aceite Dado/Quando/Então (bloqueio automático do checklist)
- Revisão técnica não realizada

#### Achados importantes

- Melhor especificada do cluster Apponta: MSG01/MSG02, gatilho pós-sincronização, janela 24h
- Permissão genérica (RG02) — ressalva, não bloqueante isolada se CAs existissem

#### Recomendação

Retornar ao analista para formalizar CAs testáveis; candidata a **Pronta** após isso + revisão técnica.

---

### [147345](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147345) — Carga única de Parametrizações

| Campo | Valor |
| --- | --- |
| Sprint | Sprint 84 |
| Feature pai | [146808](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/146808) — Feature Aprovada |
| Escopo desta análise | Sim |

#### Veredito

**Não pronta**

#### Checklist resumido

| Área | Status |
| --- | --- |
| Feature aprovada | ✅ |
| Estrutura US (escopo, RN, CA) | ❌ |
| Revisão de requisitos | ❌ Rejeitada |
| Revisão técnica | Não realizada |
| Cobertura RN ↔ CA | ❌ |

#### Bloqueios

- Parecer requirements-reviewer = **Rejeitada**
- RG06: “validar com equipe” — chave de unicidade e usuário de auditoria
- US sem critérios de aceite Dado/Quando/Então
- Mecanismo de execução da carga indefinido (tela/job/script) e comportamento de reexecução
- Revisão técnica não realizada

#### Achados importantes

- Replica ~96% da Feature
- MSG01/MSG02 definidas; falta MSG para duplicidade e contrato inexistente
- Dependência: campos de [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146)

#### Recomendação

Escalar ao negócio — **não estimar nem iniciar dev**. Aguardar [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146).

---

### [147348](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147348) — Importação de Valores Faturados

| Campo | Valor |
| --- | --- |
| Sprint | Sprint 84 |
| Feature pai | [146830](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/146830) — Feature Aprovada |
| Escopo desta análise | Sim |

#### Veredito

**Não pronta**

#### Checklist resumido

| Área | Status |
| --- | --- |
| Feature aprovada | ✅ |
| Estrutura US (escopo, RN, CA) | ❌ — sem CA formal |
| Revisão de requisitos | ⚠️ Aprovada com ressalvas |
| Revisão técnica | Não realizada |
| Cobertura RN ↔ CA | ❌ |

#### Bloqueios

- US sem critérios de aceite Dado/Quando/Então
- Dependência explícita de [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146) ainda **Não pronta**
- Revisão técnica não realizada

#### Achados importantes

- Escopo contido; formato de colunas CSV definido
- “Conforme descrito na história #145146” (RG01/RG02)

#### Recomendação

Aguardar [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146); formalizar CAs e exemplo de linha CSV.

---

### [147943](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147943) — Contrato — Dados Financeiro e Histórico Faturamento

| Campo | Valor |
| --- | --- |
| Sprint | Sprint 84 |
| Feature pai | [147420](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147420) — Feature Aprovada |
| Escopo desta análise | Sim |

#### Veredito

**Não pronta**

#### Checklist resumido

| Área | Status |
| --- | --- |
| Feature aprovada | ✅ |
| Estrutura US (escopo, RN, CA) | ❌ — sem CA Dado/Quando/Então |
| Revisão de requisitos | ⚠️ Aprovada com ressalvas |
| Revisão técnica | Não realizada |
| Cobertura RN ↔ CA | ❌ |

#### Bloqueios

- US sem critérios de aceite Dado/Quando/Então
- Dependência de [147348](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147348) (Não pronta)
- Revisão técnica não realizada

#### Achados importantes

- Regra “Cancelado” objetiva; link Figma ✅
- Três áreas funcionais na mesma US

#### Recomendação

Aguardar cadeia [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146) → [147348](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147348); formalizar CAs.

---

### [147969](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147969) — Tabela de Preços — Cadastro de Tributação

| Campo | Valor |
| --- | --- |
| Sprint | Sprint 84 |
| Feature pai | [147496](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147496) — Feature Aprovada |
| Escopo desta análise | Sim |

#### Veredito

**Não pronta**

#### Checklist resumido

| Área | Status |
| --- | --- |
| Feature aprovada | ✅ |
| Estrutura US (escopo, RN, CA) | ❌ — sem CA formal |
| Revisão de requisitos | ❌ — achado bloqueante RG06 |
| Revisão técnica | Não realizada |
| Cobertura RN ↔ CA | ❌ |

#### Bloqueios

- RG06: “validar equipe o que será detalhado” na auditoria do histórico
- US sem critérios de aceite Dado/Quando/Então
- Revisão técnica não realizada

#### Achados importantes

- Exemplo de sobreposição de vigência (RG04) ✅; MSG01–MSG06 ✅; Figma ✅
- Escopo em duas telas — avaliar decomposição

#### Recomendação

Retornar ao analista para fechar lacuna de auditoria e formalizar CAs.

---

### [148075](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148075) — SOS

| Campo | Valor |
| --- | --- |
| Sprint | Sprint 84 |
| Feature pai | — |
| Escopo desta análise | Sim |

#### Veredito

**Não pronta**

#### Checklist resumido

| Área | Status |
| --- | --- |
| Feature aprovada | ❌ — sem Feature |
| Estrutura US (escopo, RN, CA) | ❌ — descrição vazia |
| Revisão de requisitos | ❌ Rejeitada |
| Revisão técnica | Não realizada |
| Cobertura RN ↔ CA | ❌ |

#### Bloqueios

- Sem Feature de origem
- Sem escopo, regras ou critérios de aceite
- Estado New — item placeholder

#### Recomendação

Remover da sprint ou preencher especificação completa antes de qualquer estimativa.

---

### [148152](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148152) — Dashboard Operacional APPONTAI

| Campo | Valor |
| --- | --- |
| Sprint | Sprint 84 |
| Feature pai | — |
| Escopo desta análise | Sim |

#### Veredito

**Não pronta**

#### Checklist resumido

| Área | Status |
| --- | --- |
| Feature aprovada | ❌ — sem Feature |
| Estrutura US (escopo, RN, CA) | ❌ — descrição vazia |
| Revisão de requisitos | ❌ Rejeitada |
| Revisão técnica | Não realizada |
| Cobertura RN ↔ CA | ❌ |

#### Bloqueios

- Sem Feature de origem
- Sem escopo — Tasks filhas em execução (Frontend, APIs) sem especificação rastreável
- RG06 — Dev implementando sem US definida

#### Recomendação

Pausar tasks ou documentar US imediatamente; criar Feature se aplicável.

---

## Achados transversais

### Critérios de aceite (bloqueio sistêmico)

**Nenhuma** das 9 US possui critérios de aceite em formato **Dado/Quando/Então** (ou CA01, CA02…). Regras estão em prosa (“Como fazer”), o que impede validação objetiva pelo QA e aciona bloqueio automático do checklist.

### Decomposição e cobertura

| Cluster | USs | Risco |
| --- | --- | --- |
| Controle de Receitas | 145146 → 147345 → 110227 | Cadeia longa; três USs monolíticas; ordem de entrega crítica |
| Importação / Contrato | 147348 → 147943 | Dependem do cluster acima |
| Apponta | 145541, 148152 | 145541 razoável; 148152 sem spec |
| Tributação | 147969 | Lacuna RG06 pendente |

### Dependências entre sprints

- [148087](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148087) (Feature [147137](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147137)) está na **Sprint 83** com “Teste QA aprovado”, enquanto a Feature permanece alocada na Sprint 84 — revisar alocação no board.

### Inconsistências Feature ↔ US

- Todas as Features pai estão **Feature Aprovada** ✅
- Feature [147137](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147137) na sprint sem US no escopo — execução aparentemente concluída em sprint anterior

### Riscos para o sprint planning

1. **0/9 US prontas** — risco alto de retrabalho e bloqueios em QA
2. Cadeia Controle de Receitas pode serializar 3 USs grandes na mesma sprint
3. [148152](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148152) com dev ativo sem requisitos — dívida de especificação
4. Revisão técnica ausente em todas as US
5. Sprint também contém 22 bugs e 24 tasks — capacidade vs requisitos incompletos

### Candidatas a prontidão mais rápida (após refinamento mínimo)

| US | O que falta para Pronta |
| --- | --- |
| [145541](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145541) | CAs Dado/Quando/Então + revisão técnica |
| [147348](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147348) | CAs + desbloquear dependência [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146) |
| [147943](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147943) | CAs + cadeia de dependências |

---

## USs de contexto (fora do escopo, mesma Feature)

| US | Link | Sprint | Estado | Relevância para o escopo |
| --- | --- | --- | --- | --- |
| 148087 | [148087](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148087) | Sprint 83 | Teste QA aprovado | Feature [147137](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147137) está na Sprint 84 mas a US de execução já foi entregue/testada na sprint anterior |

---

## Próximos passos

1. **Compartilhar este relatório** com o facilitador do sprint planning antes da cerimônia.
2. **Remover ou especificar** [148075](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148075) e [148152](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148152).
3. **Fechar lacunas RG06** em [147345](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147345) e [147969](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147969) com negócio.
4. **Decompor** [110227](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/110227) e [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146).
5. **Formalizar CAs** (Dado/Quando/Então) em todas as US candidatas — começar por [145541](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145541).
6. **Executar tech-lead-reviewer** nas US que retornarem do analista.
7. **Revisar alocação** da Feature [147137](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147137) na Sprint 84.

---

## Anexo — Entrada da análise

```text
Modo: sprint
Parâmetros: Sprint 84 — Vix - GRLog
Organização: aguiabranca
Projeto: Vix - GRLog
Time: Vix - GRLog Team
Sprint ID: 440c74f6-90a5-4b6b-9bc8-c2c8d8f1cd03
Período: 2026-06-15 a 2026-06-30
USs resolvidas: 9
Features expandidas: 143425, 144922, 145543, 146808, 146830, 147420, 147496, 147137
USs de contexto incluídas: 148087
Parecer prévio: requirements-guidelines + parecer 110227/145146/147345
Revisão técnica: não realizada
Fonte: Azure DevOps (az boards query / az boards work-item show)
Política: somente leitura
Checklist: skills/delivery/sprint-readiness-reviewer/checklist.md
```
