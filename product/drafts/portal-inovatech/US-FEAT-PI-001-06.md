# US-FEAT-PI-001-06 - Registrar dependência de repositório

---

# Referências

## Feature

* FEAT-PI-001 — Disponibilizar workspace para conversas. Aprovada em 21/10/2026 por ps.brunoe@aguiabranca.com.br.

## Artefatos

* Figma: ainda não desenhado. Arquivo previsto: https://www.figma.com/design/ih1UFMUzvt3HiW7hy7T3ej/Portal-Inova%C3%A7%C3%A3o?node-id=0-1
* Protótipo: não existe para esta entrega.
* Fluxo: FEAT-PI-001, RG10.
* Documento complementar: nenhum além da Feature.
* API/Swagger: não há contrato publicado.

---

# Escopo

Permitir que o administrador registre, no workspace, uma dependência explícita de repositório de outro workspace, com justificativa.

Fora desta US: consultar o repositório na busca. Esta US grava a dependência e a ausência dela. A busca que respeita esse registro é entrega posterior.

---

# Regras de Negócio

## RN01

Somente quem possui a permissão administrador cria ou remove a dependência.

## RN02

Um repositório de outro workspace não entra na consulta deste workspace enquanto não existir dependência gravada para ele.

## RN03

A dependência grava o workspace de origem, o repositório e a justificativa. Sem justificativa, a dependência não é gravada.

## RN04

Criar ou remover a dependência não conclui etapa obrigatória e não muda, sozinha, o status do workspace para `disponível`.

---

# Critérios de Aceite

## CA01

Dado que o repositório `api-beta` pertence ao workspace Beta e Alfa não tem dependência para ele

Quando a configuração de consulta de Alfa é lida

Então `api-beta` não está autorizado na consulta de Alfa

## CA02

Dado que o administrador de Alfa informa o workspace Beta, o repositório `api-beta` e a justificativa "consome o contrato publicado"

Quando ele grava a dependência

Então Alfa passa a ter essa dependência, com essa justificativa

## CA03

Dado que a justificativa está vazia

Quando o administrador tenta gravar a dependência

Então a dependência não é gravada

## CA04

Dado que Alfa está `em configuração` por falta de responsável

Quando o administrador grava uma dependência válida

Então Alfa continua `em configuração`

## CA05

Dado que a pessoa não possui a permissão administrador

Quando ela tenta gravar uma dependência

Então a API recusa a ação e nada é gravado

---

# Exemplos de Negócio

## Exemplo 01

### Cenário

Alfa precisa ler um repositório que pertence a Beta.

### Entrada

Workspace Alfa. Repositório `api-beta` do workspace Beta. Justificativa "consome o contrato publicado".

### Resultado Esperado

A dependência fica gravada em Alfa. Sem essa gravação, `api-beta` não fica autorizado na consulta de Alfa.

---

# Observações

* Depende da US-FEAT-PI-001-02 para existirem workspaces.
* A busca que deixa de mencionar o repositório sem dependência é entrega posterior. O registro e a recusa de gravação sem justificativa cabem nesta US.
* Não criar work item no Azure DevOps a partir deste rascunho.
