# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 16:49:37

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

- VTC_STAGE linhas brutas: 32.711
- VTC_STAGE deduplicada: 27.551
- Fonte original linhas brutas: 540.264
- Fonte original linhas consolidadas: 30.754
- Fonte original deduplicada: 24.603
- Com fonte original atualizada: 23.872
- Sem fonte original atualizada: 3.679
- Cobertura: 86,65%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `5b13f289f42ae1cd144dfcd6250f00dd8b906f201cbefe685ed06e65bff9e42b`
- Hash fonte original fresca: `c44a608508de9aa969b71b65b4b913a630132f68a5c0e1fc44b72263ec803650`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.551
- Linhas operacionais finais: 23.850
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 538, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3141, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.087 | 1.087 | 0 | OK |
| Loggers Entregues | 7.724 | 7.724 | 0 | OK |
| Loggers Retornados | 5.754 | 5.754 | 0 | OK |
| Loggers Pendentes | 1.970 | 1.970 | 0 | OK |
| Taxa de Retorno | 74,5% | 74,5% | +0,0 p,p, | OK |
| Taxa de Pendencia | 25,5% | 25,5% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.087
- Loggers Entregues: 7.724
- Loggers Retornados: 5.754
- Loggers Pendentes: 1.970
- Taxa de Retorno: 74.5%
- Taxa de Pendencia: 25.5%

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
