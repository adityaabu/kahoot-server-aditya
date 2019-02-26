from .crypt import encrypt
from .token import encode, decode
from functools import wraps
from flask import request, g

def generateToken(data):
    data = encrypt(data,4)
    token = encode (data)

    return token

def verifySignIn(f):
    @wraps(f)
    def decoratedFunction(*args, **kwargs):
        # body = request.json
        token = request.headers["Authorization"] #"Authorization" itu di insomnia tab header, lalu di samping header [value] isinya Bearer <token>
        data = decode(token)
        username = encrypt(data["fata"],4)

        g.username = username
        print ("lewat decorator")
        return f(*args, **kwargs)
    return decoratedFunction