# Checklist — Requirements Reviewer

Use para cada User Story revisada.

## Estrutura (template)

- [ ] Título segue `US-{FEATURE}-{ORDEM} - {DESCRIÇÃO}`
- [ ] Seção Referências presente com Feature identificada
- [ ] Artefatos complementares referenciados por link (quando existirem na Feature)
- [ ] Escopo presente e objetivo
- [ ] Regras de Negócio numeradas (`RN01`, `RN02`, …)
- [ ] Critérios de Aceite em Dado/Quando/Então (`CA01`, `CA02`, …)
- [ ] Observações preenchidas quando há dependências ou restrições

## Clareza e testabilidade

- [ ] Cada RN possui apenas uma interpretação válida
- [ ] CAs são verificáveis pelo QA sem contexto adicional
- [ ] Não há termos vagos sem definição (ex.: "rapidamente", "quando possível")
- [ ] Exemplos presentes para cálculos, datas, períodos, ordenações, aprovações ou integrações

## Rastreabilidade

- [ ] Feature de origem identificável
- [ ] Escopo da US está contido na Feature (não extrapola)
- [ ] RNs da US derivam da Feature (nenhuma inventada)
- [ ] RNs relevantes da Feature para este escopo estão cobertas
- [ ] CAs cobrem as RNs declaradas nesta US

## Escopo e decomposição

- [ ] US não replica integralmente a Feature
- [ ] Escopo é implementável e validável de forma independente (quando decomposição aplicável)
- [ ] Ordem no identificador coerente com dependências declaradas

## Prontidão

- [ ] Nenhuma lacuna funcional não sinalizada
- [ ] Dúvidas para o negócio estão explícitas (se houver)
- [ ] Feature de origem está aprovada (quando Feature fornecida)
