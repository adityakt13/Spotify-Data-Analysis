import pandas as pd
import streamlit as st
import plotly.express as px

# page config
st.set_page_config(
    page_title='Spotify App',
    page_icon='🦖',
    layout='wide'
)

st.sidebar.title('🦕 Spotify App 🦖')
st.image('Spotify-Data-Analysis/Spotify.jpg', use_column_width=True)

# load data
@st.cache_data
def load_spotify():
    data = pd.read_csv('Spotify-Data-Analysis/SpotifyFeatures.csv', index_col=0)
    return data

with st.spinner('Loading Pokemon Data ...'):
    spotify = load_spotify()
    st.sidebar.success("Loaded Spotify Data")

show_data = st.sidebar.checkbox('Show the dataset')
if show_data:
    st.subheader('Spotify Data')
    st.dataframe(spotify, use_container_width=True)

type1 = st.sidebar.selectbox('Select genre', spotify['Type 1'].unique())
subset = spotify[spotify['Type 1'] == type1] # filter

tabs = st.tabs(['Data','Univariate Analysis','Bivariate Analysis', 'Trivariate Analysis'])

# Data tab
tabs[0].subheader(f'{type1} Genres')
tabs[0].dataframe(subset, use_container_width=True)