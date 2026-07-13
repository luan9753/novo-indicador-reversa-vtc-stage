# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 01:41:44

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
- Fonte original linhas brutas: 539.704
- Fonte original linhas consolidadas: 30.480
- Fonte original deduplicada: 24.415
- Com fonte original atualizada: 23.735
- Sem fonte original atualizada: 3.691
- Cobertura: 86,54%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `78b282d84ba7ccdf8c95df432fefc6a202ff4bb82f608934a08f4e1184203ebc`
- Hash fonte original fresca: `06afcf2642f90d1b158d7c1910c6da5afb382c80fc89ecea06c6098966561c65`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.426
- Linhas operacionais finais: 23.713
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 555, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3136, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.165 | 1.165 | 0 | OK |
| Loggers Entregues | 7.921 | 7.921 | 0 | OK |
| Loggers Retornados | 5.590 | 5.590 | 0 | OK |
| Loggers Pendentes | 2.331 | 2.331 | 0 | OK |
| Taxa de Retorno | 70,6% | 70,6% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,4% | 29,4% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.165
- Loggers Entregues: 7.921
- Loggers Retornados: 5.590
- Loggers Pendentes: 2.331
- Taxa de Retorno: 70.6%
- Taxa de Pendencia: 29.4%

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
