# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 17:11:51

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

- VTC_STAGE linhas brutas: 32.339
- VTC_STAGE deduplicada: 27.302
- Fonte original linhas brutas: 539.110
- Fonte original linhas consolidadas: 30.889
- Fonte original deduplicada: 24.674
- Com fonte original atualizada: 23.938
- Sem fonte original atualizada: 3.364
- Cobertura: 87,68%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `544de1fb0781b9bb664431de9dd25c0f3e00143eb88fb77d5b5ef51174ad4965`
- Hash fonte original fresca: `eafd10f1350d8eabb69da327ccb8a0e9ee6bbe02fe9f6c06ec27009c7b8be233`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.302
- Linhas operacionais finais: 23.916
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2889, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.180 | 1.180 | 0 | OK |
| Loggers Entregues | 8.363 | 8.363 | 0 | OK |
| Loggers Retornados | 5.834 | 5.834 | 0 | OK |
| Loggers Pendentes | 2.529 | 2.529 | 0 | OK |
| Taxa de Retorno | 69,8% | 69,8% | +0,0 p,p, | OK |
| Taxa de Pendencia | 30,2% | 30,2% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.180
- Loggers Entregues: 8.363
- Loggers Retornados: 5.834
- Loggers Pendentes: 2.529
- Taxa de Retorno: 69.8%
- Taxa de Pendencia: 30.2%

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
