# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 00:30:55

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

- VTC_STAGE linhas brutas: 32.494
- VTC_STAGE deduplicada: 27.426
- Fonte original linhas brutas: 539.674
- Fonte original linhas consolidadas: 30.487
- Fonte original deduplicada: 24.422
- Com fonte original atualizada: 23.742
- Sem fonte original atualizada: 3.684
- Cobertura: 86,57%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `91c2e2d8c0da822eff405625357f52cfc2edd928086920da8ddb90adeb289ed5`
- Hash fonte original fresca: `1fc3da5763c919c5674f40affce0e12936e7ad5836f796b9b3c78c420567fd2a`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.426
- Linhas operacionais finais: 23.720
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 555, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3129, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.165 | 1.165 | 0 | OK |
| Loggers Entregues | 7.921 | 7.921 | 0 | OK |
| Loggers Retornados | 5.590 | 5.590 | 0 | OK |
| Loggers Pendentes | 2.331 | 2.331 | 0 | OK |
| Taxa de Retorno | 70,6% | 70,6% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,4% | 29,4% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.165
- Loggers Entregues: 7.921
- Loggers Retornados: 5.590
- Loggers Pendentes: 2.331
- Taxa de Retorno: 70.6%
- Taxa de Pendencia: 29.4%

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
