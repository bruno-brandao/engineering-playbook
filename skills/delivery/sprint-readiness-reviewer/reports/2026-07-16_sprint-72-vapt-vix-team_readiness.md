# Relatório de Prontidão para Sprint — Sprint 72 Vapt (Vix Team)

**Data:** 2026-07-16  
**Projeto:** [Vix](https://dev.azure.com/aguiabranca/Vix)  
**Time:** Vix Team  
**Produto / contexto:** Vapt (Jornada)  
**Sprint:** Sprint 72 (27/07/2026 – 07/08/2026) — **futura** (sprint atual do time: Sprint 71)  
**Escopo analisado:** todas as User Stories alocadas em `Vix\Sprint 72`  
**Gerado por:** sprint-readiness-reviewer  
**Base:** `product/us-guidelines.md` + checklist de prontidão (sem parecer prévio de requirements-reviewer / tech-lead-reviewer)

---

## Resumo executivo

| Métrica | Valor |
| --- | --- |
| Work items na sprint | 18 (10 US + 8 Task) |
| USs no escopo | 10 |
| **Prontas** | **0** |
| **Não prontas** | **10** |
| Features envolvidas | 2 ([150978](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/150978), [151015](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151015)) |
| Features aprovadas | **0** (ambas em `New`) |
| Features com pendência | 2 |
| USs sem Feature pai | 2 ([145507](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/145507), [149350](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149350)) |
| USs de contexto (outras sprints) | 0 |
| Story Points preenchidos | 0 / 10 |

**Recomendação geral:** **Não iniciar execução plena das USs na Sprint 72 até aprovação das Features e fechamento das lacunas.** Manter na sprint apenas o bloco operacional de **tasks de atualização de libs / documentação** (já em andamento) e, se necessário, a US [149350](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149350) já **Closed** como histórico — não como demanda nova.

Priorizar antes do planning:

1. Aprovar (ou explicitamente rejeitar) Features [150978](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/150978) e [151015](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151015).
2. Fechar dúvidas de negócio da [150979](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/150979).
3. Completar CA faltantes e anexar protótipos acessíveis nas USs de liderança.
4. Especificar ou retirar [145507](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/145507) (descrição vazia).

---

## Composição da sprint (visão geral)

| Tipo | Qtd | IDs |
| --- | --- | --- |
| User Story | 10 | [145507](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/145507), [149350](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149350), [150979](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/150979), [151017](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151017)–[151025](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151025), [151038](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151038) |
| Task | 8 | [149575](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149575)–[149580](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149580) (upgrade app), [149631](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149631), [149633](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149633) (wiki regras VAPT) |

**Observação:** as Features pai estão na **Sprint 71**, não na 72 — as USs de liderança/apontamento foram puxadas à frente da aprovação formal.

---

## Contexto por Feature

> USs da mesma Feature podem estar em sprints distintas. Esta seção consolida o panorama completo.

### Feature [150978](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/150978) — Desativação automática de apontamentos em workflow fechado

| Campo | Valor |
| --- | --- |
| Estado | `New` (board `New`) — **não aprovada** |
| Iteration | `Vix\Sprint 71` |
| USs no escopo | [150979](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/150979) |
| USs em outras sprints | Nenhuma |
| USs sem sprint | Nenhuma |

**Cobertura da Feature**

- Conteúdo da Feature: contexto/objetivo presentes; placeholders (`[Inserir ID]`, Epic vazio).
- Cobertura pelas USs: **parcial mas alinhada** — a US cobre o núcleo (validar fase + inativar + não recalcular).
- Lacunas: Feature não aprovada; dúvidas de negócio abertas na US (reativação de batidas tardias; valor de `responsavel_desativacao`).
- Dependências: API `/api/apontamentos`, modelo de período/workflow/jornada.

---

### Feature [151015](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151015) — Gestão dinâmica de aprovadores / liderança

| Campo | Valor |
| --- | --- |
| Estado | `New` (board `New`) — **não aprovada** |
| Iteration | `Vix\Sprint 71` |
| USs no escopo | [151017](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151017), [151019](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151019), [151021](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151021), [151022](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151022), [151023](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151023), [151025](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151025), [151038](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151038) |
| USs em outras sprints | Nenhuma |
| USs sem sprint | Nenhuma |

**Cobertura da Feature**

- Decomposição em 7 USs: **boa** (modelo → regras → UI → permissões → ações → WhatsApp).
- Protótipos na Feature: anexos ADO (OK). Em várias USs há links `file:///C:/Users/pauloferreira/...` — **inacessíveis** ao time.
- Ordem sugerida de dependência: **01 → 02 → 05 → 03/04/06**; **07** pode ser paralelo após 01 (hierarquia), mas é preparação — risco de escopo “meia entrega”.
- Feature não aprovada → bloqueio automático de todas as 7 USs.

---

## Detalhamento por User Story (escopo)

### [145507](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/145507) — Atualização das versões de libs e vulnerabilidades do front do backoffice

| Campo | Valor |
| --- | --- |
| Sprint | Sprint 72 |
| Feature pai | **Ausente** |
| Estado | Aguardando desenvolvimento |

#### Veredito

**Não pronta**

#### Checklist resumido

| Área | Status |
| --- | --- |
| Feature aprovada | ❌ sem Feature |
| Estrutura US (escopo, RN, CA) | ❌ descrição/AC vazios |
| Revisão de requisitos | ❌ Pendente |
| Revisão técnica | ❌ Não realizada |
| Cobertura RN ↔ CA | ❌ |

#### Bloqueios

- Sem Feature vinculada
- Sem escopo, RN e CA

#### Recomendação

Retornar ao analista — espelhar o padrão das tasks do app ([149575](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149575)+) ou escrever US completa; ou converter em Tasks.

---

### [149350](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149350) — Atualização das versões de libs e vulnerabilidades do app

| Campo | Valor |
| --- | --- |
| Sprint | Sprint 72 |
| Feature pai | **Ausente** |
| Estado | **Closed** |

#### Veredito

**Não pronta** (para nova entrega) — item já **fechado**

#### Checklist resumido

| Área | Status |
| --- | --- |
| Feature aprovada | ❌ sem Feature |
| Estrutura US (escopo, RN, CA) | ❌ descrição vazia |
| Trabalho operacional | ⚠️ coberto pelas Tasks 149575–149580 |

#### Bloqueios

- US Closed sem especificação; prontidão de requisitos irrelevante para reabertura

#### Recomendação

Tratar como **histórico**. Planejar capacidade pelas **Tasks** filhas/relacionadas, não pela US.

---

### [150979](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/150979) — US-FEAT-APONTAMENTO-WORKFLOW-FECHADO-01

| Campo | Valor |
| --- | --- |
| Sprint | Sprint 72 |
| Feature pai | [150978](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/150978) — `New` |
| Estado | New / Backlog |

#### Veredito

**Não pronta**

#### Checklist resumido

| Área | Status |
| --- | --- |
| Feature aprovada | ❌ Feature `New` |
| Estrutura US (escopo, RN, CA) | ✅ RN01–03 + CA01–03 + exemplos |
| Revisão de requisitos | ⚠️ conteúdo bom, mas lacunas explícitas abertas |
| Revisão técnica | ❌ Não realizada |
| Cobertura RN ↔ CA | ✅ |

#### Bloqueios

- Feature não aprovada
- Dúvidas de negócio **não resolvidas** (reativação de batidas tardias; string vs ID de `SISTEMA`)
- Sem story points / parecer técnico

#### Achados importantes

- Qualidade textual acima da média do backlog — boa base após aprovação e fechamento das lacunas
- CA03 deixa ambíguo se batida inativa “some” ou “aparece marcada” no espelho

#### Recomendação

Aguardar Feature + PO nas lacunas; depois tech-lead-reviewer (impacto no motor de apuração).

---

### [151017](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151017) — GESTAO-LIDERANCA-01 (modelo / view / job SAP)

| Campo | Valor |
| --- | --- |
| Feature pai | [151015](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151015) — `New` |

#### Veredito

**Não pronta**

#### Checklist

| Área | Status |
| --- | --- |
| Feature aprovada | ❌ |
| Estrutura | ✅ escopo + RN + CA |
| Cobertura RN ↔ CA | ❌ RN04 (carga inicial) e RN05 (job demissão) **sem CA** |

#### Bloqueios

- Feature não aprovada; RN04/RN05 sem CA; specs técnicas embutidas (SQL) misturam camada US/Feature

#### Recomendação

Aguardar Feature; acrescentar CA para carga inicial e rotina diária; validar view recursiva com tech lead (ciclos / performance).

---

### [151019](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151019) — GESTAO-LIDERANCA-02 (associação / transferência)

#### Veredito

**Não pronta**

| Área | Status |
| --- | --- |
| Feature aprovada | ❌ |
| Estrutura | ✅ |
| Cobertura RN ↔ CA | ⚠️ RN04 (transferência coletiva de demitido) só parcialmente coberta por CA03 (substituição) |

#### Bloqueios

- Feature não aprovada; falta CA dedicado ao fluxo de transferência coletiva (RN04)

#### Recomendação

Aguardar Feature; alinhar CA ao fluxo completo de transferência.

---

### [151021](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151021) — GESTAO-LIDERANCA-05 (permissionamento)

#### Veredito

**Não pronta**

| Área | Status |
| --- | --- |
| Feature aprovada | ❌ |
| Estrutura | ✅ RN01–03 / CA01–03 |
| Cobertura RN ↔ CA | ⚠️ RN02 (self-service) e RN03 (auditoria do parâmetro) **sem CA explícito** |

#### Bloqueios

- Feature não aprovada; impacto transversal em todas as telas de ponto — exige revisão técnica obrigatória

#### Recomendação

Aguardar Feature + tech-lead-reviewer (modo híbrido / risco de regressão de permissão).

---

### [151022](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151022) — GESTAO-LIDERANCA-03 (painel / filtros / export)

#### Veredito

**Não pronta**

| Área | Status |
| --- | --- |
| Feature aprovada | ❌ |
| Estrutura | ✅ |
| Artefatos | ❌ protótipos `file://` locais inacessíveis |
| Cobertura RN ↔ CA | ⚠️ filtros/chips/PDF assíncrono (>500) pouco cobertos pelos 3 CAs |

#### Bloqueios

- Feature não aprovada; protótipos locais; volume de UI alto para 3 CAs

#### Recomendação

Trocar links por anexos ADO (como na Feature); expandir CAs de filtros e export PDF.

---

### [151023](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151023) — GESTAO-LIDERANCA-04 (árvore)

#### Veredito

**Não pronta**

| Área | Status |
| --- | --- |
| Feature aprovada | ❌ |
| Estrutura | ✅ |
| Cobertura RN ↔ CA | ❌ RN04 (busca e destaque) **sem CA** |
| Artefatos | ❌ `file://` local |

#### Bloqueios

- Feature não aprovada; CA de busca ausente; protótipo inacessível

---

### [151025](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151025) — GESTAO-LIDERANCA-06 (menu de contexto)

#### Veredito

**Não pronta**

| Área | Status |
| --- | --- |
| Feature aprovada | ❌ |
| Estrutura | ✅ (5 RNs, 2 CAs) |
| Cobertura RN ↔ CA | ❌ várias ações do menu sem CA dedicado |
| Artefatos | ❌ `file://` local |

#### Bloqueios

- Feature não aprovada; RN ↔ CA incompleta; depende de 01–03

---

### [151038](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151038) — GESTAO-LIDERANCA-07 (preparação WhatsApp)

#### Veredito

**Não pronta**

| Área | Status |
| --- | --- |
| Feature aprovada | ❌ |
| Estrutura | ✅ escopo “preparação” + RNs de fluxo |
| Escopo | ⚠️ mistura preparação de arquitetura com fluxos completos de bot (risco de escopo inchado) |
| Cobertura RN ↔ CA | ⚠️ 4 RNs / 2 CAs |

#### Bloqueios

- Feature não aprovada; fronteira “preparação” vs “integração WhatsApp” ambígua para Dev/QA
- Dependência forte de hierarquia (US-01) e de `PERMITE_GERAR_PIN`

#### Recomendação

Aguardar Feature; delimitar entrega (só fila/schema vs bot end-to-end) antes do planning.

---

## Achados transversais

### Decomposição e cobertura

- Feature [151015](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151015) está bem decomposta em 7 USs, mas **todas** entraram na mesma sprint futura com Feature ainda `New` — anti-padrão do playbook (US só após Feature aprovada).
- Várias USs têm **mais RNs do que CAs** (01, 02, 04, 05, 06, 07).

### Dependências entre sprints / itens

- Features na Sprint **71**; USs na **72** — planning da 72 depende de aprovação ainda na 71.
- Bloco de libs: US [149350](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149350) Closed + Tasks [149575](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149575)–[149580](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149580); backoffice [145507](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/145507) sem espelhamento.
- [151021](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151021) (permissionamento) é **ponto único de risco** para regressão em todo o Vapt.

### Inconsistências Feature ↔ US

- Features `New` com USs já na sprint.
- Protótipos OK na Feature ADO; quebrados (`file://`) nas USs 03/04/06.
- Nomenclatura “Liderança” vs “Aprovadores de Ponto” oscila entre Feature e USs.

### Riscos para o sprint planning

| Risco | Severidade |
| --- | --- |
| Nenhuma US pronta pelo checklist | Alta |
| Feature [151015](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151015) = 7 USs sem SP | Alta (capacidade) |
| Permissionamento híbrido sem revisão técnica | Alta |
| WhatsApp “preparação” pode virar integração completa | Média |
| US [145507](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/145507) vazia | Média |
| Tasks de docs VAPT sem vínculo a Feature/US de produto | Baixa (ok se trabalho transversal) |

---

## USs de contexto (fora do escopo, mesma Feature)

Nenhuma — todas as USs filhas das Features envolvidas já estão na Sprint 72.

---

## Tasks na sprint (sem veredito de prontidão de US)

| ID | Título | Estado | Nota |
| --- | --- | --- | --- |
| [149575](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149575) | Migrar stack base Expo/RN/React | Active | Única task Active |
| [149576](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149576)–[149580](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149580) | Libs, builds, regressão, rollout | New | Pacote de upgrade do app |
| [149631](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149631), [149633](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/149633) | Wiki / manutenção regras VAPT | New | Documentação |

Esses itens podem seguir no planning como **capacidade operacional**, independentemente das USs de Feature.

---

## Próximos passos

1. **Negócio / PO:** aprovar ou devolver Features [150978](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/150978) e [151015](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151015).
2. **Analista:** fechar lacunas da [150979](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/150979); completar CAs faltantes nas USs 01–07; corrigir anexos de protótipo; especificar [145507](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/145507).
3. **Tech Lead:** revisar [151017](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151017) (view/job), [151021](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151021) (permissionamento) e [151038](https://dev.azure.com/aguiabranca/Vix/_workitems/edit/151038) (fronteira WhatsApp).
4. **Planning Sprint 72:** priorizar Tasks de upgrade + docs; só puxar USs de Feature após estados aprovados e checklist verde.
5. Encaminhar este relatório ao facilitador do sprint planning.

---

## Anexo — Entrada da análise

```text
Modo: sprint
Parâmetros: Sprint 72 | Projeto Vix | Time Vix Team | contexto Vapt
USs resolvidas: 10
Features expandidas: 150978, 151015
USs de contexto incluídas: (nenhuma)
Tasks observadas: 8
Pareceres prévios: nenhum
```
