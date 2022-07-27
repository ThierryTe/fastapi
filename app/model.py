from email.policy import default
from pydantic import BaseModel,Field,EmailStr


class PostSchema(BaseModel):
    id:int = Field(default=None)
    title:str =Field(default=None)
    content:str=Field(default=None)

    class config:
        schema_extra ={
            "post_demo":{
                "title": "Titre a propos d'annimaux",
                "content": "Description a propos d'annimaux"
            }
        }
class UserSchema(BaseModel):
    fullname:str = Field(default=None)
    email:EmailStr = Field(default=None)
    password:str = Field(default=None)
    
    class config:
        the_schema ={
            "user_demo":{
                "fullname":"Tewende",
                "email":"kimatewende@gmail.com",
                "password":"12345"
            }

        }
        
class UserLoginSchema(BaseModel):
    email:EmailStr = Field(default=None)
    password:str = Field(default=None)
    
    class config:
        the_schema ={
            "user_login_demo":{
                "email":"kimatewende@gmail.com",
                "password":"12345"
            }

        }