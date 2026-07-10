# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 10:57:48

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

- VTC_STAGE linhas brutas: 32.022
- VTC_STAGE deduplicada: 27.082
- Fonte original linhas brutas: 538.626
- Fonte original linhas consolidadas: 30.571
- Fonte original deduplicada: 24.453
- Com fonte original atualizada: 23.720
- Sem fonte original atualizada: 3.362
- Cobertura: 87,59%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `c8e96aa98ef41614fc9f079ab226e7105aa06296a122bba169bad7540c6dd050`
- Hash fonte original fresca: `df82a43f2972b9af98cfa41a70e13b5378e7e393fae5c35b97473dd677eb0519`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.082
- Linhas operacionais finais: 23.698
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2887, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.138 | 1.138 | 0 | OK |
| Loggers Entregues | 8.145 | 8.145 | 0 | OK |
| Loggers Retornados | 5.720 | 5.720 | 0 | OK |
| Loggers Pendentes | 2.425 | 2.425 | 0 | OK |
| Taxa de Retorno | 70,2% | 70,2% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,8% | 29,8% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.138
- Loggers Entregues: 8.145
- Loggers Retornados: 5.720
- Loggers Pendentes: 2.425
- Taxa de Retorno: 70.2%
- Taxa de Pendencia: 29.8%

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
