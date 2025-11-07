from flask import Flask
from config import Config
from models import db
from models.user import User

print("🔧 Test de connexion à la base de données...")

app = Flask(__name__)
app.config.from_object(Config)

print(f"📊 DATABASE_URL: {app.config['SQLALCHEMY_DATABASE_URI']}")

db.init_app(app)

with app.app_context():
    try:
        # Supprime et recrée toutes les tables
        print("🗑️  Suppression des anciennes tables...")
        db.drop_all()
        
        print("🏗️  Création des tables...")
        db.create_all()
        
        print("✅ Tables créées avec succès !")
        
        # Teste une insertion
        print("\n👤 Test d'insertion d'un utilisateur...")
        test_user = User(username="testuser", email="test@example.com")
        test_user.set_password("password123")
        
        db.session.add(test_user)
        db.session.commit()
        
        print("✅ Utilisateur créé !")
        
        # Vérifie qu'on peut le récupérer
        user = User.query.filter_by(username="testuser").first()
        if user:
            print(f"✅ Utilisateur trouvé : {user.username} ({user.email})")
            print(f"✅ Mot de passe correct : {user.check_password('password123')}")
        else:
            print("❌ Utilisateur non trouvé")
            
    except Exception as e:
        print(f"❌ Erreur : {e}")
        import traceback
        traceback.print_exc()