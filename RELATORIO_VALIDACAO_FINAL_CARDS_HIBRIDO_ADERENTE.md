# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 09/07/2026 22:57:43

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

- VTC_STAGE linhas brutas: 31.951
- VTC_STAGE deduplicada: 27.029
- Fonte original linhas brutas: 538.389
- Fonte original linhas consolidadas: 30.499
- Fonte original deduplicada: 24.400
- Com fonte original atualizada: 23.668
- Sem fonte original atualizada: 3.361
- Cobertura: 87,57%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `9ec6f18cb10793b351a571b02ee2fdcf46fcf063dd486eefd230cd5dbde0ec2e`
- Hash fonte original fresca: `66e82f86b94abf0c42a8647ec330716842877753a219e048bc694399d3d9e83b`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.029
- Linhas operacionais finais: 23.646
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2886, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.153 | 1.153 | 0 | OK |
| Loggers Entregues | 8.668 | 8.668 | 0 | OK |
| Loggers Retornados | 6.105 | 6.105 | 0 | OK |
| Loggers Pendentes | 2.563 | 2.563 | 0 | OK |
| Taxa de Retorno | 70,4% | 70,4% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,6% | 29,6% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.153
- Loggers Entregues: 8.668
- Loggers Retornados: 6.105
- Loggers Pendentes: 2.563
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
