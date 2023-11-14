
import motor.motor_asyncio
from model import Todo
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
import os

MONGODB_URI = os.environ.get("MONGODB_URI")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
database = client.TodoList
collection = database['todo']

# try:
#     client.admin.command('ping')
#     print('pinged successfully')
# except Exception as e:
#     print(e)s


async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo(title, desc):
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document

async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True
