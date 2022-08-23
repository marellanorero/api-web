from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required, create_access_token
from models import db

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = 'my-secret-key'
db.init_app(app)
Migrate(app, db)
CORS(app)
jwt = JWTManager(app)

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()