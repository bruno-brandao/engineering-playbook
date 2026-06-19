# Checklist — Tech Lead Reviewer

Use para cada User Story revisada.

## Regras de Negócio (implementabilidade)

- [ ] Cada RN descreve comportamento concreto do sistema (não genérico — `us-guidelines.md` RG02)
- [ ] Nenhuma RN exige que o desenvolvedor defina regra de negócio (RG06)
- [ ] Condições, estados e transições estão explícitos onde aplicável
- [ ] Exceções documentadas (permissão, dado inválido, registro inexistente, integração indisponível)
- [ ] Exemplos presentes para cálculos, datas, ordenações, aprovações ou integrações complexas
- [ ] RNs não se contradizem entre si
- [ ] CAs cobrem os cenários técnicos críticos derivados das RNs (incluindo erro e borda)

## Escopo e entrega

- [ ] Escopo identifica o artefato técnico a entregar (API, UI, job, evento, etc.)
- [ ] Fronteira da US clara — sem escopo técnico implícito de outra US
- [ ] Referências técnicas presentes (Swagger, Figma, fluxo, doc de integração) quando necessárias
- [ ] Observações trazem dependências técnicas conhecidas

## Dados e persistência

- [ ] Entidades ou campos impactados são identificáveis a partir das RNs
- [ ] Regras de unicidade, histórico ou soft delete estão explícitas quando relevantes
- [ ] Migração ou backfill necessário está sinalizado (ou N/A)

## Integrações

- [ ] Sistemas externos e direção do fluxo identificados (entrada/saída)
- [ ] Comportamento em falha de integração definido ou sinalizado como pendência
- [ ] Formato de payload ou contrato referenciado quando a US depende de integração

## Segurança e permissões

- [ ] Perfis ou papéis com acesso definidos nas RNs (quando há controle de acesso)
- [ ] Dados sensíveis tratados explicitamente (mascaramento, restrição, auditoria)
- [ ] Operações críticas exigem rastreabilidade quando aplicável

## Performance e operação

- [ ] Volume ou paginação considerados em consultas/listagens
- [ ] Operações longas ou assíncronas sinalizadas quando o escopo implica processamento pesado
- [ ] Limites ou SLAs relevantes documentados ou marcados como pendência de negócio

## Dependências e decomposição

- [ ] Dependências de outras USs ou features declaradas
- [ ] Ordem no identificador coerente com dependências técnicas
- [ ] Nenhuma US concentra risco técnico desproporcional sem sinalização

## Prontidão técnica

- [ ] Nenhuma decisão de arquitetura crítica deixada implícita
- [ ] Lacunas técnicas sinalizadas com responsável (analista, negócio, arquitetura)
- [ ] Parecer do requirements-reviewer considerado (quando fornecido)
