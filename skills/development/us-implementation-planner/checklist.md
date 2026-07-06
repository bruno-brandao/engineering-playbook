# Checklist — US Implementation Planner

## Etapa 0 (obrigatória)

- [ ] Branch de implementação confirmada com o dev
- [ ] `scan verify` executado por repo candidato
- [ ] Relatório de validação exibido **antes** do plano
- [ ] Gate respeitado (ref_stale / divergent sem ressalva explícita)

## Análise da US

- [ ] Escopo, RNs e CAs lidos integralmente
- [ ] Feature pai consultada (se disponível)
- [ ] Lacunas RG06 sinalizadas como perguntas bloqueantes

## Contexto técnico

- [ ] L0 project-map carregado
- [ ] L1 repo-profile dos repos impactados
- [ ] L2 manifest search por keywords (≤ 8 nós L3)
- [ ] integration-graph consultado
- [ ] Repos legacy alertados

## Plano de saída

- [ ] Mapeamento RN → CA → tarefa técnica
- [ ] Ordem: dados → backend → integração → UI
- [ ] Riscos e impactos não previstos
- [ ] Estratégia de teste por CA
- [ ] Checklist pré-PR
- [ ] Origem citada (KB / Código / Inferido)
