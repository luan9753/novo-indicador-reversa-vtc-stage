# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 11:27:12

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

- VTC_STAGE linhas brutas: 32.065
- VTC_STAGE deduplicada: 27.110
- Fonte original linhas brutas: 538.639
- Fonte original linhas consolidadas: 30.613
- Fonte original deduplicada: 24.480
- Com fonte original atualizada: 23.747
- Sem fonte original atualizada: 3.363
- Cobertura: 87,59%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `4c393de8b1ee9b89714bd0fd761f4d3b84031282b21777b845ba20befd49f49f`
- Hash fonte original fresca: `c32ed3acafff32d5a7645f3a591f91f3a1065069c111d8614fa02fd0b22de3c6`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.110
- Linhas operacionais finais: 23.725
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2888, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.145 | 1.145 | 0 | OK |
| Loggers Entregues | 8.172 | 8.172 | 0 | OK |
| Loggers Retornados | 5.720 | 5.720 | 0 | OK |
| Loggers Pendentes | 2.452 | 2.452 | 0 | OK |
| Taxa de Retorno | 70,0% | 70,0% | +0,0 p,p, | OK |
| Taxa de Pendencia | 30,0% | 30,0% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.145
- Loggers Entregues: 8.172
- Loggers Retornados: 5.720
- Loggers Pendentes: 2.452
- Taxa de Retorno: 70.0%
- Taxa de Pendencia: 30.0%

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
