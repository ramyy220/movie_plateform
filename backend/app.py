from flask import Flask
from flask_cors import CORS  # type: ignore
from flask_jwt_extended import JWTManager # type: ignore
from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialiser les extensions
    db.init_app(app)
    CORS(app)
    JWTManager(app) 
    
    # Importer et enregistrer les blueprints
    from routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    
    # Créer les tables
    with app.app_context():
        db.create_all()
        print("✅ Base de données initialisée !")
    
    # Route de test
    @app.route('/')
    def home():
        return {'message': '🎬 Movie Platform API is running!'}
    
    @app.route('/health')
    def health():
        return {'status': 'healthy', 'database': 'connected'}
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)