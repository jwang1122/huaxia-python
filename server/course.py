import uuid
from pymongo import MongoClient
from pprint import pprint
from bson.json_util import dumps

client = MongoClient("mongodb://localhost:27017")
db = client["huaxia"]
classes = db.classes

class0 = {'_id':uuid.uuid4().hex,"title": "课程名称", "teacher": "Johnson", "classroom": "201", "price": 499.99}

#result = students.insert_one(student)
#if result.acknowledged:
#    print("Course Added. The student Id is", result.inserted_id)

group1 = [
    {'_id':uuid.uuid4().hex,"title": "课程名称", "teacher": "Johnson", "classroom": "201", "price": 499.99},
    {'_id':uuid.uuid4().hex,"title": "课程名称", "teacher": "Johnson", "classroom": "201", "price": 499.99},
    {'_id':uuid.uuid4().hex,"title": "课程名称", "teacher": "Johnson", "classroom": "201", "price": 499.99}，
    {'_id':uuid.uuid4().hex,"title": "课程名称", "teacher": "Johnson", "classroom": "201", "price": 499.99},
    {'_id':uuid.uuid4().hex,"title": "课程名称", "teacher": "Johnson", "classroom": "201", "price": 499.99}，
]

#results = students.insert_many(group1)
#for id in results.inserted_ids:
#    print("Student is Added. The Id is", str(id))

#classes.delete_one({'_id':'4359008a994544cc87f379c4508637b7'})

#classes = classes.find({
#    'teacher':'习近平‘
#});
#for s in classes:
#    pprint(s)

#classes = classes.find().sort([('price', 1)])
#for s in classes:
#    pprint(s)
#print(group1)

#classes = db.classes.find()
#for c in classes:
#    pprint(c)