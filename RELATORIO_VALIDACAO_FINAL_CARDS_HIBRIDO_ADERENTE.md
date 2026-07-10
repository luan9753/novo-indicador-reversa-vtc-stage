# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 15:15:04

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

- VTC_STAGE linhas brutas: 32.184
- VTC_STAGE deduplicada: 27.195
- Fonte original linhas brutas: 538.831
- Fonte original linhas consolidadas: 30.732
- Fonte original deduplicada: 24.565
- Com fonte original atualizada: 23.831
- Sem fonte original atualizada: 3.364
- Cobertura: 87,63%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `e2f0f2335ac9b4cd2425b053b554ab5ca722b2b9499ceeee28d135ac83be2810`
- Hash fonte original fresca: `2bc518e3d52c101d6a694d3765722089bf9b56755cd114420d8b055f23159cae`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.195
- Linhas operacionais finais: 23.809
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2889, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.160 | 1.160 | 0 | OK |
| Loggers Entregues | 8.256 | 8.256 | 0 | OK |
| Loggers Retornados | 5.834 | 5.834 | 0 | OK |
| Loggers Pendentes | 2.422 | 2.422 | 0 | OK |
| Taxa de Retorno | 70,7% | 70,7% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,3% | 29,3% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.160
- Loggers Entregues: 8.256
- Loggers Retornados: 5.834
- Loggers Pendentes: 2.422
- Taxa de Retorno: 70.7%
- Taxa de Pendencia: 29.3%

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
