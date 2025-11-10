from flask import Blueprint, request, jsonify
from services.tmdb_service import (
    get_movie_popular,
    get_movie_rated,
    get_movie_upcoming,
    search_movies,
    get_movie_discover,
    get_movie_now_playing,
)

movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/search', methods=['GET'])
def search():
    """ search movies"""
    query = request.args.get('query')
    if not query:
        return jsonify({'message': 'Query parameter is required.'}), 400
    
    results = search_movies(query)
    if isinstance(results, dict) and results.get("error"):
        return jsonify({'message': results.get("error"), 'details': results.get("details")}), 500
    return jsonify(results), 200

@movies_bp.route('/discover', methods=['GET'])
def discover_movies():
    try:
        count = int(request.args.get('count', 20))
    except ValueError:
        count = 20
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    tmdb_data = get_movie_discover(page=page)
    if isinstance(tmdb_data, dict) and tmdb_data.get("error"):
        return jsonify({'message': tmdb_data.get("error"), 'details': tmdb_data.get("details")}), 500

    results = tmdb_data.get('results', [])
    sliced = results[:max(0, count)]
    response = {
        "results": sliced,
        "page": tmdb_data.get("page", page),
        "total_pages": tmdb_data.get("total_pages", 1),
        "total_results": tmdb_data.get("total_results", len(results))
    }
    return jsonify(response), 200

@movies_bp.route('/movie/now_playing', methods=['GET'])
def now_playing_movies():
    ''' now playing movies'''
    try:
        count = int(request.args.get('count', 20))
    except ValueError:
        count = 20
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    tmdb_data = get_movie_now_playing(page=page)
    if isinstance(tmdb_data, dict) and tmdb_data.get("error"):
        return jsonify({'message': tmdb_data.get("error"), 'details': tmdb_data.get("details")}), 500

    results = tmdb_data.get('results', [])
    sliced = results[:max(0, count)]
    response = {
        "results": sliced,
        "page": tmdb_data.get("page", page),
        "total_pages": tmdb_data.get("total_pages", 1),
        "total_results": tmdb_data.get("total_results", len(results))
    }
    return jsonify(response), 200

@movies_bp.route('/movie/popular', methods=['GET'])
def popular_movies():
    ''' popular movies'''
    try:
        count = int(request.args.get('count', 20))
    except ValueError:
        count = 20
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    tmdb_data = get_movie_popular(page=page)
    if isinstance(tmdb_data, dict) and tmdb_data.get("error"):
        return jsonify({'message': tmdb_data.get("error"), 'details': tmdb_data.get("details")}), 500

    results = tmdb_data.get('results', [])
    sliced = results[:max(0, count)]
    response = {
        "results": sliced,
        "page": tmdb_data.get("page", page),
        "total_pages": tmdb_data.get("total_pages", 1),
        "total_results": tmdb_data.get("total_results", len(results))
    }
    return jsonify(response), 200

@movies_bp.route('/movie/top_rated', methods=['GET'])
def rated_movies():
    ''' top rated movies'''
    try:
        count = int(request.args.get('count', 20))
    except ValueError:
        count = 20
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    tmdb_data = get_movie_rated(page=page)
    if isinstance(tmdb_data, dict) and tmdb_data.get("error"):
        return jsonify({'message': tmdb_data.get("error"), 'details': tmdb_data.get("details")}), 500

    results = tmdb_data.get('results', [])
    sliced = results[:max(0, count)]
    response = {
        "results": sliced,
        "page": tmdb_data.get("page", page),
        "total_pages": tmdb_data.get("total_pages", 1),
        "total_results": tmdb_data.get("total_results", len(results))
    }
    return jsonify(response), 200

@movies_bp.route('/movie/upcoming', methods=['GET'])
def upcoming_movies():
    ''' upcoming movies'''
    try:
        count = int(request.args.get('count', 20))
    except ValueError:
        count = 20
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    tmdb_data = get_movie_upcoming(page=page)
    if isinstance(tmdb_data, dict) and tmdb_data.get("error"):
        return jsonify({'message': tmdb_data.get("error"), 'details': tmdb_data.get("details")}), 500

    results = tmdb_data.get('results', [])
    sliced = results[:max(0, count)]
    response = {
        "results": sliced,
        "page": tmdb_data.get("page", page),
        "total_pages": tmdb_data.get("total_pages", 1),
        "total_results": tmdb_data.get("total_results", len(results))
    }
    return jsonify(response), 200
