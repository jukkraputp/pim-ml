import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Exploratory Data Analysis')

if 'df' in st.session_state:
    df = st.session_state['df']

    selected_col = st.sidebar.multiselect('Select columns', df.columns)
    if len(selected_col) == 0:
        selected_col = df.columns
    st.write(df[selected_col])

    corr = df[selected_col].corr(numeric_only=True).round(2)
    fig = px.imshow(corr, text_auto=True)
    st.plotly_chart(fig)