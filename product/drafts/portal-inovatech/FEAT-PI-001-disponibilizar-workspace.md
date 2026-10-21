# FEAT-PI-001 — Disponibilizar workspace para conversas

Rascunho do Portal Inovatech. Ainda não existe work item no Azure DevOps. Este arquivo não cria nem altera item no backlog.

Origem das regras: plano de produto do Portal Inovatech. Aprovada pelo negócio em 21/10/2026.

---

# Referências

## Iniciativa / Epic

* Portal Inovatech. Repositório da aplicação: https://github.com/bruno-brandao/portal-inovatech
* Este rascunho fica no engineering-playbook. O código da aplicação não fica neste repositório.

## Artefatos

* Protótipo / imagem da tela: ainda não desenhado. Arquivo Figma previsto: https://www.figma.com/design/ih1UFMUzvt3HiW7hy7T3ej/Portal-Inova%C3%A7%C3%A3o?node-id=0-1
* Fluxo: as cinco etapas obrigatórias abaixo, nesta ordem de conclusão. A ordem em que o administrador preenche pode variar; o status `disponível` só sai quando as cinco estão concluídas.
* Documento complementar: `project-context/templates/project-map.yaml` e `project-context/schemas/project-map.schema.json`, somente como modelo da importação inicial.

---

# Contexto

O Portal Inovatech atende qualquer projeto do Azure DevOps da organização configurada no ambiente. Existir no Azure DevOps não torna o projeto utilizável nas conversas.

Hoje o mapa de repositórios, branch e donos vive em `project-map.yaml` no engineering-playbook. Esse arquivo inclui `local_path`, que é caminho de máquina de quem desenvolve. A conversa, a pipeline e o ingest não podem depender desse arquivo nem desse caminho.

Sem uma configuração publicada por workspace, uma conversa poderia consultar projeto, repositório ou area path que o administrador ainda não liberou.

---

# Objetivo

Permitir que um administrador publique um workspace por projeto do Azure DevOps, com as etapas obrigatórias concluídas, para que só então esse workspace apareça para conversa, busca e sessão.

---

# Escopo

**Incluído:**

* Painel de admin do Portal Inovatech.
* Lista dos projetos que o token do administrador lê no Azure DevOps.
* Habilitação do projeto, confirmação do mapa do processo, marcação de area paths, publicação do mapa do projeto e nomeação do responsável.
* Status `em configuração` e `disponível`.
* Importação inicial por upload de `project-map.yaml` na tela, com exportação de modelo e instrução de cada campo. `local_path` não é gravado.
* Declaração explícita de que a conversa ainda não consulta código.
* Dependência explícita de repositório de outro workspace, com justificativa.

**Fora:**

* Escrever Feature ou User Story.
* Conversar, buscar documentação ou abrir sessão. Enquanto o workspace está `em configuração`, essas ações não abrem.
* Gravar dado no Databricks. A configuração fica no Supabase.
* Criar ou editar work item no Azure DevOps.
* Indexar repositório, calcular embedding ou desenhar o panorama.
* Tratar um projeto nomeado como caso especial do produto.

---

# Quem pode fazer

Pessoa que possui a permissão de sistema administrador.

O Entra ID só autentica. Editor, aprovador e leitor ficam no controle do próprio portal, no Supabase, e podem ser editados. A permissão administrador não entra nessa lista editável. Não há grupo do Entra ID para essas permissões.

A lista de projetos usa o access token delegado do Entra ID dessa pessoa, somente leitura (`vso.work`, `vso.project`, `vso.profile`). Não existe PAT, nem pessoal nem compartilhado, nem campo para informar token. O que ela enxerga no Azure DevOps é a permissão que o Entra ID já concede a ela. A permissão do portal limita o que ela pode configurar.

Quem não tem a permissão de administrador não habilita projeto, não publica mapa e não muda o status do workspace.

---

# Regras Gerais

## RG01 — Um workspace por projeto

Cada projeto do Azure DevOps habilitado gera um workspace. O identificador do workspace é o par organização + projeto lidos do Azure DevOps. Dois workspaces não apontam para o mesmo projeto.

Exemplo: o projeto "Alfa" na organização configurada no ambiente vira um workspace. O projeto "Beta" vira outro. O nome "Alfa" não existe no código do portal.

## RG02 — Habilitar o projeto

O administrador escolhe um projeto que o token dele lê e habilita a integração com o playbook. Existir no `GET /_apis/projects` não publica o workspace e não o coloca no seletor de conversas.

Ao habilitar, o workspace nasce com status `em configuração`.

## RG03 — Confirmar o mapa do processo

O administrador confirma o mapa do processo daquele projeto: tipo do work item, estados e campos usados na cópia para o Azure DevOps e no dashboard.

O portal lê esse mapa do processo do projeto. Feature, User Story e Product Backlog Item não ficam fixos no código. A confirmação grava a leitura daquele momento, com autor e data.

Sem essa confirmação, o workspace permanece `em configuração`.

## RG04 — Marcar area paths

O administrador marca quais area paths a conversa daquele workspace pode usar. Area path não marcado não entra em conversa, busca nem sessão desse workspace.

A lista de area paths vem do Azure DevOps com o token do administrador. Sem ao menos um area path marcado, o workspace permanece `em configuração`.

## RG05 — Publicar o mapa do projeto ou dispensar código

O administrador faz uma das duas ações:

1. Publica o mapa do projeto, com os repositórios incluídos.
2. Declara que a conversa ainda não consulta código.

As duas ações se excluem. Publicar o mapa remove a declaração de dispensa. Declarar a dispensa não publica repositório.

O mapa publicado guarda, por repositório: nome, URL no Azure DevOps, status (`active`, `legacy` ou `discontinued`), branch de referência, descrição, stack e donos. Também guarda a branch de referência padrão do workspace e o perfil de indexação (`minimal`, `standard` ou `full`).

`local_path` não é gravado, mesmo que venha no YAML importado.

A importação é um upload do YAML no painel. A mesma tela exporta um modelo vazio e mostra a instrução do que é cada campo: organização, projeto, branch de referência padrão, perfil de indexação (`minimal`, `standard`, `full`) e, por repositório, nome, URL, status (`active`, `legacy`, `discontinued`), branch, descrição, stack e donos. A instrução diz que `local_path` é ignorado.

O upload preenche o mapa. Não publica sozinho e não conclui as outras etapas. A pessoa revisa os campos e publica numa ação separada.

A cópia publicada no portal é a que a conversa, a pipeline e o ingest usam. O YAML do playbook serve só para essa importação inicial. Cada publicação grava autor e data.

Sem publicação do mapa e sem a declaração de dispensa, o workspace permanece `em configuração`.

## RG06 — Nomear o responsável

O administrador define o responsável no painel, no próprio workspace. O valor não vem de grupo nem de atributo fixo do Entra ID. A escolha fica gravada no workspace.

Sem responsável definido nesse campo, o workspace permanece `em configuração`.

## RG07 — Status disponível

O workspace passa a `disponível` somente quando as cinco etapas estão concluídas: projeto habilitado, mapa do processo confirmado, ao menos um area path marcado, mapa publicado ou código dispensado, e responsável nomeado.

Se o administrador desfaz uma etapa, o status volta para `em configuração` na hora. Conversa, busca e sessão daquele workspace deixam de abrir.

O painel mostra, para cada workspace `em configuração`, quais etapas faltam.

## RG08 — Quem vê o workspace

Uma pessoa vê o workspace no seletor somente se as duas condições são verdadeiras: o status está `disponível` e o token dela lê esse projeto no Azure DevOps.

Workspace `em configuração` aparece para o administrador, no painel de admin, e não aparece no seletor de conversas.

## RG09 — Bloqueio antes de estar disponível

Com status `em configuração`, o portal não abre conversa, busca nem sessão nesse workspace. A API rejeita essas chamadas para esse `workspace_id`.

Toda conversa, rascunho, parecer, documento indexado e chamada de IA de uma funcionalidade posterior leva `workspace_id`. Esta Feature não implementa essas ações. Ela impede que elas abram antes do status `disponível`.

## RG10 — Repositório de outro workspace

Um repositório de outro workspace não entra na consulta deste. O administrador pode criar uma dependência explícita, com justificativa e com o controle de acesso dessa dependência. Até essa dependência existir, a busca não consulta nem menciona esse repositório.

A dependência não substitui as cinco etapas e não torna o workspace `disponível` sozinha.

## RG11 — Desempenho da lista

A lista de projetos e a lista de repositórios do mapa abrem com 10 itens. A pessoa pode mudar a página para 30 ou 50. Não há outro tamanho.

A tela não carrega todos os projetos da organização nem todos os repositórios do workspace de uma vez. Trocar o tamanho pede de novo só a página visível.

## RG12 — Permissão administrador do sistema

O portal já inclui a permissão administrador. Ela não nasce de cadastro na tela.

Essa permissão não pode ser renomeada, ter o que ela permite alterado, nem ser excluída. A tela não oferece essas ações para ela.

Atribuir ou retirar a permissão de uma pessoa não edita a permissão. Só muda quem a possui.

Na primeira instalação, a permissão administrador fica atribuída à conta cujo e-mail de login no Entra ID é `ps.brunoe@aguiabranca.com.br`. Outro e-mail não recebe essa atribuição inicial. Depois da instalação, atribuir ou retirar segue a regra acima.

Editor, aprovador e leitor não seguem essa trava.

---

# Aprovação

| Campo | Valor |
| --- | --- |
| Status | [x] Aprovada pelo negócio |
| Data | 21/10/2026 |
| Responsável (negócio) | ps.brunoe@aguiabranca.com.br |

---

# Observações

* User Stories derivadas após a aprovação: US-FEAT-PI-001-01 a US-FEAT-PI-001-06, nesta pasta. A divisão separa permissão, habilitação, processo e area path, mapa, conclusão do status e dependência entre workspaces, porque cada uma se implementa e se testa sem as outras.
* O protótipo Figma desta tela ainda não existe. O link da tela entra na Feature quando o quadro estiver desenhado.
* Não criar o work item no Azure DevOps a partir deste rascunho sem ação explícita de uma pessoa.
