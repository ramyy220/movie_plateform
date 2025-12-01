import requests
import os

TMDB_API_KEY = os.getenv("TMDB_API_KEY")


def search_movies(query):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": query, "language": "fr-FR"}
    response = requests.get(url, params=params)
    return response.json()


def get_movie_discover(page: int = 1):
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {"api_key": TMDB_API_KEY, "language": "fr-FR", "page": page}
    response = requests.get(url, params=params)
    return response.json()


def get_movie_now_playing(page: int = 1):
    url = "https://api.themoviedb.org/3/movie/now_playing"
    params = {"api_key": TMDB_API_KEY, "language": "fr-FR", "page": page}
    response = requests.get(url, params=params)
    return response.json()


def get_movie_popular(page: int = 1):
    url = "https://api.themoviedb.org/3/movie/popular"
    params = {"api_key": TMDB_API_KEY, "language": "fr-FR", "page": page}
    response = requests.get(url, params=params)
    return response.json()


def get_movie_rated(page: int = 1):
    url = "https://api.themoviedb.org/3/movie/top_rated"
    params = {"api_key": TMDB_API_KEY, "language": "fr-FR", "page": page}
    response = requests.get(url, params=params)
    return response.json()


def get_movie_upcoming(page: int = 1):
    url = "https://api.themoviedb.org/3/movie/upcoming"
    params = {"api_key": TMDB_API_KEY, "language": "fr-FR", "page": page}
    response = requests.get(url, params=params)
    return response.json()
