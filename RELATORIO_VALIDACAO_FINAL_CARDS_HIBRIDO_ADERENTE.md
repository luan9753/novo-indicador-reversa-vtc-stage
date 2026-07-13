# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 17:03:39

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
- Fonte original linhas brutas: 540.328
- Fonte original linhas consolidadas: 30.754
- Fonte original deduplicada: 24.603
- Com fonte original atualizada: 23.878
- Sem fonte original atualizada: 3.679
- Cobertura: 86,65%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `2b0c5f37f2ab201801e6b50b2ba6197dc77a5a911efd060dd60abd449cf9a41c`
- Hash fonte original fresca: `c44a608508de9aa969b71b65b4b913a630132f68a5c0e1fc44b72263ec803650`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.557
- Linhas operacionais finais: 23.856
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 537, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3142, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.093 | 1.093 | 0 | OK |
| Loggers Entregues | 7.730 | 7.730 | 0 | OK |
| Loggers Retornados | 5.754 | 5.754 | 0 | OK |
| Loggers Pendentes | 1.976 | 1.976 | 0 | OK |
| Taxa de Retorno | 74,4% | 74,4% | +0,0 p,p, | OK |
| Taxa de Pendencia | 25,6% | 25,6% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.093
- Loggers Entregues: 7.730
- Loggers Retornados: 5.754
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
