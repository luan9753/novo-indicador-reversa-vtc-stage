# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 09:58:43

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

- VTC_STAGE linhas brutas: 32.648
- VTC_STAGE deduplicada: 27.519
- Fonte original linhas brutas: 539.979
- Fonte original linhas consolidadas: 30.495
- Fonte original deduplicada: 24.380
- Com fonte original atualizada: 23.831
- Sem fonte original atualizada: 3.688
- Cobertura: 86,60%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `a13a7678fcdfc59aa732b2d72ccd1a89dfc80b66ebd4dcff50da4dc552d996ad`
- Hash fonte original fresca: `e432378e6c09c11572149f4b97c9810915dee496b91d4936975a354416cadcb0`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.519
- Linhas operacionais finais: 23.809
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 549, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3139, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.098 | 1.098 | 0 | OK |
| Loggers Entregues | 7.698 | 7.698 | 0 | OK |
| Loggers Retornados | 5.536 | 5.536 | 0 | OK |
| Loggers Pendentes | 2.162 | 2.162 | 0 | OK |
| Taxa de Retorno | 71,9% | 71,9% | +0,0 p,p, | OK |
| Taxa de Pendencia | 28,1% | 28,1% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.098
- Loggers Entregues: 7.698
- Loggers Retornados: 5.536
- Loggers Pendentes: 2.162
- Taxa de Retorno: 71.9%
- Taxa de Pendencia: 28.1%

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
