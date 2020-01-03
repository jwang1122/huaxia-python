from pymongo import MongoClient
import uuid
from pprint import pprint

client = MongoClient('mongodb://localhost:27017')
db = client['huaxia']
introductions = db.introductions

intruduction = {
    '_id':uuid.uuid4().hex,
    'html':'<h1>课程（每年一级)</h1>

<h2>课程描述：<h2>
<p>
这个为期三年的课程是我们中文语言的初级课程。本课程的目的是让学生在中国语文（普通话）上，建立听，说，读，写的良好基础，并让学生初步了解中国文化。学生将学习汉语拼音，汉字部首和笔划，建立中文词汇，不断加强学生的中文阅读能力，介绍不同的中文句子结构和语法。在这三年的课程后，学生将能够使用中文交流，能阅读简单的中文文章，掌握300-500个汉字或短语。
</p>
<h2>课程和资源：</h2>
<p> 
《中文》1,2,3：由暨南大学中国语言文化学院出版，共9本书，包括3本教科书，6本练习册（A册和B册），修订版中华人民共和国国务院，1999年
</p>',
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
    create()
#    createMulti()
#    findUsername("wei")
    
