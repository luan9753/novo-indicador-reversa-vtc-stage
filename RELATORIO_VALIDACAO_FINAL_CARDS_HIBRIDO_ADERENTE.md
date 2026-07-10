# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 17:26:50

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

- VTC_STAGE linhas brutas: 32.341
- VTC_STAGE deduplicada: 27.304
- Fonte original linhas brutas: 539.159
- Fonte original linhas consolidadas: 30.891
- Fonte original deduplicada: 24.676
- Com fonte original atualizada: 23.940
- Sem fonte original atualizada: 3.364
- Cobertura: 87,68%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `572b8849310e5a272d82261d76b8727f0b640dbc2df85ce8665081e9f591aa00`
- Hash fonte original fresca: `ee360d28d1a76ffbe06cecf6da73eed14117f9a01ae0fc78672d40964d7ad7f4`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.304
- Linhas operacionais finais: 23.918
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2889, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.182 | 1.182 | 0 | OK |
| Loggers Entregues | 8.365 | 8.365 | 0 | OK |
| Loggers Retornados | 5.972 | 5.972 | 0 | OK |
| Loggers Pendentes | 2.393 | 2.393 | 0 | OK |
| Taxa de Retorno | 71,4% | 71,4% | +0,0 p,p, | OK |
| Taxa de Pendencia | 28,6% | 28,6% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.182
- Loggers Entregues: 8.365
- Loggers Retornados: 5.972
- Loggers Pendentes: 2.393
- Taxa de Retorno: 71.4%
- Taxa de Pendencia: 28.6%

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
