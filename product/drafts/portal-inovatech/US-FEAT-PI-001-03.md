# US-FEAT-PI-001-03 - Confirmar processo e area paths

---

# Referências

## Feature

* FEAT-PI-001 — Disponibilizar workspace para conversas. Aprovada em 21/10/2026 por ps.brunoe@aguiabranca.com.br.

## Artefatos

* Figma: ainda não desenhado. Arquivo previsto: https://www.figma.com/design/ih1UFMUzvt3HiW7hy7T3ej/Portal-Inova%C3%A7%C3%A3o?node-id=0-1
* Protótipo: não existe para esta entrega.
* Fluxo: FEAT-PI-001, RG03 e RG04.
* Documento complementar: nenhum além da Feature.
* API/Swagger: leitura do processo e dos area paths do projeto com o token delegado de quem está logado.

---

# Escopo

No workspace já habilitado, gravar a confirmação do mapa do processo e os area paths marcados para a conversa.

Fora desta US: publicar repositório, nomear responsável, mudar o status para `disponível` e abrir conversa.

---

# Regras de Negócio

## RN01

Somente quem possui a permissão administrador confirma o processo e marca area path nesse workspace.

## RN02

O portal lê do projeto, com o token da pessoa, o tipo do work item, os estados e os campos usados na cópia para o Azure DevOps e no dashboard. Feature, User Story e Product Backlog Item não são listas fixas no código.

## RN03

Confirmar grava essa leitura, o autor e a data. Sem confirmação gravada, o workspace permanece `em configuração`.

## RN04

A lista de area paths vem do Azure DevOps com o token da pessoa. Se o Azure DevOps responder 403, a tela informa ausência de permissão e não grava area path.

## RN05

O administrador marca um ou mais area paths. Area path não marcado fica registrado como fora da conversa desse workspace.

## RN06

Sem ao menos um area path marcado, a etapa de area path não está concluída e o workspace permanece `em configuração`.

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

## CA03

Dado que o Azure DevOps devolve os area paths A e B para Alfa

Quando o administrador marca só A

Então A fica marcado para a conversa e B fica de fora

## CA04

Dado que nenhum area path está marcado

Quando as etapas são consultadas

Então a etapa de area path aparece pendente e o status continua `em configuração`

## CA05

Dado que o token recebe 403 ao pedir os area paths

Quando o administrador abre essa etapa

Então a tela informa ausência de permissão e nenhum area path é gravado

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
* A cópia e o dashboard que usam esse mapa são entregas posteriores. Esta US só grava e exige a confirmação.
* Não criar work item no Azure DevOps a partir deste rascunho.
