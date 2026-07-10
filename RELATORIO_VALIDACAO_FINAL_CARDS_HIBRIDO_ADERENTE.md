# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 09:28:58

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

- VTC_STAGE linhas brutas: 31.998
- VTC_STAGE deduplicada: 27.064
- Fonte original linhas brutas: 538.568
- Fonte original linhas consolidadas: 30.548
- Fonte original deduplicada: 24.437
- Com fonte original atualizada: 23.703
- Sem fonte original atualizada: 3.361
- Cobertura: 87,58%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `613794b6f54c6b1caeabdd2fba6ad677c6f7d0c1c96cc67f036f38b992d81354`
- Hash fonte original fresca: `dda45ae91ca372a099c7316a7746caec1f636b89e2cc3201c766130de5c3b3b0`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.064
- Linhas operacionais finais: 23.681
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2886, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.163 | 1.163 | 0 | OK |
| Loggers Entregues | 8.703 | 8.703 | 0 | OK |
| Loggers Retornados | 6.273 | 6.273 | 0 | OK |
| Loggers Pendentes | 2.430 | 2.430 | 0 | OK |
| Taxa de Retorno | 72,1% | 72,1% | +0,0 p,p, | OK |
| Taxa de Pendencia | 27,9% | 27,9% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.163
- Loggers Entregues: 8.703
- Loggers Retornados: 6.273
- Loggers Pendentes: 2.430
- Taxa de Retorno: 72.1%
- Taxa de Pendencia: 27.9%

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
