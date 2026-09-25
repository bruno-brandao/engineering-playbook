# Parecer de Release — {versão/janela}

## Veredito

`Pronta | Pronta com ressalvas | Go/No-Go pendente | Não pronta`

## Escopo

| Componente | Versão/PR | Status | Dependências |
| --- | --- | --- | --- |
| {serviço} | {referência} | Aprovado/Pendente | {dependência} |

## Evidências de qualidade

| Evidência | Resultado | Origem | Atualidade |
| --- | --- | --- | --- |
| CI | Aprovado | {pipeline/link} | {data/commit} |
| Testes | Aprovado | {relatório} | {data/commit} |
| Review | Aprovado | {parecer} | {data/commit} |

## Implantação

- Ordem: {sequência}
- Migrations: {avaliação ou N/A}
- Configuração/secrets: {status}
- Feature flags: {status ou N/A}
- Rollout: {estratégia}

## Rollback

- Procedimento: {referência}
- Critério de acionamento: {condição}
- Limitações/irreversibilidades: {descrição}

## Operação pós-release

- Smoke tests: {lista}
- Métricas/alertas: {referências}
- Responsável: {papel/pessoa}
- Critério de sucesso: {condição}

## Bloqueios

1. {controle ou evidência ausente}

## Ressalvas aceitas

| Risco | Responsável | Condição/prazo |
| --- | --- | --- |
| {risco} | {responsável} | {condição} |

## Decisão humana necessária

- [ ] Go
- [ ] No-Go
- [ ] Adiar para obter {evidência}
