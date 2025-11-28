from .auth import auth_bp
from .movie import movies_bp
from .favorites import favorites_bp

__all__ = ["auth_bp", "movies_bp", "favorites_bp", "user_bp"]