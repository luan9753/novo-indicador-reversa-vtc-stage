# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 04:14:08

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

- VTC_STAGE linhas brutas: 32.494
- VTC_STAGE deduplicada: 27.426
- Fonte original linhas brutas: 539.841
- Fonte original linhas consolidadas: 30.352
- Fonte original deduplicada: 24.291
- Com fonte original atualizada: 23.749
- Sem fonte original atualizada: 3.677
- Cobertura: 86,59%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `64df3d83c956625c577fa6d3e1166572cdc9b83a11b43584f6e5a921385e1e6e`
- Hash fonte original fresca: `973a5c966407566b0bcd858ed8fe003529ed634493fe85e29c87ad47f991c35e`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.426
- Linhas operacionais finais: 23.727
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 538, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3139, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.165 | 1.165 | 0 | OK |
| Loggers Entregues | 7.938 | 7.938 | 0 | OK |
| Loggers Retornados | 5.672 | 5.672 | 0 | OK |
| Loggers Pendentes | 2.266 | 2.266 | 0 | OK |
| Taxa de Retorno | 71,5% | 71,5% | +0,0 p,p, | OK |
| Taxa de Pendencia | 28,5% | 28,5% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.165
- Loggers Entregues: 7.938
- Loggers Retornados: 5.672
- Loggers Pendentes: 2.266
- Taxa de Retorno: 71.5%
- Taxa de Pendencia: 28.5%

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
