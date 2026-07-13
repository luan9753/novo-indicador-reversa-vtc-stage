# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 07:39:12

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

- VTC_STAGE linhas brutas: 32.546
- VTC_STAGE deduplicada: 27.465
- Fonte original linhas brutas: 539.889
- Fonte original linhas consolidadas: 30.386
- Fonte original deduplicada: 24.319
- Com fonte original atualizada: 23.777
- Sem fonte original atualizada: 3.688
- Cobertura: 86,57%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `728de7494fbbd67f33108fd4c6ec52049bd0d85fa4067cbeda2812234ca25f0b`
- Hash fonte original fresca: `4d75cce263075ba6640181124a7f974bcd2f10141342ab07f0493b625b64402f`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.465
- Linhas operacionais finais: 23.755
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 549, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3139, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.167 | 1.167 | 0 | OK |
| Loggers Entregues | 7.966 | 7.966 | 0 | OK |
| Loggers Retornados | 5.682 | 5.682 | 0 | OK |
| Loggers Pendentes | 2.284 | 2.284 | 0 | OK |
| Taxa de Retorno | 71,3% | 71,3% | +0,0 p,p, | OK |
| Taxa de Pendencia | 28,7% | 28,7% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.167
- Loggers Entregues: 7.966
- Loggers Retornados: 5.682
- Loggers Pendentes: 2.284
- Taxa de Retorno: 71.3%
- Taxa de Pendencia: 28.7%

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
