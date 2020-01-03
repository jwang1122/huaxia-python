import uuid
from pymongo import MongoClient
from pprint import pprint
from bson.json_util import dumps

client = MongoClient("mongodb://localhost:27017")
db = client["huaxia"]
courses = db.courses

course = {'_id':uuid.uuid4().hex,"title": "课程名称", "teacher": "Johnson", "classroom": "201", "price": 499.99}

#result = courses.insert_one(course)
#if result.acknowledged:
#    print("Course Added. The student Id is", result.inserted_id)

group1 = [
    {'_id':uuid.uuid4().hex,"title": "CSL 幼儿中文", "teacher": "邹元元", "classroom": "201", "infolink":"grade1-3","price": 399.99},
    {'_id':uuid.uuid4().hex,"title": "汉语拼音", "teacher": "康红", "classroom": "202", "infolink":"grade1-3","price": 499.99},
    {'_id':uuid.uuid4().hex,"title": "汉语拼音（新生班）", "teacher": "康红", "classroom": "202", "infolink":"grade1-3","price": 499.99}，
    {'_id':uuid.uuid4().hex,"title": "中文一年级", "teacher": "刘俐俐", "classroom": "203", "infolink":"grade1-3","price": 499.99},
    {'_id':uuid.uuid4().hex,"title": "中文二年级", "teacher": "张怡", "classroom": "105", "infolink":"grade1-3","price": 399.99}，
]

results = courses.insert_many(group1)
for id in results.inserted_ids:
    print("Student is Added. The Id is", str(id))

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