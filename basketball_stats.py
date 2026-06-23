import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../Data/stsbyseasons_clean2.csv')

st.title('🏀 EDA - Stats by Season')