# Exemplo — CRUD simples (uma única US)

## Contexto da Feature

`FEAT-042` — Cadastro de parâmetro de sistema com três campos (código, descrição, valor) e validações básicas.

## Decisão de decomposição

**Uma única User Story.** Poucas regras, baixa complexidade, mesmas validações para cadastro e edição.

## User Story gerada

### US-FEAT-042-01 - Implementar cadastro e edição de parâmetro de sistema

#### Referências

* Feature: FEAT-042

#### Escopo

Implementar cadastro e edição de parâmetro de sistema com os campos código, descrição e valor.

#### Regras de Negócio

**RN01** — O código é obrigatório, único e aceita até 20 caracteres alfanuméricos.

**RN02** — A descrição é obrigatória e aceita até 100 caracteres.

**RN03** — O valor é obrigatório e aceita até 255 caracteres.

#### Critérios de Aceite

**CA01**

Dado que o usuário acessa o cadastro de parâmetro
Quando preenche código, descrição e valor válidos e salva
Então o parâmetro é persistido e exibido na listagem

**CA02**

Dado que existe um parâmetro cadastrado
Quando o usuário edita descrição ou valor e salva
Então as alterações são persistidas mantendo o código original

**CA03**

Dado que o usuário tenta salvar com código duplicado
Quando confirma o cadastro
Então o sistema exibe mensagem de erro e não persiste o registro
