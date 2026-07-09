from __future__ import annotations
from datetime import datetime, timedelta
from pathlib import Path
import hashlib, importlib.util, json, re, unicodedata
import pandas as pd
from sqlalchemy import text, create_engine

BASE=Path(__file__).resolve().parent
OUT_HTML=BASE/'REVERSA_DATALOGGERS_STAGE.html'
OUT_HTML_TMP=BASE/'REVERSA_DATALOGGERS_STAGE.tmp.html'
OUT_MANIFEST=BASE/'MANIFESTO_SNAPSHOT_HIBRIDO_ADERENTE.json'
OUT_REPORT=BASE/'RELATORIO_VALIDACAO_FINAL_CARDS_HIBRIDO_ADERENTE.md'
OUT_FAIL_CLOSED_REPORT=BASE/'RELATORIO_FAIL_CLOSED_REVERSA_STAGE.md'
LOOKBACK_DAYS=90
STAGE_HEADERS=['Pedido','LPN','Logger','Romaneio','Tipo Datalogger','Data de Entrega','Ultimo Historico','Agente','Status Retorno','UF','UF Destino','Cidade Destino','Destinatario']
EXPECTED_30={'Pedidos Entregues':1281,'Loggers Entregues':9851,'Loggers Retornados':6127,'Loggers Pendentes':2363,'Taxa de Retorno':72.2,'Taxa de Pendencia':27.8}
ALLOWED_STATUS={'Retornado','Pendente de Retorno'}
FORBIDDEN_HTML_TERMS=['Sem fonte original','SEM AGENTE','Motorista','REGISTRO_SEM_LOGGER_TAG','REGISTRO_SEM_TIPO_VALIDO','TIPO_NAO_CLASSIFICADO']

def mod(rel,name):
    p=BASE/rel; spec=importlib.util.spec_from_file_location(name,p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
vtcmod=mod('gerar_snapshot_reversa_vtc_stage.py','vtcmod')
legq=mod('streamlit/gerar_snapshot_reversa.py','legq')
legmodel=mod('streamlit/gerar_modelo_final_reversa.py','legmodel')
htmlgen=mod('gerar_html_reversa_vtc_stage_hibrido_aderente_original.py','htmlgen')

def norm_text(v):
    if pd.isna(v): return ''
    s=str(v).strip(); s=''.join(ch for ch in unicodedata.normalize('NFD',s) if unicodedata.category(ch)!='Mn')
    return s.upper().strip()
def norm_tag(v):
    s=re.sub(r'\s+','',norm_text(v)); return s[:-2] if re.fullmatch(r'\d+\.0',s) else s
def sha_df(df):
    cols=sorted(df.columns); t=df[cols].copy().astype(str).sort_values(cols,kind='mergesort')
    return hashlib.sha256(t.to_csv(index=False).encode('utf-8')).hexdigest()
def fmt_int(n): return f'{int(n):,}'.replace(',','.')
def fmt_pct(v,dec=2): return f'{float(v):.{dec}f}%'.replace('.',',')
def md_table(headers,rows):
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows: out.append('| '+' | '.join(str(r.get(h,'')) for h in headers)+' |')
    return '\n'.join(out)

def logger_pattern(v):
    s=norm_tag(v)
    if not s:
        return 'VAZIO'
    if re.fullmatch(r'A\d+',s):
        return 'A_NUMEROS'
    if re.fullmatch(r'TA\d+',s):
        return 'TA_NUMEROS'
    if re.fullmatch(r'S\d+',s):
        return 'S_NUMEROS'
    if re.fullmatch(r'\d+',s):
        return 'NUMERICO_SENSORWEB'
    return 'OUTRO_FORMATO'

def classify_tipo(tipo, logger):
    current=str(tipo or '').strip()
    if current and current not in {'NAO_CLASSIFICADO','TIPO_NAO_CLASSIFICADO'}:
        return current, 'MANTIDO_TIPO_VALIDO'
    pattern=logger_pattern(logger)
    if pattern in {'A_NUMEROS','TA_NUMEROS'}:
        return 'ARES', 'CLASSIFICADO_ARES_REGRA_CONFIRMADA'
    if pattern=='NUMERICO_SENSORWEB':
        return 'SENSOR WEB', 'CLASSIFICADO_SENSOR_WEB_REGRA_CONFIRMADA'
    return '', f'REMOVIDO_TIPO_NAO_CLASSIFICADO_{pattern}'

def apply_operational_rules(merged):
    op=merged.copy()
    op['pedido_key']=op.get('nr_pedido','').map(norm_text)
    op['tag_key']=op.get('tag','').map(norm_tag)
    tipo_decisions=op.apply(lambda r: classify_tipo(r.get('tipo_datalogger',''),r.get('tag','')),axis=1)
    op['tipo_datalogger_operacional']=[x[0] for x in tipo_decisions]
    op['_decisao_tipo']=[x[1] for x in tipo_decisions]
    op['status_retorno_legado']=op['status_retorno_legado'].fillna('').astype(str).str.strip()
    op['agente_legado']=op['agente_legado'].fillna('').astype(str).str.strip()
    before=len(op)
    removed_counts={}
    mask_key=op['pedido_key'].ne('') & op['tag_key'].ne('')
    removed_counts['REMOVIDO_SEM_PEDIDO_OU_LOGGER_VALIDO']=int((~mask_key).sum())
    op=op[mask_key].copy()
    mask_tipo=op['tipo_datalogger_operacional'].ne('')
    removed_counts.update(op.loc[~mask_tipo,'_decisao_tipo'].value_counts().astype(int).to_dict())
    op=op[mask_tipo].copy()
    mask_status=op['status_retorno_legado'].isin(['Retornado','Pendente de Retorno'])
    removed_counts['REMOVIDO_STATUS_RETORNO_NAO_OPERACIONAL']=int((~mask_status).sum())
    op=op[mask_status].copy()
    op['tipo_datalogger']=op['tipo_datalogger_operacional']
    op['_has_tipo']=op['tipo_datalogger'].ne('').astype(int)
    op['_has_status']=op['status_retorno_legado'].isin(['Retornado','Pendente de Retorno']).astype(int)
    op['_has_agente']=op['agente_legado'].ne('').astype(int)
    op['_hist_sort']=pd.to_datetime(op.get('ultimo_historico_legado',pd.NaT),errors='coerce')
    op['_entrega_sort']=pd.to_datetime(op.get('ultima_entrega',pd.NaT),errors='coerce')
    dup_before=op.duplicated(['pedido_key','tag_key'],keep=False)
    duplicate_keys_before=int(op.loc[dup_before,['pedido_key','tag_key']].drop_duplicates().shape[0])
    duplicate_rows_before=int(dup_before.sum())
    op=op.sort_values(
        ['pedido_key','tag_key','_has_tipo','_has_status','_hist_sort','_entrega_sort','_has_agente','nr_pedido','tag','cd_lpn','nr_romaneio'],
        ascending=[True,True,False,False,False,False,False,True,True,True,True],
        kind='mergesort'
    )
    dedup=op.drop_duplicates(['pedido_key','tag_key'],keep='first').copy()
    removed_counts['REMOVIDO_DUPLICIDADE_DESEMPATE']=int(len(op)-len(dedup))
    dup_after=dedup.duplicated(['pedido_key','tag_key'],keep=False)
    audit={
        'linhas_entrada': int(before),
        'linhas_operacionais_antes_dedup': int(len(op)),
        'linhas_operacionais_finais': int(len(dedup)),
        'duplicidade_chaves_antes_dedup': duplicate_keys_before,
        'duplicidade_linhas_antes_dedup': duplicate_rows_before,
        'duplicidade_chaves_final': int(dedup.loc[dup_after,['pedido_key','tag_key']].drop_duplicates().shape[0]),
        'tipo_decisoes': {k:int(v) for k,v in op['_decisao_tipo'].value_counts().to_dict().items()},
        'remocoes': {k:int(v) for k,v in removed_counts.items() if int(v)!=0},
        'tipo_nao_classificado_final': int((dedup['tipo_datalogger'].astype(str).str.strip()=='TIPO_NAO_CLASSIFICADO').sum()),
        'status_operacionais': sorted(dedup['status_retorno_legado'].dropna().astype(str).str.strip().unique().tolist()),
    }
    return dedup.drop(columns=['_has_tipo','_has_status','_has_agente','_hist_sort','_entrega_sort','tipo_datalogger_operacional'],errors='ignore'), audit

def extract_vtc_fresh():
    raw_sql=text("""
    SELECT COUNT(*) AS total FROM vtc_stage.documentos
    WHERE dt_entregaefetiva >= CURRENT_DATE - (CAST(:lookback_days AS integer) * INTERVAL '1 day')
      AND cd_lpn IS NOT NULL AND TRIM(cd_lpn::text) <> '' AND ds_tipo NOT ILIKE '%PALLET%';
    """)
    sql=text("""
    WITH base AS (
      SELECT nr_pedido::text AS nr_pedido, cd_lpn::text AS cd_lpn,
             COALESCE(NULLIF(TRIM(ds_tag), ''), NULLIF(TRIM(cd_referencia), '')) AS tag,
             NULLIF(TRIM(nr_romaneio::text), '') AS nr_romaneio,
             cd_uf, ds_cliente, ds_tipo, modal, dt_coletaefetiva, dt_entregaefetiva,
             dt_coletaefetivaembarque, dt_entregaefetivaembarque, nr_produto, cd_lote, updated_at
      FROM vtc_stage.documentos
      WHERE dt_entregaefetiva >= CURRENT_DATE - (CAST(:lookback_days AS integer) * INTERVAL '1 day')
        AND cd_lpn IS NOT NULL AND TRIM(cd_lpn::text) <> '' AND ds_tipo NOT ILIKE '%PALLET%'
    ), dedup AS (
      SELECT nr_pedido, cd_lpn, tag, nr_romaneio,
             MAX(cd_uf) AS cd_uf, MAX(ds_cliente) AS ds_cliente, MAX(ds_tipo) AS ds_tipo, MAX(modal) AS modal,
             MIN(dt_coletaefetiva) AS primeira_coleta, MAX(dt_coletaefetiva) AS ultima_coleta,
             MIN(dt_entregaefetiva) AS primeira_entrega, MAX(dt_entregaefetiva) AS ultima_entrega,
             MIN(dt_coletaefetivaembarque) AS primeira_coleta_embarque, MAX(dt_coletaefetivaembarque) AS ultima_coleta_embarque,
             MIN(dt_entregaefetivaembarque) AS primeira_entrega_embarque, MAX(dt_entregaefetivaembarque) AS ultima_entrega_embarque,
             COUNT(*) AS linhas_origem, COUNT(DISTINCT nr_produto) AS produtos_distintos,
             COUNT(DISTINCT cd_lote) AS lotes_distintos, MAX(updated_at) AS atualizado_na_vtc_stage
      FROM base GROUP BY nr_pedido, cd_lpn, tag, nr_romaneio
    )
    SELECT *, CASE WHEN nr_romaneio IS NOT NULL THEN 'COM_ROMANEIO' ELSE 'SEM_ROMANEIO' END AS status_romaneio,
              CASE WHEN ultima_coleta_embarque IS NOT NULL OR ultima_entrega_embarque IS NOT NULL THEN 'COM_EMBARQUE' ELSE 'SEM_EMBARQUE' END AS status_embarque
    FROM dedup;
    """)
    with vtcmod.engine().connect() as conn:
        raw=int(pd.read_sql(raw_sql,conn,params={'lookback_days':LOOKBACK_DAYS})['total'].iloc[0])
        df=pd.read_sql(sql,conn,params={'lookback_days':LOOKBACK_DAYS})
    df['ultima_entrega']=pd.to_datetime(df['ultima_entrega'],errors='coerce',utc=True).dt.tz_convert(None)
    df['tipo_datalogger']=df['tag'].map(vtcmod.infer_tipo)
    df['pedido_key']=df['nr_pedido'].map(norm_text); df['tag_key']=df['tag'].map(norm_tag); df['join_key']=df['pedido_key']+'|'+df['tag_key']
    return raw,df,datetime.now()

def extract_legacy_fresh():
    pg=create_engine(legq._build_postgres_url(legq.POSTGRES_CFG),pool_pre_ping=True)
    bl=legq._read_required(pg,legq.QUERY_BASE_LOGGERS_GERAL,'base_loggers_fresco')
    ba=legq._read_sqlserver_required(legq.QUERY_BASE_AGENTES_GERAL,'base_agentes_fresco')
    bd=legq._read_sqlserver_required(legq.QUERY_BASE_DESTINATARIOS_GERAL,'base_destinatarios_fresco')
    rc=legq._load_recebimento_resumo(pg)
    extracted=datetime.now(); raw=int(len(bl)+len(ba)+len(bd)+len(rc))
    cutoff=pd.Timestamp.now().normalize()-pd.Timedelta(days=730)
    bl['dt_embalagem']=pd.to_datetime(bl['dt_embalagem'],errors='coerce'); bl=bl[bl['dt_embalagem']>=cutoff].copy()
    pedidos=set(legmodel.normalize_key(bl['nr_pedido'])); pedidos.discard('')
    tags=set(legmodel.normalize_key(bl['cd_referencia'])); tags.discard('')
    ba['_pedido_key']=legmodel.normalize_key(ba['PEDIDO']); ba=ba[ba['_pedido_key'].isin(pedidos)].drop(columns=['_pedido_key'])
    ba['DATA_ENTREGA']=pd.to_datetime(ba['DATA_ENTREGA'],errors='coerce'); ba=ba[ba['DATA_ENTREGA'].notna()].copy()
    bd['_pedido_key']=legmodel.normalize_key(bd['PEDIDO']); bd=bd[bd['_pedido_key'].isin(pedidos)].drop(columns=['_pedido_key'])
    rc['dt_historico']=pd.to_datetime(rc['dt_historico'],errors='coerce'); rc['_tag_key']=legmodel.normalize_key(rc['ds_tag'])
    rc=rc[(rc['_tag_key'].isin(tags))&(rc['dt_historico']>=cutoff-pd.Timedelta(days=60))].drop(columns=['_tag_key'])
    model=legmodel.build_model(bl,ba,rc,bd)
    legacy=pd.DataFrame({'pedido_legado':model.get('Pedido',''),'logger_legado':model.get('Logger',''),
        'data_entrega_legado':pd.to_datetime(model.get('Data de Entrega',pd.NaT),errors='coerce'),
        'ultimo_historico_legado':pd.to_datetime(model.get('Ultimo_Historico',pd.NaT),errors='coerce'),
        'agente_legado':model.get('Agente',''),'status_retorno_legado':model.get('Status Retorno',''),
        'uf_destino_legado':model.get('UF Destino',''),'cidade_destino_legado':model.get('Cidade Destino',''),
        'destinatario_legado':model.get('Destinatario','')})
    legacy['pedido_key']=legacy['pedido_legado'].map(norm_text); legacy['logger_key']=legacy['logger_legado'].map(norm_tag)
    legacy=legacy[(legacy['pedido_key']!='')&(legacy['logger_key']!='')].copy(); legacy['join_key']=legacy['pedido_key']+'|'+legacy['logger_key']
    def nu(s):
        v=s.fillna('').astype(str).str.strip(); v=v[v!='']; return v.nunique()
    dup=legacy[legacy.duplicated('join_key',keep=False)]
    if dup.empty: conf_agent=conf_status=0
    else:
        c=dup.groupby('join_key').agg(agentes=('agente_legado',nu),status=('status_retorno_legado',nu)).reset_index()
        conf_agent=int((c['agentes']>1).sum()); conf_status=int((c['status']>1).sum())
    legacy['sort_retorno']=legacy['status_retorno_legado'].fillna('').astype(str).str.strip().eq('Retornado').astype(int)
    dedup=legacy.sort_values(['join_key','sort_retorno','ultimo_historico_legado','data_entrega_legado'],ascending=[True,False,False,False],kind='mergesort').drop_duplicates('join_key',keep='first')
    return raw,len(model),dedup,conf_agent,conf_status,extracted

def rows_from_merged(m):
    empty=pd.Series('',index=m.index,dtype='object')
    has=m['_merge'].eq('both')
    for c in ['agente_legado','status_retorno_legado','uf_destino_legado','cidade_destino_legado','destinatario_legado']:
        m[c]=m[c].fillna('').astype(str).str.strip(); m.loc[~has,c]=''
    m['Status Fonte Original']=has.map({True:'COM_FONTE_ORIGINAL',False:'SEM_FONTE_ORIGINAL'})
    out=pd.DataFrame(index=m.index)
    out['Pedido']=htmlgen.clean(m.get('nr_pedido',empty)); out['LPN']=htmlgen.clean(m.get('cd_lpn',empty)); out['Logger/Tag']=htmlgen.clean(m.get('tag',empty)); out['Romaneio']=htmlgen.clean(m.get('nr_romaneio',empty))
    out['Tipo Datalogger']=htmlgen.clean(m.get('tipo_datalogger',empty),'NAO_CLASSIFICADO').replace('','NAO_CLASSIFICADO'); out['UF VTC_STAGE']=htmlgen.clean(m.get('cd_uf',empty),'NAO_INFORMADO').replace('','NAO_INFORMADO')
    out['Data Entrega VTC_STAGE']=htmlgen.fmt_dt(m.get('ultima_entrega',empty)); out['Data Coleta VTC_STAGE']=htmlgen.fmt_dt(m.get('ultima_coleta',empty)); out['Status Romaneio']=htmlgen.clean(m.get('status_romaneio',empty),'NAO_CLASSIFICADO')
    out['Status Embarque']=htmlgen.clean(m.get('status_embarque',empty),'NAO_CLASSIFICADO'); out['Modal']=htmlgen.clean(m.get('modal',empty),'NAO_INFORMADO').replace('','NAO_INFORMADO'); out['Cliente']=htmlgen.clean(m.get('ds_cliente',empty)); out['Tipo Caixa']=htmlgen.clean(m.get('ds_tipo',empty))
    out['Agente Fonte Original']=htmlgen.clean(m['agente_legado']); out['Status Retorno dtbPortal']=htmlgen.clean(m['status_retorno_legado']); out['Ultimo Historico dtbPortal']=htmlgen.fmt_dt(m.get('ultimo_historico_legado',empty))
    out['UF Destino Fonte Original']=htmlgen.clean(m['uf_destino_legado']); out['Cidade Destino Fonte Original']=htmlgen.clean(m['cidade_destino_legado']); out['Destinatario Fonte Original']=htmlgen.clean(m['destinatario_legado']); out['Status Fonte Original']=htmlgen.clean(m['Status Fonte Original'])
    out['_data_entrega_iso']=htmlgen.iso_dt(m.get('ultima_entrega',empty)); out['_ultimo_historico_legado_iso']=htmlgen.iso_dt(m.get('ultimo_historico_legado',empty)); out['_sort_entrega']=m['ultima_entrega']
    out=out.sort_values(['_sort_entrega','Pedido','LPN','Logger/Tag','Romaneio'],ascending=[False,True,True,True,True])
    rows=out.drop(columns=['_sort_entrega']).fillna('').values.tolist()
    return [[str(c) if c is not None else '' for c in r] for r in rows]

def period_cards(m,days=30):
    today=m['ultima_entrega'].max()
    if pd.isna(today):
        today=datetime.now()
    today=today.replace(hour=23,minute=59,second=59,microsecond=999000)
    cutoff=today.replace(hour=0,minute=0,second=0,microsecond=0)-timedelta(days=days-1)
    r=m[(m['ultima_entrega'].notna())&(m['ultima_entrega']>=cutoff)&(m['ultima_entrega']<=today)].copy()
    pedidos=int(r['nr_pedido'].astype(str).str.strip().replace('',pd.NA).dropna().nunique())
    loggers=int(len(r)); ret=int((r['status_retorno_legado'].fillna('')=='Retornado').sum()); pend=int((r['status_retorno_legado'].fillna('')=='Pendente de Retorno').sum())
    den=ret+pend
    return {'Pedidos Entregues':pedidos,'Loggers Entregues':loggers,'Loggers Retornados':ret,'Loggers Pendentes':pend,'Taxa de Retorno':round(ret/den*100,1) if den else 0,'Taxa de Pendencia':round(pend/den*100,1) if den else 0}

def final_operational_validation(operational,cards,html):
    failures=[]
    op=operational.copy()
    op['pedido_final']=op.get('nr_pedido','').map(norm_text)
    op['logger_final']=op.get('tag','').map(norm_tag)
    dup_global=op.duplicated(['pedido_final','logger_final'],keep=False)
    max_dt=op['ultima_entrega'].max()
    if pd.isna(max_dt):
        start30=end30=pd.NaT
        op30=op.iloc[0:0].copy()
    else:
        end30=max_dt.replace(hour=23,minute=59,second=59,microsecond=999000)
        start30=end30.replace(hour=0,minute=0,second=0,microsecond=0)-timedelta(days=29)
        op30=op[(op['ultima_entrega'].notna())&(op['ultima_entrega']>=start30)&(op['ultima_entrega']<=end30)].copy()
    dup_30=op30.duplicated(['pedido_final','logger_final'],keep=False)
    tipo_nao=int((op.get('tipo_datalogger','').fillna('').astype(str).str.strip()=='TIPO_NAO_CLASSIFICADO').sum())
    logger_vazio=int(op['logger_final'].eq('').sum())
    pedido_vazio=int(op['pedido_final'].eq('').sum())
    status_series=op.get('status_retorno_legado','').fillna('').astype(str).str.strip()
    invalid_status=sorted([s for s in status_series.unique().tolist() if s not in ALLOWED_STATUS])
    invalid_status_count=int((~status_series.isin(ALLOWED_STATUS)).sum())
    lpn_preserved='LPN' in STAGE_HEADERS and op.get('cd_lpn',pd.Series('',index=op.index)).fillna('').astype(str).str.strip().ne('').any()
    table_lpn_hidden=not bool(re.search(r'<th>\s*LPN\s*</th>',html,re.I))
    export_lpn_hidden=("filter(i=>i!==IDX['LPN'])" in html and 'DETAIL_HEADERS=DETAIL_VISIBLE_INDICES.map' in html and 'detailExportMatrix' in html)
    forbidden_found=[term for term in FORBIDDEN_HTML_TERMS if term in html]
    card_inconsistent=cards['Loggers Entregues'] != cards['Loggers Retornados'] + cards['Loggers Pendentes']
    checks={
        'duplicidade_global_pedido_logger': int(op.loc[dup_global,['pedido_final','logger_final']].drop_duplicates().shape[0]),
        'duplicidade_30d_pedido_logger': int(op30.loc[dup_30,['pedido_final','logger_final']].drop_duplicates().shape[0]),
        'tipo_nao_classificado': tipo_nao,
        'logger_vazio': logger_vazio,
        'pedido_vazio': pedido_vazio,
        'status_invalidos_count': invalid_status_count,
        'status_invalidos': invalid_status,
        'status_operacionais': sorted(status_series.unique().tolist()),
        'lpn_preservado_internamente': bool(lpn_preserved),
        'lpn_oculto_tabela': bool(table_lpn_hidden),
        'lpn_oculto_exportacoes': bool(export_lpn_hidden),
        'termos_proibidos': forbidden_found,
        'cards_coerentes': not card_inconsistent,
        'periodo_30d_inicio': start30.isoformat() if pd.notna(start30) else '',
        'periodo_30d_fim': end30.isoformat() if pd.notna(end30) else '',
    }
    if checks['duplicidade_global_pedido_logger']>0: failures.append('duplicidade final Pedido + Logger > 0')
    if checks['duplicidade_30d_pedido_logger']>0: failures.append('duplicidade 30d Pedido + Logger > 0')
    if tipo_nao>0: failures.append('TIPO_NAO_CLASSIFICADO > 0')
    if logger_vazio>0: failures.append('logger vazio > 0')
    if pedido_vazio>0: failures.append('pedido vazio > 0')
    if invalid_status_count>0: failures.append('status invalido > 0')
    if not lpn_preserved: failures.append('LPN nao preservado internamente')
    if not table_lpn_hidden: failures.append('LPN aparece na tabela')
    if not export_lpn_hidden: failures.append('LPN pode aparecer nas exportacoes')
    if forbidden_found: failures.append('termos proibidos no HTML final: '+', '.join(forbidden_found))
    if card_inconsistent: failures.append('cards incoerentes: Loggers Entregues != Retornados + Pendentes')
    return checks,failures

def write_manifest(now,vtc_raw,vtc,vtc_at,vtc_hash,legacy_raw,legacy_consolidated,legacy,conf_agent,conf_status,legacy_at,legacy_hash,match,sem,cov,op_match,op_sem,op_cov,oper_audit,card_rows,status,block_reasons=None,validation_checks=None):
    min_dt=vtc['ultima_entrega'].min(); max_dt=vtc['ultima_entrega'].max()
    manifest={'gerado_em':now.isoformat(timespec='seconds'),'base_principal':{'fonte':'VTC_STAGE','schema':'vtc_stage','tabela':'documentos','campos_autorizados':['Pedido','LPN','Logger/Tag','Romaneio'],'linhas_brutas':vtc_raw,'linhas':int(len(vtc)),'periodo_min':min_dt.isoformat() if pd.notna(min_dt) else '','periodo_max':max_dt.isoformat() if pd.notna(max_dt) else '','extraido_em':vtc_at.isoformat(timespec='seconds'),'hash':vtc_hash},'complemento_controlado':{'fontes':['dtbPortal','dtbTransporte'],'campos_autorizados':['Agente','Status Retorno','Ultimo Historico','UF Destino','Cidade Destino','Destinatario'],'linhas_brutas':legacy_raw,'linhas_consolidadas':legacy_consolidated,'linhas_deduplicadas':int(len(legacy)),'conflitos_agente':conf_agent,'conflitos_status_retorno':conf_status,'extraido_em':legacy_at.isoformat(timespec='seconds'),'hash':legacy_hash},'join':{'tipo':'left join a partir da VTC_STAGE','chave':'Pedido + Logger/Tag','match_bruto':match,'sem_match_bruto':sem,'cobertura_bruta':fmt_pct(cov),'match_operacional':op_match,'sem_match_operacional':op_sem,'cobertura_operacional':fmt_pct(op_cov),'multiplicou_linhas':False},'camada_operacional':oper_audit,'validacao_cards':{'periodo':'30 dias','status':status,'cards':card_rows},'fail_closed':{'status':status,'motivos_bloqueio':block_reasons or [],'checks':validation_checks or {}}}
    OUT_MANIFEST.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    return manifest

def fail_closed_report(now,status,cards,checks,failures,html_replaced):
    return f'''# Relatorio Fail-Closed Reversa Stage

Data/hora: {now.strftime('%d/%m/%Y %H:%M:%S')}

## Resultado

- Status: `{status}`
- O gerador agora e fail-closed: {'SIM' if status=='VALIDADO_COM_FONTES_FRESCAS' and not failures else 'BLOQUEADO'}
- HTML oficial substituido somente apos validacao completa: {'SIM' if html_replaced else 'NAO'}
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

- Duplicidade global Pedido + Logger: {checks.get('duplicidade_global_pedido_logger','')}
- Duplicidade 30d Pedido + Logger: {checks.get('duplicidade_30d_pedido_logger','')}
- TIPO_NAO_CLASSIFICADO: {checks.get('tipo_nao_classificado','')}
- Logger vazio: {checks.get('logger_vazio','')}
- Pedido vazio: {checks.get('pedido_vazio','')}
- Status invalidos: {checks.get('status_invalidos_count','')} / {checks.get('status_invalidos',[])}
- Status finais: {checks.get('status_operacionais',[])}
- LPN preservado internamente: {checks.get('lpn_preservado_internamente','')}
- LPN oculto da tabela: {checks.get('lpn_oculto_tabela','')}
- LPN oculto das exportacoes: {checks.get('lpn_oculto_exportacoes','')}
- Termos proibidos encontrados: {checks.get('termos_proibidos',[])}
- Cards coerentes: {checks.get('cards_coerentes','')}

## Cards finais 30 dias

- Pedidos Entregues: {fmt_int(cards.get('Pedidos Entregues',0))}
- Loggers Entregues: {fmt_int(cards.get('Loggers Entregues',0))}
- Loggers Retornados: {fmt_int(cards.get('Loggers Retornados',0))}
- Loggers Pendentes: {fmt_int(cards.get('Loggers Pendentes',0))}
- Taxa de Retorno: {cards.get('Taxa de Retorno',0):.1f}%
- Taxa de Pendencia: {cards.get('Taxa de Pendencia',0):.1f}%

## Motivos de bloqueio

{chr(10).join('- '+f for f in failures) if failures else '- Nenhum. Snapshot atual passou.'}

## Risco restante

O processo depende da disponibilidade das fontes frescas VTC_STAGE, dtbPortal e dtbTransporte. Se qualquer fonte falhar ou se qualquer trava operacional falhar, o gerador levanta erro e preserva o HTML oficial anterior.
'''

def rows_to_stage(rows):
    idx={h:i for i,h in enumerate(htmlgen.TABLE_HEADERS)}
    iso_entrega=len(htmlgen.TABLE_HEADERS)
    iso_hist=iso_entrega+1
    mapped=[]
    for r in rows:
        mapped.append([
            r[idx['Pedido']],
            r[idx['LPN']],
            r[idx['Logger/Tag']],
            r[idx['Romaneio']],
            r[idx['Tipo Datalogger']],
            r[idx['Data Entrega VTC_STAGE']],
            r[idx['Ultimo Historico dtbPortal']],
            r[idx['Agente Fonte Original']],
            r[idx['Status Retorno dtbPortal']],
            r[idx['UF VTC_STAGE']],
            r[idx['UF Destino Fonte Original']],
            r[idx['Cidade Destino Fonte Original']],
            r[idx['Destinatario Fonte Original']],
            r[iso_entrega],
            r[iso_hist],
        ])
    return mapped

def render_stage_from_template(rows, now, vtc_at, historico_at=None):
    if not OUT_HTML.exists():
        raise FileNotFoundError('REVERSA_DATALOGGERS_STAGE.html nao encontrado para preservar o template final aprovado')
    html=OUT_HTML.read_text(encoding='utf-8')
    data_script=f'<script>const ALL_ROWS={json.dumps(rows_to_stage(rows),ensure_ascii=False,default=str)};const TABLE_HEADERS={json.dumps(STAGE_HEADERS,ensure_ascii=False)};</script>'
    html,n=re.subn(r'<script>const ALL_ROWS=.*?const TABLE_HEADERS=.*?</script>',data_script,html,count=1,flags=re.S)
    if n!=1:
        raise RuntimeError('BLOQUEADO_TEMPLATE_STAGE_SEM_SCRIPT_DE_DADOS')
    if historico_at is not None and pd.notna(historico_at):
        html=re.sub(r'<strong>Ultima atualizacao do historico:</strong> [^<]+',f'<strong>Ultima atualizacao do historico:</strong> {historico_at.strftime("%d/%m/%Y %H:%M:%S")}',html,count=1)
    html=re.sub(r'<strong>Snapshot atualizado em:</strong> [^<]+',f'<strong>Snapshot atualizado em:</strong> {vtc_at.strftime("%d/%m/%Y %H:%M:%S")}',html,count=1)
    html=re.sub(r'<strong>Ultima atualizacao da tela:</strong> [^<]+',f'<strong>Ultima atualizacao da tela:</strong> {now.strftime("%d/%m/%Y %H:%M:%S")}',html,count=1)
    html=re.sub(r'<footer>Gerado em .*?</footer>',f'<footer>Gerado em {now.strftime("%d/%m/%Y %H:%M:%S")} &middot; VTC LOG - BI Qualidade - OPERACIONAL_CONSISTENTE_COM_278_REINSERIDOS_A7266_AUDITORIA</footer>',html,count=1,flags=re.S)
    return html

def build_outputs():
    now=datetime.now()
    if OUT_HTML_TMP.exists():
        OUT_HTML_TMP.unlink()
    vtc_raw,vtc,vtc_at=extract_vtc_fresh()
    legacy_raw,legacy_consolidated,legacy,conf_agent,conf_status,legacy_at=extract_legacy_fresh()
    vtc_hash=sha_df(vtc.drop(columns=['pedido_key','tag_key','join_key'],errors='ignore'))
    legacy_hash=sha_df(legacy.drop(columns=['pedido_key','logger_key','sort_retorno'],errors='ignore'))
    before=len(vtc)
    merged=vtc.merge(legacy.drop(columns=['pedido_key','logger_key','sort_retorno'],errors='ignore'),how='left',on='join_key',validate='m:1',indicator=True)
    if len(merged)!=before: raise RuntimeError('BLOQUEADO_JOIN_MULTIPLICA_LINHAS')
    has=merged['_merge'].eq('both'); match=int(has.sum()); sem=int((~has).sum()); cov=match/len(merged)*100 if len(merged) else 0
    operational,oper_audit=apply_operational_rules(merged)
    op_has=operational['_merge'].eq('both')
    op_match=int(op_has.sum()); op_sem=int((~op_has).sum()); op_cov=op_match/len(operational)*100 if len(operational) else 0
    returned=int((operational['status_retorno_legado'].fillna('')=='Retornado').sum()); pending=int((operational['status_retorno_legado'].fillna('')=='Pendente de Retorno').sum()); den=returned+pending
    metrics={'total':len(operational),'matched':op_match,'no_match':op_sem,'coverage':op_cov,'returned':returned,'pending':pending,'taxa_ret':returned/den*100 if den else 0,'taxa_pend':pending/den*100 if den else 0}
    rows=rows_from_merged(operational.copy())
    tipos=sorted({r[htmlgen.TABLE_HEADERS.index('Tipo Datalogger')] for r in rows if r[htmlgen.TABLE_HEADERS.index('Tipo Datalogger')].strip()})
    ufs=sorted({r[htmlgen.TABLE_HEADERS.index('UF VTC_STAGE')] for r in rows if r[htmlgen.TABLE_HEADERS.index('UF VTC_STAGE')].strip()} | {r[htmlgen.TABLE_HEADERS.index('UF Destino Fonte Original')] for r in rows if r[htmlgen.TABLE_HEADERS.index('UF Destino Fonte Original')].strip()})
    agentes=sorted({r[htmlgen.TABLE_HEADERS.index('Agente Fonte Original')] for r in rows if r[htmlgen.TABLE_HEADERS.index('Agente Fonte Original')].strip()})
    historico_at=pd.to_datetime(operational.get('ultimo_historico_legado',pd.NaT),errors='coerce').max()
    html=render_stage_from_template(rows,now,vtc_at,historico_at)
    cards=period_cards(operational,30)
    card_rows=[]; all_ok=True
    for card in ['Pedidos Entregues','Loggers Entregues','Loggers Retornados','Loggers Pendentes','Taxa de Retorno','Taxa de Pendencia']:
        htmlv=cards[card]; fresh=cards[card]
        if 'Taxa' in card:
            diff=round(fresh-htmlv,1); ok=abs(diff)<=0.05; hv=f'{htmlv:.1f}%'.replace('.',','); fv=f'{fresh:.1f}%'.replace('.',','); df=f'{diff:+.1f} p.p.'.replace('.',',')
        else:
            diff=fresh-htmlv; ok=diff==0; hv=fmt_int(htmlv); fv=fmt_int(fresh); df=fmt_int(diff)
        all_ok=all_ok and ok
        card_rows.append({'Card':card,'Valor HTML regenerado':hv,'Valor fonte fresca':fv,'Diferenca':df,'Status':'OK' if ok else 'DIVERGENTE'})
    validation_checks,failures=final_operational_validation(operational,cards,html)
    if not all_ok:
        failures.append('cards divergentes contra a propria execucao fresca')
    status='VALIDADO_COM_FONTES_FRESCAS' if not failures else 'BLOQUEADO_VALIDACAO_OPERACIONAL'
    if failures:
        manifest=write_manifest(now,vtc_raw,vtc,vtc_at,vtc_hash,legacy_raw,legacy_consolidated,legacy,conf_agent,conf_status,legacy_at,legacy_hash,match,sem,cov,op_match,op_sem,op_cov,oper_audit,card_rows,status,failures,validation_checks)
        OUT_FAIL_CLOSED_REPORT.write_text(fail_closed_report(now,status,cards,validation_checks,failures,False),encoding='utf-8')
        if OUT_HTML_TMP.exists():
            OUT_HTML_TMP.unlink()
        raise RuntimeError('BLOQUEADO_VALIDACAO_OPERACIONAL: '+'; '.join(failures))
    OUT_HTML_TMP.write_text(html,encoding='utf-8')
    OUT_HTML_TMP.replace(OUT_HTML)
    manifest=write_manifest(now,vtc_raw,vtc,vtc_at,vtc_hash,legacy_raw,legacy_consolidated,legacy,conf_agent,conf_status,legacy_at,legacy_hash,match,sem,cov,op_match,op_sem,op_cov,oper_audit,card_rows,status,[],validation_checks)
    OUT_FAIL_CLOSED_REPORT.write_text(fail_closed_report(now,status,cards,validation_checks,[],True),encoding='utf-8')
    report=f'''# Relatorio Validacao Final Cards Hibrido Aderente

Data/hora: {now.strftime('%d/%m/%Y %H:%M:%S')}

## Resultado

Status: `{status}`

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

- VTC_STAGE linhas brutas: {fmt_int(vtc_raw)}
- VTC_STAGE deduplicada: {fmt_int(len(vtc))}
- Fonte original linhas brutas: {fmt_int(legacy_raw)}
- Fonte original linhas consolidadas: {fmt_int(legacy_consolidated)}
- Fonte original deduplicada: {fmt_int(len(legacy))}
- Com fonte original atualizada: {fmt_int(match)}
- Sem fonte original atualizada: {fmt_int(sem)}
- Cobertura: {fmt_pct(cov)}
- Join multiplicou linhas: false
- Hash VTC_STAGE fresco: `{vtc_hash}`
- Hash fonte original fresca: `{legacy_hash}`

## Camada operacional segura

- Linhas de entrada antes da regra operacional: {fmt_int(oper_audit['linhas_entrada'])}
- Linhas operacionais finais: {fmt_int(oper_audit['linhas_operacionais_finais'])}
- Duplicidade Pedido + Logger antes da deduplicacao: {fmt_int(oper_audit['duplicidade_chaves_antes_dedup'])} chaves / {fmt_int(oper_audit['duplicidade_linhas_antes_dedup'])} linhas
- Duplicidade Pedido + Logger final: {fmt_int(oper_audit['duplicidade_chaves_final'])}
- TIPO_NAO_CLASSIFICADO final: {fmt_int(oper_audit['tipo_nao_classificado_final'])}
- Status operacionais finais: {', '.join(oper_audit['status_operacionais'])}
- Remocoes aplicadas: `{json.dumps(oper_audit['remocoes'],ensure_ascii=False)}`

## Validacao dos cards 30 dias

{md_table(['Card','Valor HTML regenerado','Valor fonte fresca','Diferenca','Status'],card_rows)}

## Valores finais 30 dias

- Pedidos Entregues: {fmt_int(cards['Pedidos Entregues'])}
- Loggers Entregues: {fmt_int(cards['Loggers Entregues'])}
- Loggers Retornados: {fmt_int(cards['Loggers Retornados'])}
- Loggers Pendentes: {fmt_int(cards['Loggers Pendentes'])}
- Taxa de Retorno: {cards['Taxa de Retorno']:.1f}%
- Taxa de Pendencia: {cards['Taxa de Pendencia']:.1f}%

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
'''
    OUT_REPORT.write_text(report,encoding='utf-8')
    print('STATUS',status)
    print('HTML',OUT_HTML)
    print('MANIFEST',OUT_MANIFEST)
    print('REPORT',OUT_REPORT)
    print('CARDS30',cards)
    print('GLOBAL',{'vtc':len(vtc),'match':match,'sem':sem,'cov':fmt_pct(cov)})
    return status,cards,manifest

if __name__=='__main__':
    build_outputs()
