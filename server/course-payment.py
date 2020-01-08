from pymongo import MongoClient
import uuid
from pprint import pprint

client = MongoClient('mongodb://localhost:27017')
db = client['huaxia']
course_payments = db.course_payments

charge = {
    '_id':uuid.uuid4().hex,
    'courseId':'02cede6d0b404dfe82b869f83f39131b',
    'studentId':'bbd82fefe11040a396fe1964e86cb29d',
    'chanrgeId':'password',
}

def create():
    result = course_payments.insert_one(charge)
    if result.acknowledged:
        print("charge Added. The charge Id is", result.inserted_id)



def createMulti():
    results = users.insert_many(user_array)
    for id in results.inserted_ids:
        print("Course Added. The course Id is", str(id))

if(__name__ == '__main__'):
    create()

    
