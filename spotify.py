import pandas as pd
import streamlit as st
import plotly.express as px

# page config
st.set_page_config(
    page_title='Spotify',
    page_icon='🦖',
    layout='wide'
)

st.sidebar.title('🦕 Spotify Analysis 🦖')
st.image('Spotify-Data-Analysis\Spotify.jpg', use_column_width=True)

# load data
@st.cache_data
def load_spotify():
    data = pd.read_csv('Spotify-Data-Analysis/SpotifyFeatures.csv', index_col=0)
    return data

with st.spinner('Loading Spotify Data ...'):
    spotify = load_spotify()
    st.sidebar.success("Loaded Spotify Data")

show_data = st.sidebar.checkbox('Show the dataset')
if show_data:
    st.subheader('Spotify Data')
    st.dataframe(spotify, use_container_width=True)

type1 = st.sidebar.selectbox('Select Spotify song', spotify['genre'].unique())
subset = spotify[spotify['genre'] == type1] # filter

tabs = st.tabs(['Data','Univariate Analysis','Bivariate Analysis'])

# Data tab
tabs[0].subheader(f'{type1} Song')
tabs[0].dataframe(subset, use_container_width=True)

# # Univariate Analysis tab
# # Attack
# ss = subset.sort_values(by='Attack')
# fig1 = px.histogram(ss, x='Attack', nbins=20)
# fig2 = px.bar(ss, x='Name', y='Attack')
# tabs[1].subheader(f'{type1} Stats')
# tabs[1].subheader('Attack')
# tabs[1].plotly_chart(fig1, use_container_width=True)
# tabs[1].plotly_chart(fig2, use_container_width=True)

# # Defense
# ss = subset.sort_values(by='Defense')
# fig1 = px.histogram(ss, x='Defense', nbins=20)
# fig2 = px.bar(ss, x='Name', y='Defense')
# tabs[1].subheader(f'{type1} Stats')
# tabs[1].subheader('Defense')
# tabs[1].plotly_chart(fig1, use_container_width=True)
# tabs[1].plotly_chart(fig2, use_container_width=True)

# # do the same for HP, Sp. Atk, Sp. Def, Speed

# # Bivariate Analysis tab
# x = tabs[2].selectbox('Select X',pokemon.select_dtypes('number').columns)
# y = tabs[2].selectbox('Select Y',pokemon.select_dtypes('number').columns)
# c = tabs[2].selectbox('Select Color',pokemon.select_dtypes(exclude='number').columns)
# fig = px.scatter(subset, x=x, y=y, color=c, hover_data=['Name'], size=x, size_max=60)
# tabs[2].subheader(f'{type1} : {x} vs {y} by {c}')
# tabs[2].plotly_chart(fig, use_container_width=True)

# # trivariate analysis
# x = tabs[3].selectbox('Select X data',pokemon.select_dtypes('number').columns)
# y = tabs[3].selectbox('Select Y data',pokemon.select_dtypes('number').columns)
# z = tabs[3].selectbox('Select Z data',pokemon.select_dtypes('number').columns)
# c = tabs[3].selectbox('Select Color type',pokemon.select_dtypes(exclude='number').columns)
# fig = px.scatter_3d(subset, x=x, y=y, z=z, color=c, hover_data=['Name'], size=x, size_max=60)
# tabs[3].subheader(f'{type1} : {x} vs {y} vs {z} by {c}')
# tabs[3].plotly_chart(fig, use_container_width=True) 