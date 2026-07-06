# Plano de Implementação — {US-ID}

## Validação de contexto

{validation_section}

## Resumo

{2-3 frases}

## Repos impactados

| Repo | Status | Branch | Notas |
| --- | --- | --- | --- |
| {repo} | active/legacy | {branch} | {notas} |

## Mapeamento RN → CA → Tarefas

| RN | CA | Tarefa técnica | Repo | Origem |
| --- | --- | --- | --- | --- |
| RN01 | CA01 | {tarefa} | {repo} | [KB @ sha] / [Código] |

## Plano por fases

### Fase 1 — Dados / contratos

- [ ] {tarefa}

### Fase 2 — Backend / domínio

- [ ] {tarefa}

### Fase 3 — Integração

- [ ] {tarefa}

### Fase 4 — UI (se aplicável)

- [ ] {tarefa}

## Arquivos / nós KB prováveis

- [[{NodeId}]] — {descrição} `[KB @ {commit}]`

## Riscos e impactos não previstos

| Risco | Severidade | Mitigação |
| --- | --- | --- |
| {risco} | Alta/Média | {ação} |

## Premissas e perguntas abertas

- [ ] {pergunta} _(confirmar com negócio)_

## Estratégia de teste

| CA | Tipo de teste | Cenário |
| --- | --- | --- |
| CA01 | Integração / unitário | {cenário} |

## Checklist pré-PR

- [ ] RNs implementadas com guard clauses documentadas
- [ ] Logs para casos edge (ex.: placa não encontrada)
- [ ] Testes cobrindo CAs principais
- [ ] `scan sync --branch {branch}` se KB alterada
