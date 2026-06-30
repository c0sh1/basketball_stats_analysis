import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Top Jugadores", page_icon="🏆", layout="wide")

df = pd.read_csv(Path(__file__).parent.parent / "Data" / "stsbyseasonclean.csv")

@st.cache_data
def load_data():
    df = pd.read_csv(Path(__file__).parent.parent / "Data" / "stsbyseasonclean.csv")
    return df

df = load_data()

st.title("🏆 Top Jugadores")

# ______Función para resetear______
def resetear_filtros():
    st.session_state.liga = "Todas"
    st.session_state.temporada = "Todas"
    st.session_state.stage = "Todos"
    st.session_state.equipo = "Todos"
    st.session_state.jugador = "Todos"

# ______Leer selección actual (de la ejecución anterior)_______
liga_actual = st.session_state.get('liga', 'Todas')
temporada_actual = st.session_state.get('temporada', 'Todas')
stage_actual = st.session_state.get('stage', 'Todos')
equipo_actual = st.session_state.get('equipo', 'Todos')
jugador_actual = st.session_state.get('jugador', 'Todos')

# ______Filtrar el df aplicando todos los filtros MENOS uno______
def filtrar_excepto(excluir):
    d = df.copy()
    if excluir != 'liga' and liga_actual != 'Todas':
        d = d[d['League'] == liga_actual]
    if excluir != 'temporada' and temporada_actual != 'Todas':
        d = d[d['Season'] == temporada_actual]
    if excluir != 'stage' and stage_actual != 'Todos':
        d = d[d['Stage'] == stage_actual]
    if excluir != 'equipo' and equipo_actual != 'Todos':
        d = d[d['Team'] == equipo_actual]
    if excluir != 'jugador' and jugador_actual != 'Todos':
        d = d[d['Player'] == jugador_actual]
    return d

# ______Filtros en la barra lateral______
st.sidebar.header("Filtros")

ligas = ['Todas'] + sorted(filtrar_excepto('liga')['League'].unique().tolist())
liga_sel = st.sidebar.selectbox("Liga", ligas, key="liga")

temporadas = ['Todas'] + sorted(filtrar_excepto('temporada')['Season'].unique().tolist())
temporada_sel = st.sidebar.selectbox("Temporada", temporadas, key="temporada")

stages = ['Todos'] + sorted(filtrar_excepto('stage')['Stage'].unique().tolist())
stage_sel = st.sidebar.selectbox("Stage", stages, key="stage")

equipos = ['Todos'] + sorted(filtrar_excepto('equipo')['Team'].unique().tolist())
equipo_sel = st.sidebar.selectbox("Equipo", equipos, key="equipo")

jugadores = ['Todos'] + sorted(filtrar_excepto('jugador')['Player'].unique().tolist())
jugador_sel = st.sidebar.selectbox("Jugador", jugadores, key="jugador")

st.sidebar.button("🔄 Resetear filtros", on_click=resetear_filtros)

# ______df_filtrado final (todos los filtros aplicados)______
df_filtrado = filtrar_excepto(None)

# ───── Mostrar resultado ─────
st.write(f"Mostrando {df_filtrado.shape[0]} registros")
st.dataframe(df_filtrado)

# ______Tabs______
st.divider()

if liga_sel == 'Todas':
    st.info("💡 Mostrando jugadores de todas las ligas. Las estadísticas brutas no son directamente comparables entre ligas con diferente número de minutos jugados.")

tab1, tab2 = st.tabs(["🏆 Top 10 por Puntos", "📈 Evolución del Jugador"])

with tab1:
    st.markdown("### 🏆 Top 10 por Puntos")
    st.markdown('###### Usa los filtros')

    top10 = (
        df_filtrado[['Player', 'Team', 'Season', 'PTS', 'REB', 'AST', 'MIN']]
        .sort_values('PTS', ascending=False)
        .head(10)
        .reset_index(drop=True)
    )
    st.dataframe(top10)

with tab2:
    if jugador_sel != 'Todos':
        st.markdown(f"### 📈 Evolución de {jugador_sel}")

        if df_filtrado.duplicated(subset='Season').any():
            st.warning("⚠️ Este jugador tiene varios registros por temporada (Regular Season/Playoffs/International). Filtra por Stage para una vista más clara.")

        evolucion = df_filtrado[['Season', 'PTS', 'REB', 'AST']].set_index('Season')
        st.line_chart(evolucion)
    else:
        st.warning("Selecciona un jugador en la barra lateral para ver su evolución")