# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 17:41:25

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

- VTC_STAGE linhas brutas: 32.346
- VTC_STAGE deduplicada: 27.308
- Fonte original linhas brutas: 539.181
- Fonte original linhas consolidadas: 30.900
- Fonte original deduplicada: 24.681
- Com fonte original atualizada: 23.944
- Sem fonte original atualizada: 3.364
- Cobertura: 87,68%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `16b55e8793c50bcbc95347deaa40f07222622c209379912d8f8c3444a5fb2e66`
- Hash fonte original fresca: `65068645f4c1a23a971854d36adcbf1d75475c554830de1c61e7e0d43eb4e614`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.308
- Linhas operacionais finais: 23.922
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2889, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.186 | 1.186 | 0 | OK |
| Loggers Entregues | 8.369 | 8.369 | 0 | OK |
| Loggers Retornados | 6.112 | 6.112 | 0 | OK |
| Loggers Pendentes | 2.257 | 2.257 | 0 | OK |
| Taxa de Retorno | 73,0% | 73,0% | +0,0 p,p, | OK |
| Taxa de Pendencia | 27,0% | 27,0% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.186
- Loggers Entregues: 8.369
- Loggers Retornados: 6.112
- Loggers Pendentes: 2.257
- Taxa de Retorno: 73.0%
- Taxa de Pendencia: 27.0%

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
