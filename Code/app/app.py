import streamlit as st
# on stream lit
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv
# mandatory for st to provide the page config
st.set_page_config(page_title="Anime Recommnder",layout="wide")

load_dotenv()

@st.cache_resource
# to initialize the pipeline

# What it does:
# Caches the return value of the function
# Runs the function only on the first call
# Reuses the cached result on subsequent calls
# Persists across user interactions and reruns
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")
# now we give the query , a place user can ask question in the stremlit

query = st.text_input("Enter your anime prefernces eg. : light hearted anime with school settings")
# if query provided 
if query:
    # fetching recommendations for you.....
    # spinner is used to show the user that the system is working
    # make it better looking
    with st.spinner("Fetching recommendations for you....."):
        response = pipeline.recommend(query)# output is generated
        st.markdown("### Recommendations")
        st.write(response)


