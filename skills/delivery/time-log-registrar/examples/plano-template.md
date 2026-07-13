# Modelo de plano JSON

Arquivos prontos para copiar e ajustar antes do `register`.

| Arquivo | Uso |
| --- | --- |
| [plano-perfil.json](plano-perfil.json) | Com perfil salvo (`identify`) — sem campos de dev |
| [plano-template.json](plano-template.json) | Uma entrada com dev explícito |
| [plano-dia-completo.json](plano-dia-completo.json) | Dia de 7h com várias atividades |
| [plano-update.json](plano-update.json) | Corrigir entrada existente (`-Update`) |

## Perfil do desenvolvedor

Configurar uma vez:

```powershell
.\timelog.ps1 identify -Organization aguiabranca -DeveloperEmail seu@email.com.br
.\timelog.ps1 whoami
```

Arquivo local: `scripts/.dev-profile.json` — cada dev cria o seu via `identify`; está em `scripts/.gitignore` e **não deve ser commitado**.

## Campos por entrada

| Campo | Obrigatório | Descrição |
| --- | --- | --- |
| `developerEmail` | Com perfil: não | E-mail do dev no Azure DevOps |
| `developerUserId` | Com perfil: não | GUID do usuário — acelera resolução |
| `workItemId` | Sim | ID numérico do work item |
| `activity` | Sim | String exata do dropdown — ver [activities.md](../references/activities.md) |
| `hours` | Sim* | Horas de duração (como na tela) |
| `minutes` | Sim* | Minutos de duração (0–59) |
| `startTime` | Padrão `09:00` | Hora de início (`HH:mm`) |
| `notes` | Não | Notas livres |
| `id` / `__etag` | Só em update | Obter via `timelog.ps1 list` |

\* Informe `hours` + `minutes` (preferido) ou `time` / `minutes` como total em minutos.

**Não** preencher `developerName` — o script resolve o display name completo via API (ex.: `Paulo Henrique Araujo (Vix Logística)`).

## O que o script grava na API

| Entrada do plano | Campo na API |
| --- | --- |
| `date` + `startTime` | `date`: `"2026-07-10 09:00"` |
| `startTime` | `startTime`: `"09:00"` |
| `hours` + `minutes` | `time`: total em minutos |
| `notes` | `notes` |
| (automático) | `workItemName`, `user`, `userId` |

## Comandos

```powershell
cd skills/delivery/time-log-registrar/scripts

# Perfil (modo dev)
.\timelog.ps1 identify -Organization aguiabranca -DeveloperEmail seu@email.com.br

# Preview com perfil
.\timelog.ps1 register -InputFile ..\examples\plano-perfil.json -DryRun

# Preview tech lead / sem perfil
.\timelog.ps1 register -InputFile ..\examples\plano-template.json -DryRun

# Gravar
.\timelog.ps1 register -InputFile ..\examples\plano-perfil.json

# Atualizar entrada existente
.\timelog.ps1 register -InputFile ..\examples\plano-update.json -Update
```
