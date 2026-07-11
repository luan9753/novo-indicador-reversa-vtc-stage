# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 11/07/2026 00:49:02

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

- VTC_STAGE linhas brutas: 32.611
- VTC_STAGE deduplicada: 27.514
- Fonte original linhas brutas: 539.246
- Fonte original linhas consolidadas: 31.064
- Fonte original deduplicada: 24.786
- Com fonte original atualizada: 24.049
- Sem fonte original atualizada: 3.465
- Cobertura: 87,41%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `b90f47244fe6ba0bda97f16fe2b6b7883b236225b6b80668562e75814326d88c`
- Hash fonte original fresca: `3d9a2d777570c952120bfec99100a574d561117539e6916f6bba7dc9330d525f`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.514
- Linhas operacionais finais: 24.027
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 583, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2882, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.200 | 1.200 | 0 | OK |
| Loggers Entregues | 8.474 | 8.474 | 0 | OK |
| Loggers Retornados | 6.112 | 6.112 | 0 | OK |
| Loggers Pendentes | 2.362 | 2.362 | 0 | OK |
| Taxa de Retorno | 72,1% | 72,1% | +0,0 p,p, | OK |
| Taxa de Pendencia | 27,9% | 27,9% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.200
- Loggers Entregues: 8.474
- Loggers Retornados: 6.112
- Loggers Pendentes: 2.362
- Taxa de Retorno: 72.1%
- Taxa de Pendencia: 27.9%

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
