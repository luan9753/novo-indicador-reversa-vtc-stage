# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 13:47:29

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

- VTC_STAGE linhas brutas: 32.683
- VTC_STAGE deduplicada: 27.534
- Fonte original linhas brutas: 540.044
- Fonte original linhas consolidadas: 30.706
- Fonte original deduplicada: 24.569
- Com fonte original atualizada: 23.845
- Sem fonte original atualizada: 3.689
- Cobertura: 86,60%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `af89cca03ce43299e175028a1188d6901c299f34ae7a0fddc361fef20bcf50e0`
- Hash fonte original fresca: `e0768546b8341f216f55144d2ba74555e827e92e89013d82f7b8df87cbd20787`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.534
- Linhas operacionais finais: 23.823
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 549, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3140, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.086 | 1.086 | 0 | OK |
| Loggers Entregues | 7.697 | 7.697 | 0 | OK |
| Loggers Retornados | 5.527 | 5.527 | 0 | OK |
| Loggers Pendentes | 2.170 | 2.170 | 0 | OK |
| Taxa de Retorno | 71,8% | 71,8% | +0,0 p,p, | OK |
| Taxa de Pendencia | 28,2% | 28,2% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.086
- Loggers Entregues: 7.697
- Loggers Retornados: 5.527
- Loggers Pendentes: 2.170
- Taxa de Retorno: 71.8%
- Taxa de Pendencia: 28.2%

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
