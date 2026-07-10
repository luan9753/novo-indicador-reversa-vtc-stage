# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 13:08:20

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

- VTC_STAGE linhas brutas: 32.070
- VTC_STAGE deduplicada: 27.115
- Fonte original linhas brutas: 538.693
- Fonte original linhas consolidadas: 30.651
- Fonte original deduplicada: 24.508
- Com fonte original atualizada: 23.752
- Sem fonte original atualizada: 3.363
- Cobertura: 87,60%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `d07525e9d9d57ce671b6a0d009e5257484ed00f378835639f788486edf82b5ec`
- Hash fonte original fresca: `6381e7ab7fafaa75ce709d8bd0e3bd767eec862264baf1ba36059ec74fcf1eb1`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.115
- Linhas operacionais finais: 23.730
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2888, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.150 | 1.150 | 0 | OK |
| Loggers Entregues | 8.177 | 8.177 | 0 | OK |
| Loggers Retornados | 5.720 | 5.720 | 0 | OK |
| Loggers Pendentes | 2.457 | 2.457 | 0 | OK |
| Taxa de Retorno | 70,0% | 70,0% | +0,0 p,p, | OK |
| Taxa de Pendencia | 30,0% | 30,0% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.150
- Loggers Entregues: 8.177
- Loggers Retornados: 5.720
- Loggers Pendentes: 2.457
- Taxa de Retorno: 70.0%
- Taxa de Pendencia: 30.0%

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
