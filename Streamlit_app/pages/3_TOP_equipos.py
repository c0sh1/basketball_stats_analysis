import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Top Equipos", page_icon="🏆", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv(Path(__file__).parent.parent.parent / "Data" / "stsbyseasonclean.csv")
    return df

df = load_data()

# ───── Preparar datos ─────
df_nba = df[df['League'] == 'NBA'].copy()
df_int = df[df['Stage'] == 'International'].copy()

df_nba = df_nba[df_nba['MIN'] > 0]
df_int = df_int[df_int['MIN'] > 0]

# ───── Filtro Q1 minutos por liga ─────
q1_min = df_int.groupby('League')['MIN'].quantile(0.25)
df_int = df_int.merge(q1_min.rename('min_req'), on='League')
df_int = df_int[df_int['MIN'] >= df_int['min_req']].copy()

# ───── Calcular performance y performpermin ─────
df_nba['performance'] = df_nba['PTS'] + df_nba['REB'] + df_nba['AST'] + df_nba['STL'] + df_nba['BLK']
df_nba['performpermin'] = df_nba['performance'] / df_nba['MIN']

df_int['performance'] = df_int['PTS'] + df_int['REB'] + df_int['AST'] + df_int['STL'] + df_int['BLK']
df_int['performpermin'] = df_int['performance'] / df_int['MIN']

# ───── Filtrar equipos con 10+ jugadores únicos en total ─────
equipos_validos = df_int.groupby('Team')['Player'].nunique()
equipos_validos = equipos_validos[equipos_validos >= 10].index
df_int_f = df_int[df_int['Team'].isin(equipos_validos)].copy()

# ───── Top 5 NBA — promedio histórico + mejor temporada ─────
team_avg_nba = (
    df_nba.groupby('Team')['performpermin']
    .mean()
    .reset_index()
    .sort_values('performpermin', ascending=False)
    .head(5)
    .reset_index(drop=True)
)

best_season_nba = (
    df_nba.groupby(['Team', 'Season'])['performpermin']
    .mean()
    .reset_index()
    .sort_values('performpermin', ascending=False)
    .drop_duplicates(subset='Team')[['Team', 'Season']]
)

top5_nba = team_avg_nba.merge(best_season_nba, on='Team')
top5_nba.columns = ['Equipo', 'Performance', 'Mejor Season']

# ───── Top 5 Internacional — promedio histórico + mejor temporada ─────
team_avg_int = (
    df_int_f.groupby(['Team', 'League'])['performpermin']
    .mean()
    .reset_index()
    .sort_values('performpermin', ascending=False)
    .head(5)
    .reset_index(drop=True)
)

best_season_int = (
    df_int_f.groupby(['Team', 'League', 'Season'])['performpermin']
    .mean()
    .reset_index()
    .sort_values('performpermin', ascending=False)
    .drop_duplicates(subset=['Team', 'League'])[['Team', 'League', 'Season']]
)

top5_int = team_avg_int.merge(best_season_int, on=['Team', 'League'])
top5_int.columns = ['Equipo', 'Liga', 'Performance', 'Mejor Season']

st.title("🏆 Top Equipos")

# ───── Tabs principales ─────
tab_rankings, tab_graficas = st.tabs(["🏀 Top 5 Histórico", "📊 Gráficas"])

with tab_rankings:

    stats = ['PTS', 'REB', 'AST', 'STL', 'BLK']

    # ───── Indicadores clave históricos ─────
    st.markdown("### Indicadores clave históricos")

    col1, col_radar1, col2 = st.columns([2, 3, 2])

    with col1:
        with st.container(border=True):
            st.metric("Mejor equipo NBA",
                      top5_nba.iloc[0]['Equipo'],
                      f"{top5_nba.iloc[0]['Performance']:.3f} perf/min")
            st.caption(f"🏀 NBA | Mejor temporada: {top5_nba.iloc[0]['Mejor Season']}")

    with col2:
        with st.container(border=True):
            st.metric("Mejor equipo Internacional",
                      top5_int.iloc[0]['Equipo'],
                      f"{top5_int.iloc[0]['Performance']:.3f} perf/min")
            st.caption(f"🌍 {top5_int.iloc[0]['Liga']} | Mejor temporada: {top5_int.iloc[0]['Mejor Season']}")

    st.divider()  # ← divider entre secciones

    # ───── Filtro por temporada ─────
    st.markdown("### 🔎 Explorar por temporada")
    temporadas = sorted(df['Season'].unique().tolist())
    temporada_sel = st.select_slider("Selecciona una temporada", options=temporadas)

    df_nba_sel = df_nba[df_nba['Season'] == temporada_sel]
    df_int_sel = df_int_f[df_int_f['Season'] == temporada_sel]

    mejor_nba_team = None
    mejor_int_team = None

    col1, col_radar2, col2 = st.columns([2, 3, 2])

    with col1:
        with st.container(border=True):
            if df_nba_sel.empty:
                st.warning("No hay datos NBA para esta temporada")
            else:
                mejor_nba = (
                    df_nba_sel.groupby('Team')['performpermin']
                    .mean()
                    .sort_values(ascending=False)
                    .reset_index()
                    .iloc[0]
                )
                mejor_nba_team = mejor_nba['Team']
                st.metric("Mejor equipo NBA",
                          mejor_nba_team,
                          f"{mejor_nba['performpermin']:.3f} perf/min")
                st.caption(f"🏀 NBA | {temporada_sel}")

    with col2:
        with st.container(border=True):
            if df_int_sel.empty:
                st.warning("No hay datos internacionales para esta temporada")
            else:
                mejor_int = (
                    df_int_sel.groupby(['Team', 'League'])['performpermin']
                    .mean()
                    .reset_index()
                    .sort_values('performpermin', ascending=False)
                    .iloc[0]
                )
                mejor_int_team = mejor_int['Team']
                st.metric("Mejor equipo Internacional",
                          mejor_int_team,
                          f"{mejor_int['performpermin']:.3f} perf/min")
                st.caption(f"🌍 {mejor_int['League']} | {temporada_sel}")

    # ───── Radar en el centro ─────
    with col_radar2:
        equipos_comparar = {
            f"{top5_nba.iloc[0]['Equipo']} (Histórico NBA)": df_nba[df_nba['Team'] == top5_nba.iloc[0]['Equipo']][stats].mean(),
            f"{top5_int.iloc[0]['Equipo']} (Histórico Intl)": df_int_f[df_int_f['Team'] == top5_int.iloc[0]['Equipo']][stats].mean(),
        }

        if mejor_nba_team:
            equipos_comparar[f"{mejor_nba_team} ({temporada_sel} NBA)"] = df_nba_sel[df_nba_sel['Team'] == mejor_nba_team][stats].mean()

        if mejor_int_team:
            equipos_comparar[f"{mejor_int_team} ({temporada_sel} Intl)"] = df_int_sel[df_int_sel['Team'] == mejor_int_team][stats].mean()

        all_values = pd.DataFrame(equipos_comparar).T
        for stat in stats:
            min_val = all_values[stat].min()
            max_val = all_values[stat].max()
            if max_val != min_val:
                all_values[stat] = (all_values[stat] - min_val) / (max_val - min_val)
            else:
                all_values[stat] = 0

        colors_plotly = ['purple', 'coral', 'steelblue', 'green']
        fig = go.Figure()

        for i, (nombre, row) in enumerate(all_values.iterrows()):
            valores = row[stats].tolist()
            valores += valores[:1]
            categorias = stats + [stats[0]]

            fig.add_trace(go.Scatterpolar(
                r=valores,
                theta=categorias,
                fill='toself',
                name=nombre,
                line_color=colors_plotly[i % len(colors_plotly)],
                opacity=0.7
            ))

        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
            showlegend=True,
            height=600
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    tab_nba, tab_int = st.tabs(["🏀 Top 5 NBA", "🌍 Top 5 Internacional"])

    with tab_nba:
        st.markdown("### Top 5 equipos NBA histórico")
        st.dataframe(top5_nba)

    with tab_int:
        st.markdown("### Top 5 equipos Internacionales histórico")
        st.dataframe(top5_int)

with tab_graficas:
    st.markdown("### Comparativa Top 5 NBA vs Top 5 Internacional")

    top5_nba_plot = top5_nba.copy()
    top5_nba_plot['label'] = top5_nba_plot['Equipo'] + ' (NBA)'

    top5_int_plot = top5_int.copy()
    top5_int_plot['label'] = top5_int_plot['Equipo'] + ' (' + top5_int_plot['Liga'] + ')'

    combined = pd.concat([
        top5_nba_plot[['label', 'Performance']],
        top5_int_plot[['label', 'Performance']]
    ]).sort_values('Performance', ascending=True).reset_index(drop=True)

    colors = combined['label'].apply(lambda x: 'purple' if '(NBA)' in x else 'coral')

    fig2, ax = plt.subplots(figsize=(10, 7))
    ax.barh(combined['label'], combined['Performance'], color=colors)
    ax.set_title('Top 5 Equipos NBA vs Internacional — Performance por minuto')
    ax.set_xlabel('Performance por minuto (promedio)')

    for spine in ax.spines.values():
        spine.set_visible(False)

    for i, val in enumerate(combined['Performance']):
        ax.text(val + 0.005, i, f'{val:.3f}', va='center', fontsize=9)

    plt.tight_layout()
    st.pyplot(fig2)