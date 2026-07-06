---
tags: [job, batch, sap, sima-backend, AtivosCompraMobilizacao]
kb_domain: sima-backend
tipo: job
namespace: Sima.Jobs.DailyUpdate
ultima_sincronizacao: "2026-06-25T12:00:00Z"
reference_branch: main
source_commit: pilot-seed
source_file: Jobs/AtualizacaoDiariaJob.cs
source_hash: pilot
wikilinks_out: [SIMA_IAtivoRepository, DW_VWImobilizadosSapGeralSIMA]
---

# AtualizacaoDiariaJob

> Nota piloto DCP — gerada para US-147722. Substituir por output de `scan sync` quando repo local disponível.

## Contrato

- **Tipo:** `job` / rotina batch diária
- **Arquivo esperado:** `Jobs/AtualizacaoDiariaJob.cs` _(confirmar path no repo)_
- **Request:** execução agendada (sem payload HTTP)
- **Response:** `Task` — processamento em lote de ativos

## Dependências (grafo)

- [Banco de Dados] [[SIMA_IAtivoRepository]] — localizar ativo por placa (`CodigoSapVix`)
- [Data Warehouse] [[DW_VWImobilizadosSapGeralSIMA]] — fonte status faturamento SAP

## Fluxo (marcos)

- Código executa: consulta `[DW].[VWImobilizadosSapGeralSIMA]`
- [Condição] Se: view indisponível ou vazia → encerrar sem alterações (RN06)
- Código executa: filtrar `StatusFaturamento == 'Veículo Faturado'` (RN02)
- Código executa: `ativoRepository.FindByPlaca(CodigoSapVix)` (RN03)
- [Condição] Se: ativo não encontrado → ignorar registro, continuar (RN08)
- Código executa: `ativo.SetDataDesativacao(...)` (RN04)
- [Condição] Se: ativo já desativado e sumiu da view → **não** limpar data (RN07 — confirmar negócio)
- Código executa: `unitOfWork.SaveChangesAsync()`

## Efeitos colaterais

- Persistência de `DataDesativacao` no ativo SIMA
- Ativo deixa de aparecer no estoque venda (RN05 — filtro existente)
- Log recomendado: placas não encontradas no SIMA

## Saídas HTTP (clients)

_Nenhuma — integração via view DW (leitura)._

## Regras de negócio vinculadas

| RN | Descrição |
| --- | --- |
| RN01 | Fonte = view DW |
| RN02 | Filtro status exato `'Veículo Faturado'` |
| RN03 | Match por placa |
| RN04 | Preencher DataDesativacao |
| RN05 | Estoque exclui inativos |
| RN06 | View indisponível → no-op |
| RN07 | Não reverter desativação |
| RN08 | Placa não encontrada → skip |
