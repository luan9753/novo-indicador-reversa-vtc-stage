# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 14/07/2026 07:26:55

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

- VTC_STAGE linhas brutas: 32.275
- VTC_STAGE deduplicada: 27.292
- Fonte original linhas brutas: 540.995
- Fonte original linhas consolidadas: 30.428
- Fonte original deduplicada: 24.290
- Com fonte original atualizada: 23.630
- Sem fonte original atualizada: 3.662
- Cobertura: 86,58%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `9f05bd1b4ce34522352f6deea15f8926f7ed2e8cc92a718c6690a1ca013e8b4e`
- Hash fonte original fresca: `4d276a34e3104b39b994d7ab92f1a28ed23bb25a01fcaef4cb622e417569e872`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.292
- Linhas operacionais finais: 23.608
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 517, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3145, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.105 | 1.105 | 0 | OK |
| Loggers Entregues | 7.761 | 7.761 | 0 | OK |
| Loggers Retornados | 5.773 | 5.773 | 0 | OK |
| Loggers Pendentes | 1.988 | 1.988 | 0 | OK |
| Taxa de Retorno | 74,4% | 74,4% | +0,0 p,p, | OK |
| Taxa de Pendencia | 25,6% | 25,6% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.105
- Loggers Entregues: 7.761
- Loggers Retornados: 5.773
- Loggers Pendentes: 1.988
- Taxa de Retorno: 74.4%
- Taxa de Pendencia: 25.6%

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
