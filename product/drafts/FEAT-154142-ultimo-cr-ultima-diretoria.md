# 154142 — Último CR e última diretoria nas grades de desmobilização

[Feature no Azure DevOps](https://dev.azure.com/aguiabranca/AtivosCompraMobilizacao/_workitems/edit/154142)

Título atual: *[12550737112] Inclusão coluna e campo Preservação da Diretoria de Origem*

Título sugerido para o work item:

**[12550737112] Exibir último CR e última diretoria nas grades de desmobilização**

Epic pai: [143894](https://dev.azure.com/aguiabranca/AtivosCompraMobilizacao/_workitems/edit/143894) — [Melhorias Funcionais] D. Ativos - 2026

Este texto substitui a descrição vigente. A versão no Azure DevOps fala em BI, ZFI e preservação de diretoria de origem. Não aplicar este rascunho automaticamente no Azure DevOps.

---

# Título

Como usuário das grades de desmobilização, quero visualizar e filtrar o último CR operacional e a última diretoria, para consultar a origem operacional do ativo junto com o CR e a diretoria atuais.

---

# Descrição

As grades do processo de desmobilização já mostram e filtram o CR atual e a diretoria atual do ativo. O CR atual ocupa duas colunas: **Número CR** e **Descrição CR**. A diretoria atual ocupa a coluna **Diretoria**. Esses valores são lidos do planejamento atual. A desmobilização não grava centro de resultado nem diretoria.

O planejamento também já tem o último CR operacional do ativo e, nesse CR, a diretoria cadastrada. As grades e as exportações não exibem nem filtram esses dados. Quem consulta o processo não distingue o CR e a diretoria atuais do último CR operacional e da diretoria desse CR.

O valor exibido é o estado atual do planejamento. Ele acompanha o ativo. A desmobilização não fotografa esses dados na abertura, na aprovação nem na conclusão.

---

# Regras de negócio

## RN01 — Último CR

Último CR é o último centro de resultado operacional do planejamento (`UltimoCentroResultadoOperacional`).

Na grade e na exportação ele ocupa duas colunas, no mesmo desenho de Número CR e Descrição CR:

* **Número Último CR** — código do último CR operacional, no mesmo formato de Número CR
* **Descrição Último CR** — nome do último CR operacional, no mesmo formato de Descrição CR

Essas colunas ficam imediatamente depois de Descrição CR: Número CR, Descrição CR, Número Último CR, Descrição Último CR.

## RN02 — Última diretoria

Última diretoria é a diretoria cadastrada no último CR operacional.

Não existe campo próprio de última diretoria. A descrição exibida é a da diretoria desse centro de resultado.

A coluna **Última Diretoria** fica imediatamente depois de Diretoria.

## RN03 — Estado atual, sem fotografia

Cada processo de desmobilização aponta para o ativo pelo planejamento atual.

Último CR e última diretoria acompanham o planejamento atual. A abertura, a aprovação e a conclusão da desmobilização não gravam esses valores no processo.

Uma mudança posterior do último CR operacional no planejamento passa a aparecer nas grades, inclusive no histórico de aprovações e nos processos já concluídos.

## RN04 — CR atual e diretoria atual

Número CR, Descrição CR, Diretoria e os filtros de CR atual e de diretoria atual permanecem, com o comportamento que já têm hoje.

CR atual e último CR podem ser diferentes. Diretoria atual e última diretoria também podem ser diferentes.

## RN05 — Registro sem último CR operacional

Quando o planejamento não tem último CR operacional, Número Último CR, Descrição Último CR e Última Diretoria ficam em branco.

Esse registro não entra no resultado quando o filtro de último CR ou o filtro de última diretoria está preenchido.

## RN06 — Filtros

As grades que já filtram CR e diretoria passam a aceitar, no mesmo padrão de `DiretoriaIds` e `CentroResultadoIds`:

* `UltimoCentroResultadoIds` — seleção múltipla pelo id do último CR operacional
* `UltimaDiretoriaIds` — seleção múltipla pelo id da diretoria do último CR operacional

O filtro de última diretoria considera a diretoria do último CR operacional, não a diretoria do CR atual.

A combinação entre filtros, inclusive com `DiretoriaIds` e `CentroResultadoIds`, segue o padrão já usado nessas grades.

## RN07 — Ordenação

A ordenação de Número Último CR segue Número CR. A de Descrição Último CR segue Descrição CR. A de Última Diretoria segue Diretoria.

Registros com a coluna em branco ocupam a mesma posição relativa já usada quando Número CR, Descrição CR ou Diretoria estão vazios.

## RN08 — Permissão

A permissão de visualização permanece a de cada tela atual e olha apenas para o CR atual e a diretoria atual.

Quem já vê o registro vê Número Último CR, Descrição Último CR e Última Diretoria. Essas colunas não têm recorte próprio: o valor aparece mesmo quando o último CR operacional, ou a diretoria dele, está fora dos centros de resultado e diretorias permitidos ao usuário.

## RN09 — Grades e exportações

Número Último CR, Descrição Último CR e Última Diretoria entram na grade e na exportação, na ordem definida em RN01 e RN02. Os filtros novos entram nas mesmas consultas:

| Tela | Consulta | Exportação |
| --- | --- | --- |
| Acompanhamento | `GET api/PlanejamentoDesmobilizacao/acompanhamento` | `POST exportar-acompanhamento` |
| Radar | `GET radar` | `POST exportar-radar` |
| Aprovações aguardando análise | `GET aprovacoes-aguardando-analise` | `POST exportar-aprovacoes-aguardando-analise` |
| Histórico de aprovações | `GET aprovacoes-historico` | `POST exportar-aprovacoes-historico` |
| Gestão da desmobilização | `GET gestao-desmobilizacao` | `POST exportar-gestao-desmobilizacao` |
| Análise fiscal | `GET analise-fiscal` | `POST analise-fiscal/exportar` |

A exportação usa os mesmos filtros da consulta, inclusive `UltimoCentroResultadoIds` e `UltimaDiretoriaIds`, repete o valor exibido na grade e mantém a mesma ordem de colunas.

---

# Critérios de aceite

## Grade

### CA01 — Colunas nas seis grades

Dado um processo de desmobilização cujo planejamento tem CR atual e último CR operacional preenchidos, iguais ou diferentes

Quando o usuário abre Acompanhamento, Radar, Aprovações aguardando análise, Histórico de aprovações, Gestão da desmobilização ou Análise fiscal

Então cada grade exibe Número Último CR e Descrição Último CR imediatamente depois de Descrição CR, com código e nome no mesmo formato de Número CR e Descrição CR

E exibe Última Diretoria imediatamente depois de Diretoria, com a diretoria cadastrada nesse último CR

E Número CR, Descrição CR e Diretoria continuam visíveis, com os valores do CR atual do planejamento

### CA02 — Valor corrente também no histórico e no processo concluído

Dado um processo já aprovado ou concluído

E que o último CR operacional do planejamento foi alterado depois da aprovação ou da conclusão

Quando o usuário abre qualquer uma das seis grades, inclusive o Histórico de aprovações

Então Número Último CR, Descrição Último CR e Última Diretoria mostram o último CR operacional atual do planejamento e a diretoria desse CR

### CA03 — Ordenação

Dada uma grade com processos de último CR e última diretoria diferentes, inclusive registros em branco

Quando o usuário ordena por Número Último CR

Então a ordem segue o mesmo critério de Número CR

Quando o usuário ordena por Descrição Último CR

Então a ordem segue o mesmo critério de Descrição CR

Quando o usuário ordena por Última Diretoria

Então a ordem segue o mesmo critério de Diretoria

### CA04 — Permissão só no atual

Dado um processo visível para o usuário pelo CR atual e pela diretoria atual

E cujo último CR operacional, ou a diretoria desse CR, está fora dos centros de resultado e diretorias permitidos a ele

Quando o usuário abre a grade ou exporta o resultado

Então Número Último CR, Descrição Último CR e Última Diretoria mostram o valor do planejamento

E o registro não é ocultado por causa do último CR nem da última diretoria

## Filtro

### CA05 — Filtro de último CR

Dado processos com último CR operacional A, último CR operacional B e sem último CR operacional

Quando o usuário preenche `UltimoCentroResultadoIds` apenas com o id de A, em qualquer uma das seis consultas

Então o resultado traz os processos cujo último CR operacional é A

E não traz os de B nem os sem último CR operacional

### CA06 — Filtro de última diretoria usa o último CR

Dado um processo cujo CR atual pertence à diretoria X e cujo último CR operacional pertence à diretoria Y

Quando o usuário preenche `UltimaDiretoriaIds` apenas com o id de Y

Então o processo entra no resultado

Quando o usuário preenche `UltimaDiretoriaIds` apenas com o id de X

Então o processo fica de fora, ainda que a diretoria atual seja X

### CA07 — Filtros atuais preservados e combinados

Dado os filtros `DiretoriaIds` e `CentroResultadoIds` já existentes

Quando o usuário combina um deles com `UltimoCentroResultadoIds` ou `UltimaDiretoriaIds`

Então CR atual e diretoria atual continuam filtrando pelo CR atual

E a combinação entre os filtros segue o padrão já usado na grade

E a seleção múltipla de cada filtro novo continua sendo por id

## Exportação

### CA08 — Colunas nos seis arquivos

Dado um conjunto de processos retornado por uma das seis consultas, com e sem último CR operacional

Quando o usuário exporta por `POST exportar-acompanhamento`, `POST exportar-radar`, `POST exportar-aprovacoes-aguardando-analise`, `POST exportar-aprovacoes-historico`, `POST exportar-gestao-desmobilizacao` ou `POST analise-fiscal/exportar`

Então o arquivo contém Número Último CR e Descrição Último CR depois de Descrição CR, e Última Diretoria depois de Diretoria, no mesmo formato da grade

E contém as mesmas linhas da consulta, já aplicados `UltimoCentroResultadoIds` e `UltimaDiretoriaIds` quando informados

E Número CR, Descrição CR e Diretoria permanecem no arquivo

## Registro sem último CR

### CA09 — Colunas em branco

Dado um processo cujo planejamento está sem último CR operacional

Quando o usuário abre qualquer uma das seis grades ou exporta o resultado sem preencher os filtros novos

Então Número Último CR, Descrição Último CR e Última Diretoria ficam em branco nesse registro

E o registro continua na grade e na exportação se os demais filtros o incluírem

### CA10 — Fora do resultado quando o filtro novo está preenchido

Dado um processo cujo planejamento está sem último CR operacional

Quando o usuário preenche `UltimoCentroResultadoIds`, `UltimaDiretoriaIds` ou os dois

Então o processo não entra na grade nem na exportação

---

# Notas técnicas

A origem dos dados já está no planejamento atual. A desmobilização só aponta para ele.

* `PlanejamentoDesmobilizacao` referencia o ativo por `PlanejamentoAtualId`.
* CR atual e diretoria atual já saem de `PlanejamentoAtual.CentroResultado` e de `CentroResultado.Diretoria`.
* Número Último CR e Descrição Último CR saem de `PlanejamentoAtual.UltimoCentroResultadoOperacionalId` e do `CentroResultado` relacionado (código e nome).
* Última Diretoria sai de `CentroResultado.DiretoriaId` e `Diretoria.Descricao` desse mesmo centro de resultado.
* Com `UltimoCentroResultadoOperacionalId` nulo, Número Último CR, Descrição Último CR e Última Diretoria ficam vazios.

Não há gravação desses valores em `PlanejamentoDesmobilizacao`.

---

# Fora de escopo

* Linha do tempo ou histórico de trocas de CR e diretoria.
* Tabela nova, fotografia na desmobilização ou gravação desses valores em `PlanejamentoDesmobilizacao`.
* Uso de `AlteracaoCentroResultadoPlanejamentoAtual`, `PlanejamentoAtualHistoricoAlteracaoCentroResultado` ou `OrcamentoHistoricoDiretoria`.
* Custos, dashboard de custos e parametrização de alçada.
