from flask_sqlalchemy import SQLAlchemy  # type: ignore

db = SQLAlchemy()

from .user import User  # noqa: E402
from .favorites import Favorites  # noqa: E402

__all__ = ['db', 'User', 'Favorites']