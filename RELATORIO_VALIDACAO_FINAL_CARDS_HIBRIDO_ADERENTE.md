# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 16:12:36

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

- VTC_STAGE linhas brutas: 32.245
- VTC_STAGE deduplicada: 27.214
- Fonte original linhas brutas: 538.956
- Fonte original linhas consolidadas: 30.854
- Fonte original deduplicada: 24.644
- Com fonte original atualizada: 23.850
- Sem fonte original atualizada: 3.364
- Cobertura: 87,64%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `e786c45f1cad1f3eb8256acc4dbae0baaffeff86a42ddf6142db6644b74b280e`
- Hash fonte original fresca: `e7cdaa315c1d5f7507bbd300e41680a2d5e682a368b9dec020f4a9729fb48b28`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.214
- Linhas operacionais finais: 23.828
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2889, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.169 | 1.169 | 0 | OK |
| Loggers Entregues | 8.275 | 8.275 | 0 | OK |
| Loggers Retornados | 5.834 | 5.834 | 0 | OK |
| Loggers Pendentes | 2.441 | 2.441 | 0 | OK |
| Taxa de Retorno | 70,5% | 70,5% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,5% | 29,5% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.169
- Loggers Entregues: 8.275
- Loggers Retornados: 5.834
- Loggers Pendentes: 2.441
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
