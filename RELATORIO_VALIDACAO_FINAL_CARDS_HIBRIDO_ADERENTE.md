# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 16:42:17

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

- VTC_STAGE linhas brutas: 32.315
- VTC_STAGE deduplicada: 27.281
- Fonte original linhas brutas: 539.028
- Fonte original linhas consolidadas: 30.889
- Fonte original deduplicada: 24.674
- Com fonte original atualizada: 23.917
- Sem fonte original atualizada: 3.364
- Cobertura: 87,67%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `b0c880af35825d366e2e3460230e0f9cf5b06adc38e35a668fc456923359c982`
- Hash fonte original fresca: `6f972d70e4450443f79d4b310b58551bc3ff832eb5f206c51c23c23b62179a61`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.281
- Linhas operacionais finais: 23.895
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2889, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.179 | 1.179 | 0 | OK |
| Loggers Entregues | 8.342 | 8.342 | 0 | OK |
| Loggers Retornados | 5.834 | 5.834 | 0 | OK |
| Loggers Pendentes | 2.508 | 2.508 | 0 | OK |
| Taxa de Retorno | 69,9% | 69,9% | +0,0 p,p, | OK |
| Taxa de Pendencia | 30,1% | 30,1% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.179
- Loggers Entregues: 8.342
- Loggers Retornados: 5.834
- Loggers Pendentes: 2.508
- Taxa de Retorno: 69.9%
- Taxa de Pendencia: 30.1%

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
