from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity # type: ignore
from models import db
from models.favorites import Favorites

favorites_bp = Blueprint('favorites', __name__)

@favorites_bp.route('/favorites', methods=['GET'])
@jwt_required()
def get_user_favorites():
    """Get a list of favorite movies for the authenticated user."""
    user_id_str = get_jwt_identity()
    try: 
        user_id = int(user_id_str)
    except (TypeError, ValueError):
        return jsonify({"msg": "Invalid user ID"}), 400
    
    user_favorites = Favorites.query.filter_by(user_id=user_id).all()
    return jsonify([fav.to_dict() for fav in user_favorites]), 200


@favorites_bp.route('/favorites', methods=['POST'])
@jwt_required()
def add_favorite():
    data = request.get_json() or {}
    movie_id = data.get('movie_id')
    if movie_id is None: 
        return jsonify({"msg": "movie_id is required"}), 400
    
    user_id = int(get_jwt_identity())
    
    existing = Favorites.query.filter_by(user_id=user_id, movie_id=movie_id).first()
    if existing:
        return jsonify({"msg": "Movie already in favorites"}), 400
    
    fav = Favorites(
        user_id=user_id,
        movie_id=movie_id,
        title=data.get('title'),
        poster_path=data.get('poster_path')
    )
    
    db.session.add(fav)
    db.session.commit()
    return jsonify(fav.to_dict()), 201

@favorites_bp.route('/favorites/<int:movie_id>', methods=['DELETE'])
@jwt_required()
def remove_favorite(movie_id):
    user_id = int(get_jwt_identity())
    
    fav = Favorites.query.filter_by(user_id=user_id, movie_id=movie_id).first()
    if not fav:
        return jsonify({"msg": "Favorite not found"}), 404
    
    db.session.delete(fav)
    db.session.commit()
    return jsonify({"msg": "Favorite removed"}), 200
    

