from app import create_app
from models import db
from sqlalchemy import inspect, text

app = create_app()
with app.app_context():
    print(f"🔍 URI de la base : {app.config['SQLALCHEMY_DATABASE_URI']}")
    print(f"🔍 Engine : {db.engine.url}")
    
    # Tester la connexion
    try:
        with db.engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            print(f"✅ Connexion réussie !")
            print(f"📌 Version PostgreSQL : {version}")
            
            # Vérifier les tables
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"📊 Tables trouvées : {tables}")
            
            # Compter les enregistrements
            for table in tables:
                result = conn.execute(text(f"SELECT COUNT(*) FROM {table}"))
                count = result.fetchone()[0]
                print(f"   - {table}: {count} enregistrements")
                
    except Exception as e:
        print(f"❌ Erreur de connexion : {e}")