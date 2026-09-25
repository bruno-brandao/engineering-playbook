# Checklist — Code Reviewer

## Contexto

- [ ] Intenção da mudança compreendida
- [ ] Regras e padrões locais carregados
- [ ] Código relacionado e contratos consultados
- [ ] Evidências do gate/CI consideradas

## Correção

- [ ] Caminhos feliz, erro e limites avaliados
- [ ] Null/estado/transições avaliados
- [ ] Compatibilidade e regressões avaliadas
- [ ] Transações, concorrência e idempotência avaliadas

## Segurança e operação

- [ ] Autenticação e autorização avaliadas
- [ ] Dados sensíveis e logs avaliados
- [ ] Inputs, outputs e injeções avaliados
- [ ] Performance, volume e recursos avaliados
- [ ] Configuração, migrations e rollback avaliados
- [ ] Observabilidade e tratamento de falhas avaliados

## Qualidade do achado

- [ ] Cenário e impacto concretos
- [ ] Mitigações existentes verificadas
- [ ] Arquivo/trecho citado
- [ ] Severidade e confiança atribuídas
- [ ] Duplicatas consolidadas
- [ ] Preferências sem guideline omitidas
- [ ] Nenhuma ação de escrita no PR executada
