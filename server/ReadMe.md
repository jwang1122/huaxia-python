# Stripe Python Server

## Back to main document
[Master ReadMe.md](../ReadMe.md)


## Start python stripe server
```
cd server
source env/bin/activate
python app.py
```
[Open browser, check server](http://localhost:5000/ping)

## Setup Python Server
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
pip install stripe
pip install pymongo
```
where in requirements.txt includes all necessary modules, such as pymongo...

## Database maintenance tool
1. user.py; maintain huaxia.users collection
2. course.py; maintain huaxia.classes collection

## Integration tests
[Check server startup](http://localhost:5000/ping)
[get all courses](http://localhost:5000/courses)
[Find user by name: wei](http://localhost:5000/users/wei)
[Insert one course]
[Delete one course]
[Modify one course]