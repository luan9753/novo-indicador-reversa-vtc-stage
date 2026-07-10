# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 05:50:39

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

- VTC_STAGE linhas brutas: 31.964
- VTC_STAGE deduplicada: 27.035
- Fonte original linhas brutas: 538.483
- Fonte original linhas consolidadas: 30.513
- Fonte original deduplicada: 24.407
- Com fonte original atualizada: 23.674
- Sem fonte original atualizada: 3.361
- Cobertura: 87,57%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `880525b4fb545da83def7d6b9fddba1e09a929c952f4f9fed1e1eeebfadea263`
- Hash fonte original fresca: `9a0e7da12cc64fd63f012fb5e378def5b6718978c2a71d6c7c1ceee93b190abe`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.035
- Linhas operacionais finais: 23.652
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2886, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.159 | 1.159 | 0 | OK |
| Loggers Entregues | 8.674 | 8.674 | 0 | OK |
| Loggers Retornados | 6.235 | 6.235 | 0 | OK |
| Loggers Pendentes | 2.439 | 2.439 | 0 | OK |
| Taxa de Retorno | 71,9% | 71,9% | +0,0 p,p, | OK |
| Taxa de Pendencia | 28,1% | 28,1% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.159
- Loggers Entregues: 8.674
- Loggers Retornados: 6.235
- Loggers Pendentes: 2.439
- Taxa de Retorno: 71.9%
- Taxa de Pendencia: 28.1%

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
