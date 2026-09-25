# Plano de Testes — {US-ID}

## Status

`Completo | Provisório | Bloqueado`

## Escopo e riscos

| Área | Risco | Cobertura proposta |
| --- | --- | --- |
| Regra de negócio | Alto | Unitário + integração |

## Matriz de rastreabilidade

| ID | RN/CA | Cenário | Camada | Prioridade | Evidência |
| --- | --- | --- | --- | --- | --- |
| CT-01 | RN01 / CA01 | Dado {contexto}, quando {ação}, então {resultado} | Integração | Obrigatório | Resposta e persistência |

## Massa, mocks e dependências

- **Dados:** {massa não sensível}
- **Mocks/fakes:** {integração}
- **Serviços/ambiente:** {pré-requisito}

## Não funcionais aplicáveis

- Segurança: {cenário ou N/A}
- Performance: {cenário ou N/A}
- Acessibilidade: {cenário ou N/A}
- Observabilidade: {evidência ou N/A}

## Lacunas e perguntas

### Bloqueantes

- [RNxx] {decisão necessária}

### Premissas

- {premissa explicitamente aceita}

## Fora de escopo

- {item}

## Handoff

- Automação local: `.agents/skills/test-generation/SKILL.md` disponível/não disponível
- Próximo passo: {desenvolvimento | QA | refinamento}
