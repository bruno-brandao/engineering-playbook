# 152449 — Parcelamento via cartão de crédito na plataforma de vendas (INT015)

[Feature no Azure DevOps](https://dev.azure.com/aguiabranca/Ativos%20-%20Plataforma%20de%20Vendas/_workitems/edit/152449)

---

# Referências

## Iniciativa / Epic

* [152449](https://dev.azure.com/aguiabranca/Ativos%20-%20Plataforma%20de%20Vendas/_workitems/edit/152449) — Parcelamento via cartão de crédito na plataforma de vendas (INT015)
* Integração INT015 — Parcelamento de Cartão de Crédito

## Artefatos

* Protótipo / imagem da tela: *(a definir)*
* Documento complementar: Análise de impacto — FW Diretoria de Ativos | Integração INT015 — Dúvidas sobre Parcelamento de Cartão de Créditos
* E-mail Meyrielen: código SAP `"X"` para crédito no `tipoVencimento`
* Observação DTI: outras intervenções INT015 em avaliação — avaliar empacotamento se houver mudança de contrato/SOA

---

# Contexto

Na plataforma de vendas, as formas de pagamento disponíveis na tela **Em Negociação** são apenas **Boleto** e **Crédito em conta**. O parcelamento já existe, porém utiliza crédito em conta (depósito), não cartão de crédito.

No envio SAP via INT015, o campo `tipoVencimento` só é montado quando há boleto, no formato `B|{condicaoPagamentoSAP}|{codigoBanco}`. Quando a negociação é apenas crédito em conta / parcelamento sem boleto, o campo `tipoVencimento` não é enviado no payload.

É necessário disponibilizar **parcelamento via cartão de crédito**, alinhando a plataforma e o payload INT015 ao código **`X`** (crédito) no primeiro segmento de `tipoVencimento`, no formato:

`Forma de pagamento | Condição de Pagamento SAP | Código do Banco`

> Atenção: não confundir **Crédito em conta** (depósito) com **Cartão de crédito** SAP (`X`).

---

# Objetivo

Permitir a seleção de **Cartão de crédito** como forma de pagamento exclusivamente em **parcelamento**, e enviar corretamente o `tipoVencimento` com prefixo **`X`** na INT015, alinhado às condições habilitadas no SAP e no SOA.

---

# Escopo

**Incluído:**

* Tela **Em Negociação** — incluir opção Cartão de crédito no select de forma de pagamento (somente PARCELAMENTO)
* Persistência do novo tipo de forma de pagamento (ex.: `CARTAO_CREDITO`)
* Envio INT015 — montar `tipoVencimento = X|{condicaoSAP}|{banco}` para cartão
* Exibição do novo tipo nas telas Aguardando Liberação de Crédito, Documentação Pendente e listagens/relatórios (`FORMA_PRINCIPAL`)
* Cadastro/ativação das condições de pagamento SAP de parcelamento cartão em QAS
* Reutilizar as validações já existentes das demais condições de pagamento

**Telas impactadas:**

* Em Negociação (`/pageemnegociacao`) — escolha e cadastro da forma
* Aguardando Liberação de Crédito — exibição + seleção da condição SAP
* Documentação Pendente — exibição do tipo
* Cadastro Condição Pagamento SAP (`/pagecondpagamento`)
* Listagens / relatórios / ficha de venda — rótulo da forma principal

**Fora de escopo:**

* Cartão de crédito à vista
* Combinações de formas de pagamento (ex.: entrada em outra forma + parcelamento em cartão)
* Tela de comissão parceiro
* Telas liberado para retirada / vendido
* Fluxo parceiro faturamento

---

# Quem pode fazer

Usuários com acesso à tela **Em Negociação** e aos fluxos de liberação de crédito, documentação pendente e cadastro de condição de pagamento SAP, conforme permissões já existentes da plataforma de vendas.

---

# Regras Gerais

## RG01

O sistema deve disponibilizar a forma de pagamento **Cartão de crédito** na tela Em Negociação, distinta de **Boleto** e de **Crédito em conta**.

## RG02

Ao cadastrar forma Cartão de crédito, o sistema deve persistir o tipo correspondente (ex.: `CARTAO_CREDITO`) em `NGCIA_FORMA_PAGAMENTO.DS_TIPO`.

## RG03

Cartão de crédito deve estar disponível **somente** para **PARCELAMENTO**. Não deve ser oferecido para pagamento à vista.

## RG04

Quando a forma enviada à INT015 for Cartão de crédito, o sistema deve montar:

`tipoVencimento = X|{condicaoPagamentoSAP}|{codigoBanco}`

## RG05

Quando a forma for Boleto, o sistema mantém:

`tipoVencimento = B|{condicaoPagamentoSAP}|{codigoBanco}`

e continua preenchendo `numeroBoleto` conforme as regras atuais.

## RG06

A negociação utiliza **apenas uma** condição/forma de pagamento. O campo `tipoVencimento` deve ser enviado no payload INT015 quando a forma for **boleto** ou **cartão de crédito**.

## RG07

Para Cartão de crédito, o sistema **não** deve exigir nem enviar `numeroBoleto` no payload INT015.

## RG08

No formato `X|condição|banco`, a condição de pagamento SAP e o código do banco devem existir e estar disponíveis em QAS.

## RG09

Somente condições de pagamento SAP cadastradas/ativas e habilitadas para parcelamento via cartão devem ser selecionáveis no fluxo de faturamento / liberação de crédito.

## RG10

As validações de valor, parcelas, documentos e demais regras aplicadas às condições de pagamento já existentes devem ser **as mesmas** para Cartão de crédito.

## RG11

Não haverá combinações de formas de pagamento envolvendo Cartão de crédito. O parcelamento via cartão é a condição única da negociação.

## RG12

Telas e listagens que exibem forma de pagamento devem apresentar rótulo legível para **Cartão de crédito** (não classificar como Depósito nem como Boleto).

## RG13

**Crédito em conta** continua representando depósito e **não** deve gerar prefixo `X` no `tipoVencimento`.

---

# Aprovação

| Campo | Valor |
| --- | --- |
| Status | [x] Aprovada pelo negócio |
| Data | 25/05/2026 |
| Responsável (negócio) | Camila Delai |

---

# Observações

## Integração

* Integração impactada: **INT015** (envio SAP)
* Prefixo cartão no `tipoVencimento`: **`X`**
* Prefixo boleto (atual): **`B`**

## Decisões de negócio

| Tema | Decisão |
| --- | --- |
| Escopo de uso | Cartão apenas em PARCELAMENTO (não à vista) |
| Condição de pagamento | Apenas uma condição por negociação |
| `numeroBoleto` | Não é enviado para cartão |
| Cadastro QAS | Condição SAP e banco devem existir em QAS |
| Validações | Mesmas das condições de pagamento existentes |
| Combinações | Não haverá combinações de formas com cartão |

## Dependências

* Garantir em QAS a existência da condição de pagamento SAP e do código do banco para o formato `X|condição|banco`
* Avaliar com DTI se o ajuste deve ser empacotado com outras intervenções INT015 em avaliação
