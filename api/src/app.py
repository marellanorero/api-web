from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required, create_access_token
from models import db, User, Contact

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'dialect+driver://user:pass@host:port/database'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgre@localhost:5432/postgres'
app.config['JWT_SECRET_KEY'] = 'my-secret-key'
db.init_app(app)
Migrate(app, db)
CORS(app)
jwt = JWTManager(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/users', methods=['GET'])
@app.route('/api/users/<int:id>', methods=['GET'])
def users(id = None):
    if request.method == 'GET':
        if id is not None:
            user = User.query.get(id)
            if not user: return jsonify({"msg":"User not found"}), 404
            return jsonify(user.serialize()), 200
        else:
            users = User.query.all()
            users = list(map(lambda user: user.serialize(), users))

            return jsonify(users), 200


@app.route('/api/contacts', methods=['GET', 'POST'])
@app.route('/api/contacts/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def contacts(id = None):
    if request.method == 'GET':
        if id is not None:
            contact = Contact.query.get(id)
            if not contact: return jsonify({"msg":"Contact not found"}), 404
            return jsonify(contact.serialize()), 200
        else:
            contacts = Contact.query.order_by("id").all()
            contacts = list(map(lambda contact: contact.serialize(), contacts))

            return jsonify(contacts), 200

    if request.method == 'POST':
        name = request.json.get("name")
        phone=request.json.get("phone")
        email=request.json.get("email", "")
        user_id = request.json.get("user_id")

        if not name: return jsonify({"msg":"Name is required!!"}), 400
        if not phone: return jsonify({"msg":"Phone is required!!"}), 400
        if not user_id: return jsonify({"msg":"User is required!!"}), 400
       
        contact = Contact()
        contact.name = name
        contact.phone = phone
        contact.user_id = user_id
        contact.email=email
        contact.save()

        return jsonify(contact.serialize()), 201

    if request.method == 'PUT':
        name = request.json.get("name")
        phone=request.json.get("phone")
        email=request.json.get("email", "")

        if not name: return jsonify({"msg":"Name is required!!"}), 400
        if not phone: return jsonify({"msg":"Phone is required!!"}), 400
       
        contact = Contact.query.get(id)
        if not contact: return jsonify({"msg":"Contact not found"}), 404

        contact.name = name
        contact.phone = phone
        contact.email=email
        contact.update()

        return jsonify(contact.serialize()), 200

    if request.method == 'DELETE':
        contact = Contact.query.get(id)
        if not contact: return jsonify({"msg":"Contact not found"}), 404

        contact.delete()

        return jsonify({"msg":"success, user was deleted"}), 200
        

if __name__ == '__main__':
    app.run()