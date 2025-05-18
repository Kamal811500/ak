import streamlit as st
st.header('WELOCME TO streamlit ak app')
import pandas as pd
import numpy as np
df = pd.read_excel("movies.xlsx")
df = pd.read_csv("C:/Users/KAMAL/Documents/movies.csv") 
df = pd.read_csv("movies.csv")
print(df.columns)
def recommend_movies(movie_title, num_recommendations=5):
    if movie_title not in df['title'].values:
        return ["Movie not found! Try another title."]

    movie_idx = df[df['title'] == movie_title].index[0]
    similarity_scores = list(enumerate(cosine_sim[movie_idx]))
    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
    
    return [df.iloc[i[0]]["title"] for i in sorted_movies]
import streamlit as st

st.header('WELCOME TO Streamlit AK App')

movie_to_search = st.text_input("Enter a movie title:")
if movie_to_search:
    recommendations = recommend_movies(movie_to_search)
    st.write(f"Movies similar to '{movie_to_search}':")
    st.write(recommendations)
