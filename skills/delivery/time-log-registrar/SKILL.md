---
name: time-log-registrar
description: >-
  Registra horas de trabalho no Azure DevOps via extensão TechsBCN Time Log
  (Time Log Entries). Suporta modo desenvolvedor (próprio dia) e modo tech lead
  (registro em lote na daily). Use quando o usuário pedir para lançar horas,
  preencher time log, registrar apontamento de horas, ou apontar tempo em work
  items do Azure DevOps.
---

# Time Log Registrar

## Objetivo

Registrar **time log entries** em work items do Azure DevOps usando a extensão **TechsBCN DevOps-TimeLog** (aba *Time Log Entries*).

Esta é a **única skill do playbook com permissão de escrita** no Azure DevOps — limitada exclusivamente a documentos da coleção `TimeLogData`. Não altera work items, estados, comentários ou capacity.

## Exceção à política de somente leitura

As [agent-guidelines](../../../ai/agent-guidelines.md) proíbem escrita no DevOps para todas as outras skills. **Esta skill é exceção explícita** para time logs via Extension Management API.

| Permitido | Proibido |
| --- | --- |
| Criar e editar entradas em `TimeLogData` | Alterar work items (título, estado, campos) |
| Ler work items, capacity e usuários | Adicionar comentários em work items |
| Resolver `userId` via Identities/Graph API | Alterar capacity ou sprint settings |

## Documentos de referência

* [api-reference.md](references/api-reference.md) — endpoints, schema e mapeamento de usuário
* [activities.md](references/activities.md) — atividades válidas no dropdown
* [azure-devops-integration.md](../../../ai/azure-devops-integration.md) — org, projeto e MCP

## Modos de operação

| Modo | Quem usa | Entrada típica |
| --- | --- | --- |
| **Desenvolvedor** | O próprio dev | "Hoje trabalhei 4h na 150334 em coding e 3h em daily" |
| **Tech lead (daily)** | TL na reunião | Lista do que cada dev fez + work items; opcionalmente devs da capacity da sprint |

### Jornada prevista

* **7 horas por dia útil** (420 minutos) — validar que o total do dia fecha em 7h salvo pedido explícito em contrário.
* Entradas podem ser distribuídas em vários work items e atividades.

### Campos da tela vs API

O formulário exibe **Start time**, **Hours** e **Minutes**, mas a API persiste de outra forma (igual às entradas criadas pela UI):

| Campo na API | Origem | Exemplo (1h às 9h) |
| --- | --- | --- |
| `time` | Total em minutos (`hours×60 + minutes`) | `60` |
| `startTime` | Hora de início | `"09:00"` |
| `date` | Data + hora combinadas | `"2026-07-10 09:00"` |
| `notes` | Notas | `"SOS 150060"` |
| `workItemName` | Título do work item | `"6981892 - ..."` |

No JSON do plano, informe `date` (só a data) + `startTime` + `hours`/`minutes` — o script monta `date` completo na API.

## Pré-requisitos

### Perfil do desenvolvedor (recomendado)

Configurar **uma vez** para não buscar nome, e-mail e `userId` a cada registro:

```powershell
.\scripts\timelog.ps1 identify -Organization aguiabranca -DeveloperEmail seu@email.com.br
.\scripts\timelog.ps1 whoami
```

Salva em `scripts/.dev-profile.json` — arquivo **local por dev**, listado em `scripts/.gitignore` (não commitar). Depois, planos JSON podem omitir `developerEmail` e `developerUserId` — ver [examples/plano-perfil.json](examples/plano-perfil.json).

| Comando | Uso |
| --- | --- |
| `identify` | Resolve via API e salva perfil |
| `whoami` | Mostra perfil ativo |
| `identify -Clear` | Remove perfil salvo |

**Regra para o agente:** no modo desenvolvedor, executar `whoami` no início. Se não houver perfil, pedir e-mail do dev e rodar `identify` antes do primeiro `register`.

### PAT dedicado (não usar MCP read-only)

Variável de ambiente: `ADO_TIMELOG_PAT`

| Escopo | Uso |
| --- | --- |
| **Extension Data** (Read & manage) | Criar/editar time logs |
| **Work Items** (Read) | Validar IDs e títulos |
| **Graph** (Read) | Complementar display name na resolução por e-mail |
| **Project and Team** (Read) | Capacity da sprint |

Criar PAT em: `https://dev.azure.com/{org}/_usersSettings/tokens`

### Scripts

Executar a partir da pasta da skill:

```powershell
# Perfil (uma vez por dev)
.\scripts\timelog.ps1 identify -Organization aguiabranca -DeveloperEmail seu@email.com.br
.\scripts\timelog.ps1 whoami

# Listar devs com capacity na sprint atual
.\scripts\timelog.ps1 capacity -Organization aguiabranca -Project "Vix - GRLog" -Team "Vix - GRLog Team"

# Validar plano sem gravar (com perfil: plano-perfil.json)
.\scripts\timelog.ps1 register -InputFile ..\examples\plano-perfil.json -DryRun

# Gravar após confirmação do usuário
.\scripts\timelog.ps1 register -InputFile ..\examples\plano-perfil.json
```

---

## Regras obrigatórias

### 1. Sempre mostrar preview antes de gravar

Montar tabela com: data, dev, work item, atividade, horas, notas. **Nunca** executar `register` sem confirmação explícita do usuário.

### 2. Validar total do dia

Para cada dev + data, somar minutos. Alertar se ≠ 420 min (7h). Permitir prosseguir apenas se o usuário confirmar o desvio.

### 3. Atividades exatas

Usar strings **idênticas** ao dropdown da extensão — ver [activities.md](references/activities.md). Em caso de dúvida, listar a mais próxima e pedir confirmação.

### 4. Resolver usuário via API (não assumir)

O campo `user` deve ser o **display name completo** do Azure DevOps (ex.: `Paulo Henrique Araujo (Vix Logística)`), não um nome abreviado.

* **Com perfil salvo** (`identify`): usar identidade do perfil sem nova busca na API.
* **Sem perfil** ou **modo tech lead**: resolver via Identities/Graph por `developerEmail` — **não** usar só `developerName` (ambíguo)

### 5. Evitar duplicatas

Antes de gravar, consultar entradas existentes do dia (`timelog.ps1 list`). Se já houver lançamentos, perguntar se deve substituir, complementar ou cancelar.

### 6. Work item deve existir

Validar cada `workItemId` via MCP ou REST antes de gravar.

---

## Fluxo — modo desenvolvedor

### Etapa 1 — Coletar informações

Extrair da mensagem do usuário (ou perguntar o que faltar):

* **Data** (padrão: hoje)
* **Work item(s)** — ID ou título para busca
* **Atividades** e duração de cada bloco
* **Notas** opcionais por entrada
* **Desenvolvedor** — usar perfil salvo (`whoami`); se ausente, pedir e-mail e executar `identify`

### Etapa 2 — Interpretar linguagem natural

Exemplos de parsing:

| Entrada | Interpretação |
| --- | --- |
| "4h na 150334 implementando" | 240 min, Coding / Implementação, WI 150334 |
| "1h de daily" | 60 min, Daily Scrum / Reunião Diária, WI conforme contexto ou WI de capacidade/SOS |
| "code review 2h no PR da 148075" | 120 min, Code Review / Pull Requests, WI 148075 |

### Etapa 3 — Montar plano JSON

Usar como base [examples/plano-perfil.json](examples/plano-perfil.json) se houver perfil salvo, ou [examples/plano-template.json](examples/plano-template.json) para registro avulso / tech lead.

**Com perfil** (sem campos de dev):

```json
{
  "date": "2026-07-13",
  "entries": [
    {
      "workItemId": 150060,
      "activity": "Coding / Implementação",
      "hours": 5,
      "minutes": 0,
      "startTime": "09:00",
      "notes": ""
    }
  ]
}
```

**Sem perfil** (informar dev explicitamente):

```json
{
  "organization": "aguiabranca",
  "date": "2026-07-10",
  "entries": [
    {
      "developerEmail": "dev@empresa.com.br",
      "developerUserId": "00000000-0000-0000-0000-000000000000",
      "workItemId": 150060,
      "activity": "Suporte Técnico / Atendimento",
      "hours": 1,
      "minutes": 0,
      "startTime": "09:00",
      "notes": ""
    }
  ]
}
```

Para dia completo (7h) ou correção de entrada, ver [examples/plano-template.md](examples/plano-template.md).

### Etapa 4 — Validar e confirmar

```powershell
.\scripts\timelog.ps1 register -InputFile ..\examples\plano-perfil.json -DryRun
```

(Com perfil use `plano-perfil.json`; tech lead ou sem perfil use `plano-template.json` com `developerEmail` em cada entrada.)

Apresentar preview ao usuário. Aguardar **"confirmar"** ou ajustes.

### Etapa 5 — Gravar

```powershell
.\scripts\timelog.ps1 register -InputFile ..\examples\plano-perfil.json
```

Reportar IDs criados e links dos work items.

---

## Fluxo — modo tech lead (daily)

### Etapa 1 — Definir escopo de devs

**Opção A — Capacity da sprint (recomendado):**

```powershell
.\scripts\timelog.ps1 capacity -Organization {org} -Project {projeto} -Team {time} [-Iteration "Sprint 93"]
```

Listar devs com `capacityPerDay > 0`. Usar como checklist na daily.

**Opção B — Lista explícita** informada pelo TL.

### Etapa 2 — Coletar apontamentos por dev

Para cada dev presente na daily, registrar:

* O que fez (linguagem natural → atividades + work items)
* Distribuição das 7h

Aceitar formato livre, por exemplo:

> "Matheus: 5h na 150334 em coding, 1h code review, 1h daily"
> "Ana: 6h bugfix na 148075, 1h planning"

### Etapa 3 — Resolver identidades

Para cada dev, resolver `userId` via e-mail (`timelog.ps1 resolve-user -DeveloperEmail` ou durante `register`).

### Etapa 4 — Preview consolidado

Tabela única com todos os devs, validação de 7h por pessoa, work items e atividades.

### Etapa 5 — Confirmação e gravação

Mesmo fluxo do modo desenvolvedor: `DryRun` → confirmação → `register`.

---

## Edição de entradas existentes

Para corrigir uma entrada já lançada:

1. `timelog.ps1 list -Date {data}` — usa perfil salvo; ou `-DeveloperEmail` no modo tech lead — obter `id` e `__etag`
2. Montar JSON com `"id"` e `"__etag"` preenchidos
3. `register` com `-Update` (PUT em vez de POST)

---

## Recursos

| Recurso | Uso |
| --- | --- |
| [checklist.md](checklist.md) | Validação antes de gravar |
| [references/api-reference.md](references/api-reference.md) | API e schema |
| [references/activities.md](references/activities.md) | Lista de atividades |
| [examples/plano-template.md](examples/plano-template.md) | **Modelo JSON** — campos e comandos |
| [examples/plano-template.json](examples/plano-template.json) | Plano de 1 entrada (com dev explícito) |
| [examples/plano-perfil.json](examples/plano-perfil.json) | Plano com perfil salvo (sem dev) |
| [examples/dev-profile.example.json](examples/dev-profile.example.json) | Schema do perfil local |
| [examples/plano-dia-completo.json](examples/plano-dia-completo.json) | Plano de 7h (várias entradas) |
| [examples/plano-update.json](examples/plano-update.json) | Correção de entrada existente |
| [examples/dev-day.md](examples/dev-day.md) | Exemplo modo desenvolvedor |
| [examples/tech-lead-daily.md](examples/tech-lead-daily.md) | Exemplo modo tech lead |
| [scripts/timelog.ps1](scripts/timelog.ps1) | CLI de registro |

---

## Integração com MCP (leitura)

Usar MCP `ado` para:

* Buscar work item por ID ou query
* Confirmar título e tipo do item
* Listar itens da sprint atual

**Não** usar MCP para escrita — usar `scripts/timelog.ps1` com PAT.

---

## Mensagens de erro comuns

| Erro | Ação |
| --- | --- |
| `401 Unauthorized` | Verificar `ADO_TIMELOG_PAT` e escopos |
| `User not found` | Confirmar e-mail; usar `identify` ou `resolve-user -DeveloperEmail` — evitar busca só por nome |
| `Work item not found` | Validar ID e projeto |
| `Activity not in list` | Corrigir string conforme [activities.md](references/activities.md) |
| Total ≠ 7h | Ajustar distribuição ou confirmar exceção com usuário |
