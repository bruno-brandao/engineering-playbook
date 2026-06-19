# Exemplo — CRUD complexo (múltiplas USs)

## Contexto da Feature

`FEAT-087` — Gestão de colaboradores com cadastro, consulta paginada, aprovação de alterações, histórico de mudanças e integração com RH.

## Decisão de decomposição

**Quatro User Stories.** Fluxos independentes, integração específica, alto volume de testes e possibilidade de desenvolvimento paralelo.

| US | Justificativa |
| --- | --- |
| 01 — Endpoint de consulta | Entrega backend isolada, validável por API |
| 02 — Tela de consulta | Depende do endpoint, escopo de UI distinto |
| 03 — Cadastro e edição | Regras de validação e fluxo de aprovação próprios |
| 04 — Integração RH | Integração externa com ciclo de vida separado |

## User Story gerada (exemplo parcial — US 03)

### US-FEAT-087-03 - Implementar cadastro e edição de colaboradores

#### Referências

* Feature: FEAT-087
* Figma: [link do protótipo]
* Fluxo de aprovação: [link do diagrama]

#### Escopo

Implementar formulário de cadastro e edição de colaboradores com submissão para aprovação do gestor.

#### Regras de Negócio

**RN01** — Alterações em colaboradores ativos exigem aprovação do gestor direto antes de persistir.

**RN02** — Cadastros novos ficam com status "Pendente" até aprovação.

**RN03** — CPF deve ser válido e único no sistema.

#### Critérios de Aceite

**CA01**

Dado que o usuário cadastra um colaborador com dados válidos
Quando submete o formulário
Então o colaborador é criado com status "Pendente" e notificação é enviada ao gestor

**CA02**

Dado que um colaborador ativo recebe alteração de cargo
Quando o usuário salva a edição
Então a alteração só é aplicada após aprovação do gestor

#### Observações

* Depende de US-FEAT-087-01 para consulta pós-cadastro.
* Integração com RH (US-FEAT-087-04) ocorre após aprovação.
