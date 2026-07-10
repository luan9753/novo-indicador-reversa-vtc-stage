# Relatorio Fail-Closed Reversa Stage

Data/hora: 10/07/2026 12:39:46

## Resultado

- Status: `VALIDADO_COM_FONTES_FRESCAS`
- O gerador agora e fail-closed: SIM
- HTML oficial substituido somente apos validacao completa: SIM
- Arquivo temporario usado antes da troca atomica: `REVERSA_DATALOGGERS_STAGE.tmp.html`

## Validacoes que bloqueiam a geracao

- Duplicidade final Pedido + Logger > 0
- Duplicidade 30d Pedido + Logger > 0
- TIPO_NAO_CLASSIFICADO > 0
- Logger vazio > 0
- Pedido vazio > 0
- Status diferente de Retornado/Pendente de Retorno > 0
- LPN nao preservado internamente
- LPN visivel na tabela ou exportacoes
- Termos proibidos no HTML final
- Cards incoerentes: Loggers Entregues diferente de Retornados + Pendentes

## Checks da execucao

- Duplicidade global Pedido + Logger: 0
- Duplicidade 30d Pedido + Logger: 0
- TIPO_NAO_CLASSIFICADO: 0
- Logger vazio: 0
- Pedido vazio: 0
- Status invalidos: 0 / []
- Status finais: ['Pendente de Retorno', 'Retornado']
- LPN preservado internamente: True
- LPN oculto da tabela: True
- LPN oculto das exportacoes: True
- Termos proibidos encontrados: []
- Cards coerentes: True

## Cards finais 30 dias

- Pedidos Entregues: 1.149
- Loggers Entregues: 8.176
- Loggers Retornados: 5.720
- Loggers Pendentes: 2.456
- Taxa de Retorno: 70.0%
- Taxa de Pendencia: 30.0%

## Motivos de bloqueio

- Nenhum. Snapshot atual passou.

## Risco restante

O processo depende da disponibilidade das fontes frescas VTC_STAGE, dtbPortal e dtbTransporte. Se qualquer fonte falhar ou se qualquer trava operacional falhar, o gerador levanta erro e preserva o HTML oficial anterior.
