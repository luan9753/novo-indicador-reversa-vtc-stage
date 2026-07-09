# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 09/07/2026 15:44:54

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

- VTC_STAGE linhas brutas: 32.733
- VTC_STAGE deduplicada: 27.620
- Fonte original linhas brutas: 538.290
- Fonte original linhas consolidadas: 30.377
- Fonte original deduplicada: 24.298
- Com fonte original atualizada: 23.683
- Sem fonte original atualizada: 3.937
- Cobertura: 85,75%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `9cc97cbdbe31545ece8fa682c0edc17ead7c906105add41f41e44db8f149c0bc`
- Hash fonte original fresca: `4d56878caa8a565b498b63691ea0af7cea2014f5eb5600e2e6c9aee17311eae2`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.620
- Linhas operacionais finais: 23.661
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 481, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3456, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.137 | 1.137 | 0 | OK |
| Loggers Entregues | 8.564 | 8.564 | 0 | OK |
| Loggers Retornados | 6.034 | 6.034 | 0 | OK |
| Loggers Pendentes | 2.530 | 2.530 | 0 | OK |
| Taxa de Retorno | 70,5% | 70,5% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,5% | 29,5% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.137
- Loggers Entregues: 8.564
- Loggers Retornados: 6.034
- Loggers Pendentes: 2.530
- Taxa de Retorno: 70.5%
- Taxa de Pendencia: 29.5%

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
