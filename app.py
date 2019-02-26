from flask import Flask, json, request
from src.routes import router
import jwt

app = Flask(__name__)
app.register_blueprint(router)

@app.route ('/decode')
def jwtdecode():
    decode= jwt.decode(request.json["token"],"kucing-merah",algorithms=["HS256"])
    return decode