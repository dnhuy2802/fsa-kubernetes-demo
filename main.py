import os
from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.staticfiles import StaticFiles

from api.routes.users_route import users_router

app = FastAPI()
app.mount("/data", StaticFiles(directory="data"), name="data")
app.include_router(users_router)

dbHost = os.environ.get('DB_HOST')
dbPort = os.environ.get('DB_PORT')
dbName = os.environ.get('DB_NAME')
appPort = os.environ.get('PORT')
appPublicPort = os.environ.get('PUBLIC_PORT')
print(dbHost, dbPort, dbName, appPort, appPublicPort)

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI with MongoDB",
            "dbHost": dbHost,
            "dbPort": dbPort,
            "dbName": dbName,
            "appPort": appPort,
            "appPublicPort": appPublicPort}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=int(appPort))
