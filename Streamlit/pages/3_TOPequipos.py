import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Top Equipos", page_icon="🏆", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('../Data/stsbyseasonclean.csv')
    return df

df = load_data()

st.title("🏆 Top Equipos")