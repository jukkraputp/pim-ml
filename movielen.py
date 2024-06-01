import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#ratings_path = 'https://raw.githubusercontent.com/smanihwr/ml-latest-small/master/ratings.csv'

@st.cache_data
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/smanihwr/ml-latest-small/master/movies.csv')
    df = df.join(df.pop('genres').str.get_dummies('|'))
    return df

if 'movies' not in st.session_state:
    st.session_state['movies'] = load_data()

movies = st.session_state['movies']
st.write(movies)
p = movies.iloc[:, 3:].sum(axis=0)
fig = px.pie(p, names=p.index, values=p.values)
st.plotly_chart(fig)

fig = px.bar(p, x=p.values, y=p.index)
st.plotly_chart(fig)

fig = px.imshow(movies.iloc[:, 3:].corr().round(1), text_auto=True)
st.plotly_chart(fig)

x = []
for i in movies.columns[3:]:
    x.append(st.sidebar.slider(i, 0, 5, 0))
x = np.array(x)
user_profile = x / x.sum()
st.write(user_profile)

rank = (movies.iloc[:, 3:] * user_profile).sum(axis=1)
df = pd.DataFrame(columns=['title', 'rank'])
df['title'] = movies['title']
df['rank'] = rank
df = df.sort_values('rank', ascending=False)
st.write(df)