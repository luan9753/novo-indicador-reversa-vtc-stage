# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 12:11:12

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

- VTC_STAGE linhas brutas: 32.069
- VTC_STAGE deduplicada: 27.114
- Fonte original linhas brutas: 538.659
- Fonte original linhas consolidadas: 30.617
- Fonte original deduplicada: 24.484
- Com fonte original atualizada: 23.751
- Sem fonte original atualizada: 3.363
- Cobertura: 87,60%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `b82bab09598361bcad2ddaa469fb1b4d4a3434a127c7179519ff4d13bdab9b18`
- Hash fonte original fresca: `9f7d760757fa8d4bc426a0c2d5e489233342c183118ec0a110494c197eefe59c`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.114
- Linhas operacionais finais: 23.729
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2888, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.149 | 1.149 | 0 | OK |
| Loggers Entregues | 8.176 | 8.176 | 0 | OK |
| Loggers Retornados | 5.720 | 5.720 | 0 | OK |
| Loggers Pendentes | 2.456 | 2.456 | 0 | OK |
| Taxa de Retorno | 70,0% | 70,0% | +0,0 p,p, | OK |
| Taxa de Pendencia | 30,0% | 30,0% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.149
- Loggers Entregues: 8.176
- Loggers Retornados: 5.720
- Loggers Pendentes: 2.456
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
