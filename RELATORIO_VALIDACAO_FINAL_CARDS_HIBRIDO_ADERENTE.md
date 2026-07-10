# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 19:58:55

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

- VTC_STAGE linhas brutas: 32.426
- VTC_STAGE deduplicada: 27.341
- Fonte original linhas brutas: 539.222
- Fonte original linhas consolidadas: 30.977
- Fonte original deduplicada: 24.714
- Com fonte original atualizada: 23.977
- Sem fonte original atualizada: 3.364
- Cobertura: 87,70%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `fefbcac6c23c0e37b1e17ae2f9d67e663ca7c980fd78977903a02b9cde069f08`
- Hash fonte original fresca: `7335989af40bdcfe506ca331a87307f02e94883fcdcb186c7715966fc9e3b816`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.341
- Linhas operacionais finais: 23.955
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2889, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.194 | 1.194 | 0 | OK |
| Loggers Entregues | 8.402 | 8.402 | 0 | OK |
| Loggers Retornados | 6.112 | 6.112 | 0 | OK |
| Loggers Pendentes | 2.290 | 2.290 | 0 | OK |
| Taxa de Retorno | 72,7% | 72,7% | +0,0 p,p, | OK |
| Taxa de Pendencia | 27,3% | 27,3% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.194
- Loggers Entregues: 8.402
- Loggers Retornados: 6.112
- Loggers Pendentes: 2.290
- Taxa de Retorno: 72.7%
- Taxa de Pendencia: 27.3%

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
