# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: 11/07/2026 12:56:03

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

- VTC_STAGE linhas brutas: 32.613
- VTC_STAGE deduplicada: 27.516
- Fonte original linhas brutas: 539.411
- Fonte original linhas consolidadas: 31.066
- Fonte original deduplicada: 24.788
- Com fonte original atualizada: 24.051
- Sem fonte original atualizada: 3.465
- Cobertura: 87,41%
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `caf21ac473fed8dce36d27cad0b7e823acc88cbbfd177b9d382181e8be477199`
- Hash fonte original fresca: `c7f824b7f770bce259aeb41d08e73f6e65f6417742a840efc84852f5a9761aac`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: 27.516
- Linhas operacionais finais: 24.029
- Duplicidade Pedido + Logger antes da deduplicacao: 22 chaves / 44 linhas
- Duplicidade Pedido + Logger final: 0
- TIPO_NAO_CLASSIFICADO final: 0
- Status operacionais finais: Pendente de Retorno, Retornado
- Remocoes aplicadas: `{"REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO": 583, "REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL": 2882, "REMOVIDO_DUPLICIDADE_DESEMPATE": 22}`

## Validacao dos cards 30 dias

| Card | Valor HTML regenerado | Valor fonte fresca | Diferenca | Status |
| --- | --- | --- | --- | --- |
| Pedidos Entregues | 1.160 | 1.160 | 0 | OK |
| Loggers Entregues | 7.917 | 7.917 | 0 | OK |
| Loggers Retornados | 5.561 | 5.561 | 0 | OK |
| Loggers Pendentes | 2.356 | 2.356 | 0 | OK |
| Taxa de Retorno | 70,2% | 70,2% | +0,0 p,p, | OK |
| Taxa de Pendencia | 29,8% | 29,8% | +0,0 p,p, | OK |

## Valores finais 30 dias

- Pedidos Entregues: 1.160
- Loggers Entregues: 7.917
- Loggers Retornados: 5.561
- Loggers Pendentes: 2.356
- Taxa de Retorno: 70.2%
- Taxa de Pendencia: 29.8%

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
