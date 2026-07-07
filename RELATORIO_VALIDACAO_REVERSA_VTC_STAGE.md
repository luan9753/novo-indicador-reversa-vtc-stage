# RELATORIO VALIDACAO REVERSA VTC_STAGE

Gerado em: 07/07/2026 13:45:19

## Escopo Executado

Indicador novo e isolado em `C:\Users\Administrador\Documents\NOVO INDICADOR DE REVERSA - VTC_STAGE`.

Nenhum arquivo fora da pasta isolada foi alterado. Nada foi publicado. Nenhum commit, push ou rebase foi feito. Nenhuma rotina antiga foi executada.

## Arquivos Criados

- `gerar_snapshot_reversa_vtc_stage.py`
- `snapshot_reversa_vtc_stage/base_vtc_stage_dedup.csv`
- `snapshot_reversa_vtc_stage/base_vtc_stage_dedup.pkl`
- `snapshot_reversa_vtc_stage/relatorio_validacao_vtc_stage.md`
- `RELATORIO_VALIDACAO_REVERSA_VTC_STAGE.md`
- `REVERSA_DATALOGGERS_VTC_STAGE.html`

## Arquivos Herdados Nao Executados

- `Banco_Aura/ATUALIZAR_REVERSA.bat`
- `Banco_Aura/gerar_html_reversa.py`
- `streamlit/gerar_snapshot_reversa.py`
- `streamlit/gerar_modelo_final_reversa.py`
- `streamlit/dasboard_reversa_loggers.py`
- `snapshot_reversa/`

## Fontes Usadas

- PostgreSQL configurado por `AURA_DB_*`
- Schema: `vtc_stage`
- Tabela principal: `vtc_stage.documentos`
- Corte: `dt_entregaefetiva >= DATE '2026-06-18'`

## SQLs Executadas

### Tabelas do schema

```sql
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema = 'vtc_stage'
ORDER BY table_name;
```

### Colunas candidatas para retorno/status/historico

```sql
SELECT table_schema, table_name, column_name, data_type, ordinal_position
FROM information_schema.columns
WHERE table_schema = 'vtc_stage'
  AND (
    LOWER(table_name) LIKE '%histor%'
    OR LOWER(table_name) LIKE '%retorn%'
    OR LOWER(table_name) LIKE '%revers%'
    OR LOWER(table_name) LIKE '%receb%'
    OR LOWER(table_name) LIKE '%mov%'
    OR LOWER(table_name) LIKE '%logger%'
    OR LOWER(table_name) LIKE '%device%'
    OR LOWER(column_name) LIKE '%histor%'
    OR LOWER(column_name) LIKE '%retorn%'
    OR LOWER(column_name) LIKE '%revers%'
    OR LOWER(column_name) LIKE '%receb%'
    OR LOWER(column_name) LIKE '%status%'
    OR LOWER(column_name) LIKE '%tag%'
    OR LOWER(column_name) LIKE '%logger%'
    OR LOWER(column_name) LIKE '%device%'
  )
ORDER BY table_name, ordinal_position;
```

### Base deduplicada

```sql
WITH base AS (
  SELECT
    nr_pedido::text AS nr_pedido,
    cd_lpn::text AS cd_lpn,
    COALESCE(NULLIF(TRIM(ds_tag), ''), NULLIF(TRIM(cd_referencia), '')) AS tag,
    NULLIF(TRIM(nr_romaneio::text), '') AS nr_romaneio,
    cd_uf,
    ds_cliente,
    ds_tipo,
    modal,
    dt_coletaefetiva,
    dt_entregaefetiva,
    dt_coletaefetivaembarque,
    dt_entregaefetivaembarque,
    nr_produto,
    cd_lote,
    inserted_at,
    updated_at
  FROM vtc_stage.documentos
  WHERE dt_entregaefetiva >= DATE :cutover
    AND cd_lpn IS NOT NULL
    AND TRIM(cd_lpn::text) <> ''
    AND ds_tipo NOT ILIKE '%PALLET%'
),
dedup AS (
  SELECT
    nr_pedido,
    cd_lpn,
    tag,
    MAX(nr_romaneio) AS nr_romaneio,
    MAX(cd_uf) AS cd_uf,
    MAX(ds_cliente) AS ds_cliente,
    MAX(ds_tipo) AS ds_tipo,
    MAX(modal) AS modal,
    MIN(dt_coletaefetiva) AS primeira_coleta,
    MAX(dt_coletaefetiva) AS ultima_coleta,
    MIN(dt_entregaefetiva) AS primeira_entrega,
    MAX(dt_entregaefetiva) AS ultima_entrega,
    MIN(dt_coletaefetivaembarque) AS primeira_coleta_embarque,
    MAX(dt_coletaefetivaembarque) AS ultima_coleta_embarque,
    MIN(dt_entregaefetivaembarque) AS primeira_entrega_embarque,
    MAX(dt_entregaefetivaembarque) AS ultima_entrega_embarque,
    COUNT(*) AS linhas_origem,
    COUNT(DISTINCT nr_produto) AS produtos_distintos,
    COUNT(DISTINCT cd_lote) AS lotes_distintos,
    MAX(updated_at) AS updated_at
  FROM base
  GROUP BY nr_pedido, cd_lpn, tag
)
SELECT
  *,
  CASE WHEN nr_romaneio IS NOT NULL THEN 'COM_ROMANEIO' ELSE 'SEM_ROMANEIO' END AS status_romaneio,
  CASE WHEN ultima_entrega_embarque IS NOT NULL THEN ultima_entrega_embarque ELSE ultima_entrega END AS data_referencia_saida
FROM dedup;
```

## Totais

- Total bruto em `vtc_stage.documentos`: 87,034
- Total bruto no filtro principal: 6,747
- Total deduplicado por `nr_pedido + cd_lpn + tag`: 5,941
- Pedidos unicos: 759
- LPNs unicas: 5,941
- Tags unicas preenchidas: 4,088
- Romaneios distintos: 262
- Com romaneio: 5,928 (99.7812%)
- Sem romaneio: 13 (0.2188%)
- Sem tag: 5 (0.0842%)

## Total por Tipo de Dispositivo

| tipo_datalogger | unidades |
| --- | --- |
| ARES | 5382 |
| SENSOR WEB | 241 |
| SYOS | 202 |
| ARES COM SONDA | 110 |
| SEM TAG | 5 |
| SHIELD | 1 |

## Total por Dia

| dia | caixas_lpn | pedidos_unicos | caixas_com_romaneio | romaneios_distintos | caixas_com_embarque | pedidos_com_romaneio | pedidos_com_embarque |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-07 | 211 | 17 | 211 | 12 | 211 | 17 | 17 |
| 2026-07-06 | 19 | 14 | 19 | 8 | 19 | 14 | 14 |
| 2026-07-05 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2026-07-04 | 30 | 12 | 30 | 6 | 30 | 12 | 12 |
| 2026-07-03 | 538 | 63 | 538 | 33 | 538 | 63 | 63 |
| 2026-07-02 | 214 | 37 | 214 | 20 | 214 | 37 | 37 |
| 2026-07-01 | 387 | 65 | 386 | 25 | 386 | 64 | 64 |
| 2026-06-30 | 398 | 69 | 398 | 26 | 398 | 69 | 69 |
| 2026-06-29 | 129 | 14 | 128 | 10 | 128 | 14 | 14 |
| 2026-06-27 | 10 | 10 | 10 | 3 | 10 | 10 | 10 |
| 2026-06-26 | 316 | 57 | 316 | 31 | 311 | 57 | 57 |
| 2026-06-25 | 824 | 92 | 821 | 51 | 806 | 92 | 92 |
| 2026-06-24 | 657 | 62 | 654 | 39 | 654 | 62 | 62 |
| 2026-06-23 | 417 | 46 | 417 | 26 | 417 | 46 | 46 |
| 2026-06-22 | 504 | 45 | 503 | 26 | 503 | 45 | 45 |
| 2026-06-20 | 14 | 13 | 14 | 4 | 14 | 13 | 13 |
| 2026-06-19 | 831 | 82 | 829 | 41 | 785 | 81 | 76 |
| 2026-06-18 | 441 | 60 | 439 | 33 | 421 | 60 | 60 |

## Total por UF

| uf | unidades |
| --- | --- |
| CE | 621 |
| BA | 609 |
| MG | 516 |
| PE | 418 |
| PR | 373 |
| GO | 334 |
| PA | 298 |
| PB | 270 |
| AM | 255 |
| RS | 242 |
| MA | 197 |
| SC | 195 |
| MS | 185 |
| SP | 174 |
| SE | 167 |
| ES | 149 |
| PI | 145 |
| RN | 137 |
| MT | 116 |
| AL | 96 |
| RO | 95 |
| DF | 94 |
| RJ | 77 |
| AC | 54 |
| RR | 51 |
| AP | 37 |
| TO | 36 |

## Total por Modal

| modal | unidades |
| --- | --- |
| MultiModal | 5023 |
| Rodoviário | 918 |

## Romaneio

Pedidos com multiplos romaneios: 50

| nr_pedido | romaneios_distintos |
| --- | --- |
| 556873 | 6 |
| 555569 | 5 |
| 557268 | 5 |
| 556767 | 4 |
| 557124 | 4 |
| 557254 | 4 |
| 557267 | 4 |
| 557458 | 4 |
| 557787 | 4 |
| 558857 | 4 |
| 556112 | 3 |
| 556790 | 3 |
| 557018 | 3 |
| 557137 | 3 |
| 557965 | 3 |
| 558450 | 3 |
| 556282 | 2 |
| 556714 | 2 |
| 556808 | 2 |
| 556818 | 2 |

Romaneios com multiplos pedidos: 138

| nr_romaneio | pedidos_distintos |
| --- | --- |
| 7191 | 24 |
| 6998 | 20 |
| 7172 | 20 |
| 7227 | 19 |
| 7132 | 18 |
| 7219 | 16 |
| 7063 | 14 |
| 7106 | 14 |
| 7015 | 13 |
| 7292 | 13 |
| 6979 | 12 |
| 6999 | 12 |
| 7017 | 12 |
| 7122 | 11 |
| 7230 | 11 |
| 6988 | 10 |
| 7029 | 10 |
| 7269 | 10 |
| 6974 | 9 |
| 6997 | 9 |

LPNs por romaneio e tags por romaneio foram salvos em `snapshot_reversa_vtc_stage/lpns_tags_por_romaneio.csv`.

## Inconsistencias

- Unidades sem romaneio: 13
- Unidades sem tag: 5
- LPNs com mais de uma tag: 0
- Tags repetidas em multiplas LPNs: 1,570
- Tipos nao classificados: 0

Arquivos CSV de inconsistencias foram salvos na pasta `snapshot_reversa_vtc_stage`.

## Investigacao 50 Caixas vs 20 a 25 Embarques

Arquivo gerado: `snapshot_reversa_vtc_stage/caixas_vs_embarque_por_dia.csv`.

Resumo:

| dia | caixas_lpn | pedidos_unicos | caixas_com_romaneio | romaneios_distintos | caixas_com_embarque | pedidos_com_romaneio | pedidos_com_embarque |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-07 | 211 | 17 | 211 | 12 | 211 | 17 | 17 |
| 2026-07-06 | 19 | 14 | 19 | 8 | 19 | 14 | 14 |
| 2026-07-05 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2026-07-04 | 30 | 12 | 30 | 6 | 30 | 12 | 12 |
| 2026-07-03 | 538 | 63 | 538 | 33 | 538 | 63 | 63 |
| 2026-07-02 | 214 | 37 | 214 | 20 | 214 | 37 | 37 |
| 2026-07-01 | 387 | 65 | 386 | 25 | 386 | 64 | 64 |
| 2026-06-30 | 398 | 69 | 398 | 26 | 398 | 69 | 69 |
| 2026-06-29 | 129 | 14 | 128 | 10 | 128 | 14 | 14 |
| 2026-06-27 | 10 | 10 | 10 | 3 | 10 | 10 | 10 |
| 2026-06-26 | 316 | 57 | 316 | 31 | 311 | 57 | 57 |
| 2026-06-25 | 824 | 92 | 821 | 51 | 806 | 92 | 92 |
| 2026-06-24 | 657 | 62 | 654 | 39 | 654 | 62 | 62 |
| 2026-06-23 | 417 | 46 | 417 | 26 | 417 | 46 | 46 |
| 2026-06-22 | 504 | 45 | 503 | 26 | 503 | 45 | 45 |
| 2026-06-20 | 14 | 13 | 14 | 4 | 14 | 13 | 13 |
| 2026-06-19 | 831 | 82 | 829 | 41 | 785 | 81 | 76 |
| 2026-06-18 | 441 | 60 | 439 | 33 | 421 | 60 | 60 |

Conclusao: `NAO_VALIDADO`. A equivalencia entre "caixas", "pedidos", "romaneios" e "embarques" ainda depende de confirmacao operacional.

## Retorno / Reversa

Situacao: `FONTE_DE_RETORNO_NAO_VALIDADA_NA_VTC_STAGE`.

Colunas candidatas encontradas:

| table_name | column_name | data_type |
| --- | --- | --- |
| _bkp_2logger_docs_20260601 | nr_pedido | text |
| _bkp_2logger_docs_20260601 | ds_cliente | text |
| _bkp_2logger_docs_20260601 | cd_uf | text |
| _bkp_2logger_docs_20260601 | dt_coletaefetiva | timestamp with time zone |
| _bkp_2logger_docs_20260601 | dt_entregaefetiva | timestamp with time zone |
| _bkp_2logger_docs_20260601 | ds_programasaude | text |
| _bkp_2logger_docs_20260601 | ds_tipo | text |
| _bkp_2logger_docs_20260601 | ds_tag | text |
| _bkp_2logger_docs_20260601 | cd_referencia | text |
| _bkp_2logger_docs_20260601 | nr_produto | numeric |
| _bkp_2logger_docs_20260601 | cd_produtocliente | text |
| _bkp_2logger_docs_20260601 | ds_temperaturaproduto | text |
| _bkp_2logger_docs_20260601 | ds_descricaocliente | text |
| _bkp_2logger_docs_20260601 | cd_lote | text |
| _bkp_2logger_docs_20260601 | cd_ean | text |
| _bkp_2logger_docs_20260601 | modal | text |
| _bkp_2logger_docs_20260601 | nr_romaneio | bigint |
| _bkp_2logger_docs_20260601 | imported_at | timestamp with time zone |
| _bkp_2logger_docs_20260601 | imported_into_id | uuid |
| _bkp_2logger_docs_20260601 | inserted_at | timestamp with time zone |
| _bkp_2logger_docs_20260601 | inserted_by | text |
| _bkp_2logger_docs_20260601 | updated_at | timestamp with time zone |
| _bkp_2logger_docs_20260601 | updated_by | text |
| _bkp_2logger_docs_20260601 | cd_lpn | text |
| _bkp_2logger_docs_20260601 | dt_coletaefetivaembarque | timestamp with time zone |
| _bkp_2logger_docs_20260601 | dt_entregaefetivaembarque | timestamp with time zone |
| _bkp_2logger_docs_20260601 | id_integracacaocoleta | integer |
| _bkp_2logger_syncitemlots_20260601 | id | uuid |
| _bkp_2logger_syncitemlots_20260601 | vtc_sync_item_id | uuid |
| _bkp_2logger_syncitemlots_20260601 | ean | text |
| _bkp_2logger_syncitemlots_20260601 | lot_number | text |
| _bkp_2logger_syncitemlots_20260601 | client_product_code | text |
| _bkp_2logger_syncitemlots_20260601 | product_description | text |
| _bkp_2logger_syncitemlots_20260601 | vtc_product_id | numeric |
| _bkp_2logger_syncitemlots_20260601 | metadata | jsonb |
| _bkp_2logger_syncitems_20260601 | id | uuid |
| _bkp_2logger_syncitems_20260601 | vtc_sync_order_id | uuid |
| _bkp_2logger_syncitems_20260601 | device_serial | text |
| _bkp_2logger_syncitems_20260601 | packaging_type | text |
| _bkp_2logger_syncitems_20260601 | expected_temp_raw | text |
| _bkp_2logger_syncitems_20260601 | expected_temp_min | numeric |
| _bkp_2logger_syncitems_20260601 | expected_temp_max | numeric |
| _bkp_2logger_syncitems_20260601 | thermal_category | USER-DEFINED |
| _bkp_2logger_syncitems_20260601 | stage_inserted_at | timestamp with time zone |
| _bkp_2logger_syncitems_20260601 | stage_updated_at | timestamp with time zone |
| _bkp_2logger_syncitems_20260601 | stage_inserted_by | text |
| _bkp_2logger_syncitems_20260601 | stage_updated_by | text |
| _bkp_2logger_syncitems_20260601 | ingested_at | timestamp with time zone |
| _bkp_2logger_syncitems_20260601 | last_synced_at | timestamp with time zone |
| _bkp_2logger_syncitems_20260601 | canonical_status | text |
| _bkp_2logger_syncitems_20260601 | metadata | jsonb |
| _bkp_2logger_syncitems_20260601 | points_count | integer |
| _bkp_2logger_syncitems_20260601 | min_temperature | numeric |
| _bkp_2logger_syncitems_20260601 | max_temperature | numeric |
| _bkp_2logger_syncitems_20260601 | in_range_count | integer |
| _bkp_2logger_syncitems_20260601 | out_of_range_count | integer |
| _bkp_2logger_syncitems_20260601 | sync_source | character varying |
| _bkp_2logger_syncitems_20260601 | road_manifest_number | bigint |
| _bkp_2logger_syncitems_20260601 | collection_date_embarque | timestamp with time zone |
| _bkp_2logger_syncitems_20260601 | delivery_date_embarque | timestamp with time zone |

Nenhum status `Retornado` foi criado. A base usa:

- `status_retorno = RETORNO_NAO_VALIDADO`
- `fonte_retorno = FONTE_DE_RETORNO_NAO_VALIDADA_NA_VTC_STAGE`

## Limitacoes

- Linha bruta nao foi usada como KPI.
- Registros sem romaneio foram mantidos e auditados.
- Historico anterior a `2026-06-18` nao foi misturado na base principal.
- `updated_at`, `inserted_at`, `imported_at`, `dt_entregaefetiva` e `dt_entregaefetivaembarque` nao foram usados como retorno.
- Tipo de dispositivo foi inferido por padrao da tag, sem lista fixa.

## Confirmacoes Finais

- Nenhum arquivo fora da pasta isolada foi alterado.
- Nada foi publicado.
- Nenhuma rotina antiga foi executada.
- Nenhum BAT herdado foi executado.
