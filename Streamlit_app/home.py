import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image


st.set_page_config(
    page_title="Stats by Season",
    page_icon='🏀',
    layout='wide'
)

df = pd.read_csv(Path(__file__).parent.parent / "Data" / "stsbyseasonclean.csv")


# ____________BANNER_________
banner = Image.open(Path(__file__).parent / "assets" / "banner.png")
_, col_banner, _ = st.columns([1, 2, 1])
with col_banner:
    st.image(banner, use_container_width=True)




st.title('Estadísticas por temporada')

st.markdown("""
Análisis de estadísticas de baloncesto: **NBA vs Ligas Internacionales**

Este dashboard explora datos desde 1999 hasta 2020.
""")

st.divider()

# ───── Navegación visual ─────
st.markdown("### 📂 Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.container(border=True):
        st.markdown("####  NBA 🆚 Internacional")
        st.caption("Compara estadísticas entre la NBA y las ligas internacionales")
        st.page_link("pages/1_NBA_vs_INT.py", label="Ir a la página ->")

with col2:
    with st.container(border=True):
        st.markdown("#### Top Jugadores")
        st.caption("Explora los mejores jugadores con filtros interactivos")
        st.page_link("pages/2_TOP_players.py", label="Ir a la página ->")

with col3:
    with st.container(border=True):
        st.markdown("#### Top Equipos")
        st.caption("Descubre los mejores equipos históricos y por temporada")
        st.page_link("pages/3_TOP_equipos.py", label="Ir a la página ->")

with col4:
    with st.container(border=True):
        st.markdown("#### Talento por País")
        st.caption("Qué países producen más talento en el baloncesto mundial")
        st.page_link("pages/4_Talento_pais.py", label="Ir a la página ->")

st.divider()





st.title('Estadísticas por temporada')
st.write('Análisis de estadísticas de baloncesto: NBA vs Ligas Internacionales')

# Cargar datos



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