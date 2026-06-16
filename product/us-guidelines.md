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

## User Story (US)

A User Story é o artefato utilizado pelo time de Desenvolvimento e QA para implementação e validação de uma entrega específica.

A US deve conter apenas as informações necessárias para a implementação e testes daquela entrega.

---

# Princípios

* Toda US deve possuir uma Feature associada.
* Uma US só pode ser criada após a aprovação da Feature.
* Alterações posteriores na Feature devem gerar novas Issues ou novas User Stories.
* A US deve ser objetiva.
* Objetividade não significa falta de detalhamento.
* A US deve eliminar ambiguidades e reduzir interpretações.
* A US não deve replicar integralmente a Feature.
* A US deve conter apenas as regras necessárias para a implementação proposta.
* Os critérios de aceite devem permitir que o QA valide a implementação sem depender de interpretação adicional.
* Artefatos complementares devem ser referenciados por links.

---

# Qualidade das User Stories

Uma User Story é considerada adequada quando Desenvolvimento, QA e Analista possuem o mesmo entendimento da funcionalidade.

O objetivo não é minimizar a quantidade de texto, mas garantir clareza suficiente para implementação e validação.

## Regras Gerais

### RG01 - Não deixar espaço para interpretação

Se uma regra permitir mais de uma interpretação válida, ela não está pronta para desenvolvimento.

### RG02 - Evitar regras genéricas

Evitar termos como:

* validar corretamente;
* tratar adequadamente;
* verificar permissões;
* exibir informações necessárias;
* calcular conforme regra de negócio.

Esses comportamentos devem ser descritos explicitamente.

### RG03 - Descrever comportamentos esperados

As regras devem explicar exatamente como o sistema deve se comportar.

### RG04 - Utilizar exemplos em funcionalidades complexas

Sempre que a funcionalidade envolver:

* cálculos;
* datas;
* períodos;
* aprovações;
* priorizações;
* ordenações;
* integrações;
* regras condicionais;
* fluxos complexos;

devem ser adicionados exemplos de negócio na User Story.

### RG05 - Casos de exceção devem ser documentados

Sempre que existir comportamento específico para erro, bloqueio ou situação excepcional, ele deve estar descrito.

Exemplos:

* usuário sem permissão;
* registro inexistente;
* período inválido;
* integração indisponível;
* dados obrigatórios ausentes.

### RG06 - O desenvolvedor não deve precisar adivinhar

Ao concluir a User Story, o analista deve responder:

"Existe alguma decisão de negócio que ficará a cargo do desenvolvedor?"

Se a resposta for sim, a User Story precisa ser refinada.

---

# Qualidade das Regras de Negócio

As Regras de Negócio devem definir o comportamento esperado do sistema.

## Boas práticas

### Correto

RN01 - Apenas usuários com perfil Administrador podem editar registros.

RN02 - O campo CPF não pode ser alterado após a criação do cadastro.

RN03 - Não deve ser permitido cadastrar um período que intercepte outro período existente para o mesmo colaborador.

### Evitar

RN01 - O sistema deve validar permissões.

RN02 - O sistema deve tratar conflitos de período.

RN03 - O sistema deve calcular corretamente o resultado.

## Quando utilizar exemplos

Sempre que a descrição da regra não for suficiente para eliminar ambiguidades.

Exemplo:

Período existente:
01/01/2026 a 31/01/2026

Novo período:
15/01/2026 a 20/01/2026

Resultado esperado:
Cadastro não permitido.

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
* Artefatos necessários referenciados;
* Casos complexos exemplificados quando aplicável.

---

# Responsabilidades

## Analista

* Escrever a Feature;
* Garantir aprovação do negócio;
* Criar as User Stories derivadas;
* Definir regras de negócio e critérios de aceite;
* Garantir que não existam ambiguidades na especificação.

## Desenvolvimento

* Implementar conforme definido na US;
* Reportar inconsistências, ambiguidades ou lacunas identificadas.

## QA

* Validar a implementação utilizando as regras de negócio e critérios de aceite da US.

## Negócio

* Aprovar a Feature;
* Validar a implementação final entregue.
