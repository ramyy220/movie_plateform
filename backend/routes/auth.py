from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity  # type: ignore
from flask_cors import cross_origin  # type: ignore
from models import db
from models.user import User
from datetime import timedelta

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    """Register a new user."""
    try:
        data = request.get_json()

        if (
            not data
            or not data.get("username")
            or not data.get("password")
            or not data.get("email")
        ):
            return (
                jsonify({"message": "Username, email and password are required."}),
                400,
            )

        if User.query.filter_by(email=data["email"]).first():
            return jsonify({"message": "User already exists."}), 409

        if User.query.filter_by(username=data["username"]).first():
            return jsonify({"message": "Username already taken."}), 409

        user = User(
            username=data["username"],
            email=data["email"],
        )
        user.set_password(data["password"])

        db.session.add(user)
        db.session.commit()

        access_token = create_access_token(
            identity=str(user.id), expires_delta=timedelta(days=1)
        )

        return (
            jsonify(
                {
                    "message": "User registered successfully.",
                    "user": user.to_dict(),
                    "access_token": access_token,
                }
            ),
            201,
        )

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Internal server error.", "error": str(e)}), 500


@auth_bp.route("/login", methods=["POST"])
def login():
    """Configure user login."""
    try:
        data = request.get_json()

        if not data or not data.get("email") or not data.get("password"):
            return jsonify({"message": "Email and password are required."}), 400

        user = User.query.filter_by(email=data["email"]).first()

        if not user or not user.check_password(data["password"]):
            return jsonify({"message": "Invalid email or password."}), 401

        access_token = create_access_token(
            identity=str(user.id), expires_delta=timedelta(days=1)
        )

        return (
            jsonify(
                {
                    "message": "Login successful.",
                    "user": user.to_dict(),
                    "access_token": access_token,
                }
            ),
            200,
        )
    except Exception as e:
        return jsonify({"message": "Internal server error.", "error": str(e)}), 500


@auth_bp.route("/me", methods=["GET"])
@cross_origin(headers=["Content-Type", "Authorization"])
@jwt_required()
def get_current_user():
    """Get the currently logged-in user."""
    try:
        user_id_str = get_jwt_identity()
        try:
            user_id = int(user_id_str)
        except (TypeError, ValueError):
            return jsonify({"message": "Invalid token subject."}), 400

        user = User.query.get(user_id)

        if not user:
            return jsonify({"message": "User not found."}), 404

        return jsonify({"user": user.to_dict()}), 200
    except Exception as e:
        return jsonify({"message": "Internal server error.", "error": str(e)}), 500


@auth_bp.route("/logout", methods=["POST"])
@cross_origin(headers=["Content-Type", "Authorization"])
@jwt_required()
def logout():
    """User logout (handled client-side by discarding the token)."""
    return (
        jsonify(
            {
                "message": "Logout successful. Please discard the token on the client side."
            }
        ),
        200,
    )


@auth_bp.route("/verify-password", methods=["POST"])
@cross_origin(headers=["Content-Type", "Authorization"])
@jwt_required()
def verify_password():
    try:
        data = request.get_json()
        if not data or not data.get("password"):
            return jsonify({"message": "Password is requerid."}), 400

        user_id_str = get_jwt_identity()
        try:
            user_id = int(user_id_str)
        except (TypeError, ValueError):
            return jsonify({"message": "Invalid token subject."}), 400

        user = User.query.get(user_id)
        if not user or not user.check_password(data["password"]):
            return jsonify({"message": "Invalid password."}), 401
        return jsonify({"message": "Password verified successfully."}), 200
    except Exception as e:
        return jsonify({"message": "Internal server error.", "error": str(e)}), 500
