import os
from fastapi import FastAPI
from pymongo import MongoClient

from api.routes.users_route import users_router

app = FastAPI()
app.include_router(users_router)

dbHost = os.environ.get('DB_HOST')
dbPort = os.environ.get('DB_PORT')
dbName = os.environ.get('DB_NAME')
CONNECTION_STRING = f"mongodb://{dbHost}:{dbPort}/{dbName}"

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)
print(client.server_info())

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI with MongoDB",
            "dbHost": dbHost,
            "dbPort": dbPort,
            "dbName": dbName}