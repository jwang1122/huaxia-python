import logging
log_format = '%(asctime)s %(levelname)s [%(name)s] - %(message)s::%(filename)s::%(lineno)d'
logging.basicConfig(filename='mylogs.log', filemode='w', level=logging.INFO, format=log_format)
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


def remove_course(course_id):
    logger.info("@JWANG: " + course_id)
    client = MongoClient('mongodb://localhost:27017')
    db = client['huaxia']
    courses = db.courses
    return courses.delete_one({'_id': course_id })


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/courses', methods=['GET', 'POST'])
def all_courses():
    response_object = {'status': 'success'}
    client = MongoClient('mongodb://localhost:27017')
    db = client['huaxia']
    courses = db.courses

    if request.method == 'POST':
        post_data = request.get_json()
        json = {
            '_id':uuid.uuid4().hex,
            'title': post_data.get('title'),
            'teacher': post_data.get('teacher'),
            'classroom': post_data.get('classroom'),
            'infolink': post_data.get('infolink'),
            'price': post_data.get('price'),           
        }
        response_object['message'] = addCourse(json)
    else:
        all_courses = courses.find()
        mycourses = []
        for c in all_courses:
            mycourses.append(c)
        response_object['courses'] = mycourses
    return jsonify(response_object)

def addCourse(course):
    client = MongoClient('mongodb://localhost:27017')
    db = client['huaxia']
    courses = db.courses
    result = courses.insert_one(course)
    if result.acknowledged:
        return 'course added!' + result.inserted_id

def findCourse(course_id):
    client = MongoClient('mongodb://localhost:27017')
    db = client['huaxia']
    courses = db.courses
    return courses.find_one({'_id':course_id})

def findUser(username):
    client = MongoClient('mongodb://localhost:27017')
    db = client['huaxia']
    users = db.users
    return users.find_one({'username':username})

@app.route('/users/<username>', methods=['GET'])
def getUser(username):
    response_object = {'status': 'success'}
    response_object['user'] = findUser(username)
    return jsonify(response_object)
    
@app.route('/courses/<course_id>', methods=['GET', 'PUT', 'DELETE'])
def single_course(course_id):
    logger.info("@JWANG: " + course_id);
    response_object = {'status': 'success'}
    if request.method == 'GET':
        response_object['course'] = findCourse(course_id)
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_course(course_id)
        course={
            '_id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'teacher': post_data.get('teacher'),
            'classroom': post_data.get('classroom'),
            'infolink': post_data.get('infolink'),
            'price': post_data.get('price'),
        }
        addCourse(course)
        response_object['message'] = 'course updated!'
    if request.method == 'DELETE':
        remove_course(course_id)
        response_object['message'] = 'course removed!'
    return jsonify(response_object)

@app.route('/charge', methods=['POST'])
def create_charge():
    post_data = request.get_json()
    logger.info("@JWANG: " + post_data.get('course')['price']);
    amount = round(float(post_data.get('course')['price']) * 100)
#    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
    stripe.api_key = STRIPE_SECRET_KEY
    charge = stripe.Charge.create(
        amount=amount,
        currency='usd',
        card=post_data.get('token'),
        description=post_data.get('course')['title'] + '/' + post_data.get('course')['teacher']
    )
    response_object = {
        'status': 'success',
        'charge': charge
    }
    return jsonify(response_object), 200

@app.route('/files/<filename>')
def readfile(filename):
    with open('../src/assets/' + filename + '.html') as f:
        text = f.read()

    response_object = {
        'status': 'success',
        'html': text
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