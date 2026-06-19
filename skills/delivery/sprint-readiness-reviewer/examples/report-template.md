# Relatório de Prontidão para Sprint — {ESCOPO}

**Data:** {YYYY-MM-DD}  
**Projeto:** {PROJETO}  
**Escopo analisado:** {Sprint N | Lista de USs: 147776, 147777, …}  
**Gerado por:** sprint-readiness-reviewer

---

## Resumo executivo

| Métrica | Valor |
| --- | --- |
| USs no escopo | {N} |
| Prontas | {N} |
| Não prontas | {N} |
| Features envolvidas | {N} |
| Features aprovadas | {N} |
| Features com pendência | {N} |
| USs de contexto (outras sprints) | {N} |

**Recomendação geral:** {Incluir todas na sprint | Incluir parcialmente | Adiar sprint planning | Retornar ao analista}

---

## Contexto por Feature

> USs da mesma Feature podem estar distribuídas em sprints diferentes. Esta seção consolida o panorama completo da Feature, não apenas o recorte da sprint analisada.

### Feature [{ID}]({URL}) — {Título}

| Campo | Valor |
| --- | --- |
| Estado | {Feature Aprovada \| Feature Reprovada \| …} |
| USs no escopo desta análise | {lista com links} |
| USs da mesma Feature em outras sprints | {lista com links e sprint, ou "Nenhuma"} |
| USs da mesma Feature sem sprint | {lista ou "Nenhuma"} |

**Cobertura da Feature**

- RGs da Feature cobertas pelas USs do escopo: {sim/parcial/não — detalhar}
- Lacunas de decomposição identificadas: {descrição ou "Nenhuma"}
- Dependências entre USs (mesma Feature ou entre Features): {descrição ou "Nenhuma"}

---

## Detalhamento por User Story (escopo)

### [{ID}]({URL}) — {Título}

| Campo | Valor |
| --- | --- |
| Sprint | {Sprint 93 \| Backlog \| —} |
| Feature pai | [{ID}]({URL}) — {estado} |
| Escopo desta análise | {Sim — solicitada \| Não — contexto} |

#### Veredito

**{Pronta | Não pronta}**

#### Checklist resumido

| Área | Status |
| --- | --- |
| Feature aprovada | {✅ \| ❌ \| ⚠️ não confirmado} |
| Estrutura US (escopo, RN, CA) | {✅ \| ❌} |
| Revisão de requisitos | {✅ Aprovada \| ⚠️ Ressalvas \| ❌ Pendente} |
| Revisão técnica | {✅ \| ⚠️ \| ❌ \| Não realizada} |
| Cobertura RN ↔ CA | {✅ \| ❌ — detalhar} |

#### Bloqueios

- {bloqueio 1 — critério violado}
- {ou "Nenhum"}

#### Achados importantes

- {achado ou "Nenhum"}

#### Recomendação

{Incluir na sprint | Retornar ao analista | Aguardar Feature | Aguardar US irmã {ID}}

---

## Achados transversais

Consolidar o que só aparece ao olhar o conjunto (escopo + contexto):

### Decomposição e cobertura

- {Ex.: Feature 147726 tem 3 USs; apenas 1 está no escopo — RN05 sem CA em nenhuma US}

### Dependências entre sprints

- {Ex.: US 147776 depende de US 148606 (Feature 147517) ainda no backlog}

### Inconsistências Feature ↔ US

- {Ex.: Feature reprovada com US em desenvolvimento}

### Riscos para o sprint planning

- {lista}

---

## USs de contexto (fora do escopo, mesma Feature)

| US | Link | Sprint | Estado | Relevância para o escopo |
| --- | --- | --- | --- | --- |
| {ID} | [{ID}]({URL}) | {Sprint X} | {Estado} | {Por que importa para a análise} |

---

## Próximos passos

1. {ação prioritária}
2. {ação}
3. {Encaminhar relatório ao time antes do sprint planning}

---

## Anexo — Entrada da análise

```text
Modo: {sprint | lista de USs | sprint + filtros}
Parâmetros: {Sprint 93 | 147776, 147777}
USs resolvidas: {N}
Features expandidas: {IDs}
USs de contexto incluídas: {IDs}
```
