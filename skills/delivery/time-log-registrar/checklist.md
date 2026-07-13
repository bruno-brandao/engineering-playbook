# Checklist — Time Log Registrar

Antes de executar `register` (sem `-DryRun`):

## Perfil

- [ ] `whoami` executado — perfil existe ou `identify` feito nesta sessão
- [ ] Modo dev usa [plano-perfil.json](examples/plano-perfil.json) (sem `developerEmail` no JSON)

## Entrada

- [ ] Data informada ou assumida (hoje) confirmada
- [ ] Cada `workItemId` validado (existe e título coerente)
- [ ] Cada dev resolvido para `userId` + display name
- [ ] Atividades com strings exatas de [activities.md](references/activities.md)

## Totais

- [ ] Por dev + data: soma = 420 min (7h), ou desvio explicitamente aprovado
- [ ] Nenhuma entrada com 0 minutos
- [ ] Horas convertidas corretamente (1h = 60 min)

## Duplicatas

- [ ] Consultado `list` para a data — sem conflito, ou usuário escolheu complementar/substituir

## Autorização

- [ ] Preview apresentado ao usuário
- [ ] Confirmação explícita recebida ("confirmar", "pode lançar", etc.)
- [ ] `ADO_TIMELOG_PAT` configurado (não commitar PAT)

## Pós-gravação

- [ ] IDs das entradas reportados
- [ ] Links dos work items na resposta
- [ ] Erros parciais listados com dev/entrada afetada
