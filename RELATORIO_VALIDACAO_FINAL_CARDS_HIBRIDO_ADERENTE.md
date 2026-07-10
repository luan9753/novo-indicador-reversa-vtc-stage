# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 13:22:27

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

- VTC_STAGE linhas brutas: 32.103
- VTC_STAGE deduplicada: 27.138
- Fonte original linhas brutas: 538.715
- Fonte original linhas consolidadas: 30.652
- Fonte original deduplicada: 24.509
- Com fonte original atualizada: 23.776
- Sem fonte original atualizada: 3.362
- Cobertura: 87,61%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `6cd697b4634b87c59013c38fcf02629964a4ba37a6199dbcc42fa955c89d3e8e`
- Hash fonte original fresca: `8efe74b7e57d6e40a5b91d75a468f9f7027f136c00d5f04b413c5a6b04a9e7ef`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.138
- Linhas operacionais finais: 23.754
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2887, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.155 | 1.155 | 0 | OK |
| Loggers Entregues | 8.201 | 8.201 | 0 | OK |
| Loggers Retornados | 5.834 | 5.834 | 0 | OK |
| Loggers Pendentes | 2.367 | 2.367 | 0 | OK |
| Taxa de Retorno | 71,1% | 71,1% | +0,0 p,p, | OK |
| Taxa de Pendencia | 28,9% | 28,9% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.155
- Loggers Entregues: 8.201
- Loggers Retornados: 5.834
- Loggers Pendentes: 2.367
- Taxa de Retorno: 71.1%
- Taxa de Pendencia: 28.9%

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
