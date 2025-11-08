import requests
import os

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def search_movies(query):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": query,
        "language": "fr-FR"
    }
    response = requests.get(url, params=params)
    return response.json()
