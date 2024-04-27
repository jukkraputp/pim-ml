import seaborn as sns
import streamlit as st

st.title('Iris Dataset')
df = sns.load_dataset('iris')
df
st.sidebar.title('Input Parameters')
for col in df.columns:
    if col != 'species':
        st.sidebar.slider(col, .9*df[col].min(), 1.1*df[col].max(), df[col].mean())

