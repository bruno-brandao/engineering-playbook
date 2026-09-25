# Checklist — QA Test Designer

## Entradas

- [ ] US, RNs e CAs identificados
- [ ] Revisões funcional e técnica consideradas
- [ ] Plano de implementação consultado quando disponível
- [ ] Lacunas e premissas separadas

## Cobertura

- [ ] Cada RN relevante possui ao menos um cenário
- [ ] Caminho feliz, erros e limites foram avaliados
- [ ] Permissões e dados sensíveis foram avaliados
- [ ] Integrações, retry e idempotência foram avaliados
- [ ] Regressões relacionadas foram identificadas
- [ ] Não funcionais foram incluídos somente quando aplicáveis

## Execução

- [ ] Camada de teste escolhida por risco
- [ ] Massa, mocks e dependências descritos
- [ ] Evidência esperada definida
- [ ] Prioridade atribuída
- [ ] Nenhum framework foi inventado
- [ ] Skill local `test-generation` usada ou ausência declarada

## Saída

- [ ] Matriz RN/CA → cenário completa
- [ ] Bloqueios destacados
- [ ] Itens fora de escopo explícitos
- [ ] Próximo passo definido
