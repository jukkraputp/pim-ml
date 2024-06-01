import streamlit as st
import pandas as pd
import numpy as np


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