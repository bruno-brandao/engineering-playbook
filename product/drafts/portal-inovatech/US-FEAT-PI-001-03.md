# US-FEAT-PI-001-03 - Confirmar o processo

---

# Referências

## Feature

* FEAT-PI-001 — Disponibilizar workspace para conversas. Aprovada em 21/10/2026 por ps.brunoe@aguiabranca.com.br.

## Artefatos

* Figma: ainda não desenhado. Arquivo previsto: https://www.figma.com/design/ih1UFMUzvt3HiW7hy7T3ej/Portal-Inova%C3%A7%C3%A3o?node-id=0-1
* Protótipo: não existe para esta entrega.
* Fluxo: FEAT-PI-001, RG03.
* Documento complementar: nenhum além da Feature.
* API/Swagger: leitura do processo do projeto com o token delegado de quem está logado.

---

# Escopo

No workspace já habilitado, gravar a confirmação do mapa do processo. Area path não é gravado nesta US: a consulta usa o que o token já lê.

Fora desta US: publicar repositório, nomear responsável, mudar o status para `disponível` e abrir conversa.

---

# Regras de Negócio

## RN01

Somente quem possui a permissão administrador confirma o processo nesse workspace.

## RN02

O portal lê do projeto, com o token da pessoa, o tipo do work item, os estados e os campos usados na cópia para o Azure DevOps e no dashboard. Feature, User Story e Product Backlog Item não são listas fixas no código.

## RN03

Confirmar grava essa leitura, o autor e a data. Sem confirmação gravada, o workspace permanece `em configuração`.

---

# Critérios de Aceite

## CA01

Dado que o workspace Alfa está `em configuração` e o processo do projeto tem os tipos devolvidos pelo Azure DevOps

Quando o administrador confirma o mapa do processo

Então o portal grava esses tipos, estados e campos, com autor e data, e não substitui a resposta do Azure DevOps por uma lista fixa

## CA02

Dado que o workspace Alfa não tem confirmação de processo

Quando as etapas são consultadas

Então a etapa de processo aparece pendente e o status continua `em configuração`

---

# Exemplos de Negócio

## Exemplo 01

### Cenário

Projeto cujo processo usa Product Backlog Item, não User Story.

### Entrada

O Azure DevOps devolve o tipo Product Backlog Item, os estados New e Done e os campos título e descrição.

### Resultado Esperado

A confirmação grava Product Backlog Item, New, Done, título e descrição. A tela não exige o tipo User Story.

---

# Observações

* Depende da US-FEAT-PI-001-02, porque o workspace já precisa existir.
* A cópia e o dashboard que usam esse mapa são entregas posteriores. Esta US só grava e exige a confirmação do processo.
* Area path e sprint ficam de fora desta confirmação. A FEAT-PI-001, RG04, manda lê-los na consulta com o token da pessoa.
* Não criar work item no Azure DevOps a partir deste rascunho.
