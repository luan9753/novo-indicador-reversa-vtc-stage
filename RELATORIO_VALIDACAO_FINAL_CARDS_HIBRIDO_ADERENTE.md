# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 09/07/2026 18:06:25

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

- VTC_STAGE linhas brutas: 32.815
- VTC_STAGE deduplicada: 27.686
- Fonte original linhas brutas: 538.328
- Fonte original linhas consolidadas: 30.496
- Fonte original deduplicada: 24.399
- Com fonte original atualizada: 23.772
- Sem fonte original atualizada: 3.914
- Cobertura: 85,86%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `049f85f9a17b5ffeab9df493394f18f102aa5d6a68d2e9f68cb20592415c90da`
- Hash fonte original fresca: `cfc55e6e5f197cbd36834d7ee9244d425cf0884e2b829f5fa6465e172688c4cd`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.686
- Linhas operacionais finais: 23.750
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 481, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3433, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.151 | 1.151 | 0 | OK |
| Loggers Entregues | 8.655 | 8.655 | 0 | OK |
| Loggers Retornados | 6.073 | 6.073 | 0 | OK |
| Loggers Pendentes | 2.582 | 2.582 | 0 | OK |
| Taxa de Retorno | 70,2% | 70,2% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,8% | 29,8% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.151
- Loggers Entregues: 8.655
- Loggers Retornados: 6.073
- Loggers Pendentes: 2.582
- Taxa de Retorno: 70.2%
- Taxa de Pendencia: 29.8%

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
