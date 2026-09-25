---
name: local-verification
description: >-
  Executa as verificações locais comprovadas do projeto antes de concluir uma
  alteração ou abrir Pull Request. Use após mudanças de código e no gate pré-PR.
---

# Local Verification

## Objetivo

Validar alterações com os mesmos comandos e pré-requisitos adotados pelo projeto e pela CI.

## Fontes

{{COMMAND_SOURCES}}

## Pré-requisitos

{{PREREQUISITES}}

## Fluxo

1. Verificar o estado do repositório e identificar arquivos alterados.
2. Executar, na ordem abaixo, somente os comandos aplicáveis à mudança:

{{VERIFICATION_COMMANDS}}

3. Interromper quando uma falha tornar etapas posteriores inválidas.
4. Registrar comando, exit code e resumo da evidência.
5. Não corrigir falhas automaticamente; apresentar diagnóstico e pedir autorização para uma etapa de correção.

## Restrições

{{RESTRICTIONS}}

## Saída

| Verificação | Comando | Resultado | Evidência |
| --- | --- | --- | --- |
| {{CHECK_NAME}} | `{{CHECK_COMMAND}}` | Aprovada/Falhou/Não aplicável | {{EVIDENCE}} |

**Veredito:** `Aprovado`, `Aprovado com ressalvas` ou `Reprovado`.
