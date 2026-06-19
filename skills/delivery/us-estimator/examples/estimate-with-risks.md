# Exemplo — Importação com integração (confiança Média)

## Contexto

US similar a export/import de Data Vencimento NF: arquivo .XLS, cálculo de dias, de/para SAP, mudança de etapa.

## Saída

# Estimativa — US-148431 — Exportar/Importar Data de Vencimento NF

> Pré-estimativa em horas. Validar com o time de desenvolvimento antes de comprometer na sprint.

## Resumo

| Campo | Valor |
| --- | --- |
| Total estimado | 28h (faixa: 22–36h) |
| Confiança | Média |
| Tipo principal | Import/Export + Regras + Integração (SAP) |

## Premissas

- Layout do arquivo conforme anexo da Feature.
- De/para SAP segue planilha `Qtd_dias_vencimento_ajustada.xlsx`.
- Pedidos em *Aguardando Faturamento* apenas.
- RN02 (estrutura do arquivo) será preenchida antes do desenvolvimento.

## Decomposição (horas)

| Atividade | Horas | Observação |
| --- | --- | --- |
| Refinamento técnico | 2 | Alinhar layout, SAP e transição de etapa |
| Backend | 12 | Export, import, validações, cálculo, persistência, SAP |
| Frontend | 4 | Botão, menu, feedback de importação |
| Integração | 4 | De/para condição pagamento SAP |
| Testes (dev) | 3 | Cenários import/export e cálculo |
| Testes (QA) | 5 | 5+ CAs + erros de arquivo e etapa |
| Ajustes / review | 2 | Review e correções |
| **Total** | **32** | Faixa **22–36h** por RN02 pendente e regras de erro não detalhadas |

## Riscos que podem aumentar esforço

- RN02 indefinida — impacto: +4–8h.
- Regras de erro na importação não especificadas — impacto: +4h.
- Comportamento com pedido parcialmente inválido no lote — impacto: +4–6h.

## Lacunas que impedem estimativa precisa

- Estrutura exata das colunas (RN02 vazia).
- Tratamento de erro linha a linha vs. arquivo inteiro.

## Recomendação

Refinar US (RN02 + CAs de erro) antes de comprometer. Se urgente, reservar buffer de 30% na sprint.
