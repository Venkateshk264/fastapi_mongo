from fastapi import APIRouter

from models.user import User
from config.db import conn,collection
# from schemas.user import userEntity,usersEntity
from schemas.user import serializeDict,serializeList
from bson import ObjectId

user = APIRouter()

@user.get('/')

async def find_all():
    # print(conn.local.user.find())
    return serializeList(conn.sample_database.students.find())

@user.post('/studentdata')

async def create_students(user:User):
    name = user.name
    email = user.email
    password = user.password
    collection.insert_one({"name":name,"email":email,"password":password})
    return "successfull"


@user.get('/single_student/{id}')

async def find_one(id):
    # print(conn.local.user.find())
    # return userEntity(conn.sample_database.students.find_one(({"_id":ObjectId(id)})))
    return serializeDict(collection.find_one({"_id":ObjectId(id)}))


@user.put('/update_data/{id}')

async def update_student(id,user:User):

    collection.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})
    return serializeDict(conn.sample_database.students.find_one(({"_id":ObjectId(id)})))


@user.delete('/delete_data/{id}')

async def delete_student(id):

    # return collection.find_one_and_delete({"_id":ObjectId(id)})
     return serializeDict(conn.sample_database.students.find_one_and_delete({"_id":ObjectId(id)}))





@user.get('/student/{name}')
async def find_by_name(name):
    query = {"name":{"$regex":name, "$options":"i"}}
    return serializeList(collection.find(query))