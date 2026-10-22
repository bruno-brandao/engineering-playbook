# US-FEAT-PI-001-05 - Concluir o workspace e controlar o acesso

---

# Referências

## Feature

* FEAT-PI-001 — Disponibilizar workspace para conversas. Aprovada em 21/10/2026 por ps.brunoe@aguiabranca.com.br.

## Artefatos

* Figma: ainda não desenhado. Arquivo previsto: https://www.figma.com/design/ih1UFMUzvt3HiW7hy7T3ej/Portal-Inova%C3%A7%C3%A3o?node-id=0-1
* Protótipo: não existe para esta entrega.
* Fluxo: FEAT-PI-001, RG06, RG07, RG08 e RG09.
* Documento complementar: nenhum além da Feature.
* API/Swagger: não há contrato publicado.

---

# Escopo

Gravar o responsável do workspace, calcular o status `disponível` a partir das quatro etapas e impedir conversa, busca e sessão enquanto o workspace não está disponível.

Fora desta US: implementar a conversa, a busca e a sessão. Esta US só recusa essas chamadas para workspace que não está `disponível`.

---

# Regras de Negócio

## RN01

Somente quem possui a permissão administrador define o responsável e desfaz uma etapa.

## RN02

O responsável é escolhido no painel, no próprio workspace, entre as pessoas que já entraram no portal, e fica gravado nesse workspace. E-mail ou nome sem entrada correspondente no portal não é gravado. O valor não é lido de grupo nem de atributo fixo do Entra ID.

## RN03

Sem responsável gravado, a etapa do responsável não está concluída e o workspace permanece `em configuração`.

## RN04

O status passa a `disponível` somente quando as quatro etapas estão concluídas: projeto habilitado, mapa do processo confirmado, mapa publicado ou código dispensado, e responsável gravado. Area path e sprint não entram na conta.

## RN05

Se uma etapa concluída é desfeita, o status volta para `em configuração` na mesma ação.

## RN06

Para cada workspace `em configuração`, o painel lista as etapas que faltam.

## RN07

O seletor de conversas mostra o workspace somente quando o status está `disponível` e o token da pessoa lê esse projeto no Azure DevOps. Workspace `em configuração` aparece no painel de admin e não aparece no seletor.

## RN08

Com status `em configuração`, a API rejeita conversa, busca e sessão desse `workspace_id`.

---

# Critérios de Aceite

## CA01

Dado que as outras três etapas de Alfa estão concluídas e não há responsável

Quando as etapas são consultadas

Então a etapa do responsável aparece pendente e o status continua `em configuração`

## CA02

Dado que as quatro etapas de Alfa estão concluídas

Quando o status é consultado

Então Alfa está `disponível`

## CA03

Dado que Alfa está `disponível`

Quando o administrador desfaz a confirmação do processo

Então Alfa volta para `em configuração` na mesma ação e o painel mostra a etapa de processo pendente

## CA04

Dado que Alfa está `em configuração` e Beta está `disponível`, e o token da pessoa lê os dois projetos

Quando a pessoa abre o seletor de conversas

Então Beta aparece e Alfa não aparece

## CA05

Dado que Alfa está `disponível` e o token da pessoa não lê Alfa

Quando ela abre o seletor

Então Alfa não aparece

## CA06

Dado que Alfa está `em configuração`

Quando uma chamada de conversa, busca ou sessão envia o `workspace_id` de Alfa

Então a API rejeita a chamada

## CA07

Dado que Maria já entrou no portal e `nao.entrou@aguiabranca.com.br` nunca entrou

Quando o administrador escolhe Maria como responsável de Alfa e, em outra tentativa, informa `nao.entrou@aguiabranca.com.br`

Então Maria fica gravada como responsável e o e-mail sem entrada no portal não é gravado

---

# Exemplos de Negócio

## Exemplo 01

### Cenário

Três etapas prontas e responsável ausente.

### Entrada

Alfa habilitado, processo confirmado, mapa publicado, responsável vazio.

### Resultado Esperado

Status `em configuração`. O painel mostra só a etapa do responsável como pendente.

## Exemplo 02

### Cenário

Workspace disponível perde uma etapa.

### Entrada

Alfa `disponível`. O administrador apaga o responsável.

### Resultado Esperado

Alfa fica `em configuração`. Conversa, busca e sessão desse `workspace_id` passam a ser rejeitadas.

---

# Observações

* Depende das US-FEAT-PI-001-02, US-FEAT-PI-001-03 e US-FEAT-PI-001-04, que concluem as outras etapas.
* A tela de conversa em si não faz parte desta US.
* Não criar work item no Azure DevOps a partir deste rascunho.
