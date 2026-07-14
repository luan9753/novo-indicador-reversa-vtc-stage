# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 14/07/2026 08:36:07

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

- VTC_STAGE linhas brutas: 32.289
- VTC_STAGE deduplicada: 27.303
- Fonte original linhas brutas: 541.043
- Fonte original linhas consolidadas: 30.447
- Fonte original deduplicada: 24.305
- Com fonte original atualizada: 23.641
- Sem fonte original atualizada: 3.662
- Cobertura: 86,59%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `a736a79295f66e98ebe93c05ccaccb8fbe1354182e0544e8a6b49d799d771332`
- Hash fonte original fresca: `07e4a5e8a18e8a3e672b59567c8d57fdea33bb85c23ef028c218c355edaec72c`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.303
- Linhas operacionais finais: 23.619
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 517, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3145, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.106 | 1.106 | 0 | OK |
| Loggers Entregues | 7.772 | 7.772 | 0 | OK |
| Loggers Retornados | 5.773 | 5.773 | 0 | OK |
| Loggers Pendentes | 1.999 | 1.999 | 0 | OK |
| Taxa de Retorno | 74,3% | 74,3% | +0,0 p,p, | OK |
| Taxa de Pendencia | 25,7% | 25,7% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.106
- Loggers Entregues: 7.772
- Loggers Retornados: 5.773
- Loggers Pendentes: 1.999
- Taxa de Retorno: 74.3%
- Taxa de Pendencia: 25.7%

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
