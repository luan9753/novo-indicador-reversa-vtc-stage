# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 17:17:40

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

- VTC_STAGE linhas brutas: 32.717
- VTC_STAGE deduplicada: 27.557
- Fonte original linhas brutas: 540.349
- Fonte original linhas consolidadas: 30.768
- Fonte original deduplicada: 24.609
- Com fonte original atualizada: 23.879
- Sem fonte original atualizada: 3.678
- Cobertura: 86,65%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `3b0c68e3da16cc961de24d14f06a181aa47650fa0582f91fed090ff02898ea12`
- Hash fonte original fresca: `7b1d05d71fff09fad8293b6be8e731ca905c84bdb29965f80f92a9b770ac2f0c`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.557
- Linhas operacionais finais: 23.857
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 537, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3141, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.093 | 1.093 | 0 | OK |
| Loggers Entregues | 7.731 | 7.731 | 0 | OK |
| Loggers Retornados | 5.755 | 5.755 | 0 | OK |
| Loggers Pendentes | 1.976 | 1.976 | 0 | OK |
| Taxa de Retorno | 74,4% | 74,4% | +0,0 p,p, | OK |
| Taxa de Pendencia | 25,6% | 25,6% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.093
- Loggers Entregues: 7.731
- Loggers Retornados: 5.755
- Loggers Pendentes: 1.976
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
