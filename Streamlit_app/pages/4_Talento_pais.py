import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(page_title="Talento por País", page_icon="🌍", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv(Path(__file__).parent.parent.parent / "Data" / "stsbyseasonclean.csv")
    return df

df = load_data()

st.title("🌍 Talento por País")

# ───── Preparar datos igual que en el EDA ─────
df_c = df.copy()
df_c = df_c[df_c['MIN'] > 0]

df_nba_f = df_c[df_c['League'] == 'NBA'].copy()
df_int_f = df_c[df_c['Stage'] == 'International'].copy()

# ───── Filtro Q1 minutos Internacional ─────
q1_min = df_int_f.groupby('League')['MIN'].quantile(0.25)
df_int_f = df_int_f.merge(q1_min.rename('min_req'), on='League')
df_int_f = df_int_f[df_int_f['MIN'] >= df_int_f['min_req']].copy()

# ───── Filtro Q1 minutos NBA ─────
q1_min_nba = df_nba_f.groupby('League')['MIN'].quantile(0.25)
df_nba_f = df_nba_f.merge(q1_min_nba.rename('min_req'), on='League')
df_nba_f = df_nba_f[df_nba_f['MIN'] >= df_nba_f['min_req']].copy()

# ───── Calcular performance y performpermin ─────
for d in [df_nba_f, df_int_f]:
    d['performance'] = d['PTS'] + d['REB'] + d['AST'] + d['STL'] + d['BLK']
    d['performpermin'] = d['performance'] / d['MIN']

# ───── Combinar NBA + Internacional ─────
df_all_f = pd.concat([df_nba_f, df_int_f])

# ───── Mejor jugador mundial (sin restricción de país) ─────
mejor_jugador_mundial = (
    df_all_f.groupby(['Player', 'nationality', 'League', 'Season'])['performpermin']
    .mean()
    .reset_index()
    .sort_values('performpermin', ascending=False)
    .iloc[0]
)

# ───── Top 10 nacionalidades con mínimo 30 jugadores ─────
talento_pais = (
    df_all_f.groupby('nationality')['performpermin']
    .agg(['mean', 'count'])
    .query('count >= 30')
    .sort_values('mean', ascending=False)
    .head(10)
    .reset_index()
)
talento_pais.columns = ['Nacionalidad', 'Performance_promedio', 'Num_jugadores']
talento_pais['Performance_promedio'] = talento_pais['Performance_promedio'].round(3)

# ───── Mejor jugador por cada nacionalidad del top 10 ─────
top10_paises = talento_pais['Nacionalidad'].tolist()

mejor_jugador_pais = (
    df_all_f[df_all_f['nationality'].isin(top10_paises)]
    .loc[
        df_all_f[df_all_f['nationality'].isin(top10_paises)]
        .groupby('nationality')['performpermin']
        .idxmax(),
        ['nationality', 'Player', 'performpermin', 'Season', 'League']
    ]
    .sort_values('performpermin', ascending=False)
    .reset_index(drop=True)
)
mejor_jugador_pais.columns = ['Nacionalidad', 'Jugador', 'Performance', 'Season', 'Liga']
mejor_jugador_pais['Performance'] = mejor_jugador_pais['Performance'].round(3)

# ───── KPIs ─────
st.markdown("### Indicadores clave")

col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    with st.container(border=True):
        st.metric("País con más talento",
                  talento_pais.iloc[0]['Nacionalidad'],
                  f"{talento_pais.iloc[0]['Performance_promedio']:.3f} perf/min")
        st.caption(f"👥 {talento_pais.iloc[0]['Num_jugadores']} jugadores")

with col2:
    with st.container(border=True):
        st.metric("Mejor jugador mundial",
                  mejor_jugador_mundial['Player'],
                  f"{mejor_jugador_mundial['performpermin']:.3f} perf/min")
        st.caption(f"🌍 {mejor_jugador_mundial['nationality']} | {mejor_jugador_mundial['League']} | {mejor_jugador_mundial['Season']}")

st.divider()

# ───── Slider por temporada ─────
st.markdown("### 🔎 Mejor jugador por temporada")

temporadas = sorted(df_all_f['Season'].unique().tolist())
temporada_sel = st.select_slider("Selecciona una temporada", options=temporadas, key="slider_pais")

df_sel = df_all_f[df_all_f['Season'] == temporada_sel]

if not df_sel.empty:
    mejor_jugador_año = (
        df_sel.groupby(['Player', 'nationality', 'League'])['performpermin']
        .mean()
        .reset_index()
        .sort_values('performpermin', ascending=False)
        .iloc[0]
    )

    col1, col2, col3 = st.columns([2, 2, 1])

    with col1:
        with st.container(border=True):
            st.metric("Mejor jugador",
                      mejor_jugador_año['Player'],
                      f"{mejor_jugador_año['performpermin']:.3f} perf/min")
            st.caption(f"🌍 {mejor_jugador_año['nationality']} | {mejor_jugador_año['League']} | {temporada_sel}")

st.divider()

# ───── Tabs ─────
tab1, tab2 = st.tabs(["🌍 Top 10 Nacionalidades", "📊 Gráfica"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Top 10 países por talento")
        st.dataframe(talento_pais)

    with col2:
        st.markdown("### Mejor jugador por nacionalidad")
        st.dataframe(mejor_jugador_pais)

with tab2:
    st.markdown("### Top 10 países por performance promedio")

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(talento_pais['Nacionalidad'], talento_pais['Performance_promedio'], color='purple')
    ax.set_title('Top 10 Nacionalidades por Performance promedio')
    ax.set_xlabel('Performance por minuto (promedio)')
    ax.invert_yaxis()

    for spine in ax.spines.values():
        spine.set_visible(False)

    for i, val in enumerate(talento_pais['Performance_promedio']):
        ax.text(val + 0.001, i, f'{val:.3f}', va='center', fontsize=9)

    plt.tight_layout()
    st.pyplot(fig)