# 155330 — Parametrizações > Fluxo de Fotos — Clonar parametrização (alterando o tipo de avaliação)

[Feature no Azure DevOps](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/155330)

---

# Referências

## Iniciativa / Epic

* [123128](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/123128) — Feature Backoffice Avalia GAB
* [122326](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/122326) — Epic pai (quando aplicável)

## Artefatos

* Tela de listagem (comportamento atual): [123129](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/123129) — Parametrização > Fluxo de Fotos — Listar
* Cadastro da parametrização (estrutura a ser copiada): [123302](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/123302) — Parametrizações > Fluxo de Fotos — Adicionar
* Edição (não é o fluxo desta Feature): [123301](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/123301)
* Origem do dropdown Tipo de Avaliação: [123130](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/123130)
* Protótipo da listagem / cadastro existente: [Figma — Backoffice Avalia GAB](https://www.figma.com/proto/cw65es6uHRrcBFn3LpHMaM/-DESIGN--APP---BACKOFFICE-AVALIA-GAB?node-id=5532-20046&t=9roGgY6JGMYYHBav-1&scaling=min-zoom&content-scaling=fixed&page-id=5277:5622&starting-point-node-id=5277:6247)
* Protótipo / imagem da modal de clone: *(a definir — ação nova na listagem)*
* Print da listagem atual (menu de três pontos com Editar / Inativar): anexo da conversa de refinamento

---

# Contexto

No Backoffice Avalia GAB, o cadastro de **Fluxo de Fotos** ([123302](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/123302)) exige montar Tipo de Vistoria, Tipo de Avaliação, Grupo de Categoria, seções e fotos (ordem, obrigatoriedade e demais configurações da parametrização).

Na prática, vários fluxos compartilham a mesma estrutura de seções e fotos e diferem apenas no **Tipo de Avaliação** (ex.: Rotina — Devolução GTF vs. Rotina — Entrega GTF, para o mesmo Tipo de Vistoria e Grupo de Categoria). Hoje o usuário precisa cadastrar o fluxo do zero, o que gera retrabalho e risco de divergência entre parametrizações equivalentes.

A listagem ([123129](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/123129)) já oferece, no menu de três pontos da coluna **Ações**, as opções **Editar** e **Inativar**/**Ativar**. Não existe ação de clonar.

---

# Objetivo

Permitir clonar um Fluxo de Fotos existente a partir da listagem, gerando um **novo** registro com a mesma parametrização (tipo de vistoria, grupo de categoria, seções, fotos, ordem e obrigatoriedade), alterando **somente** o Tipo de Avaliação escolhido pelo usuário, sem permitir combinação duplicada.

---

# Escopo

**Incluído:**

* Tela **Menu > Parametrizações > Fluxo de Fotos** (listagem)
* Nova ação **Clonar** no menu de três pontos da coluna Ações
* Modal de confirmação/clone com:
  * informações básicas do fluxo origem
  * quantidade de seções e de fotos que serão clonadas
  * dropdown obrigatório de **Tipo de Avaliação** (destino)
* Persistência de um **novo** Fluxo de Fotos (código novo, status inicial Ativo), copiando a estrutura da origem
* Validação de unicidade entre fluxos **Ativos** (mesma regra já usada ao **Ativar**): Tipo de Vistoria + Tipo de Avaliação + Grupo de Categoria

**Fora de escopo:**

* Alterar Tipo de Vistoria ou Grupo de Categoria no clone (permanecem iguais aos da origem)
* Editar seções/fotos dentro da modal de clone (o ajuste continua sendo pela tela de edição [123301](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/123301))
* Sincronização posterior entre origem e clone (são registros independentes)
* Alterar o formulário de cadastro ([123302](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/123302)) ou de edição ([123301](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/123301))
* Alterar a regra existente de **Ativar** na listagem (esta Feature apenas reutiliza a mesma validação de unicidade)
* Clone de vistoria operacional (fluxo distinto: [125084](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/125084))

**Telas / campos impactados:**

* Listagem Fluxo de Fotos — menu Ações (novo item Clonar)
* Nova modal Clonar Fluxo de Fotos
* Persistência do fluxo, seções e fotos (mesma estrutura do cadastro)

---

# Quem pode fazer

Usuários com permissão de **cadastrar Fluxo de Fotos** (mesma permissão da [123302](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/123302)).

Usuários sem essa permissão não devem visualizar a ação **Clonar** no menu de três pontos.

---

# Regras Gerais

## RG01

A ação **Clonar** deve ser exibida no menu de três pontos da coluna **Ações** da listagem de Fluxo de Fotos, juntamente com as ações já existentes (**Editar**, **Inativar** ou **Ativar**, conforme a situação do registro).

## RG02

A ação **Clonar** deve estar disponível para fluxos **Ativos** e **Inativos**. O clone não altera o registro origem.

## RG03

Ao clicar em **Clonar**, o sistema deve abrir uma modal (não navegar para a tela de cadastro).

## RG04

A modal deve exibir as informações básicas **somente leitura** do fluxo origem:

* Código
* Tipo de Vistoria
* Tipo de Avaliação (origem)
* Grupo de Categoria
* Situação (Ativo / Inativo)

## RG05

A modal deve informar a quantidade de seções e a quantidade de fotos que serão clonadas, calculadas a partir do fluxo origem:

* Quantidade de seções = número de seções vinculadas ao fluxo origem
* Quantidade de fotos = soma das fotos de todas as seções do fluxo origem

**Exemplo:** origem com 4 seções (3, 2, 5 e 1 fotos) → exibir **4 seções** e **11 fotos**.

## RG06

A modal deve conter o campo obrigatório **Tipo de Avaliação** (dropdown / listbox), cuja origem de dados é a lista de Tipos de Avaliação **ativos**, conforme [123130](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/123130).

## RG07

Não é permitido criar Fluxo de Fotos **Ativo** duplicado. A unicidade é a combinação:

**Tipo de Vistoria + Tipo de Avaliação + Grupo de Categoria**

A validação considera **apenas registros Ativos**, a mesma regra já existente ao **Ativar** um fluxo na listagem. Fluxos **Inativos** com a mesma combinação **não** bloqueiam o clone.

**Exemplo 1:** existe Ativo Frota + Rotina — Entrega GTF + Moto. Não é permitido clonar outro fluxo para essa combinação.

**Exemplo 2:** existe apenas Inativo Frota + Rotina — Entrega GTF + Moto. É permitido clonar para essa combinação, gerando um novo fluxo Ativo.

**Tipo de Vistoria** é obrigatório. O clone copia o valor da origem e não permite alterá-lo nem gravá-lo vazio.

## RG08

O dropdown de Tipo de Avaliação da modal deve listar apenas tipos **ativos** do cadastro ([123130](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/123130)) cuja combinação com o Tipo de Vistoria e o Grupo de Categoria da origem **não** exista em nenhum Fluxo de Fotos **Ativo**.

O Tipo de Avaliação da própria origem não deve aparecer no dropdown (o clone existe para criar a parametrização em **outro** tipo de avaliação; reativar a origem continua sendo a ação **Ativar**).

## RG09

Se não houver nenhum Tipo de Avaliação disponível no dropdown (todos os tipos ativos do cadastro já possuem fluxo **Ativo** para aquela combinação, ou não existem tipos ativos no cadastro), o sistema deve exibir a **MSG05**, manter o botão de confirmar desabilitado e não persistir clone.

## RG10

O botão de confirmar da modal permanece desabilitado enquanto o Tipo de Avaliação destino não estiver selecionado. **Cancelar** e o ícone **X** fecham a modal sem persistir.

## RG11

Ao confirmar, o sistema deve criar um **novo** Fluxo de Fotos contendo:

* Tipo de Vistoria = o da origem
* Grupo de Categoria = o da origem
* Tipo de Avaliação = o selecionado no dropdown
* Todas as seções da origem, na mesma ordem
* Todas as fotos de cada seção, na mesma ordem, com a mesma indicação de obrigatoriedade
* Demais atributos da parametrização de seção/foto existentes no cadastro (ex.: checkbox de seção obrigatória, quando houver)

## RG12

O clone deve receber um **código numérico novo**, gerado pelas mesmas regras do cadastro ([123302](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/123302)): código numérico de 6 dígitos, único, gerado automaticamente. O código da origem não é reutilizado.

## RG13

O novo fluxo deve ser gravado com situação inicial **Ativo**, mesmo que a origem esteja Inativa.

## RG14

O clone deve registrar log de cadastro no mesmo padrão do cadastro ([123302](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/123302)):

* Data no formato DD/MM/AAAA
* Usuário responsável (até 150 caracteres)

## RG15

Origem e clone são registros independentes. Alterações posteriores em um não alteram o outro.

## RG16

Não é permitido clonar um fluxo origem sem ao menos uma seção (regra alinhada ao cadastro, que exige ao menos uma seção). Nesse caso o sistema exibe a **MSG06** e não abre a persistência.

## RG17

A unicidade (RG07) deve ser revalidada no momento da persistência, com a mesma regra do **Ativar**. Se entre a abertura da modal e a confirmação outro usuário gravar um fluxo **Ativo** com a mesma combinação, o sistema não grava o clone e exibe a **MSG03**.

## RG18

Após clone com sucesso, o sistema fecha a modal, **mantém os filtros atuais** da listagem, **recarrega a tela** e exibe a **MSG01**. Não deve limpar filtros nem forçar troca da aba Ativos/Inativos.

## RG19

Em falha técnica não coberta pelas demais mensagens, o sistema exibe a **MSG02** e não cria registro parcial (fluxo sem seções/fotos).

---

# Mensagens

| Código | Texto |
| --- | --- |
| MSG01 | Fluxo de Fotos clonado com sucesso. |
| MSG02 | Erro ao clonar o Fluxo de Fotos. Tente novamente. |
| MSG03 | Já existe um Fluxo de Fotos ativo para este Tipo de Vistoria, Tipo de Avaliação e Grupo de Categoria. |
| MSG04 | Selecione o Tipo de Avaliação. |
| MSG05 | Não há Tipo de Avaliação disponível para clonar esta parametrização. |
| MSG06 | Não é possível clonar um Fluxo de Fotos sem seções. |

---

# Fluxo resumido

1. Usuário acessa Parametrizações > Fluxo de Fotos.
2. No registro desejado, abre o menu de três pontos e clica em **Clonar**.
3. Sistema abre a modal com dados da origem, totais de seções/fotos e dropdown de Tipo de Avaliação.
4. Usuário seleciona o Tipo de Avaliação destino e confirma.
5. Sistema valida unicidade e persiste o novo fluxo.
6. Sistema fecha a modal, recarrega a listagem mantendo os filtros e exibe a MSG01.

---

# Aprovação

| Campo | Valor |
| --- | --- |
| Status | [x] Aprovada pelo negócio |
| Data | |
| Responsável (negócio) | |

---

# Observações

* Modal de clone **não** existe no Figma atual; o visual deve seguir o padrão das demais modais do Fluxo de Fotos (Adicionar Seções / Definir fotos).
* Decomposição sugerida após aprovação: **uma US** (ação na listagem + modal + persistência + unicidade), salvo se o time quiser separar front e API.

## Decisões de refinamento (11/09/2026)

1. **Tipo de Vistoria é obrigatório** na parametrização; o clone sempre copia o valor da origem (RG07).
2. **Unicidade apenas entre Ativos**, reutilizando a validação já existente ao **Ativar**. Inativos não bloqueiam o clone (RG07).
3. Clone a partir de origem Inativa **nasce Ativo** (RG13).
4. Textos das mensagens **MSG01 a MSG06** aprovados pelo negócio. MSG03 ajustada para deixar explícito que a duplicidade é de fluxo **ativo**.
5. Após sucesso: **manter os filtros e recarregar a tela** (RG18).
6. Permissão: a **mesma de cadastrar Fluxo de Fotos**.
