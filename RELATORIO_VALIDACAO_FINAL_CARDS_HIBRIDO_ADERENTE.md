# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 08:29:20

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

- VTC_STAGE linhas brutas: 31.966
- VTC_STAGE deduplicada: 27.037
- Fonte original linhas brutas: 538.525
- Fonte original linhas consolidadas: 30.521
- Fonte original deduplicada: 24.412
- Com fonte original atualizada: 23.676
- Sem fonte original atualizada: 3.361
- Cobertura: 87,57%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `03022bfcb267c9e78418f4e88c821077e9fae5077e0d8e81f0ee5af988632c68`
- Hash fonte original fresca: `ff6546ebe099bf102def5591736e0b5ae28c4569b6b957d19b6d2e981fea85fa`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.037
- Linhas operacionais finais: 23.654
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2886, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.160 | 1.160 | 0 | OK |
| Loggers Entregues | 8.676 | 8.676 | 0 | OK |
| Loggers Retornados | 6.273 | 6.273 | 0 | OK |
| Loggers Pendentes | 2.403 | 2.403 | 0 | OK |
| Taxa de Retorno | 72,3% | 72,3% | +0,0 p,p, | OK |
| Taxa de Pendencia | 27,7% | 27,7% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.160
- Loggers Entregues: 8.676
- Loggers Retornados: 6.273
- Loggers Pendentes: 2.403
- Taxa de Retorno: 72.3%
- Taxa de Pendencia: 27.7%

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
