import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(
    page_title='NBA vs Ligas Internacionales',
    layout='wide'
)


# Cargar datos
df = pd.read_csv(Path(__file__).parent.parent / "Data" / "stsbyseasonclean.csv")

@st.cache_data
def load_data():
    df = pd.read_csv(Path(__file__).parent.parent / "Data" / "stsbyseasonclean.csv")
    return df


#1 _______________Filtramos los Datos de NBA e INT__________________

df_nba = df[df['League'] == 'NBA']
df_int = df[df['Stage'] == 'International']


#2 _____________________Comparaciones____________________

st.title("🆚 NBA vs Internacional")

st.markdown("### Comparativa de rendimiento promedio")

tab1, tab2 = st.tabs(['Datos', 'Gráfica'])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🏀 NBA")
        with st.container(border=True):
            st.metric("Promedio PTS", f"{df_nba['PTS'].mean():.1f}")
        with st.container(border=True):
            st.metric("Promedio REB", f"{df_nba['REB'].mean():.1f}")
        with st.container(border=True):
            st.metric("Promedio AST", f"{df_nba['AST'].mean():.1f}")
        with st.container(border=True):
            st.metric("Promedio MIN", f"{df_nba['MIN'].mean():.1f}")
        

    with col2:
        st.markdown("#### 🌍 Internacional")
        with st.container(border=True):
            st.metric("Promedio PTS", f"{df_int['PTS'].mean():.1f}")
        with st.container(border=True):
            st.metric("Promedio REB", f"{df_int['REB'].mean():.1f}")
        with st.container(border=True):
            st.metric("Promedio AST", f"{df_int['AST'].mean():.1f}")
        with st.container(border=True):
            st.metric("Promedio MIN", f"{df_int['MIN'].mean():.1f}")
    

# Estadística nomralizada______________________________

    st.markdown("### Estadísticas normalizadas")

    df_nba['performance'] = df_nba['PTS'] + df_nba['REB'] + df_nba['AST'] + df_nba['STL'] + df_nba['BLK']
    df_nba['performpermin'] = df_nba['performance'] / df_nba['MIN']

    df_int['performance'] = df_int['PTS'] + df_int['REB'] + df_int['AST'] + df_int['STL'] + df_int['BLK']
    df_int['performpermin'] = df_int['performance'] / df_int['MIN']

    # Si un jugador da 0, no normalizamos con lo siguiente:

    df_nba = df_nba[df_nba['MIN'] > 0]
    df_int = df_int[df_int['MIN'] > 0]


# KPI Normalizado_______________________________

    col3, col4 = st.columns(2)

    st.markdown('###### >1.0 -> jugador muy productivo por minuto | 0.5 - 1.0 -> buen rendimiento | <0.5 -> rendimiento bajo')
    st.markdown('###### La suma de PTS, REB, AST, STL y BLK dividida entre los minutos totales.')
    with col3:
        st.markdown("#### 🏀 NBA")
        with st.container(border=True):
            st.metric("Performance/min", f"{df_nba['performpermin'].mean():.3f}")

    with col4:
        st.markdown("#### 🌍 Internacional")
        with st.container(border=True):
            st.metric("Performance/min", f"{df_int['performpermin'].mean():.3f}")


# _______________Gáfico comparativo_________________

with tab2:

    st.markdown("### Comparativa visual")

    resumen = pd.DataFrame({
        'Liga': ['NBA', 'Internacional', 'NBA', 'Internacional', 'NBA', 'Internacional'],
        'Estadística': ['PTS', 'PTS', 'REB', 'REB', 'AST', 'AST'],
        'Valor': [
            df_nba['PTS'].mean(), df_int['PTS'].mean(),
            df_nba['REB'].mean(), df_int['REB'].mean(),
            df_nba['AST'].mean(), df_int['AST'].mean()
        ]
    })

    fig, ax = plt.subplots(figsize=(8, 5))
    colors = resumen['Liga'].apply(lambda x: 'purple' if x == 'NBA' else 'coral')

    ax.bar(
        resumen['Estadística'] + ' - ' + resumen['Liga'],
        resumen['Valor'],
        color=colors
    )
    ax.set_title('Comparativa de estadísticas promedio')
    ax.set_ylabel('Valor promedio')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    st.pyplot(fig)