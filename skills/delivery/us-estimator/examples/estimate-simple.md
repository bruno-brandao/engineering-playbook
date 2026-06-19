# Exemplo — Estimativa simples (confiança Alta)

## Contexto

US com cadastro de campo novo, 2 RNs, 3 CAs, sem integração.

## Saída

# Estimativa — US-FEAT-042-01 — Adicionar campo observação no cadastro

> Pré-estimativa em horas. Validar com o time de desenvolvimento antes de comprometer na sprint.

## Resumo

| Campo | Valor |
| --- | --- |
| Total estimado | 6h (faixa: 5–7h) |
| Confiança | Alta |
| Tipo principal | CRUD / UI simples |

## Premissas

- Tela e persistência já existem; apenas novo campo texto.
- Sem integração externa.
- Protótipo alinhado com a US.

## Decomposição (horas)

| Atividade | Horas | Observação |
| --- | --- | --- |
| Refinamento técnico | 0,5 | Alinhamento rápido |
| Backend | 2 | Campo + validação + API |
| Frontend | 2 | Input na tela existente |
| Integração | — | N/A |
| Testes (dev) | 0,5 | Teste unitário da validação |
| Testes (QA) | 1 | 3 CAs manuais |
| Ajustes / review | 0,5 | Code review |
| **Total** | **6,5** | Arredondar para **6–7h** |

## Riscos que podem aumentar esforço

- Nenhum identificado.

## Lacunas que impedem estimativa precisa

- Nenhuma.

## Recomendação

Incluir na sprint após validação rápida no planning.
