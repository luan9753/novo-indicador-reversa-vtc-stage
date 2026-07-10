# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 10:43:11

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

- VTC_STAGE linhas brutas: 32.019
- VTC_STAGE deduplicada: 27.079
- Fonte original linhas brutas: 538.621
- Fonte original linhas consolidadas: 30.570
- Fonte original deduplicada: 24.452
- Com fonte original atualizada: 23.717
- Sem fonte original atualizada: 3.362
- Cobertura: 87,58%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `7f96bcd902150f15e836f1e0a2f37a9e5f7fb9b8a5e76e6df00402c8560b6469`
- Hash fonte original fresca: `628ed9d35b942776d2c0e0b2381902ac900b4373a0a49c1f27bf354d9dc2aeb5`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.079
- Linhas operacionais finais: 23.695
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2887, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.135 | 1.135 | 0 | OK |
| Loggers Entregues | 8.142 | 8.142 | 0 | OK |
| Loggers Retornados | 5.720 | 5.720 | 0 | OK |
| Loggers Pendentes | 2.422 | 2.422 | 0 | OK |
| Taxa de Retorno | 70,3% | 70,3% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,7% | 29,7% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.135
- Loggers Entregues: 8.142
- Loggers Retornados: 5.720
- Loggers Pendentes: 2.422
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
