# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 09/07/2026 17:52:23

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

- VTC_STAGE linhas brutas: 32.795
- VTC_STAGE deduplicada: 27.671
- Fonte original linhas brutas: 538.326
- Fonte original linhas consolidadas: 30.483
- Fonte original deduplicada: 24.387
- Com fonte original atualizada: 23.757
- Sem fonte original atualizada: 3.914
- Cobertura: 85,86%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `150a65a4ab93f7747298389bd65bdf2047c9503e567c1bf65c6c21c31924276b`
- Hash fonte original fresca: `29df2f0cf90530e26f10fe040b20ebcff66b8f9ac4a5a7a8daf503c115e3e14f`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.671
- Linhas operacionais finais: 23.735
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 481, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3433, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.149 | 1.149 | 0 | OK |
| Loggers Entregues | 8.640 | 8.640 | 0 | OK |
| Loggers Retornados | 6.073 | 6.073 | 0 | OK |
| Loggers Pendentes | 2.567 | 2.567 | 0 | OK |
| Taxa de Retorno | 70,3% | 70,3% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,7% | 29,7% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.149
- Loggers Entregues: 8.640
- Loggers Retornados: 6.073
- Loggers Pendentes: 2.567
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
