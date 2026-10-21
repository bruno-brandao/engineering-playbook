# US-FEAT-PI-001-01 - Garantir a permissão administrador do sistema

---

# Referências

## Feature

* FEAT-PI-001 — Disponibilizar workspace para conversas. Aprovada em 21/10/2026 por ps.brunoe@aguiabranca.com.br.

## Artefatos

* Figma: ainda não desenhado. Arquivo previsto: https://www.figma.com/design/ih1UFMUzvt3HiW7hy7T3ej/Portal-Inova%C3%A7%C3%A3o?node-id=0-1
* Protótipo: não existe para esta entrega.
* Fluxo: a permissão nasce com a instalação. A tela não a cria.
* Documento complementar: FEAT-PI-001, RG12.
* API/Swagger: não há contrato publicado.

---

# Escopo

Entregar a permissão de sistema administrador no portal, já atribuída na primeira instalação, sem permitir que a tela altere a definição dessa permissão.

Fora desta US: habilitar workspace, editar as permissões editor, aprovador e leitor, e qualquer chamada ao Azure DevOps.

---

# Regras de Negócio

## RN01

Na instalação do portal, a permissão administrador já existe. Nenhuma tela oferece a ação de criar essa permissão.

## RN02

A tela não oferece renomear a permissão administrador, alterar o que ela permite nem excluí-la.

## RN03

Atribuir ou retirar a permissão administrador de uma pessoa grava só o vínculo da pessoa. A definição da permissão permanece a mesma.

## RN04

Na primeira instalação, a permissão administrador fica atribuída à conta cujo e-mail de login no Entra ID é `ps.brunoe@aguiabranca.com.br`.

## RN05

Uma conta cujo e-mail de login no Entra ID seja diferente de `ps.brunoe@aguiabranca.com.br` não recebe a permissão administrador na primeira instalação.

## RN06

As permissões editor, aprovador e leitor não usam a trava da RN02. Esta US não implementa a edição delas.

---

# Critérios de Aceite

## CA01

Dado que o portal acabou de ser instalado

Quando a base de permissões é consultada

Então a permissão administrador existe e está atribuída somente a `ps.brunoe@aguiabranca.com.br`

## CA02

Dado que a pessoa autenticada abre a gestão de permissões

Quando ela procura as ações da permissão administrador

Então não existem as ações de criar, renomear, alterar o que ela permite nem excluir

## CA03

Dado que outra pessoa já entrou com um e-mail diferente de `ps.brunoe@aguiabranca.com.br`

Quando a primeira instalação termina

Então essa outra pessoa não possui a permissão administrador

## CA04

Dado que um administrador retira a permissão administrador de uma pessoa e atribui a outra

Quando a definição da permissão é consultada

Então o nome e o que ela permite continuam os da instalação, e só o vínculo das pessoas mudou

---

# Exemplos de Negócio

## Exemplo 01

### Cenário

Primeira instalação com dois logins já conhecidos.

### Entrada

* `ps.brunoe@aguiabranca.com.br`
* `outra.pessoa@aguiabranca.com.br`

### Resultado Esperado

Só `ps.brunoe@aguiabranca.com.br` possui a permissão administrador.

---

# Observações

* Depende de login pelo Entra ID apenas para comparar o e-mail. O Entra ID não é a fonte da permissão.
* A permissão fica no Supabase.
* Não criar work item no Azure DevOps a partir deste rascunho.
