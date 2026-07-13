# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 18:14:25

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

- VTC_STAGE linhas brutas: 32.730
- VTC_STAGE deduplicada: 27.562
- Fonte original linhas brutas: 540.405
- Fonte original linhas consolidadas: 30.768
- Fonte original deduplicada: 24.609
- Com fonte original atualizada: 23.884
- Sem fonte original atualizada: 3.678
- Cobertura: 86,66%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `eaf37cc202f681b166da5b5031b7cc8f4fab3e3dc27c315272b7fd21ba19109b`
- Hash fonte original fresca: `5f59e7f2cf5a329c5cfcd1c3b7d4c7e3c3a543ea63f58bfe295154777148bba8`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.562
- Linhas operacionais finais: 23.862
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 537, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3141, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.098 | 1.098 | 0 | OK |
| Loggers Entregues | 7.736 | 7.736 | 0 | OK |
| Loggers Retornados | 5.755 | 5.755 | 0 | OK |
| Loggers Pendentes | 1.981 | 1.981 | 0 | OK |
| Taxa de Retorno | 74,4% | 74,4% | +0,0 p,p, | OK |
| Taxa de Pendencia | 25,6% | 25,6% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.098
- Loggers Entregues: 7.736
- Loggers Retornados: 5.755
- Loggers Pendentes: 1.981
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
