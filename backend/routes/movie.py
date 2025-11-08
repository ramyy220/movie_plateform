from flask import Blueprint, request, jsonify
from services.tmdb_service import search_movies

movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/search', methods=['GET'])
def search():
    """ search movies"""
    query = request.args.get('query')
    if not query:
        return jsonify({'message': 'Query parameter is required.'}), 400
    
    results = search_movies(query)
    return jsonify(results), 200