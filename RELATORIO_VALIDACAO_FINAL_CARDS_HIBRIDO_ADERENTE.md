# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 09/07/2026 17:24:28

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

- VTC_STAGE linhas brutas: 32.752
- VTC_STAGE deduplicada: 27.629
- Fonte original linhas brutas: 538.325
- Fonte original linhas consolidadas: 30.393
- Fonte original deduplicada: 24.305
- Com fonte original atualizada: 23.690
- Sem fonte original atualizada: 3.939
- Cobertura: 85,74%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `7ebd5630ee0f07882b8e299f3dd57f51350ac76c8fb66cda079a0c6c7932f3d7`
- Hash fonte original fresca: `ffaa04f09f7f415dd824e662667326b8de7f347c4874b0afe324b26121ffcd34`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.629
- Linhas operacionais finais: 23.668
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 481, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3458, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.146 | 1.146 | 0 | OK |
| Loggers Entregues | 8.573 | 8.573 | 0 | OK |
| Loggers Retornados | 6.073 | 6.073 | 0 | OK |
| Loggers Pendentes | 2.500 | 2.500 | 0 | OK |
| Taxa de Retorno | 70,8% | 70,8% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,2% | 29,2% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.146
- Loggers Entregues: 8.573
- Loggers Retornados: 6.073
- Loggers Pendentes: 2.500
- Taxa de Retorno: 70.8%
- Taxa de Pendencia: 29.2%

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
