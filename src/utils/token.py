from flask import abort
import jwt
from datetime import datetime, timedelta
import os
def encode(data):
    payload = {
        "data" : data,
        "exp" : datetime.utcnow() +  timedelta(days=1),
        "iat" : datetime.now()
    }
    encoded = jwt.encode(payload,os.getenv("SECRET"),algorithm="HS256").decode('utf-8')
    return encoded

def decode(data):
    # try:
    #     decoded = jwt.decode(data, "kucing-merah", algorithms=["HS256"])
    # except:
    #     abort(403)
    # return decoded
    decoded = jwt.decode(data,os.getenv("SECRET"), algorithms=["HS256"])
    return decoded
    

