# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 09:58:44

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

- VTC_STAGE linhas brutas: 31.999
- VTC_STAGE deduplicada: 27.065
- Fonte original linhas brutas: 538.575
- Fonte original linhas consolidadas: 30.548
- Fonte original deduplicada: 24.437
- Com fonte original atualizada: 23.704
- Sem fonte original atualizada: 3.361
- Cobertura: 87,58%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `b5f644ae0b534e3535ee6ae46df31bca33dcce09035c622bc90b04027238332c`
- Hash fonte original fresca: `5243d850b06868ef0edd7a99df3aa3b9a4437ec79d3004ba1919401dda6d9e8a`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.065
- Linhas operacionais finais: 23.682
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2886, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.127 | 1.127 | 0 | OK |
| Loggers Entregues | 8.128 | 8.128 | 0 | OK |
| Loggers Retornados | 5.720 | 5.720 | 0 | OK |
| Loggers Pendentes | 2.408 | 2.408 | 0 | OK |
| Taxa de Retorno | 70,4% | 70,4% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,6% | 29,6% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.127
- Loggers Entregues: 8.128
- Loggers Retornados: 5.720
- Loggers Pendentes: 2.408
- Taxa de Retorno: 70.4%
- Taxa de Pendencia: 29.6%

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
