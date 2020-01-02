import logging
log_format = '%(asctime)s %(levelname)s [%(name)s] - %(message)s::%(filename)s::%(lineno)d'
logging.basicConfig(filename='mylogs.log', filemode='w', level=logging.DEBUG, format=log_format)
logger = logging.getLogger('WANG')

import os
import uuid
import stripe

from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson.json_util import dumps
from bson.json_util import loads
from pprint import pprint

# configuration
DEBUG = True
STRIPE_SECRET_KEY = 'sk_test_HV6gIlNhTCDxDKNxrZ0tz66H00oBk1QoX3'

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_class(class_id):
    logger.info("@JWANG: " + class_id)
    client = MongoClient('mongodb://localhost:27017')
    db = client['huaxia']
    classes = db.classes
    return classes.delete_one({'_id': class_id })


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/classes', methods=['GET', 'POST'])
def all_classes():
    response_object = {'status': 'success'}
    client = MongoClient('mongodb://localhost:27017')
    db = client['huaxia']
    classes = db.classes

    if request.method == 'POST':
        post_data = request.get_json()
        json = {
            '_id':uuid.uuid4().hex,
            'title': post_data.get('title'),
            'teacher': post_data.get('teacher'),
            'classroom': post_data.get('classroom'),
            'price': post_data.get('price'),           
        }
        response_object['message'] = addClass(json)
    else:
        all_classes = classes.find()
        myclasses = []
        for c in all_classes:
            myclasses.append(c)
        response_object['classes'] = myclasses
    return jsonify(response_object)

def addClass(class0):
    client = MongoClient('mongodb://localhost:27017')
    db = client['huaxia']
    classes = db.classes
    result = classes.insert_one(class0)
    if result.acknowledged:
        return 'Class added!' + result.inserted_id

def findClass(class_id):
    client = MongoClient('mongodb://localhost:27017')
    db = client['huaxia']
    classes = db.classes
    return classes.find_one({'_id':class_id})

@app.route('/classes/<class_id>', methods=['GET', 'PUT', 'DELETE'])
def single_class(class_id):
    logger.info("@JWANG: " + class_id);
    response_object = {'status': 'success'}
    if request.method == 'GET':
        response_object['class0'] = findClass(class_id)
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_class(class_id)
        class0={
            '_id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'teacher': post_data.get('teacher'),
            'classroom': post_data.get('classroom'),
            'price': post_data.get('price'),
        }
        addClass(class0)
        response_object['message'] = 'Class updated!'
    if request.method == 'DELETE':
        remove_class(class_id)
        response_object['message'] = 'Class removed!'
    return jsonify(response_object)

@app.route('/charge', methods=['POST'])
def create_charge():
    post_data = request.get_json()
    logger.info("@JWANG: " + post_data.get('class0')['price']);
    amount = round(float(post_data.get('class0')['price']) * 100)
#    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
    stripe.api_key = STRIPE_SECRET_KEY
    charge = stripe.Charge.create(
        amount=amount,
        currency='usd',
        card=post_data.get('token'),
        description=post_data.get('class0')['title'] + '/' + post_data.get('class0')['teacher']
    )
    response_object = {
        'status': 'success',
        'charge': charge
    }
    return jsonify(response_object), 200

@app.route('/charge/<charge_id>')
def get_charge(charge_id):
    stripe.api_key = STRIPE_SECRET_KEY
    response_object = {
        'status': 'success',
        'charge': stripe.Charge.retrieve(charge_id)
    }
    return jsonify(response_object), 200

if __name__ == '__main__':
    app.run()