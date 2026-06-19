# Título

Seguir a convenção:

US-{FEATURE}-{ORDEM} - {DESCRIÇÃO}

Exemplo:

US-FEAT-123-01 - Ajustar ações do botão Ações na Lista de Mobilização

---

# Quem pode fazer (níveis de permissão)

Descrever os grupos e permissões aplicáveis a esta entrega.

Exemplo:

* Grupos Gestor Logística / Administrador: Criação, Edição, Visualização, Exclusão nas ações operacionais da Mobilização.
* Demais Grupos: Visualização e execução conforme matriz de permissão vigente por item do dropdown Ações (US001).

---

# Referências

## Feature

* FEAT-XXX

## User Stories relacionadas

* US001 — [Descrição da dependência]
* US002 — [Descrição da dependência]

## Artefatos

* Figma:
* Protótipo:
* Fluxo:
* Documento complementar:
* API/Swagger:

---

# Escopo

Descrever objetivamente o que será entregue nesta User Story.

Exemplo:

Ajustar as ações [Ação A] e [Ação B] acessíveis pelo botão Ações na Lista de Mobilização: [descrição objetiva da entrega].

Regras cobertas: RN01, RN02.

Impactos: [dependências, integrações ou US complementares impactadas].

## Telas e caminhos impactados

| Tela / Modal | Caminho de navegação | Tipo de alteração |
| --- | --- | --- |
| [Nome da tela ou modal] | [Menu > Módulo > Tela] | [Novo / Ajuste / Remoção] |
| [Nome da tela ou modal] | [Menu > Módulo > Tela] | [Novo / Ajuste / Remoção] |

## Fronteira com outras US

| Escopo | Esta US (US-XXX-XX) | Outras US |
| --- | --- | --- |
| [Funcionalidade ou modal] | [O que esta US cobre] | [US que cobre o restante] |
| [Funcionalidade ou modal] | [O que esta US cobre] | [US que cobre o restante] |
| [Funcionalidade fora do escopo] | Não cobre | [US responsável] |

---

# Botões

Listar os botões e ações de interface impactados por esta entrega.

Exemplo:

* [Ação A] (item do dropdown Ações)
* [Ação B] (item do dropdown Ações)
* Confirmar / Cancelar (modais)
* [Botão específico da regra]

---

# Como fazer

## Fluxos de Trabalho Detalhados

### RN01 — [Nome da regra]

Origem: [Ações > Item do menu].

| Campo | Tipo | Obrigatoriedade | Regra |
| --- | --- | --- | --- |
| [Campo] | [Tipo] | [Obrigatório / Opcional] | [Descrição da regra] |

[Comportamento esperado ao confirmar, cancelar ou concluir a ação.]

Registrar evento em Rastreio por registro (ver seção Rastreio).

### RN02 — [Nome da regra]

Origem: [Ações > Item do menu].

Modal:

* [Opção ou campo da modal]
* [Regra de habilitação ou seleção]

Regras:

* [Regra específica 1]
* [Regra específica 2]
* [Regra específica 3]

## Regras de Validação Específicas

| Contexto | Condição | Ação | Mensagem |
| --- | --- | --- | --- |
| [Contexto] | [Condição] | [Bloquear / Desabilitar / Exibir] | [MSG001] |
| [Contexto] | [Condição] | [Bloquear / Desabilitar / Exibir] | [MSG002] |

## Regra de Validação da Tela

Descrever validações globais da tela ou modal que se aplicam independentemente do fluxo específico.

Exemplo:

* Durante processamento, bloquear ações da modal e exibir indicador de carregamento.
* Regras de habilitação devem valer na confirmação independentemente do canal de acesso (interface ou integração).

## Regras de Cálculo

Descrever cálculos ou interseções de regras quando aplicável.

Exemplo:

Não se aplica.

Ou:

[Descrição objetiva do cálculo, com referência a US ou RN relacionada quando houver dependência.]

## Política de falha e efeitos colaterais

Descrever o comportamento esperado em caso de falha parcial ou total após confirmação.

Exemplo:

* [Ação A]: se o processamento falhar após Confirmar, a operação não deve ser registrada como concluída; o operador permanece na modal com mensagem de falha e pode tentar novamente.
* [Ação B]: se a atualização falhar parcialmente, exibir quais registros não foram alterados; registros já atualizados não devem ser revertidos automaticamente.

## Comportamento em lote

| Ação | Critério de agrupamento | Comportamento |
| --- | --- | --- |
| [Ação] | [Critério de lote] | [Comportamento esperado] |
| [Ação] | [Critério de lote] | [Comportamento esperado] |

## Rastreio (dados mínimos)

| Evento | Dados visíveis na aba Rastreio | Reenvio |
| --- | --- | --- |
| [Evento] | [Campos registrados] | [Política de reenvio ou nova geração] |
| [Evento] | [Campos registrados] | [Política de reenvio ou nova geração] |

---

# Mensagens de validação do sistema

MSG001 - "[Texto da mensagem]"

MSG002 - "[Texto da mensagem]"

MSG003 - "[Texto da mensagem]"

---

# Critérios de Aceite

## CA01

Dado que ...

Quando ...

Então ...

## CA02

Dado que ...

Quando ...

Então ...

## CA03

Dado que ...

Quando ...

Então ...

---

# Protótipo

* Wave: [URL do protótipo]

---

# Observações

Informações complementares para Desenvolvimento e QA.

Exemplos:

* Dependências técnicas;
* Restrições conhecidas;
* Integrações impactadas;
* Considerações de implementação.
