# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 21:13:42

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

- VTC_STAGE linhas brutas: 32.275
- VTC_STAGE deduplicada: 27.292
- Fonte original linhas brutas: 540.518
- Fonte original linhas consolidadas: 30.629
- Fonte original deduplicada: 24.470
- Com fonte original atualizada: 23.752
- Sem fonte original atualizada: 3.540
- Cobertura: 87,03%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `79a8f340eae0ad69098b44af6b3883dc84d91349a72343d12b0a19c4c2ea2612`
- Hash fonte original fresca: `666573bdac336f2e8e849d191bb1827d7c9c9831cc17842e57bf28c81a402dfe`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.292
- Linhas operacionais finais: 23.730
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 535, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3005, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.105 | 1.105 | 0 | OK |
| Loggers Entregues | 7.743 | 7.743 | 0 | OK |
| Loggers Retornados | 5.755 | 5.755 | 0 | OK |
| Loggers Pendentes | 1.988 | 1.988 | 0 | OK |
| Taxa de Retorno | 74,3% | 74,3% | +0,0 p,p, | OK |
| Taxa de Pendencia | 25,7% | 25,7% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.105
- Loggers Entregues: 7.743
- Loggers Retornados: 5.755
- Loggers Pendentes: 1.988
- Taxa de Retorno: 74.3%
- Taxa de Pendencia: 25.7%

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
