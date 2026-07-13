# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 09:15:35

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

- VTC_STAGE linhas brutas: 32.638
- VTC_STAGE deduplicada: 27.516
- Fonte original linhas brutas: 539.961
- Fonte original linhas consolidadas: 30.494
- Fonte original deduplicada: 24.379
- Com fonte original atualizada: 23.828
- Sem fonte original atualizada: 3.688
- Cobertura: 86,60%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `6957a7640f26f4f94ae4ca2ba6156054988de92e9b8454e3045e1d873482915b`
- Hash fonte original fresca: `684109c3955b60a6e8733e5530693eb21a96230471f932f39b48b6eaa7502394`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.516
- Linhas operacionais finais: 23.806
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 549, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3139, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.097 | 1.097 | 0 | OK |
| Loggers Entregues | 7.695 | 7.695 | 0 | OK |
| Loggers Retornados | 5.536 | 5.536 | 0 | OK |
| Loggers Pendentes | 2.159 | 2.159 | 0 | OK |
| Taxa de Retorno | 71,9% | 71,9% | +0,0 p,p, | OK |
| Taxa de Pendencia | 28,1% | 28,1% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.097
- Loggers Entregues: 7.695
- Loggers Retornados: 5.536
- Loggers Pendentes: 2.159
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
