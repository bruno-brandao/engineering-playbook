# Product Discovery

Playbook para conduzir a descoberta inicial de um problema ou oportunidade — antes da elaboração formal da Feature.

---

## Objetivo

Garantir que o time compreenda o problema, o valor de negócio e o escopo preliminar antes de investir na escrita de uma Feature.

---

## Pré-requisitos

| Item | Descrição |
| --- | --- |
| Demanda identificada | Iniciativa, solicitação de negócio ou problema reportado |
| Stakeholder disponível | Representante que esclareça o contexto de negócio |
| Facilitador designado | Analista ou PM responsável pela condução |

---

## Papéis

| Papel | Responsabilidade |
| --- | --- |
| **Facilitador** | Conduz a sessão e registra decisões |
| **Negócio** | Explica o problema, valor e restrições |
| **Engenharia** | Avalia viabilidade preliminar e riscos |
| **QA** | Antecipa impactos em qualidade e testes |

---

## Entradas

* Descrição inicial da demanda (e-mail, iniciativa, ticket);
* Dados ou evidências do problema (quando existirem);
* Restrições conhecidas (prazo, compliance, integrações).

---

## Saídas

* Problema e objetivo documentados;
* Escopo preliminar delimitado;
* Decisão: **prosseguir para Feature** ou **retornar / descartar**;
* Rascunho ou backlog item para elaboração da Feature.

---

## Passos

### 1. Entender o problema (15–20 min)

* Qual dor ou oportunidade estamos endereçando?
* Quem é impactado?
* O que acontece hoje sem essa entrega?
* Existe evidência (volume, custo, reclamações)?

**Critério de saída:** problema articulado em uma ou duas frases.

### 2. Definir o valor de negócio (10 min)

* Qual resultado mensurável esperamos?
* Como saberemos que deu certo?
* Qual a prioridade em relação a outras demandas?

### 3. Delimitar escopo preliminar (15 min)

* O que está **dentro** desta entrega?
* O que está **explicitamente fora**?
* Há dependências de outros times ou sistemas?

### 4. Avaliar viabilidade preliminar (10 min)

Com engenharia presente:

* Existe solução conhecida ou é exploratória?
* Há riscos técnicos evidentes?
* Estimativa de ordem de grandeza (pequena / média / grande)?

### 5. Decidir próximo passo (5 min)

| Decisão | Ação |
| --- | --- |
| Prosseguir | Criar ou atualizar Feature e agendar [feature-refinement.md](feature-refinement.md) |
| Informação insuficiente | Registrar pendências com responsável e prazo |
| Não prosseguir | Documentar motivo e arquivar demanda |

---

## Critérios de conclusão

1. Problema e objetivo documentados.
2. Escopo preliminar definido (incluindo o que está fora).
3. Decisão registrada sobre prosseguir ou não.
4. Se prosseguir: Feature criada ou item encaminhado para elaboração.

---

## Próxima etapa

[feature-refinement.md](feature-refinement.md) — refinamento e aprovação da Feature com o negócio.
