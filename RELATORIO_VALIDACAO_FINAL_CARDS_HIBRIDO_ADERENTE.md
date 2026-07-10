# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 14:17:59

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

- VTC_STAGE linhas brutas: 32.121
- VTC_STAGE deduplicada: 27.153
- Fonte original linhas brutas: 538.787
- Fonte original linhas consolidadas: 30.670
- Fonte original deduplicada: 24.524
- Com fonte original atualizada: 23.791
- Sem fonte original atualizada: 3.362
- Cobertura: 87,62%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `719ae6b70c6557127ca8247d757f44b84a5e67a73936b38319e5503d754bb15f`
- Hash fonte original fresca: `8b13e14adc9046f815adaf3c0a1a994329ff83ada350b7780e6b5e19ec87144f`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.153
- Linhas operacionais finais: 23.769
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2887, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.156 | 1.156 | 0 | OK |
| Loggers Entregues | 8.216 | 8.216 | 0 | OK |
| Loggers Retornados | 5.834 | 5.834 | 0 | OK |
| Loggers Pendentes | 2.382 | 2.382 | 0 | OK |
| Taxa de Retorno | 71,0% | 71,0% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,0% | 29,0% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.156
- Loggers Entregues: 8.216
- Loggers Retornados: 5.834
- Loggers Pendentes: 2.382
- Taxa de Retorno: 71.0%
- Taxa de Pendencia: 29.0%

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
