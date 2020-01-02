from pymongo import MongoClient
import uuid
from pprint import pprint

client = MongoClient('mongodb://localhost:27017')
db = client['huaxia']
users = db.users

user = {
    '_id':uuid.uuid4().hex,
    'username':'jwang',
    'email':'jwang1122@gmail.com',
    'password':'password',
    'rule':'admin',
    'applications':"['/classes']"
}

def create():
    result = users.insert_one(user)
    if result.acknowledged:
        print("User Added. The user Id is", result.inserted_id)

def findUsername(username):
    result = users.find_one({'username':username})
    pprint(result)

user_array = [
    {
        '_id':uuid.uuid4().hex,
        'username':'jwang',
        'email':'jwang1122@gmail.com',
        'password':'password',
        'rule':'admin',
        'applications':['/classes']
    },
    {
        '_id':uuid.uuid4().hex,
        'username':'wei',
        'email':'wei@gmail.com',
        'password':'password',
        'rule':'parent',
        'applications':['/classes']
    },
    {
        '_id':uuid.uuid4().hex,
        'username':'jun',
        'email':'jun@gmail.com',
        'password':'password',
        'rule':'teacher',
        'applications':['/classes']
    },
]

def createMulti():
    results = users.insert_many(user_array)
    for id in results.inserted_ids:
        print("Course Added. The course Id is", str(id))

if(__name__ == '__main__'):
#    create()
#    createMulti()
    findUsername("wei")
    
