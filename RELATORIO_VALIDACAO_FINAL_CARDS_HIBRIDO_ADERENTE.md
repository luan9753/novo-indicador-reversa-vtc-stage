# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 14/07/2026 14:41:36

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

- VTC_STAGE linhas brutas: 32.695
- VTC_STAGE deduplicada: 27.659
- Fonte original linhas brutas: 541.280
- Fonte original linhas consolidadas: 30.549
- Fonte original deduplicada: 24.361
- Com fonte original atualizada: 23.869
- Sem fonte original atualizada: 3.790
- Cobertura: 86,30%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `e0caac33bdbd0b2f390a985e67de6fbc648e647b6707c87314df21d31befdde1`
- Hash fonte original fresca: `84378d24244d7077dc5d421866bbe46104309d0e4bdf2a631b7810906b9cafc0`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.659
- Linhas operacionais finais: 23.847
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 517, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3273, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.133 | 1.133 | 0 | OK |
| Loggers Entregues | 8.061 | 8.061 | 0 | OK |
| Loggers Retornados | 5.919 | 5.919 | 0 | OK |
| Loggers Pendentes | 2.142 | 2.142 | 0 | OK |
| Taxa de Retorno | 73,4% | 73,4% | +0,0 p,p, | OK |
| Taxa de Pendencia | 26,6% | 26,6% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.133
- Loggers Entregues: 8.061
- Loggers Retornados: 5.919
- Loggers Pendentes: 2.142
- Taxa de Retorno: 73.4%
- Taxa de Pendencia: 26.6%

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
