# RELATORIO ESCOPO INICIAL - REVERSA VTC_STAGE

Data da verificacao: 2026-07-07

## Escopo

Este projeto sera tratado como um indicador novo, isolado e independente:

`NOVO INDICADOR DE REVERSA - VTC_STAGE`

Pasta obrigatoria de trabalho:

`C:\Users\Administrador\Documents\NOVO INDICADOR DE REVERSA - VTC_STAGE`

Nenhum arquivo fora desta pasta deve ser alterado. Nenhuma rotina antiga de producao deve ser executada. Nenhum commit, push, rebase, deploy ou publicacao deve ser feito.

## Diretorio Atual Validado

`C:\Users\Administrador\Documents\NOVO INDICADOR DE REVERSA - VTC_STAGE`

## Estado Git

Nao foi encontrado diretorio `.git` na raiz da pasta isolada.

## Arquivos e Pastas Encontrados

- `Banco_Aura/`
- `Banco_Aura/.env`
- `Banco_Aura/.env.example`
- `Banco_Aura/.gitignore`
- `Banco_Aura/.nojekyll`
- `Banco_Aura/ATUALIZAR_REVERSA.bat`
- `Banco_Aura/env_utils.py`
- `Banco_Aura/gerar_html_reversa.py`
- `Banco_Aura/REVERSA_LOGGER.html`
- `streamlit/`
- `streamlit/dasboard_reversa_loggers.py`
- `streamlit/gerar_modelo_final_reversa.py`
- `streamlit/gerar_snapshot_reversa.py`
- `snapshot_reversa/`
- `snapshot_reversa/base_agentes.pkl`
- `snapshot_reversa/base_destinatarios.pkl`
- `snapshot_reversa/base_loggers.pkl`
- `snapshot_reversa/modelo_final.pkl`
- `snapshot_reversa/recebimento.pkl`
- `snapshot_reversa/recebimento_resumo.pkl`
- `README_PACOTE_AURA.md`
- `requirements.txt`

## Arquivos Herdados Perigosos

Os arquivos abaixo vieram da clonagem estrutural do indicador antigo e nao devem ser executados como parte do novo indicador:

- `Banco_Aura/ATUALIZAR_REVERSA.bat`
  - contem fluxo antigo de atualizacao, commit, fetch, rebase e push;
  - aponta para a pagina antiga `https://luan9753.github.io/banco-aura-dashboard/REVERSA_DATALOGGERS.html`;
  - chama scripts herdados;
  - deve permanecer apenas como legado, sem execucao.

- `streamlit/gerar_snapshot_reversa.py`
  - gera snapshots antigos em `snapshot_reversa`;
  - usa fontes antigas do indicador de reversa;
  - nao deve ser executado para o novo indicador.

- `Banco_Aura/gerar_html_reversa.py`
  - gera o HTML antigo `REVERSA_DATALOGGERS.html`;
  - consome `snapshot_reversa`;
  - nao deve ser usado como gerador oficial do novo indicador.

- `streamlit/gerar_modelo_final_reversa.py`
  - arquivo herdado do fluxo antigo;
  - nao deve ser executado ate revisao especifica.

- `streamlit/dasboard_reversa_loggers.py`
  - dashboard herdado;
  - nao deve ser usado como dependencia do novo indicador.

- `snapshot_reversa/`
  - snapshots herdados;
  - nao devem ser usados como base oficial do novo indicador VTC_STAGE.

## BATs Herdados

Foi encontrado um BAT herdado:

- `Banco_Aura/ATUALIZAR_REVERSA.bat`

Status: **NAO EXECUTAR**.

## Confirmacoes de Escopo

- Nenhum arquivo fora da pasta isolada sera alterado.
- Nenhuma publicacao sera feita.
- Nenhum commit sera feito.
- Nenhum push sera feito.
- Nenhum rebase sera feito.
- Nenhuma rotina antiga sera executada.
- Nenhum BAT herdado sera executado.
- O indicador antigo sera usado apenas como referencia visual/conceitual, nao como dependencia.
- A nova fonte oficial em investigacao sera o schema `vtc_stage`, principalmente `vtc_stage.documentos`.

## Proximos Artefatos Permitidos

Somente dentro da pasta isolada:

- `gerar_snapshot_reversa_vtc_stage.py`
- `gerar_modelo_reversa_vtc_stage.py` se necessario
- `gerar_html_reversa_vtc_stage.py` se a base estiver consistente
- `REVERSA_DATALOGGERS_VTC_STAGE.html`
- `snapshot_reversa_vtc_stage/`
- `snapshot_reversa_vtc_stage/base_vtc_stage_dedup.csv`
- `snapshot_reversa_vtc_stage/base_vtc_stage_dedup.pkl`
- `snapshot_reversa_vtc_stage/relatorio_validacao_vtc_stage.md`
- `RELATORIO_VALIDACAO_REVERSA_VTC_STAGE.md`

## Declaracao Inicial

Este trabalho passa a ser tratado como produto de dados novo. A clonagem anterior foi apenas ponto de partida estrutural. A partir desta etapa, qualquer implementacao deve criar artefatos novos, com nomes proprios de VTC_STAGE, e sem dependencia operacional do Banco Aura original.
