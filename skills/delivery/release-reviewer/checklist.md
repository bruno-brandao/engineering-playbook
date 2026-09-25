# Checklist — Release Reviewer

## Escopo

- [ ] Versão, janela e ambiente identificados
- [ ] Itens, PRs, commits e repos conciliados
- [ ] Dependências e ordem de implantação definidas
- [ ] Mudanças fora do escopo sinalizadas

## Qualidade

- [ ] Revisões e aprovações presentes
- [ ] CI e checks obrigatórios aprovados
- [ ] Evidências de testes atuais
- [ ] Defeitos conhecidos e riscos documentados
- [ ] Compatibilidade entre componentes validada

## Implantação e recuperação

- [ ] Migrations e compatibilidade avaliadas
- [ ] Configurações, secrets e flags preparados
- [ ] Estratégia de rollout definida
- [ ] Rollback tecnicamente viável e testado/documentado
- [ ] Critérios de rollback definidos
- [ ] Backup/reconciliação avaliados quando aplicáveis

## Operação

- [ ] Smoke tests definidos
- [ ] Logs, métricas, alertas e dashboards disponíveis
- [ ] Responsáveis e comunicação definidos
- [ ] Critérios de sucesso pós-release definidos

## Governança

- [ ] Ressalvas possuem responsável e condição
- [ ] Evidências ausentes não foram tratadas como aprovadas
- [ ] Nenhuma ação em ambiente ou Azure DevOps foi executada
- [ ] Decisão final permanece humana
