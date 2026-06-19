# Agent Guidelines

Diretrizes para agentes de IA que operam com o Engineering Playbook.

---

## Princípio geral

O agente **assiste** o time — não substitui decisões humanas nem altera sistemas de registro (backlog, repositório, pipelines) sem ação explícita do usuário.

---

## Azure DevOps — somente leitura

### Política

| Permitido | Proibido |
| --- | --- |
| Ler Features, User Stories e work items relacionados | Criar, atualizar ou excluir work items |
| Consultar backlog, sprint e links entre itens | Adicionar ou editar comentários |
| Listar projetos, times e metadados | Alterar estado, atribuição ou campos |
| Gerar perguntas, sugestões e rascunhos de alteração | Aplicar alterações diretamente no Azure DevOps |

### Comportamento esperado

1. **Ler** o conteúdo via MCP ou material fornecido pelo usuário.
2. **Analisar** com as skills do playbook (`requirements-analyst`, `requirements-reviewer`, etc.).
3. **Entregar** ao usuário:
   - perguntas para o negócio;
   - sugestões de alteração em markdown;
   - rascunhos de User Stories ou pareceres de revisão.
4. **Deixar a aplicação** das mudanças a cargo do usuário no Azure DevOps.

### Quando o usuário pedir para "salvar" ou "atualizar" no DevOps

Recusar a escrita automática. Oferecer o texto formatado para cópia manual ou confirme que o usuário deseja executar a alteração ele mesmo.

### Ferramentas MCP de escrita

Mesmo que ferramentas de escrita estejam disponíveis no servidor MCP, **não invocá-las**. Esta política prevalece sobre a capacidade técnica do servidor.

Ver [azure-devops-integration.md](azure-devops-integration.md) para configuração do MCP em modo somente leitura.

---

## Skills e playbooks

* Skills em `skills/` definem **o que** analisar e **como** formatar a saída.
* Playbooks em `playbooks/` definem **como pessoas** conduzem cerimônias.
* Guidelines em `product/`, `qa/`, etc. são a **fonte canônica** de regras — não duplicar nem alterar via agente.

---

## Qualidade da saída

* Não inventar regras de negócio.
* Sinalizar lacunas e ambiguidades.
* Referenciar o documento ou critério violado em cada achado.
* Indicar a origem dos dados (ex.: "Feature FEAT-123 conforme Azure DevOps").
