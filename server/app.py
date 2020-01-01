import os
import uuid
import stripe

from flask import Flask, jsonify, request
from flask_cors import CORS


CLASSES = [
    {
        'id': uuid.uuid4().hex,
        'title': '中文一年级班',
        'teacher': '张老师',
        'classroom': '102',
        'price': '299.00'
    },
    {
        'id': uuid.uuid4().hex,
        'title': '中文二年级中班',
        'teacher': '李老师',
        'classroom': '211',
        'price': '399.00'      
    },
    {
        'id': uuid.uuid4().hex,
        'title': '中文三年级大班',
        'teacher': '王老师',
        'classroom': '206',
        'price': '499.00'

    }
]

# configuration
DEBUG = True
STRIPE_SECRET_KEY = 'sk_test_HV6gIlNhTCDxDKNxrZ0tz66H00oBk1QoX3'

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_class(class_id):
    for class0 in CLASSES:
        if class0['id'] == class_id:
            CLASSES.remove(class0)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/classes', methods=['GET', 'POST'])
def all_classes():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        CLASSES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('teacher'),
            'read': post_data.get('classroom'),
            'price': post_data.get('price'),
        })
        response_object['message'] = 'Class added!'
    else:
        response_object['classes'] = CLASSES
    return jsonify(response_object)


@app.route('/classes/<class_id>', methods=['GET', 'PUT', 'DELETE'])
def single_class(class_id):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        # TODO: refactor to a lambda and filter
        return_class = ''
        for class0 in CLASSES:
            if class0['id'] == class_id:
                return_class = class0
        response_object['class0'] = return_class
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_class(class_id)
        CLASSES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('teacher'),
            'read': post_data.get('classroom'),
            'price': post_data.get('price'),
        })
        response_object['message'] = 'Class updated!'
    if request.method == 'DELETE':
        remove_class(class_id)
        response_object['message'] = 'Class removed!'
    return jsonify(response_object)

@app.route('/charge', methods=['POST'])
def create_charge():
    post_data = request.get_json()
    amount = round(float(post_data.get('class')['price']) * 100)
#    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
    stripe.api_key = STRIPE_SECRET_KEY
    charge = stripe.Charge.create(
        amount=amount,
        currency='usd',
        card=post_data.get('token'),
        description=post_data.get('class')['title'] + '/' + post_data.get('class')['teacher']
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