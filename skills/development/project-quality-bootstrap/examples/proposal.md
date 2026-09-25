# Proposta de Skills Locais — {projeto}

## Diagnóstico

| Capacidade | Status | Evidência |
| --- | --- | --- |
| Build | Existente | `{arquivo}:{linha}` — `{comando}` |
| Testes unitários | Parcial | Framework detectado; comando não documentado |
| Lint | Ausente | Nenhum script ou etapa de CI encontrado |

## Skills existentes

- `.agents/skills/exemplo/SKILL.md` — cobre {capacidade}

## Propostas

### 1. `local-verification`

**Destino:** `.agents/skills/local-verification/SKILL.md`

**Motivo:** consolidar os mesmos comandos usados pela CI antes do PR.

**Comandos comprovados:**

| Comando | Origem |
| --- | --- |
| `{comando}` | `{arquivo}:{linha}` |

**Pré-requisitos e riscos:** {descrição}

<details>
<summary>Preview completo</summary>

```markdown
{conteúdo renderizado}
```

</details>

Criar `.agents/skills/local-verification/SKILL.md` com o conteúdo acima? **Sim/Não**

## Pendências

- {pergunta necessária para remover um placeholder ou validar um comando}

## Próximo passo

Após aprovação, criar somente os arquivos confirmados, validar e mostrar o diff para revisão antes do Pull Request.
