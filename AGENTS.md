# Engineering Playbook — Regras para Agentes

Este repositório é o Engineering Playbook da Aguiabranca. Diretrizes completas em [ai/agent-guidelines.md](ai/agent-guidelines.md).

## Princípio geral

O agente **assiste** o time — não substitui decisões humanas nem altera sistemas de registro (backlog, repositório, pipelines) sem ação explícita do usuário.

## Azure DevOps — somente leitura

| Permitido | Proibido |
| --- | --- |
| Ler Features, User Stories e work items | Criar, atualizar ou excluir work items |
| Consultar backlog, sprint e links entre itens | Adicionar ou editar comentários |
| Listar projetos, times e metadados | Alterar estado, atribuição ou campos |
| Gerar perguntas, sugestões e rascunhos | Aplicar alterações diretamente no Azure DevOps |

Mesmo que ferramentas de escrita estejam disponíveis no servidor MCP, **não invocá-las**. Esta política prevalece sobre a capacidade técnica do servidor.

**Exceção:** a skill `time-log-registrar` pode gravar time logs na extensão TechsBCN via API REST (PAT dedicado), com confirmação obrigatória do usuário. Nunca em work items.

## Estrutura do playbook

- `skills/` — instruções operacionais para IA (o que analisar, como formatar saída)
- `playbooks/` — processos passo a passo para pessoas
- `product/`, `adr/`, `project-context/` — fonte canônica de regras e templates; não duplicar nem alterar via agente
- `ai/` — diretrizes de uso de IA e integração Azure DevOps

## Qualidade da saída

- Não inventar regras de negócio.
- Sinalizar lacunas e ambiguidades.
- Referenciar o documento ou critério violado em cada achado.
- Indicar a origem dos dados (ex.: "Feature FEAT-123 conforme Azure DevOps").
