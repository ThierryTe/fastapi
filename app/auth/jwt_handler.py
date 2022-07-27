#Ce fichier est responsable de l'authentification, l'encodage ,le decodage et le renvoi du JWT 

import time
import jwt
from decouple import config

JWT_SECRET= config("secret")
JWT_ALGORITHM = config("algorithm")

#Fonction qui retourne le token généré
def token_response(token:str):
    return{
        "acces token":token
    }
#Fonction d'authentification du JWT
def signJWT(userID:str):
    payload = {
        "userID" : userID,
        "expiry" : time.time() + 600
 
    }
    token = jwt.encode(payload,JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)
def decodeJWT(token:str):
    try:
        decode_token=jwt.decode(token,JWT_SECRET,algorithm=JWT_ALGORITHM)
        return decode_token if decode_token ['expires'] >=time.time()else None
    except:
        return {}