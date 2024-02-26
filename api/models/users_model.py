from pydantic import BaseModel, EmailStr
import json
# from fastapi import Form, File, UploadFile

class Users(BaseModel):
    # name = str
    # name_default = Form(..., description="Name of the user")
    # email = str
    # email_default = Form(..., description="Email of the user")
    # image = UploadFile
    # image_default = File(..., description="Image of the user")

    name:str
    email:str
    image:str

