# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 20:13:05

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

- VTC_STAGE linhas brutas: 32.588
- VTC_STAGE deduplicada: 27.501
- Fonte original linhas brutas: 539.225
- Fonte original linhas consolidadas: 31.030
- Fonte original deduplicada: 24.766
- Com fonte original atualizada: 24.029
- Sem fonte original atualizada: 3.472
- Cobertura: 87,38%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `24fa83246bc1404acdd7c5e9ad4248be560daca36ef578f940c186f49233d57b`
- Hash fonte original fresca: `a01d6f3fcb6bfccb0164a2fd7bf1e833f18bb7dbf5ecf463cab51c0ba1e3117d`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.501
- Linhas operacionais finais: 24.007
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 583, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2889, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.196 | 1.196 | 0 | OK |
| Loggers Entregues | 8.454 | 8.454 | 0 | OK |
| Loggers Retornados | 6.112 | 6.112 | 0 | OK |
| Loggers Pendentes | 2.342 | 2.342 | 0 | OK |
| Taxa de Retorno | 72,3% | 72,3% | +0,0 p,p, | OK |
| Taxa de Pendencia | 27,7% | 27,7% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.196
- Loggers Entregues: 8.454
- Loggers Retornados: 6.112
- Loggers Pendentes: 2.342
- Taxa de Retorno: 72.3%
- Taxa de Pendencia: 27.7%

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
