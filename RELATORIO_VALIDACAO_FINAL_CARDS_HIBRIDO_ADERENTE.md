# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 13/07/2026 08:47:58

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

- VTC_STAGE linhas brutas: 32.627
- VTC_STAGE deduplicada: 27.510
- Fonte original linhas brutas: 539.938
- Fonte original linhas consolidadas: 30.473
- Fonte original deduplicada: 24.370
- Com fonte original atualizada: 23.822
- Sem fonte original atualizada: 3.688
- Cobertura: 86,59%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `483ab81345a0727afb5c59aa70528108ca1bcebd953fb08512c0a082925b6b4c`
- Hash fonte original fresca: `1c798de7ba3c54904f157b2dd63e22e08c8d624262637b00e104e5b832c0d88e`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.510
- Linhas operacionais finais: 23.800
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 549, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 3139, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.095 | 1.095 | 0 | OK |
| Loggers Entregues | 7.689 | 7.689 | 0 | OK |
| Loggers Retornados | 5.534 | 5.534 | 0 | OK |
| Loggers Pendentes | 2.155 | 2.155 | 0 | OK |
| Taxa de Retorno | 72,0% | 72,0% | +0,0 p,p, | OK |
| Taxa de Pendencia | 28,0% | 28,0% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.095
- Loggers Entregues: 7.689
- Loggers Retornados: 5.534
- Loggers Pendentes: 2.155
- Taxa de Retorno: 72.0%
- Taxa de Pendencia: 28.0%

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
