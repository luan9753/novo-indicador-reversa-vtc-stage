from __future__ import annotations

import json
import os
import re
from datetime import datetime
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


BASE_DIR = Path(__file__).resolve().parent
SNAPSHOT_DIR = BASE_DIR / "snapshot_reversa_vtc_stage"
HTML_FILE = BASE_DIR / "REVERSA_DATALOGGERS_VTC_STAGE.html"
REPORT_ROOT = BASE_DIR / "RELATORIO_VALIDACAO_REVERSA_VTC_STAGE.md"
REPORT_SNAPSHOT = SNAPSHOT_DIR / "relatorio_validacao_vtc_stage.md"
CUTOVER_DATE = "2026-06-18"


def load_env() -> None:
    for path in [BASE_DIR / ".env", BASE_DIR / "Banco_Aura" / ".env"]:
        if not path.exists():
            continue
        for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            if line.lower().startswith("export "):
                line = line[7:].strip()
            key, value = line.split("=", 1)
            key = key.strip()
            if not key or key in os.environ:
                continue
            value = value.strip().strip('"').strip("'")
            os.environ[key] = value


def connection_prefix() -> str:
    if os.getenv("VTC_STAGE_HOST"):
        return "VTC_STAGE"
    if os.getenv("AURA_DB_HOST"):
        return "AURA_DB"
    return "AURA_POSTGRES"


def engine():
    load_env()
    prefix = connection_prefix()
    url = URL.create(
        "postgresql+psycopg2",
        username=os.getenv(f"{prefix}_USER", "bi_qualidade"),
        password=os.getenv(f"{prefix}_PASSWORD", ""),
        host=os.getenv(f"{prefix}_HOST", "10.141.0.32"),
        port=int(os.getenv(f"{prefix}_PORT", "5432")),
        database=os.getenv(f"{prefix}_NAME", os.getenv(f"{prefix}_DATABASE", "dtbPortal")),
    )
    return create_engine(url, pool_pre_ping=True)


SQL_TABLES = """
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema = 'vtc_stage'
ORDER BY table_name;
"""

SQL_CANDIDATES = """
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
"""

SQL_DOC_COLUMNS = """
SELECT column_name, data_type, ordinal_position
FROM information_schema.columns
WHERE table_schema = 'vtc_stage'
  AND table_name = 'documentos'
ORDER BY ordinal_position;
"""

SQL_RAW_TOTAL = "SELECT COUNT(*) AS total FROM vtc_stage.documentos;"

SQL_RAW_FILTERED = """
SELECT COUNT(*) AS total
FROM vtc_stage.documentos
WHERE dt_entregaefetiva >= DATE :cutover
  AND cd_lpn IS NOT NULL
  AND TRIM(cd_lpn::text) <> ''
  AND ds_tipo NOT ILIKE '%PALLET%';
"""

SQL_BASE = """
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
"""


def infer_tipo(tag_value) -> str:
    tag = "" if tag_value is None else str(tag_value).strip().upper()
    if not tag:
        return "SEM TAG"
    if tag.startswith("AS"):
        return "ARES COM SONDA"
    if tag.startswith("TA") or tag.startswith("A"):
        return "ARES"
    if tag.startswith("S"):
        return "SYOS"
    if tag.startswith(("V", "B")):
        return "SHIELD"
    if re.match(r"^\d", tag):
        return "SENSOR WEB"
    return "TIPO_NAO_CLASSIFICADO"


def pct(num: int, den: int) -> float:
    return 0.0 if den == 0 else round(num * 100.0 / den, 4)


def nonblank(series: pd.Series) -> pd.Series:
    return series.fillna("").astype(str).str.strip()


def save_csv(df: pd.DataFrame, filename: str) -> None:
    df.to_csv(SNAPSHOT_DIR / filename, index=False, encoding="utf-8-sig")


def validations(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    data = df.copy()
    data["tag_norm"] = nonblank(data["tag"])
    data["romaneio_norm"] = nonblank(data["nr_romaneio"])
    data["tem_tag"] = data["tag_norm"].ne("")
    data["tem_romaneio"] = data["romaneio_norm"].ne("")
    data["tem_embarque"] = data["ultima_coleta_embarque"].notna() | data["ultima_entrega_embarque"].notna()
    data["dia"] = pd.to_datetime(data["ultima_entrega"], errors="coerce").dt.date

    out = {}
    out["volumes_por_dia"] = (
        data.groupby("dia", dropna=False)
        .agg(
            caixas_lpn=("cd_lpn", "count"),
            pedidos_unicos=("nr_pedido", "nunique"),
            caixas_com_romaneio=("tem_romaneio", "sum"),
            romaneios_distintos=("romaneio_norm", lambda s: s[s.ne("")].nunique()),
            caixas_com_embarque=("tem_embarque", "sum"),
        )
        .reset_index()
        .sort_values("dia", ascending=False)
    )
    pedidos_com_rom = data[data["tem_romaneio"]].groupby("dia")["nr_pedido"].nunique()
    pedidos_com_emb = data[data["tem_embarque"]].groupby("dia")["nr_pedido"].nunique()
    out["volumes_por_dia"]["pedidos_com_romaneio"] = out["volumes_por_dia"]["dia"].map(pedidos_com_rom).fillna(0).astype(int)
    out["volumes_por_dia"]["pedidos_com_embarque"] = out["volumes_por_dia"]["dia"].map(pedidos_com_emb).fillna(0).astype(int)

    out["volumes_por_uf"] = data.groupby(data["cd_uf"].fillna("NAO_INFORMADO")).size().reset_index(name="unidades").rename(columns={"cd_uf": "uf"}).sort_values("unidades", ascending=False)
    out["volumes_por_modal"] = data.groupby(data["modal"].fillna("NAO_INFORMADO")).size().reset_index(name="unidades").sort_values("unidades", ascending=False)
    out["volumes_por_tipo"] = data.groupby("tipo_datalogger").size().reset_index(name="unidades").sort_values("unidades", ascending=False)
    out["pedidos_multiplos_romaneios"] = data[data["tem_romaneio"]].groupby("nr_pedido")["romaneio_norm"].nunique().reset_index(name="romaneios_distintos").query("romaneios_distintos > 1").sort_values(["romaneios_distintos", "nr_pedido"], ascending=[False, True])
    out["romaneios_multiplos_pedidos"] = data[data["tem_romaneio"]].groupby("romaneio_norm")["nr_pedido"].nunique().reset_index(name="pedidos_distintos").rename(columns={"romaneio_norm": "nr_romaneio"}).query("pedidos_distintos > 1").sort_values(["pedidos_distintos", "nr_romaneio"], ascending=[False, True])
    out["lpns_multiplas_tags"] = data[data["tem_tag"]].groupby("cd_lpn")["tag_norm"].nunique().reset_index(name="tags_distintas").query("tags_distintas > 1").sort_values(["tags_distintas", "cd_lpn"], ascending=[False, True])
    out["tags_multiplas_lpns"] = data[data["tem_tag"]].groupby("tag_norm")["cd_lpn"].nunique().reset_index(name="lpns_distintas").rename(columns={"tag_norm": "tag"}).query("lpns_distintas > 1").sort_values(["lpns_distintas", "tag"], ascending=[False, True])
    out["sem_romaneio"] = data[~data["tem_romaneio"]].sort_values(["ultima_entrega", "nr_pedido", "cd_lpn"], ascending=[False, True, True])
    out["sem_tag"] = data[~data["tem_tag"]].sort_values(["ultima_entrega", "nr_pedido", "cd_lpn"], ascending=[False, True, True])
    out["tipo_nao_classificado"] = data[data["tipo_datalogger"].eq("TIPO_NAO_CLASSIFICADO")]
    out["romaneios_por_uf"] = data[data["tem_romaneio"]].groupby(data["cd_uf"].fillna("NAO_INFORMADO"))["romaneio_norm"].nunique().reset_index(name="romaneios_distintos").rename(columns={"cd_uf": "uf"}).sort_values("romaneios_distintos", ascending=False)
    out["romaneios_por_modal"] = data[data["tem_romaneio"]].groupby(data["modal"].fillna("NAO_INFORMADO"))["romaneio_norm"].nunique().reset_index(name="romaneios_distintos").sort_values("romaneios_distintos", ascending=False)
    out["lpns_tags_por_romaneio"] = data[data["tem_romaneio"]].groupby("romaneio_norm").agg(lpns=("cd_lpn", "nunique"), tags=("tag_norm", lambda s: s[s.ne("")].nunique())).reset_index().rename(columns={"romaneio_norm": "nr_romaneio"}).sort_values(["lpns", "tags"], ascending=[False, False])
    diff = data[data["ultima_entrega"].notna() & data["ultima_entrega_embarque"].notna()].copy()
    diff["diff_horas_entrega_vs_embarque"] = (pd.to_datetime(diff["ultima_entrega_embarque"]) - pd.to_datetime(diff["ultima_entrega"])).dt.total_seconds() / 3600.0
    out["diferenca_entrega_vs_embarque"] = diff.sort_values("diff_horas_entrega_vs_embarque", ascending=False)
    return out


def md_table(df: pd.DataFrame, limit: int = 20) -> str:
    if df.empty:
        return "_Sem registros._"
    sample = df.head(limit).copy().fillna("")
    headers = [str(c) for c in sample.columns]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for _, row in sample.iterrows():
        values = [str(row[col]).replace("|", "/") for col in sample.columns]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def build_report(raw_total: int, raw_filtered: int, base: pd.DataFrame, tables: pd.DataFrame, candidates: pd.DataFrame, vals: dict[str, pd.DataFrame]) -> str:
    total = len(base)
    com_rom = int((base["status_romaneio"] == "COM_ROMANEIO").sum())
    sem_rom = int((base["status_romaneio"] == "SEM_ROMANEIO").sum())
    sem_tag = int(nonblank(base["tag"]).eq("").sum())
    fonte_retorno = "FONTE_DE_RETORNO_NAO_LOCALIZADA_NA_VTC_STAGE" if candidates.empty else "FONTE_DE_RETORNO_NAO_VALIDADA_NA_VTC_STAGE"
    return f"""# RELATORIO VALIDACAO REVERSA VTC_STAGE

Gerado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}

## Escopo Executado

Indicador novo e isolado em `{BASE_DIR}`.

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

- PostgreSQL configurado por `{connection_prefix()}_*`
- Schema: `vtc_stage`
- Tabela principal: `vtc_stage.documentos`
- Corte: `dt_entregaefetiva >= DATE '{CUTOVER_DATE}'`

## SQLs Executadas

### Tabelas do schema

```sql
{SQL_TABLES.strip()}
```

### Colunas candidatas para retorno/status/historico

```sql
{SQL_CANDIDATES.strip()}
```

### Base deduplicada

```sql
{SQL_BASE.strip()}
```

## Totais

- Total bruto em `vtc_stage.documentos`: {raw_total:,}
- Total bruto no filtro principal: {raw_filtered:,}
- Total deduplicado por `nr_pedido + cd_lpn + tag`: {total:,}
- Pedidos unicos: {base["nr_pedido"].nunique():,}
- LPNs unicas: {base["cd_lpn"].nunique():,}
- Tags unicas preenchidas: {nonblank(base["tag"]).loc[lambda s: s.ne("")].nunique():,}
- Romaneios distintos: {nonblank(base["nr_romaneio"]).loc[lambda s: s.ne("")].nunique():,}
- Com romaneio: {com_rom:,} ({pct(com_rom, total)}%)
- Sem romaneio: {sem_rom:,} ({pct(sem_rom, total)}%)
- Sem tag: {sem_tag:,} ({pct(sem_tag, total)}%)

## Total por Tipo de Dispositivo

{md_table(vals["volumes_por_tipo"], 30)}

## Total por Dia

{md_table(vals["volumes_por_dia"], 30)}

## Total por UF

{md_table(vals["volumes_por_uf"], 30)}

## Total por Modal

{md_table(vals["volumes_por_modal"], 30)}

## Romaneio

Pedidos com multiplos romaneios: {len(vals["pedidos_multiplos_romaneios"]):,}

{md_table(vals["pedidos_multiplos_romaneios"], 20)}

Romaneios com multiplos pedidos: {len(vals["romaneios_multiplos_pedidos"]):,}

{md_table(vals["romaneios_multiplos_pedidos"], 20)}

LPNs por romaneio e tags por romaneio foram salvos em `snapshot_reversa_vtc_stage/lpns_tags_por_romaneio.csv`.

## Inconsistencias

- Unidades sem romaneio: {sem_rom:,}
- Unidades sem tag: {sem_tag:,}
- LPNs com mais de uma tag: {len(vals["lpns_multiplas_tags"]):,}
- Tags repetidas em multiplas LPNs: {len(vals["tags_multiplas_lpns"]):,}
- Tipos nao classificados: {len(vals["tipo_nao_classificado"]):,}

Arquivos CSV de inconsistencias foram salvos na pasta `snapshot_reversa_vtc_stage`.

## Investigacao 50 Caixas vs 20 a 25 Embarques

Arquivo gerado: `snapshot_reversa_vtc_stage/caixas_vs_embarque_por_dia.csv`.

Resumo:

{md_table(vals["volumes_por_dia"], 30)}

Conclusao: `NAO_VALIDADO`. A equivalencia entre "caixas", "pedidos", "romaneios" e "embarques" ainda depende de confirmacao operacional.

## Retorno / Reversa

Situacao: `{fonte_retorno}`.

Colunas candidatas encontradas:

{md_table(candidates[["table_name", "column_name", "data_type"]] if not candidates.empty else candidates, 60)}

Nenhum status `Retornado` foi criado. A base usa:

- `status_retorno = RETORNO_NAO_VALIDADO`
- `fonte_retorno = {fonte_retorno}`

## Limitacoes

- Linha bruta nao foi usada como KPI.
- Registros sem romaneio foram mantidos e auditados.
- Historico anterior a `{CUTOVER_DATE}` nao foi misturado na base principal.
- `updated_at`, `inserted_at`, `imported_at`, `dt_entregaefetiva` e `dt_entregaefetivaembarque` nao foram usados como retorno.
- Tipo de dispositivo foi inferido por padrao da tag, sem lista fixa.

## Confirmacoes Finais

- Nenhum arquivo fora da pasta isolada foi alterado.
- Nada foi publicado.
- Nenhuma rotina antiga foi executada.
- Nenhum BAT herdado foi executado.
"""


def build_html(base: pd.DataFrame, vals: dict[str, pd.DataFrame]) -> str:
    total = len(base)
    com_rom = int((base["status_romaneio"] == "COM_ROMANEIO").sum())
    sem_rom = int((base["status_romaneio"] == "SEM_ROMANEIO").sum())
    sem_tag = int(nonblank(base["tag"]).eq("").sum())
    detail_cols = ["nr_pedido", "nr_romaneio", "cd_lpn", "tag", "tipo_datalogger", "cd_uf", "modal", "ultima_entrega", "ultima_entrega_embarque", "status_romaneio", "status_retorno"]
    payload = {
        "dia": vals["volumes_por_dia"].head(45).astype(str).to_dict("records"),
        "tipo": vals["volumes_por_tipo"].astype(str).to_dict("records"),
        "uf": vals["volumes_por_uf"].head(30).astype(str).to_dict("records"),
        "headers": detail_cols,
        "rows": base.sort_values("ultima_entrega", ascending=False).head(500).reindex(columns=detail_cols).fillna("").astype(str).values.tolist(),
    }
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Reversa Dataloggers VTC_STAGE</title>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
body{{margin:0;background:#0c1118;color:#edf4ff;font-family:Segoe UI,Arial,sans-serif}}header{{padding:28px 32px;border-bottom:1px solid #263447}}main{{padding:22px 32px}}h1{{margin:0 0 8px;font-size:1.65rem}}.sub,.note{{color:#9db0c6}}.note{{background:#261c10;border:1px solid #72521f;color:#ffdca8;border-radius:8px;padding:12px 14px;margin-bottom:16px}}.kpis{{display:grid;grid-template-columns:repeat(4,minmax(160px,1fr));gap:12px;margin-bottom:18px}}.kpi,section{{background:#151d28;border:1px solid #263447;border-radius:8px;padding:14px}}.label{{color:#9db0c6;font-size:.78rem;text-transform:uppercase;font-weight:700}}.value{{margin-top:8px;font-size:1.55rem;font-weight:750}}.grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}.chart{{height:330px}}table{{width:100%;border-collapse:collapse;font-size:.82rem}}th,td{{border-bottom:1px solid #263447;padding:8px 10px;white-space:nowrap;text-align:left}}th{{background:#111925;color:#c8d7ea;position:sticky;top:0}}.table-wrap{{overflow:auto;max-height:480px}}@media(max-width:980px){{.kpis,.grid{{grid-template-columns:1fr}}main,header{{padding-left:16px;padding-right:16px}}}}
</style>
</head>
<body>
<header><h1>Reversa Dataloggers VTC_STAGE</h1><div class="sub">Indicador novo e isolado. Fonte: vtc_stage.documentos. Corte: {CUTOVER_DATE}. Gerado em {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}.</div></header>
<main>
<div class="note">Retorno ainda nao validado. Esta versao mede LPN, romaneio, embarque e qualidade da base; nao afirma "Retornado".</div>
<div class="kpis"><div class="kpi"><div class="label">Unidades</div><div class="value">{total:,}</div></div><div class="kpi"><div class="label">Com romaneio</div><div class="value" style="color:#4ecb71">{com_rom:,}</div></div><div class="kpi"><div class="label">Sem romaneio</div><div class="value" style="color:#f0a04b">{sem_rom:,}</div></div><div class="kpi"><div class="label">Sem tag</div><div class="value" style="color:#e06060">{sem_tag:,}</div></div></div>
<div class="grid"><section><h2>Caixas/LPNs por dia</h2><div id="dia" class="chart"></div></section><section><h2>Tipo de dispositivo</h2><div id="tipo" class="chart"></div></section><section><h2>Volumes por UF</h2><div id="uf" class="chart"></div></section><section><h2>Detalhe recente</h2><div class="table-wrap"><table id="tbl"></table></div></section></div>
</main>
<script>
const DATA = {json.dumps(payload, ensure_ascii=False)};
const cfg = {{displayModeBar:false,responsive:true}};
const layout = {{paper_bgcolor:'rgba(0,0,0,0)',plot_bgcolor:'rgba(0,0,0,0)',font:{{color:'#dceafe'}},margin:{{l:50,r:20,t:10,b:60}},xaxis:{{gridcolor:'#263447'}},yaxis:{{gridcolor:'#263447'}}}};
Plotly.newPlot('dia',[{{type:'bar',x:DATA.dia.map(r=>r.dia).reverse(),y:DATA.dia.map(r=>Number(r.caixas_lpn)).reverse(),marker:{{color:'#3a8fd9'}}}}],layout,cfg);
Plotly.newPlot('tipo',[{{type:'bar',x:DATA.tipo.map(r=>r.tipo_datalogger),y:DATA.tipo.map(r=>Number(r.unidades)),marker:{{color:'#4ecb71'}}}}],layout,cfg);
Plotly.newPlot('uf',[{{type:'bar',x:DATA.uf.map(r=>r.uf),y:DATA.uf.map(r=>Number(r.unidades)),marker:{{color:'#f0a04b'}}}}],layout,cfg);
const esc=v=>String(v).replace(/[&<>]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;'}}[c]));
document.getElementById('tbl').innerHTML='<thead><tr>'+DATA.headers.map(h=>`<th>${{esc(h)}}</th>`).join('')+'</tr></thead><tbody>'+DATA.rows.map(r=>'<tr>'+r.map(v=>`<td>${{esc(v)}}</td>`).join('')+'</tr>').join('')+'</tbody>';
</script>
</body></html>"""


def main() -> None:
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    params = {"cutover": CUTOVER_DATE}
    with engine().connect() as conn:
        tables = pd.read_sql(text(SQL_TABLES), conn)
        candidates = pd.read_sql(text(SQL_CANDIDATES), conn)
        doc_cols = pd.read_sql(text(SQL_DOC_COLUMNS), conn)
        raw_total = int(conn.execute(text(SQL_RAW_TOTAL)).scalar() or 0)
        raw_filtered = int(conn.execute(text(SQL_RAW_FILTERED), params).scalar() or 0)
        base = pd.read_sql(text(SQL_BASE), conn, params=params)

    base["tag"] = nonblank(base["tag"]).str.upper()
    base["tipo_datalogger"] = base["tag"].map(infer_tipo)
    fonte = "FONTE_DE_RETORNO_NAO_LOCALIZADA_NA_VTC_STAGE" if candidates.empty else "FONTE_DE_RETORNO_NAO_VALIDADA_NA_VTC_STAGE"
    base["status_retorno"] = "RETORNO_NAO_VALIDADO"
    base["fonte_retorno"] = fonte
    base = base.sort_values(["ultima_entrega", "nr_pedido", "cd_lpn"], ascending=[False, True, True])
    vals = validations(base)

    save_csv(tables, "schema_vtc_stage_tabelas.csv")
    save_csv(candidates, "schema_vtc_stage_colunas_candidatas_retorno.csv")
    save_csv(doc_cols, "schema_vtc_stage_documentos_colunas.csv")
    base.to_csv(SNAPSHOT_DIR / "base_vtc_stage_dedup.csv", index=False, encoding="utf-8-sig")
    base.to_pickle(SNAPSHOT_DIR / "base_vtc_stage_dedup.pkl")
    outputs = {
        "volumes_por_dia": "caixas_vs_embarque_por_dia.csv",
        "volumes_por_uf": "volumes_por_uf.csv",
        "volumes_por_modal": "volumes_por_modal.csv",
        "volumes_por_tipo": "volumes_por_tipo_datalogger.csv",
        "pedidos_multiplos_romaneios": "pedidos_multiplos_romaneios.csv",
        "romaneios_multiplos_pedidos": "romaneios_multiplos_pedidos.csv",
        "lpns_multiplas_tags": "lpns_multiplas_tags.csv",
        "tags_multiplas_lpns": "tags_multiplas_lpns.csv",
        "sem_romaneio": "inconsistencias_sem_romaneio.csv",
        "sem_tag": "inconsistencias_sem_tag.csv",
        "tipo_nao_classificado": "inconsistencias_tipo_nao_classificado.csv",
        "romaneios_por_uf": "romaneios_por_uf.csv",
        "romaneios_por_modal": "romaneios_por_modal.csv",
        "lpns_tags_por_romaneio": "lpns_tags_por_romaneio.csv",
        "diferenca_entrega_vs_embarque": "diferenca_entrega_vs_embarque.csv",
    }
    for key, filename in outputs.items():
        save_csv(vals[key], filename)

    report = build_report(raw_total, raw_filtered, base, tables, candidates, vals)
    REPORT_ROOT.write_text(report, encoding="utf-8")
    REPORT_SNAPSHOT.write_text(report, encoding="utf-8")
    if not base.empty:
        HTML_FILE.write_text(build_html(base, vals), encoding="utf-8")

    print(f"[vtc_stage] tabelas_schema={len(tables)}")
    print(f"[vtc_stage] candidatas_retorno={len(candidates)}")
    print(f"[vtc_stage] bruto_total={raw_total}")
    print(f"[vtc_stage] bruto_filtrado={raw_filtered}")
    print(f"[vtc_stage] deduplicado={len(base)}")
    print(f"[vtc_stage] snapshot={SNAPSHOT_DIR}")
    print(f"[vtc_stage] relatorio={REPORT_ROOT}")
    print(f"[vtc_stage] html={HTML_FILE}")


if __name__ == "__main__":
    main()
