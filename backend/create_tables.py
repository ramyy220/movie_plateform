#!/usr/bin/env python3
from app import create_app
from models import db

# Adapter ces imports si tes fichiers s'appellent autrement
try:
    # essais courants : models/user.py et models/favorite.py
    from models.user import User  # noqa: F401
    from models.favorites import Favorites  # noqa: F401
except Exception:
    try:
        # alternativement models/favorites.py ou models/users.py selon ton repo
        from models.favorites import Favorites  # noqa: F401
        from models.user import User  # noqa: F401
    except Exception:
        # si import échoue on affiche une erreur claire
        import traceback
        traceback.print_exc()

app = create_app()
with app.app_context():
    db.create_all()
    print("✅ create_all() exécuté. Metadonnées des tables enregistrées :", sorted(list(db.metadata.tables.keys())))