"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db , User, Dogfile , GeneralRecords
from flask_jwt_simple import (JWTManager, jwt_required, create_jwt, get_jwt_identity)


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)


# Setup the Flask-JWT-Simple extension
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)
# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)

def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/login', methods=['POST' , 'GET'])
def login():
    
    if request.method == 'POST':
        body = request.get_json()
        user = User.query.filter_by(email=body['email'], password=body['password']).first()

        if not user:
            return 'User not found', 404
        if not user.email:
            return jsonify({"msg": "Missing email parameter"}), 400
        if not user.password:
            return jsonify({"msg": "Missing password parameter"}), 400
        return jsonify({
                'token': create_jwt(identity=1),
                'id': user.id,
                'email': user.email,
                'firstName': user.firstName
              })
     # GET request
    if request.method == 'GET':
        all_users = User.query.all()
        all_users = list(map(lambda x: x.serialize(), all_users))
        return jsonify(all_users), 200

    return "Invalid Method", 404
   

@app.route('/new', methods=['POST'])
def new_user():
    if request.method == 'POST':
        body = request.get_json()

        db.session.add(User(
            firstName = body["firstName"],
            email = body["email"],
            password = body['password'],
            petname = body['petname']
            # date = body['date']
        ))
        
        db.session.commit()
        return jsonify({
            'msg': 'User Added!'
        })

@app.route('/delete', methods=['DELETE'])
def delete_user():
       # DELETE request
    if request.method == 'DELETE':
        user = User.query.get(user_id)
        if user is None:
            raise APIException('User not found', status_code=404)
        db.session.delete(user)
        db.session.commit()
        return "ok", 200

    return "Invalid Method", 404
   
# Protect a view with jwt_required, which requires a valid jwt
# to be present in the headers.
# @app.route('/protected', methods=['GET'])
# @jwt_required
# def protected():
#     # Access the identity of the current user with get_jwt_identity
#     return jsonify({'hello_from': get_jwt_identity()}), 200

@app.route('/dogfile', methods=['POST', 'GET', 'DELETE'])
def get_dogfile():

    if request.method == 'POST':
        body = request.get_json()

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if "petname" not in body:
            raise APIException('You need to specify the petname', status_code=400)
        if 'dob' not in body:
            raise APIException('You need to specify the dob', status_code=400)
        if 'imglink' not in body:
            body['imglink'] = None

        dog = Dogfile(petname=body['petname'], dob = body['dob'], imglink = body['imglink'])
        db.session.add(dog)
        db.session.commit()

        return "ok", 200
    
    # GET request
    if request.method == 'GET':
        all_dogs = Dogfile.query.all()
        all_dogs = list(map(lambda x: x.serialize(), all_dogs))
        return jsonify(all_dogs), 200

    return "Invalid Method", 404
       
       # DELETE request
    if request.method == 'DELETE':
        dog = Dogfile.query.get(DogFile_id)
        if record is None:
            raise APIException('Dogfile not found', status_code=404)
        db.session.delete(dog)
        db.session.commit()
        return "ok", 200

    return "Invalid Method", 404

@app.route('/records', methods=['POST', 'DELETE','GET'])
def get_records():

#Create a record and retrieve all records!!

    if request.method == 'POST':
        body = request.get_json()

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if "vet_name" not in body:
            raise APIException('You need to specify the vet name', status_code=400)
        if "groomer_name" not in body:
            raise APIException('You need to specify the groomer name', status_code=400)
        if 'petname' not in body:
            raise APIException('You need to specify the petname', status_code=400)
        if 'insurance_provider' not in body:
            body['insurance_provider'] = None
        if 'insurance_policy' not in body:
            body['insurance_policy'] = None
        if 'vet_address' not in body:
            body['vet_address'] = None
        if 'groomer_address' not in body:
            body['groomer_address'] = None

        record = GeneralRecords(vet_name=body['vet_name'], groomer_name=body['groomer_name'], vet_address=body['vet_address'], groomer_address=body['groomer_address'],insurance_policy = body['insurance_policy'], insurance_provider = body['insurance_provider'], petname = body['petname'])
        db.session.add(record)
        db.session.commit()

        return "ok", 200
    
    # GET request
    if request.method == 'GET':
        all_records = GeneralRecords.query.all()
        all_records = list(map(lambda x: x.serialize(), all_records))
        return jsonify(all_records), 200

    return "Invalid Method", 404

       # DELETE request
    if request.method == 'DELETE':
        record = GeneralRecords.query.get(GeneralRecords_id)
        if record is None:
            raise APIException('Record not found', status_code=404)
        db.session.delete(record)
        db.session.commit()
        return "ok", 200

    return "Invalid Method", 404


@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "hello": "oreo"
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
