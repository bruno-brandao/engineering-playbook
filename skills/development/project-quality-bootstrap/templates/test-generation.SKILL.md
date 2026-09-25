---
name: test-generation
description: >-
  Gera testes seguindo framework, estrutura, mocks e convenções comprovadas neste
  repositório. Use ao implementar comportamentos ou cobrir regressões locais.
---

# Test Generation

## Objetivo

Criar testes aderentes aos padrões reais do projeto, sem introduzir framework, dependência ou convenção não utilizada.

## Stack e referências

{{TEST_STACK_AND_REFERENCES}}

## Convenções

{{TEST_CONVENTIONS}}

## Fluxo

1. Relacionar o comportamento solicitado às regras e critérios de aceite disponíveis.
2. Ler código-alvo e testes vizinhos antes de propor novos casos.
3. Definir casos de sucesso, erro, limites e regressão aplicáveis.
4. Criar testes em `{{TEST_LOCATION_PATTERN}}` usando `{{TEST_FRAMEWORK}}`.
5. Usar apenas as estratégias de mock/fixture existentes:

{{MOCK_AND_FIXTURE_RULES}}

6. Executar os comandos comprovados:

{{TEST_COMMANDS}}

7. Reportar cobertura quando o projeto possuir comando e limiar documentados.

## Restrições

{{TEST_RESTRICTIONS}}

## Saída

- Comportamentos cobertos e rastreabilidade;
- Arquivos criados ou alterados;
- Comandos executados e resultados;
- Casos não cobertos e motivo;
- Riscos ou dependências pendentes.
