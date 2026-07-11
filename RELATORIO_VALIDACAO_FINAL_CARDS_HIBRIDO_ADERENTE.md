# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 10/07/2026 22:17:58

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

- VTC_STAGE linhas brutas: 32.584
- VTC_STAGE deduplicada: 27.501
- Fonte original linhas brutas: 539.233
- Fonte original linhas consolidadas: 31.037
- Fonte original deduplicada: 24.773
- Com fonte original atualizada: 24.036
- Sem fonte original atualizada: 3.465
- Cobertura: 87,40%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `a45740a6af160f10c3a14ec8b2977bd36ff12689948c378dba4716e08e41d50a`
- Hash fonte original fresca: `e0951581af284aaa8c3bf1d42a0b90a18021ba86f9770aa3d35af3d664f793f0`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.501
- Linhas operacionais finais: 24.014
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 583, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2882, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.197 | 1.197 | 0 | OK |
| Loggers Entregues | 8.461 | 8.461 | 0 | OK |
| Loggers Retornados | 6.112 | 6.112 | 0 | OK |
| Loggers Pendentes | 2.349 | 2.349 | 0 | OK |
| Taxa de Retorno | 72,2% | 72,2% | +0,0 p,p, | OK |
| Taxa de Pendencia | 27,8% | 27,8% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.197
- Loggers Entregues: 8.461
- Loggers Retornados: 6.112
- Loggers Pendentes: 2.349
- Taxa de Retorno: 72.2%
- Taxa de Pendencia: 27.8%

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
