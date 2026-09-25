---
name: project-quality-bootstrap
description: >-
  Diagnostica as capacidades de qualidade de um repositório e propõe skills locais
  para verificação e geração de testes. Use no primeiro uso do Engineering Playbook
  em um projeto, quando faltarem comandos confiáveis de validação, ou antes de
  configurar um gate pré-PR. Só cria arquivos após confirmação explícita.
---

# Project Quality Bootstrap

## Objetivo

Preparar um repositório consumidor para usar o fluxo de qualidade do Engineering Playbook sem impor comandos ou ferramentas genéricas. A skill identifica evidências reais no projeto, propõe skills locais portáveis em `.agents/skills/` e só grava arquivos após aprovação explícita.

## Responsabilidades

* Detectar stack, package managers, scripts, testes, CI, regras e skills existentes.
* Classificar capacidades como **Existente**, **Parcial**, **Ausente** ou **Não aplicável**.
* Propor `local-verification` e `test-generation` apenas quando houver evidência suficiente.
* Exibir preview completo, comandos, permissões e riscos antes de qualquer escrita.
* Nunca sobrescrever uma skill existente.
* Manter comandos específicos de stack no repositório consumidor, não neste plugin.

## Regras obrigatórias

1. **Diagnóstico read-only primeiro.** Não instalar dependências, executar migrations, iniciar serviços nem alterar arquivos durante a descoberta.
2. **Evidência antes de comando.** Só incluir comandos encontrados em manifests, scripts, pipelines ou documentação do próprio projeto.
3. **Placeholders bloqueiam criação.** Se um comando essencial não puder ser comprovado, manter a proposta como rascunho e pedir esclarecimento.
4. **Confirmação específica.** Pedir aprovação separada para cada arquivo a criar ou atualizar, mostrando o caminho e o conteúdo final.
5. **Sem sobrescrita.** Se o arquivo já existir, apresentar comparação e opções; não substituir automaticamente.
6. **Portabilidade.** Criar skills locais em `.agents/skills/<nome>/SKILL.md`.
7. **Sem efeitos externos.** Não abrir PR, fazer commit, push ou escrever no Azure DevOps.

## Recursos

| Recurso | Quando carregar |
| --- | --- |
| [checklist.md](checklist.md) | Durante o diagnóstico e antes de propor arquivos |
| [examples/proposal.md](examples/proposal.md) | Para formatar a proposta ao usuário |
| [templates/local-verification.SKILL.md](templates/local-verification.SKILL.md) | Quando faltarem verificações executáveis do projeto |
| [templates/test-generation.SKILL.md](templates/test-generation.SKILL.md) | Quando faltarem convenções locais para geração de testes |

## Fluxo de execução

### Etapa 1 — Descobrir instruções existentes

Ler, quando existirem:

* `AGENTS.md`, `AGENTS.local.md` e regras equivalentes;
* `.agents/skills/`, `.devin/skills/` e skills compatíveis;
* manifests e arquivos de solução/projeto;
* scripts de build e teste;
* configuração de CI/CD;
* documentação de desenvolvimento, QA e contribuição.

Não tratar exemplos ou nomes de scripts como comandos válidos sem confirmar que existem.

### Etapa 2 — Mapear capacidades

Avaliar pelo menos:

| Capacidade | Evidência esperada |
| --- | --- |
| Instalação/setup | lockfile, restore ou script documentado |
| Lint/format | script ou configuração presente |
| Typecheck/compile | script, projeto ou pipeline |
| Build | comando usado localmente ou na CI |
| Testes unitários | framework, diretório e comando |
| Integração/E2E | framework, serviços e comando |
| Cobertura | comando e limiar, se documentados |
| Geração de testes | exemplos e convenções locais |

Classificar cada item e citar a origem.

### Etapa 3 — Selecionar propostas

* Propor `local-verification` quando houver comandos comprovados para validar mudanças.
* Propor `test-generation` quando houver framework e exemplos suficientes para codificar convenções.
* Se uma capacidade exigir contexto ainda desconhecido, listar perguntas em vez de inventar valores.
* Visual regression e migration checklist podem ser recomendadas como evolução, mas não são geradas nesta versão.

### Etapa 4 — Renderizar templates

Substituir todos os marcadores `{{...}}` usando evidências do repositório. Remover seções não aplicáveis. Não mascarar marcador não resolvido.

### Etapa 5 — Apresentar proposta

Usar [examples/proposal.md](examples/proposal.md) e incluir:

1. Matriz de capacidades;
2. Skills existentes encontradas;
3. Arquivos propostos;
4. Preview completo;
5. Comandos e origem de cada comando;
6. Riscos, pré-requisitos e ações proibidas;
7. Pergunta de confirmação por arquivo.

### Etapa 6 — Criar após confirmação

Após o usuário confirmar explicitamente um arquivo:

1. Verificar novamente se o destino não passou a existir;
2. Criar apenas o arquivo aprovado;
3. Validar frontmatter, nome, placeholders e links;
4. Mostrar o diff;
5. Recomendar revisão e Pull Request.

Se o usuário negar ou não responder, não criar nada.

## Resultado esperado

Diagnóstico reproduzível e proposta segura de skills locais. A execução termina sem alterações ou com somente os arquivos individualmente aprovados pelo usuário.