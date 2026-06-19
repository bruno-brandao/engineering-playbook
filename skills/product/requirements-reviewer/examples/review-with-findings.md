# Exemplo — Parecer com achados

## Entrada

User Story `US-FEAT-087-03` revisada com Feature `FEAT-087` fornecida.

## Parecer

# Parecer de Revisão — US-FEAT-087-03

## Veredito

Requer revisão

## Resumo

A estrutura segue o template, mas há ambiguidade na regra de aprovação e critérios de aceite que não cobrem o fluxo de rejeição pelo gestor.

## Achados

### Bloqueantes

Nenhum.

### Importantes

- **[RN01]** "Alterações exigem aprovação do gestor direto" — não define prazo nem comportamento se o gestor não responder. Critério: clareza e testabilidade (`us-guidelines.md`).
- **[CA01–CA02]** Não há CA para rejeição da alteração pelo gestor. RN01 exige fluxo de aprovação completo. Critério: cobertura RN ↔ CA.

### Sugestões

- Renomear escopo para explicitar que integração com RH fica fora desta US (já mencionado em Observações, mas pode constar no Escopo).

## Recomendações

1. Esclarecer com negócio: prazo e comportamento padrão sem resposta do gestor.
2. Adicionar CA03 para rejeição pelo gestor com retorno ao solicitante.
3. Retornar ao analista para atualização.

## Próximo passo

Retornar ao [requirements-analyst](../requirements-analyst/SKILL.md) com achados documentados.
