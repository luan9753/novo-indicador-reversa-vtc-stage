# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 18:23:10

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

- VTC_STAGE linhas brutas: 32.395
- VTC_STAGE deduplicada: 27.330
- Fonte original linhas brutas: 539.204
- Fonte original linhas consolidadas: 30.945
- Fonte original deduplicada: 24.702
- Com fonte original atualizada: 23.966
- Sem fonte original atualizada: 3.364
- Cobertura: 87,69%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `994a16b719ed17738210a8bc6782182e60f28dcf1961c1d5578412c3f7112843`
- Hash fonte original fresca: `a7b8c554f9758838e11faf5e50c76a68c595d362a644e1a6a5078e2bc3d4cd3d`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.330
- Linhas operacionais finais: 23.944
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 475, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2889, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.189 | 1.189 | 0 | OK |
| Loggers Entregues | 8.391 | 8.391 | 0 | OK |
| Loggers Retornados | 6.112 | 6.112 | 0 | OK |
| Loggers Pendentes | 2.279 | 2.279 | 0 | OK |
| Taxa de Retorno | 72,8% | 72,8% | +0,0 p,p, | OK |
| Taxa de Pendencia | 27,2% | 27,2% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.189
- Loggers Entregues: 8.391
- Loggers Retornados: 6.112
- Loggers Pendentes: 2.279
- Taxa de Retorno: 72.8%
- Taxa de Pendencia: 27.2%

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
