# Integration Graph

> Gerado em 2026-06-26T20:11:04.262680+00:00

## Repos

| Repo | Status | Stack | Integrações |
| --- | --- | --- | --- |
| service-mobilizacaofrota | active | dotnet | http-client, http-client-factory |
| front-mobilizacao-frota | active | dotnet, node, docker | — |

## Grafo (WikiLinks)

### service-mobilizacaofrota
- [[service_mobilizacaofrota_IntegracaoAvaliaGabService]] → [[service_mobilizacaofrota_IHttpClientFactory]]
- [[service_mobilizacaofrota_IntegracaoDwService]] → [[service_mobilizacaofrota_IDiretoriaRepository]], [[service_mobilizacaofrota_ICentroResultadoRepository]], [[service_mobilizacaofrota_IEmpresaRepository]], [[service_mobilizacaofrota_IClienteRepository]], [[service_mobilizacaofrota_ICentroResultadoDwRepository]]
- [[service_mobilizacaofrota_LogIntegracaoService]] → —
- [[service_mobilizacaofrota_LogIntegracaoService]] → [[service_mobilizacaofrota_VixDbContext]]
- [[service_mobilizacaofrota_LogIntegracaoService]] → —
- [[service_mobilizacaofrota_LogIntegracaoService]] → —
- [[service_mobilizacaofrota_IntegracaoPlanejamentoAtualService]] → [[service_mobilizacaofrota_IHttpClientFactory]], [[service_mobilizacaofrota_AvaliaOption]], [[service_mobilizacaofrota_IPlanejamentoAtualRepository]]
- [[service_mobilizacaofrota_IntegracaoTcoService]] → [[service_mobilizacaofrota_IConfiguration]], [[service_mobilizacaofrota_IIntegracaoAvaliaGabService]], [[service_mobilizacaofrota_VixDbContext]]
- [[service_mobilizacaofrota_IntegracaoDwService]] → —
- [[service_mobilizacaofrota_IntegracaoDwService]] → —
- [[service_mobilizacaofrota_Adicional]] → —
- [[service_mobilizacaofrota_AdicionalHistorico]] → —
- [[service_mobilizacaofrota_Arquivo]] → —
- [[service_mobilizacaofrota_BaseEntity]] → —
- [[service_mobilizacaofrota_Bonificacao]] → —
- [[service_mobilizacaofrota_Cambio]] → —
- [[service_mobilizacaofrota_Categoria]] → —
- [[service_mobilizacaofrota_CentroResultado]] → —
- [[service_mobilizacaofrota_Cidade]] → —
- [[service_mobilizacaofrota_Cliente]] → —

### front-mobilizacao-frota
_Sem nós KB indexados._

## Dependências externas detectadas

_Nenhuma dependência externa detectada automaticamente._

## Cross-repo

Repos ativos no projeto:
- **service-mobilizacaofrota** pode integrar com: front-mobilizacao-frota
- **front-mobilizacao-frota** pode integrar com: service-mobilizacaofrota
