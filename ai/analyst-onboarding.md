# Guia do Analista — Usando IA com o Engineering Playbook

Este guia é para **analistas de requisitos** configurarem e usarem IA no dia a dia — **sem Git**, **sem TI** e **sem conhecimento técnico**.

Você só precisa de: navegador, conta da empresa e **15 a 30 minutos** na primeira configuração.

---

## Comece aqui — 10 minutos (sem instalar nada)

Se quiser testar **agora**:

1. Abra a User Story no **Azure DevOps**.
2. Selecione e copie toda a **descrição** (`Ctrl+C`).
3. Abra [claude.ai](https://claude.ai) ou [chatgpt.com](https://chatgpt.com) (conta corporativa ou pessoal).
4. Cole o texto e envie:

```text
Você é um revisor de requisitos. Revise a User Story abaixo.

Regras:
- Não invente regras de negócio
- Aponte lacunas e ambiguidades
- Sugira critérios de aceite em formato Dado / Quando / Então
- Não diga que alterou o Azure DevOps — só sugira o que eu devo colar lá

Entregue: Veredito, Achados e Recomendações.

[cole a US aqui]
```

5. Copie as sugestões e aplique no Azure DevOps manualmente.

Isso já funciona. As seções abaixo deixam o processo **padronizado** e **repetível**.

---

## O que você vai conseguir fazer

| Ação | Exemplo de pedido |
| --- | --- |
| Decompor Feature em User Stories | *"Analise esta Feature e sugira User Stories"* |
| Revisar uma User Story | *"Revise com o padrão requirements-reviewer"* |
| Sugerir critérios de aceite | *"Sugira critérios de aceite para esta US"* |
| Identificar lacunas | *"Quais dúvidas levar para o negócio?"* |

A IA **sugere** — você **valida** e **aplica** no Azure DevOps.

---

## Escolha seu caminho

```text
Quer começar rápido, só no navegador?
  └─ Opção 1 — Claude ou ChatGPT (recomendado para começar)

Quer digitar "Revise a US 148431" e a IA buscar no DevOps?
  └─ Opção 2 — Cursor (instala programas, configura uma vez)

Já usa Claude no computador?
  └─ Opção 3 — Claude Code

Usa outra ferramenta do time (Antigravity, etc.)?
  └─ Opção 4 — Outras IDEs
```

| Opção | Instalar algo? | Lê US pelo número no DevOps? | Dificuldade |
| --- | --- | --- | --- |
| 1 — Navegador | Não | Não — você cola o texto | Fácil |
| 2 — Cursor | Sim | Sim | Média |
| 3 — Claude Code | Sim | Opcional | Média |
| 4 — Outra IDE | Sim | Depende | Média |

---

## Passo zero — Obter os arquivos do playbook (sem Git)

Você **não precisa** instalar Git nem clonar repositório.

### Como baixar

1. Abra o repositório **engineering-playbook** no Azure DevOps (peça o link ao time uma única vez, ou busque em *Repos*).
2. Clique em **Download as ZIP** (ícone de download no canto superior direito da árvore de arquivos).
3. Clique com o botão direito no ZIP → **Extrair tudo**.
4. Escolha uma pasta fácil de lembrar, por exemplo:

```text
C:\Users\SeuNome\Documents\engineering-playbook
```

Guarde esse caminho — você vai usar nos passos seguintes.

### Atualizar depois

Quando o time publicar versão nova, baixe o ZIP de novo e **substitua** a pasta antiga. Não precisa de mais nada.

---

## Regra importante (todas as opções)

A IA **não altera** o Azure DevOps sozinha. Ela entrega texto para você copiar e colar.

| Pode | Não pode |
| --- | --- |
| Ler e analisar Features/US | Criar ou editar work items automaticamente |
| Sugerir regras e critérios de aceite | Inventar regras de negócio |
| Gerar parecer de revisão | Dizer que "já salvou" no DevOps |

---

## Skills — o que são

São **instruções prontas** para a IA. Você não precisa decorar — basta citar o nome no pedido.

| Nome | Quando usar |
| --- | --- |
| `requirements-analyst` | Transformar Feature aprovada em User Stories |
| `requirements-reviewer` | Revisar qualidade de uma User Story |
| `sprint-readiness-reviewer` | Verificar se a US está pronta para a sprint |
| `us-estimator` | Pré-estimar esforço da US em horas |

---

## Opção 1 — Navegador (recomendado para começar)

Você configura **seu próprio** espaço no Claude ou ChatGPT. Não depende de ninguém.

### 1A. Claude — criar seu projeto (15 min, uma vez)

1. Acesse [claude.ai](https://claude.ai) e faça login.
2. No menu lateral, clique em **Projects** → **Create project**.
3. Nome sugerido: `Meu Playbook — Requisitos`.
4. Clique em **Add content** ou no ícone de anexo e envie estes arquivos da pasta que você extraiu:

| Arquivo (dentro do ZIP) |
| --- |
| `product/us-guidelines.md` |
| `product/us-template.md` |
| `product/feature-guidelines.md` |
| `product/feature-template.md` |
| `skills/product/requirements-analyst/SKILL.md` |
| `skills/product/requirements-reviewer/SKILL.md` |
| `skills/delivery/sprint-readiness-reviewer/SKILL.md` |
| `skills/delivery/us-estimator/SKILL.md` |
| `skills/delivery/us-estimator/references/estimation-guidelines.md` |
| `ai/agent-guidelines.md` |

5. Em **Custom instructions** do projeto, cole:

```text
Você apoia analistas de requisitos do time Águia Branca.
Siga os arquivos anexados. Nunca invente regras de negócio.
Nunca diga que alterou o Azure DevOps.
Para revisão, use o formato do requirements-reviewer.
Para decomposição em USs, use o requirements-analyst.
```

6. Pronto. O projeto fica salvo na sua conta.

#### Uso diário

1. Copie a US ou Feature do Azure DevOps.
2. Abra seu projeto no Claude.
3. Cole e peça, por exemplo:

```text
Revise com requirements-reviewer. Entregue veredito, achados e recomendações.

[cole aqui]
```

---

### 1B. ChatGPT — criar seu GPT (15 min, uma vez)

1. Acesse [chatgpt.com](https://chatgpt.com) (versão Plus/Team permite GPTs personalizados).
2. Menu **Explore GPTs** → **Create**.
3. Nome: `Revisor de Requisitos`.
4. Em **Instructions**, cole o mesmo texto das instruções do Claude (acima).
5. Em **Knowledge**, faça upload dos mesmos arquivos listados na seção 1A.
6. Salve. Use pelo menu **My GPTs**.

#### Uso diário

Igual ao Claude: copie do DevOps → cole no GPT → copie sugestões de volta.

---

### Prompts prontos (navegador)

**Revisar User Story:**

```text
Atue como requirements-reviewer. Revise a User Story abaixo.
Entregue: Veredito, Resumo, Achados (Bloqueantes / Importantes / Sugestões), Recomendações.

[cole a US]
```

**Gerar User Stories:**

```text
Atue como requirements-analyst. A Feature abaixo está aprovada.
Sugira User Stories seguindo o us-template. Liste dúvidas para o negócio.

[cole a Feature]
```

**Estimar User Story em horas:**

```text
Atue como us-estimator. Estime a User Story abaixo em horas.
Decomponha por atividade, informe premissas, riscos e nível de confiança.
É pré-estimativa — validar com desenvolvimento.

[cole a US]
```

**Só critérios de aceite:**

```text
Sugira critérios de aceite em Dado/Quando/Então para esta US.
Não invente regras — sinalize lacunas.

[cole a US]
```

---

## Opção 2 — Cursor (lê US pelo número no DevOps)

Para quem revisa muitas USs e quer pedir: *"Revise a US 148431"*.

### O que instalar (você mesmo, uma vez)

| Programa | Onde baixar | Como instalar |
| --- | --- | --- |
| **Cursor** | [cursor.com](https://cursor.com) | Baixar → executar → Avançar → Concluir |
| **Node.js** | [nodejs.org](https://nodejs.org) | Versão **LTS** → Avançar → Concluir (padrão) |
| **Azure CLI** | [aka.ms/installazurecliwindows](https://aka.ms/installazurecliwindows) | Baixar MSI → Avançar → Concluir |

Reinicie o computador após instalar os três.

### Passo 1 — Copiar as skills para o Cursor

1. Pressione `Win + R`, digite `%USERPROFILE%\.cursor` e Enter.
2. Se a pasta `.cursor` não existir, crie-a. Dentro dela, crie a pasta `skills`.
3. Abra outra janela com sua pasta do playbook (`Documents\engineering-playbook`).
4. **Copie** (não precisa entender o que é) estas pastas inteiras:

| De (no playbook) | Para |
| --- | --- |
| `skills\product\requirements-analyst` | `%USERPROFILE%\.cursor\skills\requirements-analyst` |
| `skills\product\requirements-reviewer` | `%USERPROFILE%\.cursor\skills\requirements-reviewer` |
| `skills\delivery\sprint-readiness-reviewer` | `%USERPROFILE%\.cursor\skills\sprint-readiness-reviewer` |
| `skills\delivery\us-estimator` | `%USERPROFILE%\.cursor\skills\us-estimator` |

É arrastar e soltar as pastas — igual copiar arquivos no Windows.

### Passo 2 — Conectar ao Azure DevOps

1. Na pasta `%USERPROFILE%\.cursor`, crie um arquivo chamado `mcp.json` (use o Bloco de Notas).
2. Cole o conteúdo abaixo e salve:

```json
{
  "mcpServers": {
    "ado": {
      "command": "npx",
      "args": [
        "-y",
        "@azure-devops/mcp",
        "aguiabranca",
        "--authentication",
        "azcli",
        "-d",
        "core",
        "work",
        "work-items"
      ],
      "env": {
        "ado_mcp_project": "AtivosCompraMobilizacao",
        "ado_mcp_team": "AtivosCompraMobilizacao Team"
      }
    }
  }
}
```

3. Abra o **Prompt de Comando** (busque "cmd" no menu Iniciar).
4. Digite `az login` e Enter.
5. O navegador abrirá — entre com seu e-mail `@aguiabranca.com.br`.
6. Feche o Prompt de Comando.

### Passo 3 — Ativar no Cursor

1. Abra o **Cursor**.
2. Vá em **File → Preferences → Cursor Settings → MCP**.
3. Verifique se o servidor **ado** aparece e está **habilitado** (verde).
4. Se não aparecer, reinicie o Cursor.

### Uso diário

1. Abra o Cursor.
2. Abra o chat em modo **Agent** (não Ask).
3. Escreva:

```text
Leia a User Story 148431 no Azure DevOps e revise com requirements-reviewer.
Não altere nada no DevOps — só entregue o parecer.
```

4. Aplique as sugestões manualmente no Azure DevOps.

### Dica — abrir o playbook no Cursor (opcional)

*File → Open Folder* → selecione `Documents\engineering-playbook`. Facilita consultar templates enquanto trabalha.

### Sem Azure CLI?

Se `az login` não funcionar na sua máquina, use o Cursor **mesmo assim**: copie a US do DevOps e cole no chat, citando `requirements-reviewer`. As skills continuam funcionando.

---

## Opção 3 — Claude Code

Mesma ideia do Cursor, pasta diferente.

### Instalar

1. Siga o guia oficial: [Claude Code](https://docs.anthropic.com/en/docs/claude-code).
2. Copie as três pastas de skills para `%USERPROFILE%\.claude\skills\` (igual ao Passo 1 do Cursor, trocando `.cursor` por `.claude`).

### Uso diário

```text
Usando requirements-reviewer, revise a User Story que vou colar abaixo.

[cole a US]
```

Para MCP com DevOps, siga a [documentação Microsoft](https://learn.microsoft.com/en-us/azure/devops/mcp-server/mcp-server-overview) — é opcional; colar a US funciona sem isso.

---

## Opção 4 — Outras IDEs

Se o time usar **Antigravity** ou similar:

1. Baixe o playbook (ZIP, passo zero).
2. Copie as pastas de skills para:

| Ferramenta | Pasta de destino |
| --- | --- |
| Antigravity | `%USERPROFILE%\.agent\skills\` |
| Padrão aberto | `%USERPROFILE%\.agents\skills\` |

3. Use os mesmos prompts das opções 1 e 2.

---

## Comparativo

| | Navegador | Cursor |
| --- | --- | --- |
| Tempo de setup | ~15 min | ~30 min |
| Precisa de TI | Não | Não |
| Git | Não | Não |
| Colar US do DevOps | Sim | Opcional |
| Pedir pela número (ex.: US 148431) | Não | Sim |
| Melhor para | Começar hoje | Muitas USs por dia |

---

## Problemas comuns — resolva sozinha

| Problema | Solução |
| --- | --- |
| A IA inventou regra | Adicione ao prompt: *"Não invente — sinalize como dúvida para o negócio"* |
| Resposta genérica | Cite: *"Siga o requirements-reviewer"* ou anexe o `SKILL.md` no chat |
| Cursor não acha o DevOps | Rode `az login` de novo; verifique MCP **ado** habilitado em Settings |
| Pasta `.cursor` não aparece | No Explorer, marque *Exibir itens ocultos* |
| `mcp.json` não funciona | Confira se salvou como `.json`, não `.json.txt` |
| Playbook desatualizado | Baixe ZIP novo do Azure DevOps e copie as skills de novo |
| Sem licença ChatGPT Plus | Use Claude.ai (opção 1A) — funciona no plano gratuito com limites |
| Não acho o repositório no DevOps | Peça **só o link** do repositório ao líder — uma vez |

### Quando pedir ajuda

Só escale se:

* Sua máquina **bloqueia instalação** de programas (política da empresa) → aí use **Opção 1 (navegador)** ou peça liberação de Cursor.
* `az login` falha por **permissão de conta** → use colar/copiar no Cursor ou navegador.

---

## Checklist — sua primeira vez

**Opção navegador (15 min):**

- [ ] Baixei o ZIP do playbook e extraí
- [ ] Criei meu projeto Claude ou GPT com os arquivos anexados
- [ ] Testei revisão de uma US real do DevOps

**Opção Cursor (30 min):**

- [ ] Instalei Cursor, Node.js e Azure CLI
- [ ] Copiei as 3 pastas de skills para `%USERPROFILE%\.cursor\skills\`
- [ ] Criei `mcp.json` e fiz `az login`
- [ ] MCP **ado** habilitado no Cursor
- [ ] Testei: *"Revise a US [número] com requirements-reviewer"*

---

## Referências

* [agent-guidelines.md](agent-guidelines.md) — o que a IA pode e não pode fazer
* [azure-devops-integration.md](azure-devops-integration.md) — detalhes do MCP
* [skills/README.md](../skills/README.md) — índice de skills
* [playbooks/PIPELINE.md](../playbooks/PIPELINE.md) — fluxo de requisitos
