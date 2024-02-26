import os
import uuid
from fastapi import APIRouter, File, UploadFile, Form, Depends, Body

from api.models.users_model import Users
from api.schemas.users_schema import individual_user, list_user
from api.configs.db import users_collection
from bson.objectid import ObjectId

users_router = APIRouter(prefix="/users", tags=["users"])

IMAGEDIR = "data/users_img"

# GET Method to get all users
@users_router.get("/")
async def get_users():
    users = users_collection.find()
    return list_user(users)

# POST Method to add a user
@users_router.post("/")
async def add_users(name: str = Form(...), email: str = Form(...), upload_img: UploadFile = File(..., description="Image of the user", media_type="image/jpeg")):
    # check IMAGEDIR exists
    if not os.path.exists(IMAGEDIR):
        os.makedirs(IMAGEDIR)
    # print image name
    img_name = f"{uuid.uuid4()}.jpg"
    img_path = f"{IMAGEDIR}/{img_name}"
    content = await upload_img.read()
    with open(img_path, "wb") as f:
        f.write(content)
    name_user = name
    email_user = email
    image_user = img_path

    user = {
        "name": name_user,
        "email": email_user,
        "image": image_user
    }
    users_collection.insert_one(user)

    return {"message": "Added successfully"}

# PUT Method to update a user
@users_router.put("/{id}")
async def update_users(id: str, name: str = Form(...), email: str = Form(...), upload_img: UploadFile = File(..., description="Image of the user", media_type="image/jpeg")):
    if upload_img:
        # remove old image
        user = users_collection.find_one({"_id": ObjectId(id)})
        img_path = user["image"]
        os.remove(img_path)
        # add new image
        img_name = f"{uuid.uuid4()}.jpg"
        img_path = f"{IMAGEDIR}/{img_name}"
        content = await upload_img.read()
        with open(img_path, "wb") as f:
            f.write(content)
        name_user = name
        email_user = email
        image_user = img_path
    else:
        name_user = name
        email_user = email
        user = users_collection.find_one({"_id": ObjectId(id)})
        img_path = user["image"]
    
    users_collection.update_one({"_id": ObjectId(id)}, {"$set": {"name": name_user, "email": email_user, "image": image_user}})

    return {"message": "Updated successfully"}

# DELETE Method to delete a user
@users_router.delete("/{id}")
async def delete_users(id: str):
    # remove image
    user = users_collection.find_one({"_id": ObjectId(id)})
    img_path = user["image"]
    os.remove(img_path)
    users_collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Deleted successfully"}
