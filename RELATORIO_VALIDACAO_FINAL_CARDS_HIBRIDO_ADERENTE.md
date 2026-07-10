# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 11:12:26

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

- VTC_STAGE linhas brutas: 32.025
- VTC_STAGE deduplicada: 27.085
- Fonte original linhas brutas: 538.632
- Fonte original linhas consolidadas: 30.590
- Fonte original deduplicada: 24.465
- Com fonte original atualizada: 23.722
- Sem fonte original atualizada: 3.363
- Cobertura: 87,58%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `2d1ac206178ce408f6e2d0a17c817bd4bd8624b5b2fa3fc58557470e7465a691`
- Hash fonte original fresca: `4c3b397618c0334cd3d9e4300eff0761591f051236104137914fe7207b51ce3b`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.085
- Linhas operacionais finais: 23.700
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2888, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.140 | 1.140 | 0 | OK |
| Loggers Entregues | 8.147 | 8.147 | 0 | OK |
| Loggers Retornados | 5.720 | 5.720 | 0 | OK |
| Loggers Pendentes | 2.427 | 2.427 | 0 | OK |
| Taxa de Retorno | 70,2% | 70,2% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,8% | 29,8% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.140
- Loggers Entregues: 8.147
- Loggers Retornados: 5.720
- Loggers Pendentes: 2.427
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
