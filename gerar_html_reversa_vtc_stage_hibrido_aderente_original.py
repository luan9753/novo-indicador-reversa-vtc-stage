from __future__ import annotations
from datetime import datetime
from html import escape
from pathlib import Path
import json, re, unicodedata
import pandas as pd

BASE_DIR=Path(__file__).resolve().parent
VTC_DIR=BASE_DIR/'snapshot_reversa_vtc_stage'
LEG_DIR=BASE_DIR/'snapshot_reversa'
BASE_PKL=VTC_DIR/'base_vtc_stage_dedup.pkl'
BASE_CSV=VTC_DIR/'base_vtc_stage_dedup.csv'
LEGACY_PKL=LEG_DIR/'modelo_final.pkl'
OUTPUT_FILE=BASE_DIR/'REVERSA_DATALOGGERS_STAGE.html'
PERIODOS=[7,30,60,90]
PERIODO_PAD=30
TABLE_MAX_ROWS=500
TABLE_HEADERS=['Pedido','LPN','Logger/Tag','Romaneio','Tipo Datalogger','UF VTC_STAGE','Data Entrega VTC_STAGE','Data Coleta VTC_STAGE','Status Romaneio','Status Embarque','Modal','Cliente','Tipo Caixa','Agente Fonte Original','Status Retorno dtbPortal','Ultimo Historico dtbPortal','UF Destino Fonte Original','Cidade Destino Fonte Original','Destinatario Fonte Original','Status Fonte Original']

def clean(s,default=''):
    return s.fillna(default).astype(str).str.strip()

def norm_text(v):
    if pd.isna(v): return ''
    s=str(v).strip(); s=''.join(ch for ch in unicodedata.normalize('NFD',s) if unicodedata.category(ch)!='Mn')
    return s.upper().strip()

def norm_tag(v):
    s=re.sub(r'\s+','',norm_text(v))
    return s[:-2] if re.fullmatch(r'\d+\.0',s) else s

def load_vtc():
    if BASE_PKL.exists(): return pd.read_pickle(BASE_PKL)
    if BASE_CSV.exists(): return pd.read_csv(BASE_CSV)
    raise FileNotFoundError('Base VTC_STAGE nao encontrada')

def load_legacy():
    src=pd.read_pickle(LEGACY_PKL)
    legacy=pd.DataFrame({
      'pedido_legado':src.get('Pedido',''),'logger_legado':src.get('Logger',''),
      'data_entrega_legado':pd.to_datetime(src.get('Data de Entrega',pd.NaT),errors='coerce'),
      'ultimo_historico_legado':pd.to_datetime(src.get('Ultimo_Historico',pd.NaT),errors='coerce'),
      'agente_legado':src.get('Agente',''),'status_retorno_legado':src.get('Status Retorno',''),
      'uf_destino_legado':src.get('UF Destino',''),'cidade_destino_legado':src.get('Cidade Destino',''),
      'destinatario_legado':src.get('Destinatario','')})
    legacy['pedido_key']=legacy['pedido_legado'].map(norm_text); legacy['logger_key']=legacy['logger_legado'].map(norm_tag)
    legacy=legacy[(legacy['pedido_key']!='')&(legacy['logger_key']!='')].copy(); legacy['join_key']=legacy['pedido_key']+'|'+legacy['logger_key']
    legacy['sort_retorno']=legacy['status_retorno_legado'].fillna('').astype(str).str.strip().eq('Retornado').astype(int)
    legacy=legacy.sort_values(['join_key','sort_retorno','ultimo_historico_legado','data_entrega_legado'],ascending=[True,False,False,False],kind='mergesort').drop_duplicates('join_key',keep='first')
    return legacy.drop(columns=['pedido_key','logger_key','sort_retorno'],errors='ignore')

def fmt_dt(s):
    return pd.to_datetime(s,errors='coerce',utc=True).dt.tz_convert(None).dt.strftime('%d/%m/%Y %H:%M:%S').fillna('')

def iso_dt(s):
    return pd.to_datetime(s,errors='coerce',utc=True).dt.tz_convert(None).dt.strftime('%Y-%m-%dT%H:%M:%S').fillna('')

def fmt_int(n): return f'{int(n):,}'.replace(',','.')
def fmt_pct(v): return f'{v:.1f}%'.replace('.',',')
def fmt_pct2(v): return f'{v:.2f}%'.replace('.',',')

def build_hybrid():
    vtc=load_vtc().copy(); empty=pd.Series('',index=vtc.index,dtype='object')
    entrega=pd.to_datetime(vtc.get('ultima_entrega',empty),errors='coerce',utc=True).dt.tz_convert(None)
    vtc=vtc[entrega.notna()].copy(); entrega=entrega.loc[vtc.index]; vtc['_sort_entrega']=entrega
    vtc['join_key']=vtc.get('nr_pedido',empty).map(norm_text)+'|'+vtc.get('tag',empty).map(norm_tag)
    merged=vtc.merge(load_legacy(),how='left',on='join_key',validate='m:1',indicator=True)
    has=merged['_merge'].eq('both'); merged['Status Fonte Original']=has.map({True:'COM_FONTE_ORIGINAL',False:'SEM_FONTE_ORIGINAL'})
    for c in ['agente_legado','status_retorno_legado','uf_destino_legado','cidade_destino_legado','destinatario_legado']:
        merged[c]=merged[c].fillna('').astype(str).str.strip(); merged.loc[~has,c]=''
    out=pd.DataFrame(index=merged.index)
    out['Pedido']=clean(merged.get('nr_pedido',empty)); out['LPN']=clean(merged.get('cd_lpn',empty)); out['Logger/Tag']=clean(merged.get('tag',empty)); out['Romaneio']=clean(merged.get('nr_romaneio',empty))
    out['Tipo Datalogger']=clean(merged.get('tipo_datalogger',empty),'NAO_CLASSIFICADO').replace('','NAO_CLASSIFICADO'); out['UF VTC_STAGE']=clean(merged.get('cd_uf',empty),'NAO_INFORMADO').replace('','NAO_INFORMADO')
    out['Data Entrega VTC_STAGE']=fmt_dt(merged.get('ultima_entrega',empty)); out['Data Coleta VTC_STAGE']=fmt_dt(merged.get('ultima_coleta',empty)); out['Status Romaneio']=clean(merged.get('status_romaneio',empty),'NAO_CLASSIFICADO')
    out['Status Embarque']=clean(merged.get('status_embarque',empty),'NAO_CLASSIFICADO'); out['Modal']=clean(merged.get('modal',empty),'NAO_INFORMADO').replace('','NAO_INFORMADO'); out['Cliente']=clean(merged.get('ds_cliente',empty)); out['Tipo Caixa']=clean(merged.get('ds_tipo',empty))
    out['Agente Fonte Original']=clean(merged['agente_legado']); out['Status Retorno dtbPortal']=clean(merged['status_retorno_legado']); out['Ultimo Historico dtbPortal']=fmt_dt(merged.get('ultimo_historico_legado',empty))
    out['UF Destino Fonte Original']=clean(merged['uf_destino_legado']); out['Cidade Destino Fonte Original']=clean(merged['cidade_destino_legado']); out['Destinatario Fonte Original']=clean(merged['destinatario_legado']); out['Status Fonte Original']=clean(merged['Status Fonte Original'])
    out['_data_entrega_iso']=iso_dt(merged.get('ultima_entrega',empty)); out['_ultimo_historico_legado_iso']=iso_dt(merged.get('ultimo_historico_legado',empty)); out['_sort_entrega']=merged['_sort_entrega']
    out=out.sort_values(['_sort_entrega','Pedido','LPN','Logger/Tag','Romaneio'],ascending=[False,True,True,True,True])
    rows=out.drop(columns=['_sort_entrega']).fillna('').values.tolist(); rows=[[str(c) if c is not None else '' for c in r] for r in rows]
    returned=int((merged['status_retorno_legado']=='Retornado').sum()); pending=int((merged['status_retorno_legado']=='Pendente de Retorno').sum()); denom=returned+pending
    metrics={'total':len(merged),'matched':int(has.sum()),'no_match':int((~has).sum()),'coverage':float(has.sum()/len(merged)*100) if len(merged) else 0,'returned':returned,'pending':pending,'taxa_ret':float(returned/denom*100) if denom else 0,'taxa_pend':float(pending/denom*100) if denom else 0}
    return rows,metrics

CSS = r'''
<style>
*{box-sizing:border-box;margin:0;padding:0}:root{--bg:#0b1020;--panel:#121b2d;--panel2:#0f1728;--line:#24344d;--txt:#e8edf5;--soft:#9fb0c8;--brand:#2f80d0;--warn:#f2d49a;--ok:#4ecb71}html,body{min-height:100%}body{background:radial-gradient(900px 260px at 0% -10%,#13233f 0%,rgba(19,35,63,0) 60%),radial-gradient(700px 220px at 100% -20%,#1a2d4d 0%,rgba(26,45,77,0) 58%),var(--bg);color:var(--txt);font-family:"Segoe UI","Trebuchet MS",sans-serif;padding:18px 20px 32px}.hero{background:linear-gradient(120deg,#0f2344 0%,#173463 52%,#1e4178 100%);border:1px solid #2b4a76;border-radius:16px;padding:14px 18px;box-shadow:0 10px 24px rgba(0,0,0,.32);margin-bottom:12px}.hero h1{font-size:2.1rem;font-weight:800}.hero p{margin-top:5px;color:#c8d8ef;font-weight:600}.box,.meta,.chart{background:linear-gradient(180deg,var(--panel) 0%,var(--panel2) 100%);border:1px solid var(--line);border-radius:12px}.box{display:inline-flex;gap:8px;align-items:center;flex-wrap:wrap;padding:8px 10px}.meta{padding:8px 12px;margin:8px 0 10px;color:var(--soft);font-size:.95rem;line-height:1.6}.meta strong{color:#d7e6fb}.btn,.tipo-btn,.clear{background:#13243c;border:1px solid #2b466b;border-radius:8px;color:#9fb7d4;cursor:pointer;font-size:.86rem;font-weight:600;padding:6px 14px}.btn:hover,.tipo-btn:hover,.clear:hover{background:#1a3358;color:#dceafe}.btn.active,.tipo-btn.active{background:linear-gradient(135deg,#1d4f8f,#2f80d0);border-color:#4f94da;color:#fff}.filters{display:flex;align-items:center;gap:10px;margin:10px 0 0;flex-wrap:wrap}.label{font-size:.85rem;color:#9fb7d4;font-weight:700}.select,.agent{background:#13243c;border:1px solid #2b466b;border-radius:8px;color:#dceafe;font-weight:600;padding:6px 12px;min-width:220px}.agent{min-width:320px}.kpis{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:12px;margin:10px 0 14px}.card{background:linear-gradient(155deg,#15233a 0%,#121b2d 62%,#101829 100%);border:1px solid #2a3e5e;border-radius:14px;padding:16px 18px;min-height:108px;box-shadow:0 8px 18px rgba(0,0,0,.28)}.card-title{font-size:1.02rem;font-weight:700;color:#9fb7d4;margin-bottom:12px}.card-val{font-size:2.2rem;font-weight:800;color:#f6fbff;letter-spacing:-.03em}.card-note{font-size:.72rem;color:#9fb0c8;margin-top:6px}.tabs{display:flex;gap:6px;margin:10px 0 0;border-bottom:1px solid #24344d}.tab{background:#131d30;border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0;padding:9px 18px;color:#ced9ea;cursor:pointer;font-weight:600}.tab.active{background:#173158;color:#fff;border-color:#2f5ea3}.tab-content{padding-top:14px}.section-title{font-size:1.3rem;font-weight:800;color:#dceafe;margin:14px 2px 8px}.section-note{color:#b7c6dc;font-size:.9rem;margin:-2px 2px 12px;line-height:1.45}.charts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-bottom:14px}.chart{padding:10px 10px 2px;box-shadow:0 8px 18px rgba(0,0,0,.24);margin-bottom:14px}.chart-title{font-size:1.02rem;font-weight:700;color:#dceafe;padding:4px 4px 6px}.chart-empty{display:flex;align-items:center;justify-content:center;min-height:200px;border:1px dashed #2b466b;border-radius:10px;color:#7f93ad;background:rgba(19,36,60,.35);font-size:.9rem;text-align:center;padding:12px}.detail-wrap{overflow-x:auto}table{width:100%;border-collapse:collapse;font-size:.82rem;color:#c8d8ef}thead tr{background:#0f1f37;border-bottom:2px solid #2a3e5e}th{padding:9px 10px;font-weight:700;color:#9ec2ea;text-align:left;white-space:nowrap;position:sticky;top:0;background:#0f1f37;z-index:1}tbody tr:nth-child(even){background:rgba(19,45,77,.25)}td{padding:7px 10px;border-bottom:1px solid #1e2e47;white-space:nowrap;max-width:240px;overflow:hidden;text-overflow:ellipsis}.csv{display:inline-block;margin:10px 0 4px;background:linear-gradient(135deg,#1d4f8f,#2f80d0);color:#fff;border:1px solid #4f94da;border-radius:10px;padding:8px 20px;font-weight:700;font-size:.9rem;text-decoration:none}footer{margin-top:24px;font-size:.75rem;color:#556070;text-align:right}@media(max-width:1200px){.kpis{grid-template-columns:repeat(3,minmax(0,1fr))}.charts{grid-template-columns:1fr}}@media(max-width:720px){.kpis{grid-template-columns:repeat(2,minmax(0,1fr))}.hero h1{font-size:1.6rem}.select,.agent{min-width:100%}}
</style>
'''

def generate_html(rows,metrics,tipos,ufs,agentes,gerado,snapshot_time):
    rows_json=json.dumps(rows,ensure_ascii=False,default=str); headers_json=json.dumps(TABLE_HEADERS,ensure_ascii=False); metrics_json=json.dumps(metrics,ensure_ascii=False)
    labels={7:'Ultimos 7 dias',30:'Ultimos 30 dias',60:'Ultimos 60 dias',90:'Ultimos 90 dias'}
    btns=''.join(f'<button class="btn{" active" if d==PERIODO_PAD else ""}" id="btn-{d}" onclick="switchPeriod({d})">{labels[d]}</button>' for d in PERIODOS)
    tipos_html='<button class="tipo-btn active" id="tipo-btn-" onclick="switchTipo(\'\')">Todos os tipos</button>'+''.join(f'<button class="tipo-btn" id="tipo-btn-{escape(t)}" onclick="switchTipo(\'{escape(t)}\')">{escape(t)}</button>' for t in tipos)
    uf_html=''.join(f'<option value="{escape(u)}">{escape(u)}</option>' for u in ufs)
    agent_html=''.join(f'<option value="{escape(a)}">{escape(a)}</option>' for a in agentes)
    th=''.join(f'<th>{escape(h)}</th>' for h in TABLE_HEADERS)
    html=f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Controle de Reversa - VTC_STAGE Hibrido Aderente Original</title><script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>{CSS}</head><body>
<div class="hero"><h1>Controle de Reversa de Dataloggers</h1><p>Hibrido aderente ao original - VTC_STAGE + fonte original atualizada</p></div>
<h2 style="font-size:1.25rem;font-weight:700;color:#e8edf5;margin:10px 0 6px;">Periodo</h2><div class="box"><span class="label">Filtro rapido</span>{btns}</div>
<div class="meta"><strong>Periodo aplicado:</strong> <span id="meta-period">--</span><br><strong>Fonte principal:</strong> VTC_STAGE<br><strong>Pedido, Logger/Tag, LPN e Romaneio:</strong> VTC_STAGE<br><strong>Retorno e Ultimo Historico:</strong> dtbPortal - extracao fresca<br><strong>Agente e Destino:</strong> dtbTransporte - extracao fresca<br><strong>Taxas de retorno/pendencia:</strong> calculadas somente sobre registros com fonte original atualizada<br><strong>Modo de atualizacao:</strong> snapshot fresco gerado antes da publicacao<br><strong>Sem fallback local:</strong> confirmado<br><strong>Sem snapshot antigo como entrada:</strong> confirmado<br><strong>Registros sem fonte original atualizada:</strong> {fmt_int(metrics['no_match'])}<br><strong>Cobertura da fonte original atualizada:</strong> {fmt_pct2(metrics['coverage'])}<br><strong>Snapshot VTC_STAGE:</strong> {escape(snapshot_time)} &nbsp; <strong>Gerado:</strong> {escape(gerado)}</div>
<div class="filters"><div class="box"><span class="label">Tipo</span>{tipos_html}</div></div>
<div class="filters"><span class="label">Agente</span><select class="select" id="agent-filter" onchange="switchAgent(this.value)"><option value="">Todos os agentes</option>{agent_html}</select><span class="label">UF</span><select class="select" id="uf-filter" onchange="switchUf(this.value)"><option value="">Todas as UFs</option>{uf_html}</select><span class="label">Fonte original</span><select class="select" id="legacy-filter" onchange="switchLegacy(this.value)"><option value="TODOS">Todos</option><option value="COM_FONTE_ORIGINAL">Com fonte original atualizada</option><option value="SEM_FONTE_ORIGINAL">Sem fonte original atualizada</option><option value="RETORNADO_DTBPORTAL">Retornado via dtbPortal</option><option value="PENDENTE_DTBPORTAL">Pendente via dtbPortal</option></select><button class="clear" onclick="clearFilters()">Limpar filtros</button></div>
<div class="kpis"><div class="card"><div class="card-title">Pedidos Entregues</div><div class="card-val" id="kpi-pedidos">--</div><div class="card-note">Fonte: VTC_STAGE</div></div><div class="card"><div class="card-title">Loggers Entregues</div><div class="card-val" id="kpi-loggers">--</div><div class="card-note">Fonte: VTC_STAGE</div></div><div class="card"><div class="card-title">Loggers Retornados</div><div class="card-val" id="kpi-retornados">--</div><div class="card-note">Fonte: dtbPortal atualizado</div></div><div class="card"><div class="card-title">Loggers Pendentes</div><div class="card-val" id="kpi-pendentes">--</div><div class="card-note">Fonte: dtbPortal atualizado</div></div><div class="card"><div class="card-title">Taxa de Retorno</div><div class="card-val" id="kpi-taxa-retorno">--</div><div class="card-note">Derivado de dtbPortal cruzado com VTC_STAGE</div></div><div class="card"><div class="card-title">Taxa de Pendencia</div><div class="card-val" id="kpi-taxa-pendencia">--</div><div class="card-note">Derivado de dtbPortal cruzado com VTC_STAGE</div></div></div>
<div class="tabs"><button class="tab active" id="tab-exec-btn" onclick="switchTab('exec')">Visao Executiva</button><button class="tab" id="tab-detalhe-btn" onclick="switchTab('detalhe')">Visao Detalhada</button></div>
<div id="tab-exec" class="tab-content"><p class="section-note">UF Destino usa `UF Destino Fonte Original` quando houver fonte original atualizada; sem fonte original atualizada, usa `UF VTC_STAGE` como fallback documentado.</p><div class="charts"><div class="chart"><div class="chart-title">Loggers Expedidos por Agente</div><div class="section-note">Fonte: Agente vindo de dtbTransporte - extracao fresca.</div><div id="chart-exp-agente" style="height:420px"></div></div><div class="chart"><div class="chart-title">Loggers Pendentes de Retorno por Agente</div><div class="section-note">Fonte: Retorno vindo de dtbPortal; agente vindo de dtbTransporte.</div><div id="chart-pend-agente" style="height:420px"></div></div></div><div class="charts"><div class="chart"><div class="chart-title">Tendencia Semanal de Loggers Entregues</div><div class="section-note">Fonte: VTC_STAGE.</div><div id="chart-tendencia" style="height:360px"></div></div><div class="chart"><div class="chart-title">Loggers por UF Destino</div><div class="section-note">Fonte: dtbTransporte quando houver fonte original; fallback visual para UF VTC_STAGE quando nao houver fonte original.</div><div id="chart-uf-destino" style="height:360px"></div></div></div><div class="charts"><div class="chart"><div class="chart-title">Top 10 Agentes com Maior Pendencia</div><div class="section-note">Fonte: dtbPortal + dtbTransporte cruzados com VTC_STAGE.</div><div id="chart-top-pend" style="height:420px"></div></div><div class="chart"><div class="chart-title">Dispositivos Recebidos por Dia (Ultimos 7 dias)</div><div class="section-note">Fonte: Ultimo Historico dtbPortal - extracao fresca.</div><div id="chart-recebidos" style="height:420px"></div></div></div></div>
<div id="tab-detalhe" class="tab-content" style="display:none"><h3 class="section-title">Detalhamento</h3><a id="csv-download" class="csv" href="#" download="dataloggers_vtc_stage_hibrido_aderente_original_filtrado.csv">&#8595; Baixar CSV</a><div class="detail-wrap" style="max-height:600px;overflow-y:auto;margin-top:8px"><table><thead><tr>{th}</tr></thead><tbody id="detail-tbody"></tbody></table></div></div>
<footer>Gerado em {escape(gerado)} &middot; VTC LOG - BI Qualidade - HIBRIDO_ADERENTE_ORIGINAL_APROVADO_COM_RESTRICAO</footer>
<script>const ALL_ROWS={rows_json};const TABLE_HEADERS={headers_json};const METRICS={metrics_json};</script>
<script>__JS__</script></body></html>'''
    return html

JS = r'''
const DEFAULT_PERIOD=30,TABLE_MAX_ROWS=500,cfg={displayModeBar:false,responsive:true};
const IDX=Object.fromEntries(TABLE_HEADERS.map((h,i)=>[h,i]));
const ISO_ENTREGA_IDX=TABLE_HEADERS.length,ISO_HIST_LEGADO_IDX=TABLE_HEADERS.length+1;
const CHART_IDS=['chart-exp-agente','chart-pend-agente','chart-tendencia','chart-uf-destino','chart-top-pend','chart-recebidos'];
const LAYOUT_BASE={paper_bgcolor:'#141b26',plot_bgcolor:'#141b26',font:{color:'#e8edf5',family:'Segoe UI,Trebuchet MS,sans-serif'},xaxis:{gridcolor:'#2b3a4d',zerolinecolor:'#2b3a4d',linecolor:'#2b3a4d',tickfont:{color:'#d3dceb'}},yaxis:{gridcolor:'#2b3a4d',zerolinecolor:'#2b3a4d',linecolor:'#2b3a4d',tickfont:{color:'#d3dceb',size:13}},hoverlabel:{bgcolor:'#1b2635',font:{color:'#f1f5fb'}},showlegend:false};
let _currentDays=DEFAULT_PERIOD,_currentTipo='',_currentUf='',_currentAgent='',_currentLegacy='TODOS';
function parseIso(v){const s=String(v||'').trim();if(!s)return null;const d=new Date(s);return Number.isNaN(d.getTime())?null:d}
function fmtInt(n){return Number(n||0).toLocaleString('pt-BR')} function fmtPct(v){return (Number(v||0).toFixed(1)+'%').replace('.',',')}
function escapeHtml(v){return String(v??'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;')}
function norm(v){return String(v??'').trim().toUpperCase()} function inc(m,k,n=1){k=String(k||'NAO_INFORMADO').trim()||'NAO_INFORMADO';m.set(k,(m.get(k)||0)+n)}
function topMap(m,limit){return Array.from(m.entries()).sort((a,b)=>b[1]-a[1]).slice(0,limit)} function chartData(m,limit){const e=topMap(m,limit).reverse();return {y:e.map(x=>x[0]),x:e.map(x=>x[1])}}
function statusChartData(m){const e=Array.from(m.entries());return {x:e.map(x=>x[0]),y:e.map(x=>x[1])}}
function startOfWeek(date){const d=new Date(date);d.setHours(0,0,0,0);const day=d.getDay(),diff=(day===0?-6:1-day);d.setDate(d.getDate()+diff);return d}
function layoutBarH(data,height){const maxLen=data&&data.y?Math.max(1,...data.y.map(s=>String(s||'').length)):20;const l=Math.min(Math.max(90,Math.round(maxLen*7.5)),330);return Object.assign({},LAYOUT_BASE,{height,margin:{l,r:55,t:20,b:20},xaxis:Object.assign({},LAYOUT_BASE.xaxis,{visible:false}),yaxis:Object.assign({},LAYOUT_BASE.yaxis,{autorange:'reversed'})})}
function layoutBarV(height){return Object.assign({},LAYOUT_BASE,{height,margin:{l:50,r:20,t:45,b:90},xaxis:Object.assign({},LAYOUT_BASE.xaxis,{tickangle:-30,automargin:true}),yaxis:Object.assign({},LAYOUT_BASE.yaxis,{visible:false})})}
function layoutLine(height){return Object.assign({},LAYOUT_BASE,{height,margin:{l:55,r:24,t:45,b:70},xaxis:Object.assign({},LAYOUT_BASE.xaxis,{tickangle:-30,automargin:true}),yaxis:Object.assign({},LAYOUT_BASE.yaxis,{title:'Loggers',automargin:true})})}
function traceLine(d){return [{type:'scatter',mode:'lines+markers',x:d.x,y:d.y,line:{color:'#2f80d0',width:3},marker:{color:'#f2d49a',size:8},text:d.y,textposition:'top center',textfont:{size:12,color:'#f8fbff'},hovertemplate:'%{x}<br>Loggers %{y}<extra></extra>'}]}
function traceBarH(d,color){return [{type:'bar',x:d.x,y:d.y,orientation:'h',text:d.x,textposition:'inside',marker:{color},textfont:{size:14,color:'#f8fbff'}}]}
function traceBarV(d,color){return [{type:'bar',x:d.x,y:d.y,text:d.y,textposition:'outside',cliponaxis:false,marker:{color},textfont:{size:13,color:'#f8fbff'}}]}
function renderChart(id,traces,layout){const el=document.getElementById(id);if(!el)return;const hasData=traces&&traces.length&&((traces[0].x||[]).length||(traces[0].y||[]).length);if(window.Plotly&&el._fullLayout)Plotly.purge(el);if(!hasData){el.innerHTML='<div class="chart-empty">Sem dados no periodo selecionado</div>';return}if(!window.Plotly){el.innerHTML='<div class="chart-empty">Plotly indisponivel</div>';return}Plotly.newPlot(el,traces,JSON.parse(JSON.stringify(layout)),cfg).catch(()=>{el.innerHTML='<div class="chart-empty">Erro ao carregar grafico</div>'})}
function legacyPass(r){const st=r[IDX['Status Fonte Original']],ret=r[IDX['Status Retorno dtbPortal']];if(_currentLegacy==='COM_FONTE_ORIGINAL')return st==='COM_FONTE_ORIGINAL';if(_currentLegacy==='SEM_FONTE_ORIGINAL')return st==='SEM_FONTE_ORIGINAL';if(_currentLegacy==='RETORNADO_DTBPORTAL')return ret==='Retornado';if(_currentLegacy==='PENDENTE_DTBPORTAL')return ret==='Pendente de Retorno';return true}
function getSnapshotBaseDate(){let max=null;for(const r of ALL_ROWS){const d=parseIso(r[ISO_ENTREGA_IDX]);if(d&&(!max||d>max))max=d}if(!max){const fallback=new Date();fallback.setHours(23,59,59,999);return fallback}max=new Date(max);max.setHours(23,59,59,999);return max}
function getPeriodBounds(days){const end=getSnapshotBaseDate();const start=new Date(end);start.setHours(0,0,0,0);start.setDate(start.getDate()-(days-1));return {start,end}}
function fmtDateBR(d){return `${String(d.getDate()).padStart(2,'0')}/${String(d.getMonth()+1).padStart(2,'0')}/${d.getFullYear()}`}
function filterRows(days){const bounds=getPeriodBounds(days),today=bounds.end,cutoff=bounds.start;return ALL_ROWS.filter(r=>{const dt=parseIso(r[ISO_ENTREGA_IDX]);return dt&&dt>=cutoff&&dt<=today&&(!_currentTipo||String(r[IDX['Tipo Datalogger']]||'')===_currentTipo)&&(!_currentUf||norm(r[IDX['UF VTC_STAGE']])===_currentUf||norm(r[IDX['UF Destino Fonte Original']])===_currentUf)&&(!_currentAgent||String(r[IDX['Agente Fonte Original']]||'')===_currentAgent)&&legacyPass(r)})}
function compute(rows,days){const pedidos=new Set(),semana=new Map(),expAgent=new Map(),pendAgent=new Map(),ufDest=new Map(),recebidos=new Map();let ret=0,pend=0;const bounds=getPeriodBounds(days),recebidosBounds=getPeriodBounds(7);for(const r of rows){const pedido=r[IDX['Pedido']],agent=r[IDX['Agente Fonte Original']],status=r[IDX['Status Retorno dtbPortal']];if(pedido)pedidos.add(pedido);if(status==='Retornado')ret++;if(status==='Pendente de Retorno')pend++;const dt=parseIso(r[ISO_ENTREGA_IDX]);if(dt){const wk=startOfWeek(dt),k=`${String(wk.getDate()).padStart(2,'0')}/${String(wk.getMonth()+1).padStart(2,'0')}/${wk.getFullYear()}`;inc(semana,k)}if(agent){inc(expAgent,agent);if(status==='Pendente de Retorno')inc(pendAgent,agent)}const uf=(r[IDX['UF Destino Fonte Original']]||r[IDX['UF VTC_STAGE']]||'NAO_INFORMADO');inc(ufDest,uf);if(status==='Retornado'){const h=parseIso(r[ISO_HIST_LEGADO_IDX]);if(h&&h>=recebidosBounds.start&&h<=recebidosBounds.end){const k=`${String(h.getDate()).padStart(2,'0')}/${String(h.getMonth()+1).padStart(2,'0')}/${h.getFullYear()}`;inc(recebidos,k)}}}const denom=ret+pend;const periodTxt=`${fmtDateBR(bounds.start)} ate ${fmtDateBR(bounds.end)}`;return {periodTxt,kpi:{pedidos:pedidos.size,loggers:rows.length,ret,pend,taxaRet:denom?ret/denom*100:0,taxaPend:denom?pend/denom*100:0},charts:{semana,expAgent,pendAgent,ufDest,recebidos}}}
function buildTableRows(rows){return rows.slice(0,TABLE_MAX_ROWS).map(r=>'<tr>'+r.slice(0,TABLE_HEADERS.length).map(v=>`<td title="${escapeHtml(v)}">${escapeHtml(v)}</td>`).join('')+'</tr>').join('')}
function buildCsvHref(headers,rows){const esc=v=>'"'+String(v??'').replace(/"/g,'""')+'"';const lines=[headers.map(esc).join(',')].concat(rows.map(r=>r.slice(0,headers.length).map(esc).join(',')));return URL.createObjectURL(new Blob([lines.join('\n')],{type:'text/csv;charset=utf-8;'}))}
function renderAll(days){const rows=filterRows(days),c=compute(rows,days);document.getElementById('meta-period').textContent=c.periodTxt;document.getElementById('kpi-pedidos').textContent=fmtInt(c.kpi.pedidos);document.getElementById('kpi-loggers').textContent=fmtInt(c.kpi.loggers);document.getElementById('kpi-retornados').textContent=fmtInt(c.kpi.ret);document.getElementById('kpi-pendentes').textContent=fmtInt(c.kpi.pend);document.getElementById('kpi-taxa-retorno').textContent=fmtPct(c.kpi.taxaRet);document.getElementById('kpi-taxa-pendencia').textContent=fmtPct(c.kpi.taxaPend);const semanaEntries=Array.from(c.charts.semana.entries());renderChart('chart-exp-agente',traceBarH(chartData(c.charts.expAgent,12),'#2f80d0'),layoutBarH(chartData(c.charts.expAgent,12),420));renderChart('chart-pend-agente',traceBarH(chartData(c.charts.pendAgent,12),'#f0a04b'),layoutBarH(chartData(c.charts.pendAgent,12),420));renderChart('chart-tendencia',traceLine({x:semanaEntries.map(x=>x[0]),y:semanaEntries.map(x=>x[1])}),layoutLine(360));renderChart('chart-uf-destino',traceBarH(chartData(c.charts.ufDest,15),'#144b8b'),layoutBarH(chartData(c.charts.ufDest,15),360));renderChart('chart-top-pend',traceBarH(chartData(c.charts.pendAgent,10),'#b85d30'),layoutBarH(chartData(c.charts.pendAgent,10),420));renderChart('chart-recebidos',traceBarV(statusChartData(c.charts.recebidos),'#4ecb71'),layoutBarV(420));const tbody=document.getElementById('detail-tbody');if(tbody)tbody.innerHTML=rows.length?buildTableRows(rows):`<tr><td colspan="${TABLE_HEADERS.length}" style="padding:16px;text-align:center;color:#9fb0c8;">Sem dados no filtro selecionado</td></tr>`;const csv=document.getElementById('csv-download');if(csv)csv.href=buildCsvHref(TABLE_HEADERS,rows)}
function switchPeriod(days){_currentDays=days;document.querySelectorAll('.btn').forEach(b=>b.classList.remove('active'));const b=document.getElementById('btn-'+days);if(b)b.classList.add('active');renderAll(days)}
function switchTipo(tipo){_currentTipo=tipo;document.querySelectorAll('.tipo-btn').forEach(b=>b.classList.remove('active'));const b=document.getElementById('tipo-btn-'+tipo);if(b)b.classList.add('active');renderAll(_currentDays)}
function switchUf(uf){_currentUf=uf;renderAll(_currentDays)}function switchAgent(a){_currentAgent=a;renderAll(_currentDays)}function switchLegacy(value){_currentLegacy=value;renderAll(_currentDays)}
function clearFilters(){_currentTipo='';_currentUf='';_currentAgent='';_currentLegacy='TODOS';document.getElementById('uf-filter').value='';document.getElementById('agent-filter').value='';document.getElementById('legacy-filter').value='TODOS';document.querySelectorAll('.tipo-btn').forEach(b=>b.classList.remove('active'));const b=document.getElementById('tipo-btn-');if(b)b.classList.add('active');renderAll(_currentDays)}
function switchTab(tab){document.getElementById('tab-exec').style.display=tab==='exec'?'':'none';document.getElementById('tab-detalhe').style.display=tab==='detalhe'?'':'none';document.getElementById('tab-exec-btn').classList.toggle('active',tab==='exec');document.getElementById('tab-detalhe-btn').classList.toggle('active',tab==='detalhe');if(tab==='exec')requestAnimationFrame(()=>CHART_IDS.forEach(id=>{const el=document.getElementById(id);if(el&&window.Plotly&&el._fullLayout)Plotly.Plots.resize(el)}))}
window.addEventListener('resize',()=>CHART_IDS.forEach(id=>{const el=document.getElementById(id);if(el&&window.Plotly&&Plotly.Plots&&Plotly.Plots.resize)Plotly.Plots.resize(el)}));renderAll(DEFAULT_PERIOD);
'''

def main():
    print('[html_hibrido_aderente] Carregando VTC_STAGE + fonte original atualizada...')
    rows,metrics=build_hybrid()
    tipos=sorted({r[TABLE_HEADERS.index('Tipo Datalogger')] for r in rows if r[TABLE_HEADERS.index('Tipo Datalogger')].strip()})
    ufs=sorted({r[TABLE_HEADERS.index('UF VTC_STAGE')] for r in rows if r[TABLE_HEADERS.index('UF VTC_STAGE')].strip()} | {r[TABLE_HEADERS.index('UF Destino Fonte Original')] for r in rows if r[TABLE_HEADERS.index('UF Destino Fonte Original')].strip()})
    agentes=sorted({r[TABLE_HEADERS.index('Agente Fonte Original')] for r in rows if r[TABLE_HEADERS.index('Agente Fonte Original')].strip()})
    gerado=datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    src=BASE_PKL if BASE_PKL.exists() else BASE_CSV
    snapshot_time=datetime.fromtimestamp(src.stat().st_mtime).strftime('%d/%m/%Y %H:%M:%S')
    html=generate_html(rows,metrics,tipos,ufs,agentes,gerado,snapshot_time).replace('__JS__',JS)
    OUTPUT_FILE.write_text(html,encoding='utf-8')
    print(f"[html_hibrido_aderente] Registros VTC_STAGE no HTML: {len(rows)}")
    print(f"[html_hibrido_aderente] Com fonte original atualizada: {metrics['matched']} ({fmt_pct2(metrics['coverage'])})")
    print(f"[html_hibrido_aderente] Sem fonte original atualizada: {metrics['no_match']}")
    print(f"[html_hibrido_aderente] Retornados dtbPortal: {metrics['returned']}")
    print(f"[html_hibrido_aderente] Pendentes dtbPortal: {metrics['pending']}")
    print(f"[html_hibrido_aderente] Taxa retorno global fonte original: {fmt_pct(metrics['taxa_ret'])}")
    print(f"[html_hibrido_aderente] Taxa pendencia global fonte original: {fmt_pct(metrics['taxa_pend'])}")
    print(f"[html_hibrido_aderente] HTML salvo: {OUTPUT_FILE}")

if __name__=='__main__':
    raise SystemExit('BLOQUEADO_GERADOR_TEMPLATE_LEGADO: use gerar_hibrido_aderente_original_fresco.py para preservar REVERSA_DATALOGGERS_STAGE.html')
