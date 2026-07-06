# Análise de Requisitos — Sprint 84 GRLog

**Data:** 2026-06-22  
**Projeto:** [Vix - GRLog](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog)  
**Time:** Vix - GRLog Team  
**Sprint:** Sprint 84 (15/06/2026 – 30/06/2026)  
**Base de avaliação:** [us-guidelines.md](../../../../product/us-guidelines.md)  
**Escopo da análise:** qualidade de requisitos das User Stories — **sem** critérios de template (`us-template.md` / `feature-template.md`)

---

## Resumo executivo

| Métrica | Valor |
| --- | --- |
| User Stories na sprint | 9 |
| Features na sprint | 7 |
| Bugs | 22 |
| Tasks | 24 |
| USs aprovadas com ressalvas | 4 |
| USs que requerem revisão | 3 |
| USs bloqueantes (rejeitadas) | 2 |
| Prontidão estimada (guideline) | ~44% (4/9) |

**Recomendação geral:** não considerar a sprint pronta para execução plena de requisitos. Priorizar refinamento de [110227](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/110227), [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146) e [147345](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147345); resolver [148075](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148075) e [148152](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148152); definir US para a Feature [147137](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147137).

---

## Critérios aplicados

A análise utilizou exclusivamente o guideline de User Stories:

| Área | Critério |
| --- | --- |
| Princípios | Rastreabilidade com Feature, objetividade, eliminação de ambiguidade, US não replicar a Feature inteira |
| RG01 | Não deixar espaço para interpretação |
| RG02 | Evitar regras genéricas |
| RG03 | Descrever comportamentos esperados |
| RG04 | Utilizar exemplos em funcionalidades complexas |
| RG05 | Documentar casos de exceção |
| RG06 | O desenvolvedor não deve precisar adivinhar |
| Decomposição | Complexidade, regras independentes, validação separada, paralelismo |
| Definição de pronto | Escopo, regras, critérios testáveis, artefatos referenciados, exemplos quando aplicável |

---

## Composição da sprint

### User Stories por estado

| Estado | Qtd | IDs |
| --- | --- | --- |
| Aguardando desenvolvimento | 7 | 110227, 145146, 145541, 147345, 147348, 147943, 147969 |
| New | 2 | 148075, 148152 |

### Features na sprint

| ID | Estado | Título |
| --- | --- | --- |
| [143425](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/143425) | Feature Aprovada | Controle de Receita — Integração com o fluxo da medição |
| [144922](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/144922) | Feature Aprovada | Controle de Receitas — Melhorias na Tela Controle de Receitas |
| [145543](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145543) | Feature Aprovada | Apponta — Sincronização — Realizar Pré-Carregamento Automático |
| [146808](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/146808) | Feature Aprovada | Controle de Receitas — Carga única de Parametrizações nos Controles Fechados |
| [146830](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/146830) | Feature Aprovada | Medição — Alteração no modelo de Importação de Valores Faturados |
| [147137](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147137) | Feature Aprovada | Cliente e Empresas do Grupo — Adequação CNPJ Alfanumérico |
| [147420](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147420) | Feature Aprovada | Contrato — Alteração de Regras — Aba Dados Financeiro e Histórico Faturamento |
| [147496](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147496) | Feature Aprovada | Medição — Tabela de Preços — Adequação do Cadastro de Tributação |

---

## Resultado por User Story

### Aprovadas com ressalvas

#### [145541](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145541) — Apponta — Pré-Carregamento Automático

| Campo | Valor |
| --- | --- |
| Feature pai | [145543](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145543) — Feature Aprovada |
| Estado | Aguardando desenvolvimento |
| Replicação da Feature | ~58% |

**Pontos positivos**

- Gatilho claro: disparo automático após sincronização no aplicativo.
- Janela de 24h para verificação de pré-carregamento por centro de custo.
- Mensagens MSG01 e MSG02 definidas para falha e CR divergente.
- Falha automática não deve impactar o uso do aplicativo.

**Achados**

| Severidade | Achado | Critério |
| --- | --- | --- |
| Importante | Permissão descrita de forma genérica (“usuário com permissão de edição/criação”) | RG02 |
| Sugestão | Não há exemplo de sequência com múltiplos CRs em 24h | RG04 |

**Recomendação:** incluir na sprint após detalhar permissão específica.

---

#### [147348](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147348) — Importação de Valores Faturados

| Campo | Valor |
| --- | --- |
| Feature pai | [146830](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/146830) — Feature Aprovada |
| Estado | Aguardando desenvolvimento |
| Replicação da Feature | ~57,5% |

**Pontos positivos**

- Escopo contido: novas colunas Tributação, Alíquota e Situação no CSV.
- Formato de campos definido (texto 5 chars, decimal 3,2, lista EMITIDO/CANCELADO).
- Dependência explícita com [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146).

**Achados**

| Severidade | Achado | Critério |
| --- | --- | --- |
| Importante | “Conforme descrito na história #145146” delega entendimento a outro item | RG01, RG02 |
| Sugestão | Sem exemplo de linha CSV válida/inválida | RG04 |

**Recomendação:** incluir na sprint após explicitar regra espelhada da #145146 nesta US.

---

#### [147943](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147943) — Contrato — Dados Financeiro e Histórico Faturamento

| Campo | Valor |
| --- | --- |
| Feature pai | [147420](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147420) — Feature Aprovada |
| Estado | Aguardando desenvolvimento |
| Replicação da Feature | ~39,1% |

**Pontos positivos**

- Regra objetiva para registros com situação “Cancelado”.
- Link para protótipo Figma.
- Escopo parcial em relação à Feature.

**Achados**

| Severidade | Achado | Critério |
| --- | --- | --- |
| Importante | Toca três áreas (Dados Financeiros, Histórico Faturamento, Controle de Receita) — risco de decomposição insuficiente | Decomposição |
| Sugestão | Integração com importação sem cenários de erro documentados | RG05 |

**Recomendação:** incluir com atenção à ordem de entrega em relação à #147348.

---

#### [147969](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147969) — Tabela de Preços — Cadastro de Tributação

| Campo | Valor |
| --- | --- |
| Feature pai | [147496](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147496) — Feature Aprovada |
| Estado | Aguardando desenvolvimento |
| Replicação da Feature | ~87% |

**Pontos positivos**

- Exemplo concreto de sobreposição de vigência (linhas ISS com MSG05).
- Mensagens MSG01–MSG06 definidas.
- Link para protótipo Figma.
- Regras de accordion, vigência e ações por linha detalhadas.

**Achados**

| Severidade | Achado | Critério |
| --- | --- | --- |
| Bloqueante | “Validar equipe o que será detalhado nessa ação” na auditoria | RG06 |
| Importante | Impacto em medição sem exemplo numérico de reprocessamento | RG04 |
| Sugestão | Escopo em duas telas (Tabela de Preços e Operação) — avaliar decomposição | Decomposição |

**Recomendação:** retornar ao analista para fechar lacuna de auditoria antes do desenvolvimento.

---

### Requerem revisão

#### [110227](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/110227) — Integração Medição → Controle de Receitas

| Campo | Valor |
| --- | --- |
| Feature pai | [143425](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/143425) — Feature Aprovada |
| Estado | Aguardando desenvolvimento |
| Replicação da Feature | ~117,9% |

**Achados**

| Severidade | Achado | Critério |
| --- | --- | --- |
| Bloqueante | Replica praticamente a Feature inteira | Princípio — não replicar integralmente |
| Bloqueante | Complexidade alta: rotina diária + CUT OFF + consolidação + múltiplos tipos de cálculo | Decomposição |
| Importante | Termos “conforme parametrizações”, “conforme detalhado”, “conforme descrito” | RG02 |
| Importante | Cenários de cálculo sem exemplos numéricos | RG04 |

**Recomendação:** decompor em pelo menos três entregas: (a) rotina diária de integração por medição, (b) regras CUT OFF, (c) consolidação por operação/contrato.

---

#### [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146) — Melhorias na Tela Controle de Receitas

| Campo | Valor |
| --- | --- |
| Feature pai | [144922](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/144922) — Feature Aprovada |
| Estado | Aguardando desenvolvimento |
| Replicação da Feature | ~81,5% |

**Achados**

| Severidade | Achado | Critério |
| --- | --- | --- |
| Bloqueante | Escopo amplo: layout, permissões, flags, grid, nova aba, recálculo de colunas, integração | Decomposição |
| Importante | Replica ~82% da Feature | Princípio — não replicar integralmente |
| Importante | Recálculo “Receita a Provisionar = Total − Receita Emitida” sem exemplos | RG04 |

**Recomendação:** decompor em: (a) permissões/layout/flags, (b) aba Histórico espelhada, (c) recálculo de colunas e integração com importação.

---

#### [147345](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147345) — Carga única de Parametrizações

| Campo | Valor |
| --- | --- |
| Feature pai | [146808](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/146808) — Feature Aprovada |
| Estado | Aguardando desenvolvimento |
| Replicação da Feature | ~95,9% |

**Achados**

| Severidade | Achado | Critério |
| --- | --- | --- |
| Bloqueante | “Validar com equipe” — chave composta de unicidade | RG06 |
| Bloqueante | “Validar com equipe” — usuário registrado na auditoria | RG06 |
| Importante | Replica ~96% da Feature | Princípio — não replicar integralmente |
| Importante | Carga CSV sem exemplos de arquivo válido/inválido | RG04 |

**Recomendação:** retornar ao analista e negócio antes de iniciar desenvolvimento.

---

### Rejeitadas (bloqueantes)

#### [148075](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148075) — SOS

| Campo | Valor |
| --- | --- |
| Feature pai | — |
| Estado | New |

**Achados**

| Severidade | Achado | Critério |
| --- | --- | --- |
| Bloqueante | Sem descrição | Definição de pronto |
| Bloqueante | Sem escopo, regras ou critérios testáveis | Definição de pronto |
| Bloqueante | Sem rastreabilidade com Feature | Princípio |

**Recomendação:** preencher especificação ou remover da sprint.

---

#### [148152](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148152) — Dashboard Operacional APPONTAI

| Campo | Valor |
| --- | --- |
| Feature pai | — |
| Estado | New |

**Achados**

| Severidade | Achado | Critério |
| --- | --- | --- |
| Bloqueante | Sem descrição | Definição de pronto |
| Bloqueante | Tasks filhas em execução sem especificação rastreável | RG06, Rastreabilidade |

**Recomendação:** documentar escopo e regras ou pausar tasks até haver especificação.

---

## Feature sem User Story na sprint

### [147137](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147137) — CNPJ Alfanumérico

| Campo | Valor |
| --- | --- |
| Estado | Feature Aprovada |
| US vinculada na sprint | Nenhuma |

**Achados na Feature**

| Severidade | Achado | Critério |
| --- | --- | --- |
| Bloqueante | Sem US de execução na sprint | Princípio |
| Importante | “Validar se o sistema está aceitando os dois formatos” | RG02 |
| Importante | “Validar corretamente os 12 dígitos iniciais” | RG02 |
| Importante | Impacto em “todas as telas e relatórios” sem decomposição | Decomposição |

**Recomendação:** criar US(s) decompostas por módulo/tela ou retirar da sprint.

---

## Achados transversais

### Replicação Feature → US

| US | % do conteúdo da Feature |
| --- | --- |
| 110227 | 117,9% |
| 147345 | 95,9% |
| 147969 | 87,0% |
| 145146 | 81,5% |
| 145541 | 58,0% |
| 147348 | 57,5% |
| 147943 | 39,1% |

Três US replicam praticamente a Feature inteira, violando o princípio de escopo objetivo por entrega.

### Termos genéricos recorrentes (RG02)

Padrão repetido em quase todas as US:

> Usuário que tenha permissão de edição/criação da tela associado ao Grupo de Acesso, por Centro de Custo por CR

Sem indicar qual permissão, qual tela e qual comportamento quando negada.

### Lacunas abertas (RG06)

| Item | Lacuna |
| --- | --- |
| 147345 | Unicidade da chave composta; usuário na auditoria |
| 147969 | Detalhamento da ação Histórico na aba do item |
| 147137 | Escopo “todas as telas” sem lista fechada |

### Exemplos de negócio (RG04)

| Com exemplos | Sem exemplos (deveria ter) |
| --- | --- |
| 147969 (sobreposição de vigência) | 110227 (cálculos CUT OFF / consolidação) |
| | 147345 (linhas CSV válidas/inválidas) |
| | 145146 (recálculo Receita a Provisionar vs Emitida) |

### Rastreabilidade

- 7/9 US com parent Feature vinculado.
- 148075 e 148152 sem parent e sem conteúdo.
- Dependência cruzada 147348 → 145146 documentada.

### Decomposição recomendada

| Item | Motivo |
| --- | --- |
| 110227 | Rotina batch + parametrização + CUT OFF + consolidação |
| 145146 | UI + permissões + nova aba + recálculo + integração |
| 147969 | Accordion + vigência + duas telas + histórico/auditoria |
| 147137 | Impacto sistêmico em múltiplas telas/relatórios/banco |

---

## Veredito consolidado

| Classificação | Qtd | IDs |
| --- | --- | --- |
| Aprovada com ressalvas | 4 | 145541, 147348, 147943, 147969 |
| Requer revisão | 3 | 110227, 145146, 147345 |
| Rejeitada | 2 | 148075, 148152 |

---

## Próximos passos

1. **Bloqueantes:** preencher ou remover [148075](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148075) e [148152](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/148152).
2. **Negócio:** fechar lacunas de [147345](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147345) e [147969](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147969).
3. **Analista:** decompor [110227](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/110227) e [145146](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/145146).
4. **Backlog:** criar US para [147137](https://dev.azure.com/aguiabranca/Vix%20-%20GRLog/_workitems/edit/147137) ou retirar da sprint.
5. **Quick wins:** substituir termos genéricos de permissão; adicionar exemplos numéricos nos fluxos de cálculo.

---

## Anexo — Entrada da análise

```text
Modo: sprint
Projeto: Vix - GRLog
Organização: aguiabranca
Sprint: Sprint 84 (440c74f6-90a5-4b6b-9bc8-c2c8d8f1cd03)
Período: 2026-06-15 a 2026-06-30
Guideline: product/us-guidelines.md
Templates excluídos: us-template.md, feature-template.md
USs analisadas: 110227, 145146, 145541, 147345, 147348, 147943, 147969, 148075, 148152
Features analisadas: 143425, 144922, 145543, 146808, 146830, 147137, 147420, 147496
Fonte: Azure DevOps (az boards query / az boards work-item show)
Política: somente leitura — alterações a aplicar manualmente
```
