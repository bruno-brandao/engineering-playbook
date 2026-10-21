# 145031 — Solicitar nome e telefone do cliente na assinatura

[Feature no Azure DevOps](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/145031)

Título sugerido para substituir o atual (*App - Adicionar o cliente e CR no fluxo de vistoria*):

**App - Solicitar nome e telefone do cliente na assinatura**

Este texto substitui a descrição vigente da Feature. A versão no Azure DevOps ainda fala em CR e na primeira etapa da vistoria. Não aplicar este rascunho automaticamente no Azure DevOps.

---

# Referências

## Iniciativa / Epic

* [143458](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/143458) — [Melhorias Funcionais] - 2026

## Artefatos

* Cadastro do Tipo de Avaliação: **Cadastrar Tipo de Avaliação** (`/parametrizacao-tipos-avaliacao`)
* Interruptor já existente, não alterado por esta Feature: **Solicitar assinatura do cliente** (`PossuiAssinaturaCliente`)
* Nome já gravado na vistoria: `NomeCliente` (varchar 250), enviado hoje na finalização do app
* Tela de captura: assinatura do cliente no app Avalia+
* Consulta: **Vistorias** (`/vistorias`)
* Aba **Assinatura** de **Visualizar vistoria** e **Avaliar vistoria** (`/vistorias/visualizar/{id}` e `/vistorias/avaliar/{id}`)
* Laudo: `VistoriaLaudo.html` (seção **Dados do Cliente/Condutor**)

---

# Contexto

A descrição atual da Feature pede Cliente e CR na primeira etapa da nova vistoria, no laudo e na consulta. Essa descrição está incorreta.

Não há mudança de CR. O nome e o telefone do cliente são informados na tela de assinatura do cliente do app Avalia+, não no passo de dados da vistoria.

---

# Objetivo

Permitir que o Tipo de Avaliação peça, na assinatura do cliente, o **nome** e o **telefone** do cliente, e que o Backoffice mostre esses dois dados na consulta, na aba **Assinatura** da vistoria e no laudo.

---

# Escopo

**Incluído:**

* Interruptor **Solicitar nome e telefone do cliente** no Tipo de Avaliação, desligado por padrão
* App Avalia+: campos **Nome do cliente** e **Telefone do cliente** na tela de assinatura do cliente, somente quando o interruptor estiver ligado
* Persistência do nome e do telefone na vistoria
* Backoffice: colunas **Cliente** e **Telefone** na grid e no Excel, colunas **Nome** e **Telefone** na aba **Assinatura** da vistoria e linhas no laudo

**Fora de escopo:**

* Qualquer alteração de CR (campo, coluna, histórico, centro de resultado, laudo)
* Cliente Wave, CNPJ do Cliente Wave e o parâmetro `PossuirClienteCR`
* Pedir nome ou telefone no passo 1 (dados da vistoria)
* Exibir nome ou telefone na aba **Veículo** (Dados da vistoria)
* Alterar CPF, e-mail, foto da assinatura ou o interruptor **Solicitar assinatura do cliente**
* Editar nome ou telefone depois da assinatura, no app ou no Backoffice
* Nova permissão

---

# Quem pode fazer

Quem já inclui ou edita Tipo de Avaliação altera o interruptor novo.

Quem já realiza a vistoria no app e chega na assinatura do cliente informa nome e telefone, quando o interruptor estiver ligado.

Quem já consulta a vistoria, a aba **Assinatura** ou o laudo no Backoffice vê os dados gravados.

---

# Regras Gerais

## RG01 — Interruptor no Tipo de Avaliação

O cadastro de Tipo de Avaliação, nas telas Novo e Editar, exibe o interruptor **Solicitar nome e telefone do cliente**, na mesma linha de **Requer Avaliação** e **Solicitar assinatura do cliente**.

Em um tipo novo, o interruptor inicia desligado. Na edição, abre com o valor gravado. Salvar sem mexer no interruptor mantém o valor. Inativar ou reativar o tipo não altera o interruptor.

## RG02 — Onde os campos aparecem no app

**Nome do cliente** e **Telefone do cliente** aparecem somente na tela de assinatura do cliente.

Eles aparecem juntos quando as duas condições são verdadeiras:

* **Solicitar assinatura do cliente** está ligado nesse Tipo de Avaliação
* **Solicitar nome e telefone do cliente** está ligado nesse Tipo de Avaliação

Se qualquer um dos dois estiver desligado, a tela de assinatura não exibe esses dois campos. O interruptor novo não abre a tela de assinatura por conta própria.

O passo de dados da vistoria não exibe nome nem telefone do cliente.

## RG03 — Preenchimento

Quando os campos estão visíveis, os dois são obrigatórios para confirmar a assinatura do cliente.

* **Nome do cliente:** texto, sem ser só espaços, no máximo 250 caracteres
* **Telefone do cliente:** celular com DDD, 11 dígitos, máscara `(00) 00000-0000`

O botão de confirmar a assinatura permanece desabilitado enquanto nome ou telefone estiverem inválidos.

CPF, e-mail e a imagem da assinatura seguem como estão hoje.

## RG04 — O que fica gravado

Ao confirmar a assinatura com os campos visíveis, a vistoria grava o nome e o telefone informados. O telefone é persistido só com os 11 dígitos.

Com os campos ocultos, a confirmação da assinatura não grava telefone novo e não exige nome nesta Feature.

## RG05 — Consulta no Backoffice

A grid de vistorias e o Excel exportado incluem **Cliente** e **Telefone** para todas as vistorias, tenham o interruptor ligado ou não.

* **Cliente:** nome gravado na assinatura. Sem nome, a grid mostra `--` e o Excel deixa a célula vazia.
* **Telefone:** os 11 dígitos exibidos como `(00) 00000-0000`. Sem telefone, a grid mostra `--` e o Excel deixa a célula vazia.

As colunas de CR já existentes não mudam.

## RG06 — Aba Assinatura da vistoria

Em **Visualizar vistoria** e **Avaliar vistoria**, a aba **Assinatura** mantém a tabela atual (**Visualizar**, **Responsável**, **Data de envio**, **Usuário**) e inclui as colunas **Nome** e **Telefone**, nesta ordem, depois de **Usuário**.

* Na linha em que **Responsável** é **Cliente**, **Nome** é o nome gravado na assinatura e **Telefone** é o telefone gravado, na máscara `(00) 00000-0000`. Sem valor, a célula mostra `--`.
* Na linha em que **Responsável** é **Vistoriador**, **Nome** e **Telefone** mostram `--`.

Os campos são somente leitura. A aba **Veículo** não exibe nome nem telefone do cliente.

## RG07 — Laudo

Na seção **Dados do Cliente/Condutor** do PDF, a linha **Nome completo** usa o nome gravado na assinatura. A seção passa a ter a linha **Telefone** com o telefone gravado, na máscara `(00) 00000-0000`.

Sem telefone gravado, a linha **Telefone** não aparece. Sem nome gravado, a linha **Nome completo** permanece como está hoje.

A linha **Centro de resultado** e as demais linhas de CR não mudam.

---

# Critérios de aceite

1. Novo Tipo de Avaliação abre com **Solicitar nome e telefone do cliente** desligado.
2. Editar e salvar liga ou desliga o interruptor e a próxima abertura mostra o valor salvo.
3. Com os dois interruptores ligados, a tela de assinatura do cliente no app exibe **Nome do cliente** e **Telefone do cliente**.
4. Com **Solicitar nome e telefone do cliente** desligado, esses dois campos não aparecem na assinatura.
5. O passo de dados da vistoria não exibe nome nem telefone do cliente.
6. Com os campos visíveis, não é possível confirmar a assinatura sem nome válido e telefone de 11 dígitos.
7. A grid, o Excel e a aba **Assinatura** mostram o nome e o telefone gravados, ou vazio conforme a RG05 e a RG06. A aba **Veículo** não mostra esses campos.
8. O laudo mostra o telefone gravado e não altera CR.
9. Nenhuma tela desta Feature altera coluna, campo ou texto de CR.

---

# Exemplos

## Exemplo 01 — Assinatura com os dois interruptores ligados

Tipo de Avaliação com **Solicitar assinatura do cliente** e **Solicitar nome e telefone do cliente** ligados.

Nome: `Maria Souza`. Telefone digitado: `(27) 99999-0000`.

A assinatura confirma. A vistoria grava o nome `Maria Souza` e o telefone `27999990000`. A grid mostra `Maria Souza` e `(27) 99999-0000`. Na aba **Assinatura**, a linha **Cliente** mostra o mesmo nome e o mesmo telefone. A linha **Vistoriador** mostra `--` nas duas colunas.

## Exemplo 02 — Parâmetro desligado

Mesmo vistoriador, Tipo de Avaliação com **Solicitar nome e telefone do cliente** desligado.

A tela de assinatura não mostra nome nem telefone desta Feature. O passo de dados da vistoria também não mostra.

## Exemplo 03 — Telefone incompleto

Campos visíveis. Nome `Maria Souza`. Telefone `99999-0000` (sem DDD, 9 dígitos).

A assinatura não confirma.

---

# Premissas deste rascunho

Confirmar antes de colar no Azure DevOps:

1. Nome e telefone são obrigatórios para confirmar a assinatura quando os campos estão visíveis.
2. O telefone é celular com DDD, 11 dígitos.
3. O interruptor novo não liga sozinho **Solicitar assinatura do cliente**. Sem a tela de assinatura, nome e telefone não são pedidos.
4. A consulta mostra o que foi gravado, mesmo que o interruptor seja desligado depois.
