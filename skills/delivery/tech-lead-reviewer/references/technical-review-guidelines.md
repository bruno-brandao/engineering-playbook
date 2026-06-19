# Diretrizes de Revisão Técnica

Critérios que o Tech Lead aplica ao revisar User Stories. Complementam `product/us-guidelines.md` com foco em implementação.

---

## Princípios

1. **Implementável** — o time consegue codificar e testar sem adivinhar comportamento ou contrato.
2. **Explícito** — decisões técnicas relevantes estão na US ou em artefato referenciado.
3. **Seguro por padrão** — permissões, dados sensíveis e falhas não ficam implícitos.
4. **Entregável em fatias** — o escopo cabe em uma entrega verificável, alinhada à decomposição da Feature.

---

## O que revisar em cada RN

| Pergunta | Se "não" → |
| --- | --- |
| Dá para mapear a RN em validação, regra de domínio, query ou integração? | Achado importante ou bloqueante |
| Estados e transições estão claros? | Pedir exemplos ou diagrama de estados |
| O que acontece em erro, bloqueio ou dado ausente? | Lacuna — exigir RN ou CA de exceção |
| Há números, datas ou fórmulas sem exemplo? | Exigir exemplo de negócio |
| A RN depende de sistema externo sem contrato? | Bloqueante até referenciar API/doc |

---

## Dimensões técnicas

### Dados

* Campos novos ou alterados; obrigatoriedade e formato.
* Unicidade, relacionamentos, histórico, exclusão lógica.
* Necessidade de migração, seed ou correção de dados legados.

### APIs e contratos

* Método, rota ou operação identificável no escopo.
* Request/response ou referência a Swagger.
* Versionamento ou breaking change sinalizado.

### UI e experiência técnica

* Estados de loading, vazio, erro e sucesso quando o escopo é tela.
* Comportamento de formulário (edição parcial, campos bloqueados) alinhado às RNs.
* Referência a protótipo quando layout impacta implementação.

### Integrações

* Sistema, protocolo e responsável (produtor/consumidor).
* Idempotência, retry, timeout e compensação quando falha é crítica.
* Dados sincronizados vs consultados em tempo real.

### Segurança

* Quem pode executar a operação (perfil, tenant, escopo).
* Dados PII ou financeiros — exposição e auditoria.
* Operações irreversíveis — confirmação ou trilha.

### Performance e escala

* Listagens com paginação ou filtros quando volume é relevante.
* Jobs assíncronos para processamento longo.
* Limites de tamanho ou frequência documentados.

### Observabilidade

* Logs ou métricas mínimas quando falha afeta operação ou SLA.
* Correlation ID ou rastreio em integrações críticas.

---

## Sinais de alerta (red flags)

* RN com verbos genéricos: "validar corretamente", "tratar adequadamente".
* Escopo mistura backend e frontend sem decomposição quando complexidade é alta.
* Integração mencionada sem contrato ou mock definido.
* Regra de permissão ausente em operação de escrita ou exclusão.
* Cálculo ou regra temporal sem exemplo.
* US grande demais: muitas RNs independentes, múltiplas integrações ou fluxos paralelos.
* Dependência de outra US não declarada na ordem ou em Observações.

---

## Quando escalar

| Situação | Destino |
| --- | --- |
| Lacuna de comportamento de negócio | Analista / negócio |
| Lacuna de contrato técnico na US | Analista (complementar Observações ou RN) |
| Decisão de arquitetura transversal | ADR ou arquitetura do time |
| Conflito com padrão existente no código | Time de desenvolvimento + analista |
