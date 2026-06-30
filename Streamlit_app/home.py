import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Stats by Season",
    page_icon='🏀',
    layout='wide'
)


st.title('🏀 Stats by Season')
st.write('Análisis de estadísticas de baloncesto: NBA vs Ligas Internacionales')

# Cargar datos
df = pd.read_csv(Path(__file__).parent.parent / "Data" / "stsbyseasonclean.csv")



@st.cache_data
def load_data():
    df = pd.read_csv(Path(__file__).parent.parent / "Data" / "stsbyseasonclean.csv")
    return df




col1, col2, col3, col4 = st.columns([2, 1, 2, 1])

with col1:
    with st.container(border=True):
        st.metric("Filas", f"{df.shape[0]:,}")

with col2:
    with st.container(border=True):
        st.metric("Columnas", df.shape[1])

with col3:
    with st.container(border=True):
        st.metric("Jugadores Únicos", f"{df['Player'].nunique():,}")

st.dataframe(df.head(10))

#_________________Total ligas y promedio de puntos_____________________________

col5, col6, col7 = st.columns([1, 1, 2])

with col5:
    with st.container(border=True):
        st.metric("Ligas", df['League'].nunique())

with col6:
    with st.container(border=True):
        st.metric("Promedio PTS", f"{df['PTS'].mean():.1f}")

#______________________Promedio de Puntos NBA vs Internacional_______________________________

df_nba = df[df['League'] == 'NBA']
df_int = df[df['Stage'] == 'International']

col8, col9, col10 = st.columns([1, 1, 2])

with col8:
    with st.container(border=True):
        st.metric("Promedio PTS NBA", f"{df_nba['PTS'].mean():.1f}")

with col9:
    with st.container(border=True):
        st.metric("Promedio PTS Internacional", f"{df_int['PTS'].mean():.1f}")

#_________________________________________________________

st.divider()

with st.expander("Ver estadísticas descriptivas"):
    st.dataframe(df.describe().T)

with st.expander("Ver valores nulos"):
    nulos = df.isnull().sum()
    if nulos.sum() > 0:
        st.dataframe(nulos[nulos > 0])
    else:
        st.success("✅ No hay valores nulos")