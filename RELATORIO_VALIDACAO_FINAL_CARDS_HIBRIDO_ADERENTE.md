# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 14/07/2026 11:26:01

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

- VTC_STAGE linhas brutas: 32.610
- VTC_STAGE deduplicada: 27.613
- Fonte original linhas brutas: 541.140
- Fonte original linhas consolidadas: 30.593
- Fonte original deduplicada: 24.408
- Com fonte original atualizada: 23.884
- Sem fonte original atualizada: 3.729
- Cobertura: 86,50%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `46f0ca0d0f44309225d8ccaaf0f4f713a5474b5e1c2ee401b312222271cbf9b0`
- Hash fonte original fresca: `cc232a36c44da68a2f9b93f9a2f24ed0287ed623c71b4a67ba5a814271531330`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.613
- Linhas operacionais finais: 23.862
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 517, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3212, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.124 | 1.124 | 0 | OK |
| Loggers Entregues | 8.015 | 8.015 | 0 | OK |
| Loggers Retornados | 5.811 | 5.811 | 0 | OK |
| Loggers Pendentes | 2.204 | 2.204 | 0 | OK |
| Taxa de Retorno | 72,5% | 72,5% | +0,0 p,p, | OK |
| Taxa de Pendencia | 27,5% | 27,5% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.124
- Loggers Entregues: 8.015
- Loggers Retornados: 5.811
- Loggers Pendentes: 2.204
- Taxa de Retorno: 72.5%
- Taxa de Pendencia: 27.5%

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
