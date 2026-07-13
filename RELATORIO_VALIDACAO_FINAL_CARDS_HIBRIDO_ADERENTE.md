# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 18:41:23

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

- VTC_STAGE linhas brutas: 32.737
- VTC_STAGE deduplicada: 27.569
- Fonte original linhas brutas: 540.411
- Fonte original linhas consolidadas: 30.768
- Fonte original deduplicada: 24.609
- Com fonte original atualizada: 23.891
- Sem fonte original atualizada: 3.678
- Cobertura: 86,66%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `3180386597c2eb050c3ed6fa4d434772dc0ddc778be4b34129e85e2b017dd0be`
- Hash fonte original fresca: `5f59e7f2cf5a329c5cfcd1c3b7d4c7e3c3a543ea63f58bfe295154777148bba8`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.569
- Linhas operacionais finais: 23.869
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 537, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3141, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.105 | 1.105 | 0 | OK |
| Loggers Entregues | 7.743 | 7.743 | 0 | OK |
| Loggers Retornados | 5.755 | 5.755 | 0 | OK |
| Loggers Pendentes | 1.988 | 1.988 | 0 | OK |
| Taxa de Retorno | 74,3% | 74,3% | +0,0 p,p, | OK |
| Taxa de Pendencia | 25,7% | 25,7% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.105
- Loggers Entregues: 7.743
- Loggers Retornados: 5.755
- Loggers Pendentes: 1.988
- Taxa de Retorno: 74.3%
- Taxa de Pendencia: 25.7%

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
