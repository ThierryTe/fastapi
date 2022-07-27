import uvicorn;
from fastapi import FastAPI,Body,Depends
from app.model import PostSchema, UserSchema,UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer
posts = [
    {
    "id": 1,
    "title": "Pingouin",
    "content":"Les pigouins sont des oiseaux aquatique"
  },
     {
    "id": 2,
    "title": "Panthère",
    "content":"Les pigouins sont des oiseaux aquatique"
  },
     {
    "id": 3,
    "title": "Giraffe",
    "content":"Les pigouins sont des oiseaux aquatique"
  }

]
users=[]

app = FastAPI()

#1 Get pour le test
@app.get("/", tags=["test"])
def greet():
    return {"Bonjoir":"le monde"}
#2 liste des postes
@app.get("/posts", tags=["posts"])
def get_posts():
    return {"data":posts}

#3 obtenir un post {id}
@app.get("/posts/{id}",tags=["posts"])
def get_one_post(id:int):
    if id > len(posts):
        return {
            "erreur":"Il n'existe pas de post avec cet id"
        }
    for post in posts:
        if post["id"]==id:
            return {
                "data":post
            }

#4 création de post
@app.post("/post", dependencies=[Depends(jwtBearer())], tags=["posts"])
def add_post(post:PostSchema):
    post.id=len(posts)+1
    posts.append(post.dict())
    return{
        "info": "Post crée avec succès"
    }

#5 Inscription d'un utilisateur
@app.post("/user/signup", tags=["user"])
def user_signup(user:UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data:UserLoginSchema):
    for user in users:
        if user.email ==data.email and user.password==data.password:
            return True
        return False

#6 Login
@app.post("/user/login", tags=["user"])
def user_login(user:UserLoginSchema =Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "Erreur": "Email ou mot de passe incorrect !"
        }
