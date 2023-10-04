from googlesearch import search

import streamlit as st

"""
Created on Wed Sep 27 22:04:36 2023

@author: aribah
"""

def search_movies_by_genre(genre):
    # Construct the Google search query for books by genre
    query = f"movies in {genre} genre"
   
    # Create the Google search URL
    google_url = f"https://www.google.com/search?q={query}"
   
    # Open the default web browser and perform the Google search
    webbrowser.open_new_tab(google_url)
   

if __name__ == "__main__":
   
     st.title("Search Movies")
   
        # Input the genre of interest
     genre_of_interest = st.text_input('Enter the genre of movies you are interested')

    # genre_of_interest = input("Enter the genre of movies you are interested in: ")
     search_string = "movie genere " + genre_of_interest;
     results_1 = search(search_string, num_results=5)
     # Perform the Google search
     #search_movies_by_genre(genre_of_interest)
     for j in results_1:
         print (str(j))
         st.write(j)
