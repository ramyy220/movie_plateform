from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity # type: ignore
from flask_cors import cross_origin # type: ignore
from models import db
from models.user import User

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/update', methods=['POST'])
@cross_origin(headers=['Content-Type', 'Authorization'])
@jwt_required()
def update_user():
    try: 
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No data provided.'}), 400
        
        user_id_str = get_jwt_identity()
        try:
            user_id = int(user_id_str)
        except ValueError:
            return jsonify({'message': 'Invalid user ID.'}), 400
        
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found.'}), 404
        
        new_username = data.get('username')
        new_password = data.get('password')
        
        if new_username and new_username != user.username:
            if User.query.filter_by(username = new_username).first():
                return jsonify({'message': 'Username already taken.'}), 409
            user.username = new_username
            
        if new_password:
            if len(new_password) < 8:
                return jsonify({'message': 'Password must be at least 8 characters.'}), 400
            user.set_password(new_password)
        
        db.session.commit()
        return jsonify({'message': 'User updated successfully.'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Internal server error.', 'error': str(e)}), 500