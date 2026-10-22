# US-FEAT-PI-001-02 - Listar projetos e habilitar workspace

---

# Referências

## Feature

* FEAT-PI-001 — Disponibilizar workspace para conversas. Aprovada em 21/10/2026 por ps.brunoe@aguiabranca.com.br.

## Artefatos

* Figma: ainda não desenhado. Arquivo previsto: https://www.figma.com/design/ih1UFMUzvt3HiW7hy7T3ej/Portal-Inova%C3%A7%C3%A3o?node-id=0-1
* Protótipo: não existe para esta entrega.
* Fluxo: FEAT-PI-001, RG01 e RG02.
* Documento complementar: FEAT-PI-001, RG11.
* API/Swagger: `GET /_apis/projects` com o token delegado de quem está logado.

---

# Escopo

Entregar a lista paginada dos projetos que o token da pessoa lê no Azure DevOps e a ação de habilitar um projeto como workspace em configuração.

Fora desta US: confirmar processo, publicar mapa, nomear responsável e abrir conversa. Area path não é etapa de configuração.

---

# Regras de Negócio

## RN01

Somente uma pessoa que possui a permissão administrador habilita projeto. Quem não possui essa permissão não vê a ação e a API recusa a habilitação.

## RN02

A lista de projetos usa o access token delegado do Entra ID da pessoa logada, com os escopos de leitura `vso.work`, `vso.project` e `vso.profile`. Não existe campo para informar token. Não existe PAT.

## RN03

A lista chama `GET /_apis/projects` com esse token. Se o Azure DevOps responder 403, a tela informa ausência de permissão e não mostra projetos.

## RN04

Existir no resultado de `GET /_apis/projects` não cria workspace e não coloca o projeto no seletor de conversas.

## RN05

Ao habilitar, o portal cria um workspace com status `em configuração`. O identificador é o par organização + projeto lidos do Azure DevOps. Se esse par já tem workspace, a API recusa a ação com erro e mantém o workspace existente.

## RN06

A lista abre com 10 projetos. A pessoa pode mudar o tamanho para 30 ou para 50. Outro tamanho não é aceito. Trocar o tamanho pede de novo somente a página visível.

## RN07

O nome do projeto exibido vem do Azure DevOps. O código do portal não contém nome de projeto fixo.

## RN08

Habilitar abre um modal de confirmação sobre os projetos selecionados na lista. Não há tela própria para essa ação. A mesma ação fica na tela de detalhe do workspace. Se o projeto já tem workspace, o erro também é um modal e o workspace existente permanece.

---

# Critérios de Aceite

## CA01

Dado que a pessoa não possui a permissão administrador

Quando ela chama a habilitação de um projeto

Então a API recusa a ação e nenhum workspace é criado

## CA02

Dado que a pessoa possui a permissão administrador e o token dela lê o projeto Alfa

Quando ela abre a lista sem alterar o tamanho da página

Então a tela mostra no máximo 10 projetos e Alfa aparece somente se o token o devolveu

## CA03

Dado que a lista está aberta

Quando a pessoa escolhe 30 e, em seguida, 50

Então cada troca pede somente a página daquele tamanho, e um valor diferente de 10, 30 ou 50 é recusado

## CA04

Dado que Alfa aparece na lista e ainda não foi habilitado

Quando a pessoa habilita Alfa

Então passa a existir um workspace Alfa com status `em configuração`, e Alfa não aparece no seletor de conversas

## CA05

Dado que o workspace Alfa já existe

Quando a pessoa habilita Alfa de novo

Então a API recusa a ação com erro e continua existindo um único workspace para essa organização e esse projeto

## CA06

Dado que o Azure DevOps responde 403 para o token da pessoa

Quando ela abre a lista de projetos

Então a tela informa ausência de permissão e a lista fica vazia

---

# Exemplos de Negócio

## Exemplo 01

### Cenário

Dois projetos visíveis no token e um terceiro invisível.

### Entrada

O token lê Alfa e Beta. O token não lê Gama.

### Resultado Esperado

A lista pode mostrar Alfa e Beta. Gama não aparece. Habilitar Alfa cria um workspace. Beta continua só na lista até ser habilitado.

---

# Observações

* Depende da US-FEAT-PI-001-01 para a permissão administrador.
* O workspace é gravado no Supabase. O Databricks não recebe essa configuração.
* Não criar work item no Azure DevOps a partir deste rascunho.
