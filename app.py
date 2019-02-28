from flask import Flask, json, request, abort, jsonify
from src.routes import router
import jwt

app = Flask(__name__)
app.register_blueprint(router)

@app.route ('/decode')
def jwtdecode():
    decode= jwt.decode(request.json["token"],"kucing-merah",algorithms=["HS256"])
    return decode

@app.errorhandler(410)
def errorhandler403(e):
    print ("soal tsb gx ada")
    return ("error 410 cuy")

@app.route ('/penjumlahan/<int:firstNumber>/<int:secondNumber>')
def penjumlahan (firstNumber,secondNumber):
    return jsonify({
        "hasil jumlah":firstNumber+secondNumber
    })