# 156693 — Cancelamento de Vistoria (permitir cancelar em qualquer situação)

[Feature no Azure DevOps](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/156693)

---

# Referências

## Iniciativa / Epic

* [143458](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/143458) — [Melhorias Funcionais] - 2026

## Artefatos

* Regra atual de cancelamento (origem da restrição): [42387](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/42387) — Vistorias - Cancelar Vistoria
* Tela de consulta (botão Cancelar da grid): [42329](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/42329) — Vistoria - Consultar listagem
* Feature original do módulo: [38110](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/38110) — BackOffice - Vistoria
* Protótipo histórico da consulta/cancelamento: [Figma — Backoffice Avalia GAB (DEV)](https://www.figma.com/proto/JfIgf1pnidpTGHZGGxlv1c/%5BDEV%5D-BACKOFFICE-AVALIA-GAB?page-id=25:1730&node-id=2699:13638&viewport=2629%2C997%2C0.04&scaling=min-zoom&starting-point-node-id=2699:22289)
* Fluxo distinto (fora de escopo): Análise do gestor — [131728](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/131728)

---

# Contexto

No Backoffice Avalia GAB, a consulta de vistorias ([42329](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/42329)) permite selecionar uma ou várias vistorias na grid e acionar **Cancelar**.

Pela regra vigente ([42387](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/42387)), o sistema só conclui o cancelamento quando **todas** as vistorias selecionadas têm situação **diferente de Aprovada**. Se ao menos uma estiver **Aprovada**, a operação é bloqueada com a mensagem *"Vistoria aprovada não pode ser cancelada"*.

Na operação, essa restrição impede o time de cancelar vistorias que já avançaram no fluxo. O negócio precisa poder cancelar a vistoria **independentemente da situação atual**.

---

# Objetivo

Permitir cancelar vistorias pela **grid do Backoffice** em **qualquer situação**, mantendo confirmação, motivo obrigatório, atualização para **Cancelada** e histórico — removendo o bloqueio por situação (em especial o de **Aprovada**). O efeito desta entrega é **somente no Avalia**.

---

# Escopo

**Incluído:**

* Tela **Menu > Vistoria** (consulta / listagem / grid)
* Ação **Cancelar** da grid (individual e em lote)
* Validação de situação no frontend e no backend (API de cancelamento da grid)
* Persistência no Avalia: situação **Cancelada**, data/hora de desativação e histórico — mesmo padrão da [42387](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/42387)

**Fora de escopo:**

* App — não existe cancelamento de vistoria no aplicativo e esta Feature **não** cria essa ação
* Fluxo **Análise do gestor** (recusar/cancelar na modal de análise) — permanece como está
* Propagar o cancelamento para Precificação, Preparação, WAVE, SIMA ou Plataforma de Vendas (tratamento apenas no Avalia, nesta entrega)
* Alterar o layout da modal de cancelamento da grid (campo Motivo e botões permanecem)
* Criar nova permissão (reutiliza **Cancelar vistoria**)
* Estorno / reabertura de vistoria já cancelada

**Telas / campos impactados:**

* Listagem de Vistorias — habilitação do botão **Cancelar** da grid
* Modal de confirmação de cancelamento da grid
* Situação da vistoria (Avalia)
* Histórico da vistoria (Avalia)
* Data de desativação da vistoria (Avalia)

---

# Quem pode fazer

Usuários com a permissão **Cancelar vistoria**, a mesma da [42387](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/42387).

Usuários sem essa permissão não devem visualizar ou executar a ação **Cancelar** da grid.

---

# Regras Gerais

## RG01 — Ação e seleção (somente a grid)

O cancelamento desta Feature é **somente** o **Cancelar** da grid da consulta de vistorias: o usuário seleciona **uma ou várias** vistorias e aciona o botão **Cancelar**.

Não altera o App nem a modal de **Análise do gestor**.

## RG02 — Situação não bloqueia o cancelamento

O sistema **não** deve impedir o cancelamento com base na situação da vistoria, exceto o caso da RG03.

A validação *"se ao menos uma vistoria selecionada estiver Aprovada, bloquear"* deixa de existir no frontend e no backend da ação da grid.

A mensagem *"Vistoria aprovada não pode ser cancelada"* deixa de ser exibida.

**Exemplos:**

| Situação da vistoria | Hoje ([42387](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/42387)) | Depois desta Feature |
| --- | --- | --- |
| Em cadastramento | Permite | Permite |
| Pendente | Permite | Permite |
| Aguardando liberação do gestor | Conforme implementação atual | Permite |
| Reprovada | Conforme implementação atual | Permite |
| Aprovada | **Bloqueia** | **Permite** |
| Cancelada | Já cancelada | **Não permite** (RG03) |

## RG03 — Vistoria já cancelada

Não é permitido cancelar novamente uma vistoria cuja situação já seja **Cancelada**.

* Se a seleção contiver **somente** vistorias Canceladas, o sistema exibe a **MSG03** e **não** abre a modal.
* Se a seleção misturar vistorias Canceladas e não canceladas, o sistema exibe a **MSG03** e **não** cancela nenhuma (nem as elegíveis).

## RG04 — Modal de confirmação

Quando a seleção for válida (RG01 e RG03), o sistema exibe a modal com:

* Mensagem: *"Deseja confirmar o cancelamento das vistorias selecionadas?"*
* Campo **Motivo do cancelamento** — texto, **obrigatório** (também quando a vistoria estiver **Aprovada**)
* Botão **Cancelar** (da modal): fecha sem persistir
* Botão **Confirmar**: executa a RG05

O botão **Confirmar** permanece desabilitado enquanto o motivo estiver vazio (apenas espaços não conta como preenchido).

## RG05 — Efeito do cancelamento confirmado (somente Avalia)

Para cada vistoria da seleção, o sistema, **apenas no Avalia**:

1. Atualiza a situação para **Cancelada**
2. Grava a data de desativação como data e hora atuais
3. Grava o histórico da vistoria com:
   * Data e hora da ação
   * Usuário que executou a ação
   * Ação **"Cancelar da vistoria"**
   * Motivo informado na modal

Esta entrega **não** cancela, atualiza nem notifica Precificação, Preparação, WAVE, SIMA ou Plataforma de Vendas.

## RG06 — Lote atômico

No cancelamento em lote, ou **todas** as vistorias elegíveis da seleção são canceladas, ou **nenhuma** é persistida (não deixar lote parcial).

## RG07 — Recarregar a listagem

Após sucesso, o sistema fecha a modal, **mantém os filtros atuais**, recarrega a listagem e exibe a **MSG01**.

## RG08 — Permissão no frontend e no backend

A permissão **Cancelar vistoria** deve ser validada no frontend (exibição/habilitação do botão da grid) e no backend. Sem a permissão, a API recusa a operação mesmo se a requisição for feita diretamente.

## RG09 — Sem seleção

Se nenhuma vistoria estiver selecionada, o botão **Cancelar** da grid permanece desabilitado. Não abre modal.

---

# Mensagens

| Código | Texto |
| --- | --- |
| MSG01 | Vistoria(s) cancelada(s) com sucesso. |
| MSG02 | Não foi possível cancelar a(s) vistoria(s). Tente novamente. |
| MSG03 | Vistoria cancelada não pode ser cancelada novamente. |
| MSG04 | Informe o motivo do cancelamento. |

A mensagem atual *"Vistoria aprovada não pode ser cancelada"* **deixa de existir**.

---

# Fluxo resumido

1. Usuário com permissão acessa **Menu > Vistoria** no Backoffice.
2. Na grid, seleciona uma ou mais vistorias (qualquer situação, inclusive **Aprovada**).
3. Clica em **Cancelar**.
4. Se houver vistoria já **Cancelada** na seleção → **MSG03**, fim.
5. Sistema abre a modal e exige **Motivo**.
6. Usuário confirma.
7. Sistema grava no Avalia: situação **Cancelada**, data de desativação e histórico.
8. Listagem recarrega com os mesmos filtros e exibe **MSG01**.

---

# Decisões do negócio

Registradas em 29/09/2026, a partir das respostas do analista/negócio na elaboração da Feature:

| Tema | Decisão |
| --- | --- |
| App | Não entra. No App não é possível cancelar vistoria. |
| Superfície | Somente o **Cancelar da grid**. Análise do gestor fora. |
| Integrações | Tratar **apenas no Avalia** nesta entrega. |
| Já Cancelada | Continua **sem** poder ser cancelada de novo (RG03). |
| Motivo | Continua **obrigatório**, inclusive para vistoria **Aprovada**. |

---

# Aprovação

| Campo | Valor |
| --- | --- |
| Status | [ ] Aprovada pelo negócio |
| Data | |
| Responsável (negócio) | |

---

# Observações

* Esta Feature **altera** a regra da [42387](https://dev.azure.com/aguiabranca/AvaliaGAB/_workitems/edit/42387): o bloqueio de situação **Aprovada** é removido.
* Frontend e API da ação da grid precisam da mesma regra. Se só a tela liberar e a API continuar bloqueando **Aprovada**, a Feature não estará atendida.
* Cancelar no Avalia uma vistoria já integrada (ex.: **Aprovada** enviada a outro sistema) **não** sincroniza o destino nesta entrega. Risco conhecido e aceito pelo negócio para esta Feature.
* Não decompor em User Stories antes da aprovação formal do negócio.
