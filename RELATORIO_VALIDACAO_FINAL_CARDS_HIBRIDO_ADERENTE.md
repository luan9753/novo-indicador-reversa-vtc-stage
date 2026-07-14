# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 21:28:16

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

- VTC_STAGE linhas brutas: 32.275
- VTC_STAGE deduplicada: 27.292
- Fonte original linhas brutas: 540.562
- Fonte original linhas consolidadas: 30.647
- Fonte original deduplicada: 24.488
- Com fonte original atualizada: 23.761
- Sem fonte original atualizada: 3.531
- Cobertura: 87,06%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `ae2cc0cb020a69ae53cb1da31345d9ee280116e955f1d6ec61fcbf468fdfd26e`
- Hash fonte original fresca: `051efc871c7420237629d6c1c1c1e880ab60b9bb36e64312f9bca2754a2524d2`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.292
- Linhas operacionais finais: 23.739
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 526, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3005, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.105 | 1.105 | 0 | OK |
| Loggers Entregues | 7.752 | 7.752 | 0 | OK |
| Loggers Retornados | 5.764 | 5.764 | 0 | OK |
| Loggers Pendentes | 1.988 | 1.988 | 0 | OK |
| Taxa de Retorno | 74,4% | 74,4% | +0,0 p,p, | OK |
| Taxa de Pendencia | 25,6% | 25,6% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.105
- Loggers Entregues: 7.752
- Loggers Retornados: 5.764
- Loggers Pendentes: 1.988
- Taxa de Retorno: 74.4%
- Taxa de Pendencia: 25.6%

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
