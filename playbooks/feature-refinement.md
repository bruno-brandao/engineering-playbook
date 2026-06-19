# Feature Refinement

Playbook para conduzir o refinamento de uma Feature com o negócio até obter aprovação formal — pré-requisito para decomposição em User Stories.

---

## Objetivo

Garantir que a Feature esteja completa, sem ambiguidades e aprovada pelo negócio antes que o time inicie a criação de User Stories.

Ao final deste playbook, a Feature deve estar pronta para a skill [requirements-analyst](../skills/product/requirements-analyst/SKILL.md) ou para decomposição manual pelo analista.

---

## Pré-requisitos

| Item | Descrição |
| --- | --- |
| Problema entendido | Contexto de negócio e objetivo da entrega definidos (ver [product-discovery.md](product-discovery.md)) |
| Feature rascunhada | Documento da Feature iniciado com identificador (ex.: `FEAT-XXX`) |
| Participantes confirmados | Analista, representante de negócio e, quando aplicável, desenvolvimento e QA |
| Artefatos iniciais | Protótipos, fluxos ou referências disponíveis para discussão |

---

## Papéis

| Papel | Responsabilidade neste playbook |
| --- | --- |
| **Facilitador (Analista)** | Conduz a sessão, registra decisões e atualiza a Feature |
| **Negócio** | Esclarece regras, valida comportamentos e aprova a Feature |
| **Desenvolvimento** | Sinaliza riscos técnicos, dependências e lacunas de implementação |
| **QA** | Antecipa cenários de teste e questiona ambiguidades nos critérios |

---

## Entradas

* Rascunho da Feature com objetivo de negócio;
* Requisitos funcionais preliminares;
* Protótipos, fluxos ou mockups (quando existirem);
* Dúvidas e pendências registradas em sessões anteriores.

---

## Saídas

* Feature atualizada e versionada;
* Registro de decisões e pendências resolvidas;
* **Aprovação formal do negócio** registrada na Feature;
* Feature pronta para decomposição em User Stories.

---

## Passos

### 1. Abertura (5 min)

* Confirmar objetivo da sessão e escopo da Feature.
* Revisar participantes e tempo disponível.
* Listar pendências da sessão anterior (se houver).

### 2. Revisão do objetivo de negócio (10 min)

Validar com o negócio:

* Qual problema a Feature resolve?
* Qual o resultado esperado para o usuário ou para o negócio?
* O que **não** está no escopo desta Feature?

**Critério de saída:** objetivo compreendido por todos e escopo delimitado.

### 3. Revisão de requisitos e regras de negócio (20–40 min)

Percorrer cada requisito funcional e regra de negócio. Para cada item, verificar:

* Existe apenas uma interpretação possível?
* Há exemplos para cálculos, datas, ordenações, aprovações ou integrações?
* Existem conflitos entre regras?

Registrar dúvidas que não puderem ser resolvidas na sessão como **pendência** com responsável e prazo.

**Critério de saída:** regras documentadas ou pendências explicitamente registradas.

### 4. Revisão de fluxos e protótipos (15–20 min)

* Validar fluxos principais e alternativos (erro, cancelamento, permissões).
* Conferir se protótipos refletem as regras acordadas.
* Identificar lacunas visuais ou de fluxo.

**Critério de saída:** fluxos e artefatos alinhados com as regras de negócio.

### 5. Antecipação técnica e de testes (10–15 min)

Com desenvolvimento e QA presentes (ou de forma assíncrona):

* Há dependências técnicas ou integrações externas?
* Existem restrições de performance, segurança ou compliance?
* Os cenários de teste são identificáveis a partir da Feature?

**Critério de saída:** riscos e dependências registrados na Feature ou em observações.

### 6. Checklist de completude da Feature

Antes de solicitar aprovação, confirmar que a Feature contém:

- [ ] Identificador (`FEAT-XXX`)
- [ ] Objetivo de negócio
- [ ] Requisitos funcionais
- [ ] Regras de negócio (sem ambiguidade)
- [ ] Fluxos descritos ou referenciados
- [ ] Protótipos ou artefatos vinculados por link
- [ ] Pendências resolvidas ou com prazo definido
- [ ] Escopo explícito (o que está fora)

Referência: conteúdo mínimo definido em [us-guidelines.md](../product/us-guidelines.md#feature).

### 7. Aprovação do negócio (5 min)

* Apresentar resumo das decisões da sessão.
* Solicitar aprovação formal do representante de negócio.
* Registrar na Feature: data, responsável e status **Aprovada**.

**Sem aprovação registrada, não iniciar decomposição em User Stories.**

### 8. Encerramento e próximos passos (5 min)

* Comunicar que a próxima etapa é a decomposição em User Stories.
* Indicar responsável (analista) e prazo.
* Opcional: usar a skill [requirements-analyst](../skills/product/requirements-analyst/SKILL.md) com apoio de IA.

---

## Critérios de conclusão

O refinamento está concluído quando **todos** os itens abaixo forem verdadeiros:

1. A Feature atende ao checklist de completude (passo 6).
2. Não há pendências bloqueantes sem responsável e prazo.
3. O negócio registrou aprovação formal na Feature.
4. Artefatos complementares estão referenciados por link.

---

## O que fazer após a aprovação

| Próxima etapa | Responsável | Referência |
| --- | --- | --- |
| Decompor Feature em User Stories | Analista | [requirements-analyst](../skills/product/requirements-analyst/SKILL.md) |
| Registrar USs no backlog | Analista | [us-template.md](../product/us-template.md) |
| Planejar sprint | Time | [sprint-planning.md](sprint-planning.md) (quando disponível) |

---

## Quando retornar a este playbook

* Mudança relevante de escopo após aprovação → nova versão da Feature e nova rodada de refinamento.
* Pendência bloqueante resolvida → sessão focada apenas nos itens pendentes.
* Conflito identificado durante decomposição em USs → retornar ao passo 3 com negócio.

Alterações na Feature após USs criadas devem seguir [us-guidelines.md](../product/us-guidelines.md): gerar novas Issues ou novas User Stories, não alterar USs já em desenvolvimento sem acordo.

---

## Dicas para o facilitador

* Priorize eliminar ambiguidade — uma regra com duas interpretações bloqueia desenvolvimento e QA.
* Use exemplos concretos na hora; documente-os na Feature.
* Limite a sessão a uma Feature por vez quando a complexidade for alta.
* Registre decisões no próprio documento da Feature, não apenas em ata de reunião.
