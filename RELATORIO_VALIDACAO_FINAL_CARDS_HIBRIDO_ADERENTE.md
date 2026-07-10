# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 16:27:40

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

- VTC_STAGE linhas brutas: 32.307
- VTC_STAGE deduplicada: 27.275
- Fonte original linhas brutas: 538.979
- Fonte original linhas consolidadas: 30.859
- Fonte original deduplicada: 24.648
- Com fonte original atualizada: 23.911
- Sem fonte original atualizada: 3.364
- Cobertura: 87,67%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `a58b923a429556b944ba9cf246729d270933db5a154dd8125b6508e836ad9195`
- Hash fonte original fresca: `ee62f5506f43e0c4180c3b6ea800253244d820958144c8363ab4535d981836f8`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.275
- Linhas operacionais finais: 23.889
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2889, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.174 | 1.174 | 0 | OK |
| Loggers Entregues | 8.336 | 8.336 | 0 | OK |
| Loggers Retornados | 5.834 | 5.834 | 0 | OK |
| Loggers Pendentes | 2.502 | 2.502 | 0 | OK |
| Taxa de Retorno | 70,0% | 70,0% | +0,0 p,p, | OK |
| Taxa de Pendencia | 30,0% | 30,0% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.174
- Loggers Entregues: 8.336
- Loggers Retornados: 5.834
- Loggers Pendentes: 2.502
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
