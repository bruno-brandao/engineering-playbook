# Checklist — Sprint Readiness Reviewer

## Feature de origem

- [ ] Feature identificada (ID ou link)
- [ ] Feature em estado aprovado (ex.: *Feature Aprovada*)
- [ ] Escopo da US contido na Feature

## User Story — definição de pronto

Conforme [us-guidelines.md](../../../product/us-guidelines.md):

- [ ] Referência à Feature preenchida
- [ ] Escopo definido
- [ ] Regras de Negócio definidas
- [ ] Critérios de Aceite definidos (Dado/Quando/Então)
- [ ] Artefatos necessários referenciados

## Qualidade (revisão prévia)

- [ ] Parecer do requirements-reviewer **Aprovada** ou **Aprovada com ressalvas** — ou revisão manual equivalente
- [ ] Parecer do tech-lead-reviewer **Aprovada tecnicamente** ou **Aprovada com ressalvas** — ou revisão técnica manual equivalente
- [ ] Sem achados bloqueantes pendentes
- [ ] Cobertura RN ↔ CA verificada (cada RN relevante possui CA)

## Execução

- [ ] Dependências externas identificadas
- [ ] Sem lacunas funcionais não sinalizadas
- [ ] Dúvidas para o negócio resolvidas ou explicitamente aceitas para a sprint

## Bloqueios automáticos

Marcar **Não pronta** se qualquer item abaixo for verdadeiro:

* Feature não aprovada
* US sem critérios de aceite
* Parecer do reviewer = *Requer revisão* ou *Rejeitada*
* Parecer do tech-lead-reviewer = *Requer esclarecimentos* ou *Bloqueada tecnicamente*
* RN relevante sem CA correspondente
