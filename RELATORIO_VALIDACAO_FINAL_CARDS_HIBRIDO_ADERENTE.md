# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 15:29:35

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

- VTC_STAGE linhas brutas: 32.185
- VTC_STAGE deduplicada: 27.196
- Fonte original linhas brutas: 538.870
- Fonte original linhas consolidadas: 30.732
- Fonte original deduplicada: 24.565
- Com fonte original atualizada: 23.832
- Sem fonte original atualizada: 3.364
- Cobertura: 87,63%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `1ef4e74ec6a0a2773d25f7c501e423a2abf6b7b41f44434dca3eb89a32a4ea45`
- Hash fonte original fresca: `2bc518e3d52c101d6a694d3765722089bf9b56755cd114420d8b055f23159cae`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.196
- Linhas operacionais finais: 23.810
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2889, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.161 | 1.161 | 0 | OK |
| Loggers Entregues | 8.257 | 8.257 | 0 | OK |
| Loggers Retornados | 5.834 | 5.834 | 0 | OK |
| Loggers Pendentes | 2.423 | 2.423 | 0 | OK |
| Taxa de Retorno | 70,7% | 70,7% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,3% | 29,3% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.161
- Loggers Entregues: 8.257
- Loggers Retornados: 5.834
- Loggers Pendentes: 2.423
- Taxa de Retorno: 70.7%
- Taxa de Pendencia: 29.3%

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
