# Exemplo — Regras com cálculo e datas

## Contexto

Trecho de Feature com regra de cálculo de desconto progressivo e período de vigência.

## Por que incluir exemplos

Regras com cálculos, datas e condições exigem exemplos concretos para eliminar ambiguidade (Regra 4 da skill).

## Regras de Negócio (com exemplos embutidos)

**RN01** — O desconto é calculado sobre o valor bruto do pedido conforme faixas:

| Valor do pedido | Desconto |
| --- | --- |
| Até R$ 500,00 | 0% |
| De R$ 500,01 a R$ 2.000,00 | 5% |
| Acima de R$ 2.000,00 | 10% |

*Exemplo:* pedido de R$ 1.800,00 → desconto de 5% → valor final R$ 1.710,00.

**RN02** — A promoção é válida apenas para pedidos criados entre 01/03/2026 e 31/03/2026 (fuso America/Sao_Paulo).

*Exemplo:* pedido criado em 28/02/2026 às 23:59 → promoção não se aplica.
*Exemplo:* pedido criado em 01/03/2026 às 00:01 → promoção se aplica se demais regras forem atendidas.

**RN03** — Se o pedido contiver itens de categorias excluídas (lista na Feature), o desconto não se aplica ao pedido inteiro.

## Critérios de Aceite (derivados)

**CA01**

Dado um pedido de R$ 1.800,00 criado em 15/03/2026 sem itens excluídos
Quando o sistema calcula o total
Então o desconto aplicado é de 5% e o valor final é R$ 1.710,00

**CA02**

Dado um pedido de R$ 1.800,00 criado em 28/02/2026
Quando o sistema calcula o total
Então nenhum desconto promocional é aplicado
