import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(page_title="Top Equipos", page_icon="🏆", layout="wide")


@st.cache_data
def load_data():
    df = pd.read_csv(Path(__file__).parent.parent.parent / "Data" / "stsbyseasonclean.csv")
    return df

df = load_data()

st.title("🏆 Top Equipos")