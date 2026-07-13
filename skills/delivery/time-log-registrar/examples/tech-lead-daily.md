# Exemplo — Modo tech lead (daily)

## Contexto

Sprint 93, time Vix - GRLog. TL conduz daily e registra horas de todos os devs com capacity.

## Passo 1 — Listar devs da sprint

```powershell
.\scripts\timelog.ps1 capacity `
  -Organization aguiabranca `
  -Project "Vix - GRLog" `
  -Team "Vix - GRLog Team" `
  -Iteration "Sprint 93"
```

Saída:

```text
Dev                          Email                              Capacity/dia
Matheus Rodrigues            matheus.rodrigues@empresa.com      7
Ana Silva                    ana.silva@empresa.com              7
```

## Passo 2 — Entrada do TL

> Registra horas de ontem (09/07):
> - Matheus: 6h na 150334 coding, 1h daily
> - Ana: 4h bugfix na 148075, 2h testes na 148075, 1h planning

## Plano consolidado

| Dev | WI | Atividade | Horas |
| --- | --- | --- | --- |
| Matheus | 150334 | Coding / Implementação | 6h |
| Matheus | 150334 | Daily Scrum / Reunião Diária | 1h |
| Ana | 148075 | Correção de Bugs (Bug Fixing) | 4h |
| Ana | 148075 | Escrita de Testes | 2h |
| Ana | 148075 | Planning / Refinamento Técnico | 1h |

Totais: Matheus 7h ✓ | Ana 7h ✓

## Ponto técnico — userId

O TL está logado como `tech.lead@empresa.com`, mas as entradas serão gravadas com:

- Matheus → `userId` resolvido via e-mail na Identities API (não o do TL)
- Ana → `userId` resolvido via e-mail na Identities API

A UI mostraria o usuário logado; a API aceita `userId` explícito no documento. **Sempre** informar `developerEmail` por entrada — não usar só o nome.

## Confirmação

Montar JSON a partir de [plano-template.json](plano-template.json) — uma entrada por bloco, com `developerEmail` de cada dev. Apresentar tabela ao TL → aguardar "confirmar" → executar:

```powershell
.\timelog.ps1 register -InputFile .\plano-daily.json -DryRun
.\timelog.ps1 register -InputFile .\plano-daily.json
```
