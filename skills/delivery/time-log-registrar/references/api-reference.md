# API Reference — TechsBCN Time Log

## Extensão

| Campo | Valor |
| --- | --- |
| Publisher | `TechsBCN` |
| Extension | `DevOps-TimeLog` |
| Collection | `TimeLogData` |
| Scope | `Default` / `Current` |

## Endpoints

Base: `https://extmgmt.dev.azure.com/{organization}`

### Listar entradas

```http
GET /_apis/ExtensionManagement/InstalledExtensions/TechsBCN/DevOps-TimeLog/Data/Scopes/Default/Current/Collections/TimeLogData/Documents?api-version=7.2-preview.1
```

Resposta: `{ "value": [ ...documentos ] }`

### Criar entrada

```http
POST /_apis/ExtensionManagement/InstalledExtensions/TechsBCN/DevOps-TimeLog/Data/Scopes/Default/Current/Collections/TimeLogData/Documents?api-version=7.2-preview.1
Content-Type: application/json
```

### Atualizar entrada

```http
PUT /_apis/ExtensionManagement/InstalledExtensions/TechsBCN/DevOps-TimeLog/Data/Scopes/Default/Current/Collections/TimeLogData/Documents/{documentId}?api-version=7.2-preview.1
Content-Type: application/json
```

Autenticação: Basic com PAT (`:PAT` como senha, usuário vazio).

---

## Schema do documento

```json
{
  "id": "uuid-gerado",
  "workItemId": 150334,
  "workItemName": "Título do work item",
  "userId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "user": "Nome Exibido",
  "type": "Coding / Implementação",
  "time": 60,
  "startTime": "09:00",
  "date": "2026-07-10 09:00",
  "notes": "Notas opcionais",
  "__etag": 1
}
```

| Campo | Obrigatório | Descrição |
| --- | --- | --- |
| `id` | Sim (create) | UUID v4 — gerar no script |
| `workItemId` | Sim | ID numérico do work item |
| `workItemName` | Sim | Título do work item |
| `userId` | Sim | GUID do usuário (Identities API / `System.AssignedTo.id`) |
| `user` | Sim | Display name do usuário |
| `type` | Sim | Atividade — string exata do dropdown |
| `time` | Sim | **Total em minutos** (ex.: 420 = 7h, 60 = 1h) |
| `startTime` | Sim | Hora de início (`HH:mm`, ex.: `09:00`) |
| `date` | Sim | Data + hora: `YYYY-MM-DD HH:mm` (ex.: `2026-07-10 09:00`) |
| `notes` | Não | Notas (não usar `comment`) |
| `__etag` | Sim (update) | Versão retornada no GET |

A coluna **Time** na UI formata `time` como `H:mm`. O formulário da tela usa Hours/Minutes, mas a API grava o total em `time`.

O JSON de entrada da skill aceita `hours` + `minutes` (como na tela) ou `time` / `minutes` (total) — o script converte para `time`.

---

## Usuário (userId)

A UI da extensão **não exibe** seletor de usuário — usa o contexto do usuário logado no Azure DevOps.

A API de Extension Data **permite** definir `userId` e `user` no corpo do documento. Isso viabiliza o modo tech lead.

### Resolver usuário — Identities + Graph API

**Sempre preferir e-mail** (`-DeveloperEmail`). Busca por nome sozinha é ambígua e pode retornar usuário errado.

Ordem de resolução no script:

1. **Identities API** por e-mail — match exato em `Mail`/`Account`; display name via `customDisplayName` (nome da UI, ex.: `Bruno Eduardo Sousa Brandão (Prestador de Serviços - VIX)`), não `providerDisplayName`
2. **Graph API** por e-mail — confirma `displayName` e complementa `userId` se necessário
3. **Work item** `System.AssignedTo` — quando o WI está atribuído ao mesmo dev, usa o display name do formulário ADO

```http
GET https://vssps.dev.azure.com/{organization}/_apis/identities?searchFilter=General&filterValue={email}&queryMembership=None&api-version=6.0
```

```http
GET https://vssps.dev.azure.com/{organization}/_apis/graph/users?api-version=7.1-preview.1&filterValue={email}&filterType=MailAddress
```

Filtrar resultados do Graph por `mailAddress` exato no cliente — o filtro da API nem sempre restringe corretamente.

O `userId` gravado no time log é o `id` da Identities API (mesmo GUID de `System.AssignedTo.id` nos work items).

**Validação:** comparar `userId` de entradas existentes do mesmo dev com o valor resolvido antes do primeiro registro em produção.

---

## Capacity da sprint — listar devs

### 1. Obter iteration ID

```http
GET https://dev.azure.com/{org}/{project}/{team}/_apis/work/teamsettings/iterations?api-version=7.1
```

Filtrar por nome (`Sprint 93`) ou usar `attributes.timeFrame = current`.

### 2. Obter capacities

```http
GET https://dev.azure.com/{org}/{project}/{team}/_apis/work/teamsettings/iterations/{iterationId}/capacities?api-version=7.1
```

Retorno inclui `teamMembers[]` com:

* `teamMember.displayName`, `teamMember.uniqueName` (e-mail)
* `activities[].capacityPerDay`
* `teamMember.id` — ID do membro no time

Considerar dev com capacity se soma de `capacityPerDay` > 0.

---

## Work items — validação

```http
GET https://dev.azure.com/{org}/_apis/wit/workitems/{id}?api-version=7.1
```

Ou via MCP `ado` / `az boards work-item show`.

---

## Referências externas

* [Exportar TimeLog — TechsBCN](https://techsbcn.com/en/exporting-your-timelog-data-from-azure-devops-to-excel/)
* [Extension Management REST API](https://learn.microsoft.com/en-us/rest/api/azure/devops/extensionmanagement/)
* [Team Capacities REST API](https://learn.microsoft.com/en-us/rest/api/azure/devops/work/capacities/get-capacities-with-identity-ref-and-totals)
