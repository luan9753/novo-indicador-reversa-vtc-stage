# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 14/07/2026 14:11:20

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

- VTC_STAGE linhas brutas: 32.693
- VTC_STAGE deduplicada: 27.657
- Fonte original linhas brutas: 541.242
- Fonte original linhas consolidadas: 30.543
- Fonte original deduplicada: 24.356
- Com fonte original atualizada: 23.867
- Sem fonte original atualizada: 3.790
- Cobertura: 86,30%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `362e2449602030eaaa6647cc3c01b9982c954156461cb0872521ba05a3c181ef`
- Hash fonte original fresca: `e0eb4abab16160fd87ceb24b571cb1bc6f938325d7ad837eef7b6dfe6e589ac2`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.657
- Linhas operacionais finais: 23.845
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 517, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3273, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.131 | 1.131 | 0 | OK |
| Loggers Entregues | 8.059 | 8.059 | 0 | OK |
| Loggers Retornados | 5.813 | 5.813 | 0 | OK |
| Loggers Pendentes | 2.246 | 2.246 | 0 | OK |
| Taxa de Retorno | 72,1% | 72,1% | +0,0 p,p, | OK |
| Taxa de Pendencia | 27,9% | 27,9% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.131
- Loggers Entregues: 8.059
- Loggers Retornados: 5.813
- Loggers Pendentes: 2.246
- Taxa de Retorno: 72.1%
- Taxa de Pendencia: 27.9%

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
