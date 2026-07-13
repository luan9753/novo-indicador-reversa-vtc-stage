# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 08:33:58

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

- VTC_STAGE linhas brutas: 32.627
- VTC_STAGE deduplicada: 27.510
- Fonte original linhas brutas: 539.929
- Fonte original linhas consolidadas: 30.472
- Fonte original deduplicada: 24.369
- Com fonte original atualizada: 23.822
- Sem fonte original atualizada: 3.688
- Cobertura: 86,59%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `e043b0a8d4c3f565b4baa01a1e0919e2650eb6aa3cd5b5936914bf6075e356d0`
- Hash fonte original fresca: `c1cb35094f662c6b5dcae4cd1f3451a4b1beb17f0a6336361882020be12419ef`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.510
- Linhas operacionais finais: 23.800
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 549, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3139, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.095 | 1.095 | 0 | OK |
| Loggers Entregues | 7.689 | 7.689 | 0 | OK |
| Loggers Retornados | 5.453 | 5.453 | 0 | OK |
| Loggers Pendentes | 2.236 | 2.236 | 0 | OK |
| Taxa de Retorno | 70,9% | 70,9% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,1% | 29,1% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.095
- Loggers Entregues: 7.689
- Loggers Retornados: 5.453
- Loggers Pendentes: 2.236
- Taxa de Retorno: 70.9%
- Taxa de Pendencia: 29.1%

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
