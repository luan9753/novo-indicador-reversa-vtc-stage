# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 18:36:49

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

- VTC_STAGE linhas brutas: 32.422
- VTC_STAGE deduplicada: 27.337
- Fonte original linhas brutas: 539.207
- Fonte original linhas consolidadas: 30.973
- Fonte original deduplicada: 24.710
- Com fonte original atualizada: 23.973
- Sem fonte original atualizada: 3.364
- Cobertura: 87,69%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `dda282035c6ad4f1de54aba19c720b634da3d2c6d50b303051792f62be9a617d`
- Hash fonte original fresca: `ce769d285d8babec9f6b20699d301cfb23d1b8d9447d368993e670bbbdb20af1`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.337
- Linhas operacionais finais: 23.951
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2889, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.190 | 1.190 | 0 | OK |
| Loggers Entregues | 8.398 | 8.398 | 0 | OK |
| Loggers Retornados | 6.112 | 6.112 | 0 | OK |
| Loggers Pendentes | 2.286 | 2.286 | 0 | OK |
| Taxa de Retorno | 72,8% | 72,8% | +0,0 p,p, | OK |
| Taxa de Pendencia | 27,2% | 27,2% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.190
- Loggers Entregues: 8.398
- Loggers Retornados: 6.112
- Loggers Pendentes: 2.286
- Taxa de Retorno: 72.8%
- Taxa de Pendencia: 27.2%

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
