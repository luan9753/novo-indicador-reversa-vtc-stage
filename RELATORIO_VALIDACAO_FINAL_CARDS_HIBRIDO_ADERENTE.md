# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 14/07/2026 10:36:03

## Resultado

Status: `VALIDADO_COM_FONTES_FRESCAS`

O HTML hibrido aderente ao original foi regenerado usando somente fontes frescas.

## Fontes e campos

- Pedido = VTC_STAGE
- LPN = VTC_STAGE
- Logger/Tag = VTC_STAGE
- Romaneio = VTC_STAGE
- Agente = dtbTransporte - extracao fresca
- Status Retorno = dtbPortal - extracao fresca
- Ultimo Historico = dtbPortal - extracao fresca
- UF/Cidade/Destinatario = dtbTransporte - extracao fresca

## Execucao fresca

- VTC_STAGE linhas brutas: 32.539
- VTC_STAGE deduplicada: 27.544
- Fonte original linhas brutas: 541.104
- Fonte original linhas consolidadas: 30.512
- Fonte original deduplicada: 24.365
- Com fonte original atualizada: 23.881
- Sem fonte original atualizada: 3.663
- Cobertura: 86,70%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `0ab9d3f63ea8ea0ecde8b91436ae5bd3a91e8294ad7861faebb1005116453e88`
- Hash fonte original fresca: `c35bf2accb59ad201d937af0c905beba39b6f18268c376582706881a34b9fc01`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.544
- Linhas operacionais finais: 23.859
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 517, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3146, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.122 | 1.122 | 0 | OK |
| Loggers Entregues | 8.012 | 8.012 | 0 | OK |
| Loggers Retornados | 5.774 | 5.774 | 0 | OK |
| Loggers Pendentes | 2.238 | 2.238 | 0 | OK |
| Taxa de Retorno | 72,1% | 72,1% | +0,0 p,p, | OK |
| Taxa de Pendencia | 27,9% | 27,9% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.122
- Loggers Entregues: 8.012
- Loggers Retornados: 5.774
- Loggers Pendentes: 2.238
- Taxa de Retorno: 72.1%
- Taxa de Pendencia: 27.9%

## Confirmacoes

- Nao houve fallback local silencioso.
- Nao foi usado snapshot antigo como entrada.
- Se uma fonte falhasse, a execucao pararia com erro.
- Se uma trava operacional final falhar, a execucao levanta RuntimeError e preserva o HTML oficial anterior.
- O HTML principal `REVERSA_DATALOGGERS_VTC_STAGE.html` nao foi sobrescrito.
- O HTML oficial `REVERSA_DATALOGGERS_STAGE.html` foi substituido apenas apos validacao fail-closed.
- Nada foi publicado.
- Nenhum `git add`, commit ou push foi feito.
- Nenhum BAT antigo foi executado.
