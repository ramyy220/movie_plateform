from flask import Blueprint, request, jsonify
from models.favorites import Favorites

favorites_bp = Blueprint('favorites', __name__)

@favorites_bp.route('/favorites', methods=['GET'])
def get_user_favorites():
    """Get a list of favorite movies for the authenticated user."""
    user_id = request.args.get('user_id')
    user_favorites = Favorites.query.filter_by(user_id=user_id).all()
    return jsonify([fav.serialize() for fav in user_favorites]), 200


