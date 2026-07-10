# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 19:04:08

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

- VTC_STAGE linhas brutas: 32.424
- VTC_STAGE deduplicada: 27.339
- Fonte original linhas brutas: 539.212
- Fonte original linhas consolidadas: 30.975
- Fonte original deduplicada: 24.712
- Com fonte original atualizada: 23.975
- Sem fonte original atualizada: 3.364
- Cobertura: 87,70%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `ee8dc09512e2fed626dc04ccb38696d19bc661533c47f83895ca7989d39b7b40`
- Hash fonte original fresca: `8f960a38890899065c3ef60c58bc777618f3bdb6fda8614cc3954331e34051e8`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.339
- Linhas operacionais finais: 23.953
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2889, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.192 | 1.192 | 0 | OK |
| Loggers Entregues | 8.400 | 8.400 | 0 | OK |
| Loggers Retornados | 6.112 | 6.112 | 0 | OK |
| Loggers Pendentes | 2.288 | 2.288 | 0 | OK |
| Taxa de Retorno | 72,8% | 72,8% | +0,0 p,p, | OK |
| Taxa de Pendencia | 27,2% | 27,2% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.192
- Loggers Entregues: 8.400
- Loggers Retornados: 6.112
- Loggers Pendentes: 2.288
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
