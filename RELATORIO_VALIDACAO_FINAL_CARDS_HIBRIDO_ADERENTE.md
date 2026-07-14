# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 14/07/2026 08:52:19

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

- VTC_STAGE linhas brutas: 32.522
- VTC_STAGE deduplicada: 27.532
- Fonte original linhas brutas: 541.047
- Fonte original linhas consolidadas: 30.494
- Fonte original deduplicada: 24.352
- Com fonte original atualizada: 23.870
- Sem fonte original atualizada: 3.662
- Cobertura: 86,70%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `34ccfbba57747d885967922b671058ddbaba41d364042ebec9202af85ad9ad5d`
- Hash fonte original fresca: `b61baacf9f83921cf9a5560439f9342a66065fd1ae514ebfe2455ec2b575f0a7`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.532
- Linhas operacionais finais: 23.848
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 517, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3145, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.119 | 1.119 | 0 | OK |
| Loggers Entregues | 8.001 | 8.001 | 0 | OK |
| Loggers Retornados | 5.773 | 5.773 | 0 | OK |
| Loggers Pendentes | 2.228 | 2.228 | 0 | OK |
| Taxa de Retorno | 72,2% | 72,2% | +0,0 p,p, | OK |
| Taxa de Pendencia | 27,8% | 27,8% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.119
- Loggers Entregues: 8.001
- Loggers Retornados: 5.773
- Loggers Pendentes: 2.228
- Taxa de Retorno: 72.2%
- Taxa de Pendencia: 27.8%

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
