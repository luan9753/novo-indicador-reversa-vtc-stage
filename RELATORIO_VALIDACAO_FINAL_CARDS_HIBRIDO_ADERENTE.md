# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 11/07/2026 18:43:52

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

- VTC_STAGE linhas brutas: 32.617
- VTC_STAGE deduplicada: 27.519
- Fonte original linhas brutas: 539.524
- Fonte original linhas consolidadas: 31.070
- Fonte original deduplicada: 24.791
- Com fonte original atualizada: 24.054
- Sem fonte original atualizada: 3.465
- Cobertura: 87,41%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `e38c3c8b0f948ec4935b4ca0c653a9a50bee529c99113beb40a4b60000c204e6`
- Hash fonte original fresca: `c0a5246e0e18c430a13891838b457334d644287612dc36c9ef125b3ab73cdafd`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.519
- Linhas operacionais finais: 24.032
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 583, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2882, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.163 | 1.163 | 0 | OK |
| Loggers Entregues | 7.920 | 7.920 | 0 | OK |
| Loggers Retornados | 5.590 | 5.590 | 0 | OK |
| Loggers Pendentes | 2.330 | 2.330 | 0 | OK |
| Taxa de Retorno | 70,6% | 70,6% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,4% | 29,4% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.163
- Loggers Entregues: 7.920
- Loggers Retornados: 5.590
- Loggers Pendentes: 2.330
- Taxa de Retorno: 70.6%
- Taxa de Pendencia: 29.4%

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
