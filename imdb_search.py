import streamlit as st
import imdb

imbdSearch = imdb.IMDb()


if __name__ == "__main__":

    st.title("Search Movies")
   
    # Input the genre of interest
    genre_of_interest = st.text_input('Enter the genre of movies you are interested')
    #genre_of_interest = input("Enter the genre of movies you are interested in: ")
    #results_1 = search(search_string, num_results=5)
    results_1 = imbdSearch.search_movie(genre_of_interest)
   
     #search_movies_by_genre(genre_of_interest)
    for j in results_1:
         print (str(j))
         image_url = j.data.get('cover url')
         print(j.data.get('title'))
         print(image_url)
         st.write(j)
         if image_url is not None:
            st.image(image_url, width=100)
