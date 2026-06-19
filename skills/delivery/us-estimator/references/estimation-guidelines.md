# Diretrizes de Estimativa em Horas

Padrão de referência para a skill [us-estimator](../SKILL.md). Ajuste as faixas com o time via Pull Request quando necessário.

---

## Princípios

* Estimativa em **horas brutas de trabalho** (não calendarizadas).
* Uma hora = esforço de uma pessoa durante 1 hora produtiva.
* Não incluir espera por terceiros, aprovações de negócio ou fila de deploy — registrar como **risco** se relevante.
* Pré-estimativa do analista/IA **não substitui** consenso do time no sprint planning.

---

## Atividades padrão

| Atividade | Quando usar |
| --- | --- |
| Refinamento técnico | Sempre que a US for nova ou complexa (0,5–2h) |
| Backend | APIs, regras de negócio server-side, persistência |
| Frontend | Telas, formulários, componentes visuais |
| Integração | SAP, serviços externos, filas, de/para |
| Testes (dev) | Automação mínima do que foi implementado |
| Testes (QA) | Execução manual dos CAs + exploratório focado |
| Ajustes / review | Retorno de code review e correções |

---

## Faixas de referência por complexidade

Use como **ponto de partida**, não como teto fixo.

| Complexidade | Perfil | Faixa total típica |
| --- | --- | --- |
| XS | Ajuste de label, permissão pontual | 2–4h |
| S | Campo novo, validação simples, 1–2 CAs | 4–8h |
| M | Tela CRUD, 3–5 RNs, exportação simples | 8–16h |
| L | Importação + regras, integração leve, 6+ CAs | 16–32h |
| XL | Múltiplos fluxos, integração crítica, alto volume de testes | 32–40h+ |

Se **XL**, avaliar decomposição em múltiplas USs.

---

## Heurísticas rápidas

| Fator | Ajuste sugerido |
| --- | --- |
| Cada RN com lógica condicional não trivial | +2–4h backend |
| Importação/exportação de arquivo | +4–8h (validação + erros) |
| Integração externa (ex.: SAP) | +8–16h (mapeamento + testes) |
| Cada 3 CAs manuais adicionais | +2–4h QA |
| Tela com protótipo Figma detalhado | −10–20% incerteza frontend |
| US com lacunas / sem CAs | Confiança Baixa; faixa +50% |

---

## Confiança da estimativa

| Nível | Critério |
| --- | --- |
| **Alta** | Escopo, RNs e CAs claros; sem integração desconhecida; time já entregou algo similar |
| **Média** | US completa, mas integração ou volume de regras traz incerteza |
| **Baixa** | Lacunas na US, dependências externas indefinidas ou tecnologia nova para o time |

---

## Distribuição típica (referência)

Para US **M** full-stack no time:

| Atividade | % do total |
| --- | --- |
| Backend | 30–40% |
| Frontend | 25–35% |
| Testes (dev + QA) | 20–30% |
| Refinamento + review | 10–15% |

Ajustar quando a US for só backend ou só frontend.

---

## O que não estimar nesta skill

* Story points (usar conversão apenas se o usuário pedir).
* Capacidade da sprint (responsabilidade do sprint planning).
* Horas de gestão, daily, cerimônias.
