# ADR — Architecture Decision Records

Registro de decisões arquiteturais relevantes do time.

---

## Quando criar um ADR

* Decisão com impacto em múltiplos sistemas ou times;
* Escolha difícil de reverter;
* Trade-off significativo entre alternativas;
* Necessidade de preservar contexto para o futuro.

---

## Estrutura

Cada ADR é um arquivo numerado neste diretório:

```text
adr/
├── README.md
├── 0001-titulo-da-decisao.md
└── 0002-outra-decisao.md
```

### Template

```markdown
# ADR-NNNN: Título da decisão

## Status

[Proposta | Aceita | Substituída | Depreciada]

## Contexto

[Por que essa decisão foi necessária?]

## Problema

[O que precisamos resolver?]

## Alternativas consideradas

1. [Alternativa A] — prós e contras
2. [Alternativa B] — prós e contras

## Decisão

[O que foi decidido e por quê?]

## Consequências

* Positivas: ...
* Negativas: ...
* Riscos: ...
```

---

## Convenção de numeração

* Formato: `NNNN-titulo-em-kebab-case.md`
* Números sequenciais com 4 dígitos (0001, 0002, …)
* Título curto e descritivo

---

## Contribuição

ADRs são criados via Pull Request, seguindo as diretrizes de contribuição do repositório.
