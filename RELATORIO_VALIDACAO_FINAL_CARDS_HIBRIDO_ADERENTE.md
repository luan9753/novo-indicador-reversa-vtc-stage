# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 14/07/2026 09:36:50

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

- VTC_STAGE linhas brutas: 32.523
- VTC_STAGE deduplicada: 27.533
- Fonte original linhas brutas: 541.057
- Fonte original linhas consolidadas: 30.495
- Fonte original deduplicada: 24.353
- Com fonte original atualizada: 23.871
- Sem fonte original atualizada: 3.662
- Cobertura: 86,70%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `4c0568f3a70809c5dfb2a99cd7440035310b9c10aa29aefc6d6b52ca110706b2`
- Hash fonte original fresca: `3124dd128b83145326c2c0ff7b0a0c398aa9f83ce3ffef75f81da9ea4e5931ea`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.533
- Linhas operacionais finais: 23.849
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 517, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3145, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.120 | 1.120 | 0 | OK |
| Loggers Entregues | 8.002 | 8.002 | 0 | OK |
| Loggers Retornados | 5.774 | 5.774 | 0 | OK |
| Loggers Pendentes | 2.228 | 2.228 | 0 | OK |
| Taxa de Retorno | 72,2% | 72,2% | +0,0 p,p, | OK |
| Taxa de Pendencia | 27,8% | 27,8% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.120
- Loggers Entregues: 8.002
- Loggers Retornados: 5.774
- Loggers Pendentes: 2.228
- Taxa de Retorno: 72.2%
- Taxa de Pendencia: 27.8%

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
