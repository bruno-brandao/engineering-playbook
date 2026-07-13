# Exemplo — Modo desenvolvedor

## Pré-requisito

Perfil configurado (`identify` + `whoami`). Ver [plano-template.md](plano-template.md).

## Entrada do usuário

> Lança minhas horas de hoje na 150334: 5h implementando movimentação de escala, 1h de code review no mesmo item, 1h de daily.

## Plano interpretado

| Dev | WI | Atividade | Horas | Notas |
| --- | --- | --- | --- | --- |
| (perfil salvo) | 150334 | Coding / Implementação | 5h | Movimentação de escala |
| (perfil salvo) | 150334 | Code Review / Pull Requests | 1h | |
| (perfil salvo) | 150334 | Daily Scrum / Reunião Diária | 1h | |

**Total:** 7h ✓

## JSON gerado

Base: [plano-dia-completo.json](plano-dia-completo.json) — **sem** `developerEmail` se houver perfil; ajustar `date` e `workItemId`. Ou montar a partir de [plano-perfil.json](plano-perfil.json) com várias entradas.

## Comandos

```powershell
cd skills/delivery/time-log-registrar/scripts
.\timelog.ps1 whoami
.\timelog.ps1 register -InputFile ..\examples\plano-dia-completo.json -DryRun
# usuário confirma
.\timelog.ps1 register -InputFile ..\examples\plano-dia-completo.json
```

## Saída esperada

```text
Criada ... — Bruno Eduardo Sousa Brandão (Prestador de Serviços - VIX) — WI 150334 — Coding / Implementação — 5:00
Criada ... — Bruno Eduardo Sousa Brandão (Prestador de Serviços - VIX) — WI 150334 — Code Review / Pull Requests — 1:00
Criada ... — Bruno Eduardo Sousa Brandão (Prestador de Serviços - VIX) — WI 150334 — Daily Scrum / Reunião Diária — 1:00

3 criada(s), 0 atualizada(s).
```
