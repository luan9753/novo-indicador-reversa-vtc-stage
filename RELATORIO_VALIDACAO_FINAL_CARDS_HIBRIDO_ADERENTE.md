# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 14:59:31

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

- VTC_STAGE linhas brutas: 32.148
- VTC_STAGE deduplicada: 27.172
- Fonte original linhas brutas: 538.811
- Fonte original linhas consolidadas: 30.731
- Fonte original deduplicada: 24.564
- Com fonte original atualizada: 23.808
- Sem fonte original atualizada: 3.364
- Cobertura: 87,62%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `7d9a416cd71a8068f3ed5de17fb476eb4579617fd4ba18958ee1217721948065`
- Hash fonte original fresca: `efb9ba0d440cb17ab50b6ad55aaa46bbac149f4fefaae3f16b4f8467d0e88848`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.172
- Linhas operacionais finais: 23.786
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2889, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.158 | 1.158 | 0 | OK |
| Loggers Entregues | 8.233 | 8.233 | 0 | OK |
| Loggers Retornados | 5.834 | 5.834 | 0 | OK |
| Loggers Pendentes | 2.399 | 2.399 | 0 | OK |
| Taxa de Retorno | 70,9% | 70,9% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,1% | 29,1% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.158
- Loggers Entregues: 8.233
- Loggers Retornados: 5.834
- Loggers Pendentes: 2.399
- Taxa de Retorno: 70.9%
- Taxa de Pendencia: 29.1%

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
