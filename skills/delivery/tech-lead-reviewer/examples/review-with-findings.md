# Exemplo — Parecer técnico com achados

## Entrada

User Story `US-FEAT-087-03` com Feature `FEAT-087` e parecer do requirements-reviewer: *Requer revisão* (ambiguidade funcional em aprovação).

## Parecer

# Parecer Técnico — US-FEAT-087-03

## Veredito

Bloqueada tecnicamente

## Resumo

A US define endpoint de submissão de alteração com aprovação do gestor, mas não especifica contrato da API, comportamento em timeout da integração com RH nem modelo de persistência do status. Revisão técnica provisória até correção funcional do fluxo de aprovação.

## Revisão por Regras de Negócio

| RN | Status | Observação |
| --- | --- | --- |
| RN01 | Atenção | Aprovação do gestor sem prazo — impacta job de expiração e estado default |
| RN02 | OK | Campos obrigatórios explícitos |
| RN03 | Bloqueio | "Notificar RH após aprovação" sem contrato de integração ou payload |

## Achados

### Bloqueantes

- **[RN03 | Integrações]** Integração com RH citada sem referência a API, evento ou documento. Impossível estimar ou implementar contrato.
- **[Escopo | APIs]** Escopo não define método/rota nem operação (criar solicitação vs atualizar registro existente).

### Importantes

- **[RN01 | Dados]** Status da solicitação (rascunho, pendente, aprovada, rejeitada, expirada) não enumerado — risco de modelo inconsistente.
- **[Segurança]** RN02 não define quem pode submeter alteração em nome de outro colaborador.

### Sugestões

- Incluir em Observações se notificação ao RH é síncrona ou assíncrona.
- Referenciar protótipo da tela de confirmação para estados de erro de integração.

## Impacto técnico

| Área | Avaliação |
| --- | --- |
| Dados | Médio |
| Integrações | Alto |
| Segurança | Médio |
| Complexidade | Alto |

## Recomendações

1. Com negócio: definir estados e timeout de aprovação (desbloqueia RN01).
2. Com analista: anexar contrato ou link Swagger da integração RH.
3. Complementar escopo com operação de API e referência ao recurso afetado.
4. Não estimar até desbloqueio dos itens acima.

## Próximo passo

Retornar ao [requirements-analyst](../../../product/requirements-analyst/SKILL.md) com achados documentados.
