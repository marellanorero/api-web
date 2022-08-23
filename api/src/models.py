from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User (db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    contacts = db.relationship('Contact', backref='user')

    def serialize(self):
        return {
            "id" : self.id,
            "username" : self.username,
            "contacts": self.get_contacts()
        }
    
    def get_contacts(self):
        return list(map(lambda contact: contact.serialize(), self.contacts))

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()