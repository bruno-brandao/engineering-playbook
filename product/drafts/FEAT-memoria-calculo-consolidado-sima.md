# SIMA — Memória de cálculo da placa no consolidado

Rascunho local. Ainda não existe work item no Azure DevOps. Não aplicar este texto automaticamente.

---

# Referências

## Iniciativa / Epic

* A definir

## Artefatos

* Tela: consolidado do SIMA (caminho de menu a confirmar)
* Reclamação do cliente: *"como vou saber se o parâmetro lançado está calculando correto? Como vou saber se a placa assumiu valores do bem e se não, se tenho que colocar na mão?"*
* Protótipo: a definir

---

# Contexto

No SIMA, o cálculo do consolidado usa parâmetros e regras que podem variar conforme o dado — em especial conforme a placa do ativo. O consolidado mostra o resultado nas linhas, mas não mostra o que entrou naquele cálculo.

Quem consulta o consolidado não consegue verificar se o parâmetro lançado foi o valor usado, nem se a placa assumiu os valores do bem. Quando o bem não fornece o valor, também não fica explícito que o lançamento precisa ser feito na mão.

Uma placa gera várias linhas no consolidado. O que varia de linha para linha é o resultado exibido na grade. Os parâmetros e as regras da placa, naquele cálculo, são os mesmos para essas linhas.

---

# Objetivo

Gravar, no momento do cálculo do consolidado, a memória dos principais parâmetros e regras usados para a placa, e permitir que o usuário abra, a partir de qualquer linha dessa placa, um resumo somente leitura que responda:

* qual valor entrou no cálculo;
* se esse valor foi assumido do bem do ativo;
* se não foi assumido do bem, que o valor depende de lançamento manual.

---

# Escopo

**Incluído:**

* Gravação da memória de cálculo da placa no momento em que o consolidado é calculado
* Uma memória por placa naquele cálculo, compartilhada pelas linhas da mesma placa
* Ação em cada linha do consolidado para abrir o resumo dessa memória
* Resumo somente leitura, com valor usado e origem de cada parâmetro ou regra principal

**Fora de escopo:**

* Alterar a fórmula, a grade ou o resultado do consolidado
* Alterar o cadastro de parâmetros, o bem do ativo ou o lançamento manual
* Editar valores a partir do resumo
* Agrupar, reordenar ou fundir as linhas do consolidado
* Reconstruir a memória de consolidados calculados antes desta entrega
* Exportar a memória (planilha, PDF ou API)

**Telas impactadas:**

* Consolidado do SIMA — nova ação na linha e painel de resumo da memória da placa

---

# Quem pode fazer

Quem já consulta o consolidado abre o resumo. Esta entrega não cria permissão nova.

Quem não consulta o consolidado não vê a ação.

---

# Decisão de desenho

A memória é da **placa naquele cálculo**, não da linha.

O sistema grava um único resumo por placa quando o consolidado é calculado. Cada linha da placa guarda apenas a referência a esse resumo. A ação continua em todas as linhas, porque o usuário pode chegar em qualquer uma delas por filtro ou ordenação. Linhas da mesma placa abrem o mesmo conteúdo.

O painel informa a placa e quantas linhas daquele consolidado compartilham o resumo, para o usuário entender por que outra linha da mesma placa mostra o mesmo dado.

Alterar parâmetro, bem ou lançamento manual depois do cálculo não reescreve a memória já gravada. O resumo responde o que foi usado naquele cálculo, não o que está cadastrado agora.

Se o consolidado daquela placa for recalculado, a memória exibida passa a ser a do novo cálculo.

---

# Regras Gerais

## RG01 — Gravar no cálculo

Ao calcular o consolidado, o sistema grava a memória da placa com os principais parâmetros e regras que podem variar conforme o dado, e com o valor efetivamente usado em cada um.

A lista fechada desses parâmetros e regras fica pendente de confirmação do negócio. Enquanto essa lista não existir, a regra não nomeia campos.

## RG02 — Uma memória por placa

Naquele cálculo, existe uma memória por placa.

Todas as linhas geradas pela mesma placa apontam para essa memória. O sistema não grava uma cópia do resumo em cada linha.

## RG03 — Ação na linha

Cada linha do consolidado oferece a ação **Memória de cálculo**.

A ação abre o resumo da placa daquela linha. Linhas da mesma placa, no mesmo cálculo, abrem o mesmo resumo.

## RG04 — Alcance do resumo

O resumo identifica a placa e informa que o conteúdo vale para todas as linhas dessa placa naquele consolidado, incluindo a quantidade de linhas.

Exemplo de identificação: `Placa ABC1D23 · 4 linhas neste consolidado`.

## RG05 — O que o resumo responde

Para cada parâmetro ou regra principal da RG01, o resumo mostra:

* o nome do parâmetro ou da regra;
* o valor usado no cálculo;
* a origem do valor.

Origens desta entrega:

| Origem | Significado para o usuário |
| --- | --- |
| Assumido do bem | A placa usou o valor do bem do ativo |
| Lançado manualmente | O valor usado foi informado na mão |
| Não assumido do bem | O bem não forneceu o valor. O lançamento manual é necessário |

Quando a origem é **Não assumido do bem** e ainda não há valor lançado, o resumo não exibe um valor calculado para esse item. Exibe a origem e a indicação de que o lançamento manual é necessário.

Quando a origem é **Lançado manualmente**, o resumo exibe o valor que entrou no cálculo, para o usuário conferir o que foi lançado.

## RG06 — Somente leitura

O resumo não altera parâmetro, bem, lançamento manual nem as linhas do consolidado.

Fechar o resumo devolve o usuário à mesma consulta do consolidado, com filtros e ordenação preservados.

## RG07 — Memória do cálculo gravado

O resumo exibe a memória gravada naquele cálculo.

Mudança posterior em parâmetro, bem ou lançamento manual não altera a memória já gravada. Essa mudança só aparece se o consolidado for recalculado.

## RG08 — Recálculo

No recálculo do consolidado, o sistema substitui a memória da placa pela memória do novo cálculo.

O resumo aberto depois do recálculo mostra somente a memória nova.

---

# Exemplos

Os nomes de parâmetro abaixo são ilustrativos. A lista real depende da confirmação da RG01.

## Exemplo 01 — Placa com várias linhas e origens misturadas

A placa `ABC1D23` gerou 4 linhas no consolidado.

A memória gravada no cálculo:

| Parâmetro | Valor usado | Origem |
| --- | --- | --- |
| Parâmetro lançado | 1.250,00 | Lançado manualmente |
| Valor vindo do bem | 80.000,00 | Assumido do bem |
| Vida útil | — | Não assumido do bem |

Qualquer uma das 4 linhas abre o mesmo painel: `Placa ABC1D23 · 4 linhas neste consolidado`, com a tabela acima.

## Exemplo 02 — Conferir o parâmetro lançado

O usuário lançou `1.250,00` para a placa `ABC1D23` e calculou o consolidado.

Ao abrir a memória por uma linha dessa placa, o item correspondente mostra valor `1.250,00` e origem **Lançado manualmente**.

## Exemplo 03 — Bem sem valor

O bem da placa `DEF2G34` não possui o valor de um parâmetro principal, e ninguém lançou o valor na mão.

A memória desse item mostra origem **Não assumido do bem**, sem valor usado, e indica que o lançamento manual é necessário.

## Exemplo 04 — Cadastro muda depois do cálculo

O consolidado da placa `ABC1D23` já foi calculado com o parâmetro `1.250,00`.

Depois disso, o usuário altera o parâmetro lançado para `1.800,00` e não recalcula.

A memória continua mostrando `1.250,00`. O valor `1.800,00` só entra na memória se o consolidado for recalculado.

---

# Aprovação

| Campo | Valor |
| --- | --- |
| Status | [ ] Aprovada pelo negócio |
| Data | |
| Responsável (negócio) | |

---

# Observações

* A Feature não está aprovada. Não decompor em User Stories até a aprovação e o fechamento das pendências abaixo.
* Dependência de implementação: o cálculo atual do consolidado precisa expor, por placa, o valor usado e a origem (bem, lançamento manual ou ausência no bem). O formato técnico de persistência fica para a decomposição.
* A ação repetida na linha é intencional. O dado gravado não se repete.

---

# Pendências para o negócio

Confirmar antes de registrar no Azure DevOps:

1. Lista dos parâmetros e regras principais que entram na memória, com nome exibido ao usuário.
2. Caminho de menu e nome oficial da tela de consolidado.
3. Se "não assumido do bem" e "lançado manualmente" cobrem todas as origens reais, ou se existe outra fonte (parametrização padrão, exceção por placa, outro cadastro).
4. Se algum parâmetro varia por linha, e não só por placa. Se variar, esse item sai da memória compartilhada e precisa de regra própria.
5. O que identifica "aquele cálculo": competência, lote, data do processamento ou outro recorte. A mesma placa pode ter mais de um consolidado vigente ao mesmo tempo?
6. Recálculo substitui a memória (RG08) ou o negócio precisa consultar também o cálculo anterior.
7. Consolidados já calculados ficam sem memória, como está no fora de escopo, ou há necessidade de recalcular o histórico.
8. Quem consulta o consolidado é o público certo, e o nome da ação **Memória de cálculo** está adequado.
