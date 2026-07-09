# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 09/07/2026 18:47:26

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

- VTC_STAGE linhas brutas: 32.831
- VTC_STAGE deduplicada: 27.699
- Fonte original linhas brutas: 538.332
- Fonte original linhas consolidadas: 30.499
- Fonte original deduplicada: 24.400
- Com fonte original atualizada: 23.785
- Sem fonte original atualizada: 3.914
- Cobertura: 85,87%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `f1d00b5ea31a8c83d568207c023b034cf6f24433e9de470cda9cb2d4eecd8bc9`
- Hash fonte original fresca: `c496788a23d713da45dd12809367401af0f764c58c835917b47f5fddd22b624a`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.699
- Linhas operacionais finais: 23.763
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 481, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3433, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.153 | 1.153 | 0 | OK |
| Loggers Entregues | 8.668 | 8.668 | 0 | OK |
| Loggers Retornados | 6.073 | 6.073 | 0 | OK |
| Loggers Pendentes | 2.595 | 2.595 | 0 | OK |
| Taxa de Retorno | 70,1% | 70,1% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,9% | 29,9% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.153
- Loggers Entregues: 8.668
- Loggers Retornados: 6.073
- Loggers Pendentes: 2.595
- Taxa de Retorno: 70.1%
- Taxa de Pendencia: 29.9%

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
