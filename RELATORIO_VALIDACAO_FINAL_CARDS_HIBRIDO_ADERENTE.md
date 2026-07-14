# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 14/07/2026 10:55:07

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

- VTC_STAGE linhas brutas: 32.540
- VTC_STAGE deduplicada: 27.545
- Fonte original linhas brutas: 541.118
- Fonte original linhas consolidadas: 30.515
- Fonte original deduplicada: 24.368
- Com fonte original atualizada: 23.882
- Sem fonte original atualizada: 3.663
- Cobertura: 86,70%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `3b25690dcf5a515eca7bac38ccdad7738efd73e2bdbd773c3e485d4395eadae7`
- Hash fonte original fresca: `bf6314a0bb2dba661ce075e1ead722ec7b4adadc59edcc1bde63e176a69736b7`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.545
- Linhas operacionais finais: 23.860
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 517, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3146, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.123 | 1.123 | 0 | OK |
| Loggers Entregues | 8.013 | 8.013 | 0 | OK |
| Loggers Retornados | 5.808 | 5.808 | 0 | OK |
| Loggers Pendentes | 2.205 | 2.205 | 0 | OK |
| Taxa de Retorno | 72,5% | 72,5% | +0,0 p,p, | OK |
| Taxa de Pendencia | 27,5% | 27,5% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.123
- Loggers Entregues: 8.013
- Loggers Retornados: 5.808
- Loggers Pendentes: 2.205
- Taxa de Retorno: 72.5%
- Taxa de Pendencia: 27.5%

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
