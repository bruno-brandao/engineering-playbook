# Integração Azure DevOps

Como conectar o Cursor (e outras IDEs) ao Azure DevOps para **ler** Features e User Stories, alinhado à política de somente leitura do playbook.

---

## Política deste repositório

O Engineering Playbook opera em modo **read-suggest**:

```text
Azure DevOps  ──(MCP leitura)──►  Agente  ──(sugestões)──►  Usuário  ──(manual)──►  Azure DevOps
```

* O agente **lê** work items.
* O agente **sugere** perguntas, melhorias e rascunhos.
* O usuário **aplica** alterações no Azure DevOps.

Detalhes em [agent-guidelines.md](agent-guidelines.md).

---

## Configuração no Cursor

O arquivo do projeto fica em [`.cursor/mcp.json`](../.cursor/mcp.json).

Substitua os placeholders `sua-organizacao`, `SeuProjeto` e `SeuTime` pelos valores reais.

### Opção A — Servidor local (stdio)

Requer Node.js 20+ e autenticação via Azure CLI (`az login`).

```json
{
  "mcpServers": {
    "ado": {
      "command": "npx",
      "args": [
        "-y",
        "@azure-devops/mcp",
        "sua-organizacao",
        "--authentication",
        "azcli",
        "-d",
        "core",
        "work",
        "work-items"
      ],
      "env": {
        "ado_mcp_project": "SeuProjeto",
        "ado_mcp_team": "SeuTime"
      }
    }
  }
}
```

O domínio `work-items` limita ferramentas ao backlog. A política de **não escrever** é reforçada pelas [agent-guidelines](agent-guidelines.md) e pelas skills — o servidor local ainda pode expor ferramentas de escrita.

### Opção B — Servidor remoto com bloqueio técnico (recomendado)

O [servidor remoto do Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server?view=azure-devops) suporta o header `X-MCP-Readonly`, que restringe operações no servidor.

```json
{
  "mcpServers": {
    "ado": {
      "url": "https://mcp.dev.azure.com/sua-organizacao",
      "headers": {
        "X-MCP-Readonly": "true",
        "X-MCP-Toolsets": "work-items"
      }
    }
  }
}
```

Consulte a documentação Microsoft para autenticação e disponibilidade na sua organização.

---

## Pré-requisitos

| Item | Local (stdio) | Remoto |
| --- | --- | --- |
| Node.js 20+ | Sim | Não |
| Azure CLI (`az login`) | Recomendado | Conforme doc Microsoft |
| PAT somente leitura | Alternativa | Conforme doc Microsoft |
| Permissão Work Items (Read) | Sim | Sim |

Se usar PAT, restrinja o escopo a **Work Items: Read** (e **Project and Team: Read**).

---

## Uso com as skills

| Fluxo | Skill | Ação no DevOps |
| --- | --- | --- |
| Ler Feature e propor USs | [requirements-analyst](../skills/product/requirements-analyst/SKILL.md) | Nenhuma escrita |
| Revisar USs do backlog | [requirements-reviewer](../skills/product/requirements-reviewer/SKILL.md) | Nenhuma escrita |

### Exemplos de prompt

* *"Leia a Feature 1234 no Azure DevOps e sugira a decomposição em User Stories."*
* *"Busque as User Stories filhas da Feature 1234 e gere um parecer de revisão."*
* *"Liste perguntas em aberto para o negócio com base na Feature 1234."*

### Formato da saída sugerida

Quando houver sugestões de alteração para o Azure DevOps, entregar em bloco markdown pronto para cópia:

```markdown
## Sugestão de alteração — FEAT-1234

**Campo:** Description (ou campo customizado)

**Alteração proposta:**
[conteúdo]

**Motivo:** [referência ao checklist ou guideline]
```

---

## Mapeamento Feature / User Story

| Playbook | Tipo no Azure DevOps (padrão) |
| --- | --- |
| Feature | Feature (ou Epic, conforme processo do time) |
| User Story | User Story ou Product Backlog Item (PBI) |

### Organização aguiabranca — AtivosCompraMobilizacao

Configuração do MCP neste repositório:

| Parâmetro | Valor |
| --- | --- |
| Organização | `aguiabranca` |
| Projeto | `AtivosCompraMobilizacao` |
| Time | `AtivosCompraMobilizacao Team` |

Observações do processo atual (ajustar se necessário):

* Itens do backlog usam prefixos no título (ex.: `[A]`, `[O]`) — preservar na sugestão de alteração.
* Estados customizados (ex.: *Escrevendo*, *Em desenvolvimento*) — o agente lê o estado, mas não o altera.
* Parent com ícone de troféu costuma ser Feature ou Epic — usar como referência de rastreabilidade na análise.

Se o time usar tipos ou campos customizados adicionais, documente o mapeamento neste arquivo via Pull Request.

---

## Referências

* [Azure DevOps MCP Server — Overview](https://learn.microsoft.com/en-us/azure/devops/mcp-server/mcp-server-overview?view=azure-devops)
* [Repositório microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp)
* [Agent Guidelines](agent-guidelines.md)
