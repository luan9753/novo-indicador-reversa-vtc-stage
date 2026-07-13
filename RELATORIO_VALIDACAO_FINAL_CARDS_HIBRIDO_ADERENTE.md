# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 15:26:20

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

- VTC_STAGE linhas brutas: 32.684
- VTC_STAGE deduplicada: 27.535
- Fonte original linhas brutas: 540.075
- Fonte original linhas consolidadas: 30.713
- Fonte original deduplicada: 24.575
- Com fonte original atualizada: 23.845
- Sem fonte original atualizada: 3.690
- Cobertura: 86,60%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `1d55bf770903fd808743cbbb0723815e3fda3cc549dfa9f7d6df29e9ed6c12b1`
- Hash fonte original fresca: `711b81c396580085c52f6a745fb91d56785577616999a9eecc05c9463498c681`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.535
- Linhas operacionais finais: 23.823
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 549, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3141, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.086 | 1.086 | 0 | OK |
| Loggers Entregues | 7.697 | 7.697 | 0 | OK |
| Loggers Retornados | 5.532 | 5.532 | 0 | OK |
| Loggers Pendentes | 2.165 | 2.165 | 0 | OK |
| Taxa de Retorno | 71,9% | 71,9% | +0,0 p,p, | OK |
| Taxa de Pendencia | 28,1% | 28,1% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.086
- Loggers Entregues: 7.697
- Loggers Retornados: 5.532
- Loggers Pendentes: 2.165
- Taxa de Retorno: 71.9%
- Taxa de Pendencia: 28.1%

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
