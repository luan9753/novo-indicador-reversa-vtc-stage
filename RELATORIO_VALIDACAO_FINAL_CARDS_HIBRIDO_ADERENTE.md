# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 11/07/2026 11:46:06

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

- VTC_STAGE linhas brutas: 32.612
- VTC_STAGE deduplicada: 27.515
- Fonte original linhas brutas: 539.327
- Fonte original linhas consolidadas: 31.065
- Fonte original deduplicada: 24.787
- Com fonte original atualizada: 24.050
- Sem fonte original atualizada: 3.465
- Cobertura: 87,41%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `023a0d436dcf65377a3fd9aec9dd2a34574767ca0602656abd220be1d7966cae`
- Hash fonte original fresca: `7ace5d605ce19748a6d0a0fc4696ca20af168d1c33ffc22a215a5bd064efeef6`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.515
- Linhas operacionais finais: 24.028
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 583, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2882, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.159 | 1.159 | 0 | OK |
| Loggers Entregues | 7.916 | 7.916 | 0 | OK |
| Loggers Retornados | 5.561 | 5.561 | 0 | OK |
| Loggers Pendentes | 2.355 | 2.355 | 0 | OK |
| Taxa de Retorno | 70,3% | 70,3% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,7% | 29,7% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.159
- Loggers Entregues: 7.916
- Loggers Retornados: 5.561
- Loggers Pendentes: 2.355
- Taxa de Retorno: 70.3%
- Taxa de Pendencia: 29.7%

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
