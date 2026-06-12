# US_GUIDELINES.md

# Padrão de User Stories

## Objetivo

Este documento define o padrão para criação e manutenção de User Stories (US) utilizadas pelo time de Desenvolvimento e QA.

As User Stories são artefatos de execução derivados de uma Feature previamente aprovada pelo negócio.

---

# Conceitos

## Feature

A Feature é o artefato funcional oficial.

Ela deve conter:

* Objetivo de negócio;
* Requisitos funcionais;
* Regras de negócio;
* Fluxos;
* Protótipos;
* Aprovação do negócio.

## [User Story](us-template.md) (US)

A User Story é o artefato utilizado pelo time de Desenvolvimento e QA para implementação e validação de uma entrega específica.

A US deve conter apenas as informações necessárias para a implementação e testes daquela entrega.

---

# Princípios

* Toda US deve possuir uma Feature associada.
* Uma US só pode ser criada após a aprovação da Feature.
* Alterações posteriores na Feature devem gerar novas Issues ou novas User Stories.
* A US deve ser objetiva e possuir leitura rápida.
* A US não deve replicar integralmente a Feature.
* A US deve conter apenas as regras necessárias para a implementação proposta.
* Os critérios de aceite devem permitir que o QA valide a implementação sem depender de interpretação adicional.
* Artefatos complementares devem ser referenciados por links.

---

# Convenção de Nome

Formato:

US-{FEATURE}-{ORDEM} - {DESCRIÇÃO}

Exemplo:

US-FEAT-123-01 - Criar endpoint de consulta de perfis

US-FEAT-123-02 - Criar tela de consulta de perfis

US-FEAT-123-03 - Implementar edição de perfis

Objetivos da convenção:

* Identificar a Feature de origem;
* Facilitar rastreabilidade;
* Indicar ordem sugerida de desenvolvimento;
* Facilitar buscas e organização do backlog.

---

# Decomposição de Features

Não existe obrigatoriedade de criar uma User Story para cada operação CRUD.

A decomposição deve ser baseada na complexidade da funcionalidade.

## Deve permanecer em uma única US quando

* Possui poucas regras de negócio;
* Possui baixa complexidade;
* Compartilha as mesmas validações;
* A separação não traz ganho de clareza.

Exemplo:

Cadastro simples de parâmetro contendo poucos campos e validações.

## Deve ser dividido em múltiplas USs quando

* Possui muitas regras de negócio;
* Possui fluxos independentes;
* Cadastro, edição ou consulta possuem comportamentos distintos;
* Existem integrações específicas;
* Existe grande volume de testes;
* Permite desenvolvimento paralelo.

Exemplo:

Gestão de colaboradores contendo cadastro, consulta, aprovação, histórico e integrações.

---

# Critério de Decomposição

Ao avaliar uma funcionalidade, considerar:

1. As regras de negócio são independentes?
2. A funcionalidade pode ser implementada separadamente?
3. A funcionalidade pode ser validada separadamente?
4. A divisão melhora a clareza para Desenvolvimento e QA?

Se a resposta for positiva para a maioria dos itens, a funcionalidade deve ser dividida em múltiplas User Stories.

---

# Definição de Pronto para Desenvolvimento

Uma User Story é considerada pronta para desenvolvimento quando possuir:

* Referência para a Feature;
* Escopo definido;
* Regras de Negócio definidas;
* Critérios de Aceite definidos;
* Artefatos necessários referenciados.

---

# Responsabilidades

## Analista

* Escrever a Feature;
* Garantir aprovação do negócio;
* Criar as User Stories derivadas;
* Definir regras de negócio e critérios de aceite.

## Desenvolvimento

* Implementar conforme definido na US;
* Reportar inconsistências ou lacunas identificadas.

## QA

* Validar a implementação utilizando as regras de negócio e critérios de aceite da US.

## Negócio

* Aprovar a Feature;
* Validar a implementação final entregue.
