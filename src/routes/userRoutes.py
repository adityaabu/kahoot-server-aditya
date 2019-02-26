from flask import Flask, request, json, jsonify
import os
from . import router, baseLocation
from ..utils.crypt import encrypt
from ..utils.auth import generateToken

userFileLocation = baseLocation / "data" / "user-file.json"

@router.route('/cekToken')
def cekToken():
    token = request.headers["Authorization"][7:]
    return (token)

@router.route('/signup', methods=["POST"])
def getSignUp():
    body = request.json
    if body["username"] == body["password"]:
        return "password tidak boleh sama dengan username"

    # <proses enkripsi password>
    
    shift = 4 
    body["password"] = encrypt(body["password"],shift)
    
    #</proses enkripsi password>

    usernameData = {
        "username-list" : []
    }

    if os.path.exists(userFileLocation):
        usernameFile = open(userFileLocation, 'r')
        usernameData = json.load(usernameFile)
    else:
        usernameFile = open(userFileLocation, 'x')

    with open(userFileLocation, 'w') as usernameFile:
        usernameData["username-list"].append(body)
        usernameFile.write(str(json.dumps(usernameData)))

    return jsonify(request.json)

# Proses Sign Up #
@router.route('/signin', methods=["POST"])
def getSignIn():
    body = request.json
    usernameFile = open(userFileLocation)
    usernameData = json.load(usernameFile)
    isLogin = False
    # <proses enkripsi password>
    
    shift = 4 
    body["password"] = encrypt(body["password"],shift)
    
    #</proses encripsi password>

    for username in usernameData["username-list"]:
        if  username["username"] != body["username"]:
            return "username tidak terdaftar"
        
        elif  username["username"]  == body["username"] and username["password"] == body["password"]:
            body["token"] = generateToken(body["username"])
            # return "login berhasil
            isLogin = True
            body["status"]= isLogin 
            return jsonify(body)
        elif  username["username"]  == body["username"] and username["password"] != body["password"]:
            return "password tidak benar"
    

    

