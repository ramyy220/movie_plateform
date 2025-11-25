from models import db

class Favorites(db.Model):
    __tablename__= 'favorites'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    movie_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    poster_path = db.Column(db.String(255))
    
    def __repr__(self):
        return f'<Favorites {self.title} for User {self.user_id}>'
    
    def to_dict(self):
        """Convertit le favori en dictionnaire"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'movie_id': self.movie_id,
            'title': self.title,
            'poster_path': self.poster_path
        }
        
    def serialize(self):
        return self.to_dict()