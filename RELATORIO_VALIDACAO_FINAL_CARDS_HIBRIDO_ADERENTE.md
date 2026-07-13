# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 06:58:44

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
- Fonte original linhas brutas: 539.881
- Fonte original linhas consolidadas: 30.353
- Fonte original deduplicada: 24.292
- Com fonte original atualizada: 23.750
- Sem fonte original atualizada: 3.676
- Cobertura: 86,60%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `7ea60a483071c7461940d71ad292a1502f831f007a72e34c9cae0934cadbcca4`
- Hash fonte original fresca: `56d3afefd8cc20b247447f92d9cdb50617fc1ddfbb06c2bc78039c9fab6c4825`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.426
- Linhas operacionais finais: 23.728
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 537, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3139, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.165 | 1.165 | 0 | OK |
| Loggers Entregues | 7.939 | 7.939 | 0 | OK |
| Loggers Retornados | 5.673 | 5.673 | 0 | OK |
| Loggers Pendentes | 2.266 | 2.266 | 0 | OK |
| Taxa de Retorno | 71,5% | 71,5% | +0,0 p,p, | OK |
| Taxa de Pendencia | 28,5% | 28,5% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.165
- Loggers Entregues: 7.939
- Loggers Retornados: 5.673
- Loggers Pendentes: 2.266
- Taxa de Retorno: 71.5%
- Taxa de Pendencia: 28.5%

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
