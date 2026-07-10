# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 10:27:54

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

- VTC_STAGE linhas brutas: 32.003
- VTC_STAGE deduplicada: 27.069
- Fonte original linhas brutas: 538.604
- Fonte original linhas consolidadas: 30.553
- Fonte original deduplicada: 24.442
- Com fonte original atualizada: 23.707
- Sem fonte original atualizada: 3.362
- Cobertura: 87,58%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `56cca6bdf8f5077b43ec65915fb9311c02dcc06fde282145eba44dc4f3e50cd2`
- Hash fonte original fresca: `b6de412867bd0eced3574544b609951e5c2a790a739202a7ce4a8cc31666677e`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.069
- Linhas operacionais finais: 23.685
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2887, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.131 | 1.131 | 0 | OK |
| Loggers Entregues | 8.132 | 8.132 | 0 | OK |
| Loggers Retornados | 5.720 | 5.720 | 0 | OK |
| Loggers Pendentes | 2.412 | 2.412 | 0 | OK |
| Taxa de Retorno | 70,3% | 70,3% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,7% | 29,7% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.131
- Loggers Entregues: 8.132
- Loggers Retornados: 5.720
- Loggers Pendentes: 2.412
- Taxa de Retorno: 70.3%
- Taxa de Pendencia: 29.7%

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
