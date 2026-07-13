# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 16:35:42

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

- VTC_STAGE linhas brutas: 32.684
- VTC_STAGE deduplicada: 27.535
- Fonte original linhas brutas: 540.264
- Fonte original linhas consolidadas: 30.727
- Fonte original deduplicada: 24.587
- Com fonte original atualizada: 23.856
- Sem fonte original atualizada: 3.679
- Cobertura: 86,64%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `26f750eb43b6227ed74708d13c70f1ab2246e4400aeabe2c271af205fd742706`
- Hash fonte original fresca: `db2edc35fe1f11632c5e5f5710bec5f97cd3a83519b79377a51964ddef21958e`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.535
- Linhas operacionais finais: 23.834
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 538, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3141, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.086 | 1.086 | 0 | OK |
| Loggers Entregues | 7.708 | 7.708 | 0 | OK |
| Loggers Retornados | 5.665 | 5.665 | 0 | OK |
| Loggers Pendentes | 2.043 | 2.043 | 0 | OK |
| Taxa de Retorno | 73,5% | 73,5% | +0,0 p,p, | OK |
| Taxa de Pendencia | 26,5% | 26,5% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.086
- Loggers Entregues: 7.708
- Loggers Retornados: 5.665
- Loggers Pendentes: 2.043
- Taxa de Retorno: 73.5%
- Taxa de Pendencia: 26.5%

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
