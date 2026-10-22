# US-FEAT-PI-001-04 - Importar e publicar o mapa do projeto

---

# Referências

## Feature

* FEAT-PI-001 — Disponibilizar workspace para conversas. Aprovada em 21/10/2026 por ps.brunoe@aguiabranca.com.br.

## Artefatos

* Figma: ainda não desenhado. Arquivo previsto: https://www.figma.com/design/ih1UFMUzvt3HiW7hy7T3ej/Portal-Inova%C3%A7%C3%A3o?node-id=0-1
* Protótipo: não existe para esta entrega.
* Fluxo: FEAT-PI-001, RG05.
* Documento complementar: `project-context/templates/project-map.yaml` e `project-context/schemas/project-map.schema.json`, só como referência do modelo exportado.
* API/Swagger: não há contrato publicado.

---

# Escopo

No workspace habilitado, permitir upload do `project-map.yaml`, exportar o modelo com a instrução de cada campo, e publicar o mapa ou declarar que a conversa não consulta código.

Fora desta US: rodar pipeline, indexar repositório, calcular embedding e abrir conversa.

---

# Regras de Negócio

## RN01

Somente quem possui a permissão administrador importa, exporta o modelo, publica o mapa ou declara a dispensa de código.

## RN02

Publicar o mapa e declarar que a conversa não consulta código se excluem. Publicar remove a declaração. Declarar a dispensa não grava repositório publicado.

## RN03

O mapa publicado guarda a branch de referência padrão, o perfil de indexação (`minimal`, `standard` ou `full`) e, por repositório, nome, URL no Azure DevOps, status (`active`, `legacy` ou `discontinued`), branch de referência, descrição, stack e donos.

## RN04

`local_path` não é gravado, mesmo que venha no arquivo importado.

## RN05

A tela aceita o upload do YAML. O upload preenche os campos do mapa. O upload não publica e não conclui outra etapa.

## RN06

A mesma tela exporta um modelo vazio e mostra a instrução do que é cada campo da RN03. A instrução diz que `local_path` é ignorado.

## RN07

A lista de repositórios do mapa abre com 10 itens. A pessoa pode mudar para 30 ou 50. Outro tamanho não é aceito. Trocar o tamanho pede de novo somente a página visível.

## RN08

Publicar grava autor e data. Sem mapa publicado e sem a declaração de dispensa, a etapa não está concluída e o workspace permanece `em configuração`.

## RN09

Depois de publicado, a cópia do portal é a configuração usada pela conversa, pela pipeline e pelo ingest. O YAML de origem não é consultado de novo.

---

# Critérios de Aceite

## CA01

Dado que o administrador envia um YAML com um repositório e com `local_path`

Quando o upload termina

Então os campos da RN03 aparecem preenchidos, `local_path` não é gravado e o mapa ainda não está publicado

## CA02

Dado que o mapa está preenchido e não publicado

Quando o administrador publica

Então a publicação grava autor e data, e a declaração de dispensa de código, se existia, deixa de valer

## CA03

Dado que o administrador declara que a conversa não consulta código

Quando a declaração é gravada

Então nenhum repositório fica publicado e a etapa do mapa fica concluída por dispensa

## CA04

Dado que não há publicação nem dispensa

Quando as etapas são consultadas

Então a etapa do mapa aparece pendente e o status continua `em configuração`

## CA05

Dado que a seção Mapa da tela de configuração do workspace está aberta

Quando o administrador exporta o modelo

Então recebe um YAML vazio e vê a instrução de cada campo, incluindo que `local_path` é ignorado

## CA06

Dado que o mapa tem mais de 10 repositórios

Quando a lista abre e a pessoa escolhe 30

Então a primeira abertura mostra 10 e a troca pede somente a página de 30

---

# Exemplos de Negócio

## Exemplo 01

### Cenário

Upload com caminho de máquina.

### Entrada

Repositório `api-alfa`, status `active`, branch `develop`, `local_path` `C:\repos\api-alfa`.

### Resultado Esperado

O mapa preenchido tem `api-alfa`, `active` e `develop`. `C:\repos\api-alfa` não fica gravado. O workspace segue `em configuração` até a publicação ou a dispensa.

## Exemplo 02

### Cenário

Dispensa e publicação no mesmo workspace.

### Entrada

Primeiro a pessoa declara que a conversa não consulta código. Depois publica um mapa com `api-alfa`.

### Resultado Esperado

A declaração deixa de valer. `api-alfa` fica publicado.

---

# Observações

* Depende da US-FEAT-PI-001-02, porque o workspace já precisa existir.
* A pipeline que consome a cópia publicada é entrega posterior.
* Não criar work item no Azure DevOps a partir deste rascunho.
