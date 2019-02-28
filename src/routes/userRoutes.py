import os

from ..utils.crypt import encrypt
from . import router, baseLocation
from ..utils.auth import generateToken
from flask import Flask, request, json, jsonify
from ..utils.file import readFile, writeFile, checkFile


userFileLocation = baseLocation / "data" / "user-file.json"

@router.route('/cekToken')
def cekToken():
    token = request.headers["Authorization"][7:]
    return (token)

@router.route('/signup', methods=["POST"])
def getSignUp():
    body = request.json
    isNotUsed=False

    usernameData = {
        "username-list" : []
    }

    message ={}
    
    usernameData = checkFile(userFileLocation)
    
    if body["username"] == body["password"]:
        print ("check password")
        return "password tidak boleh sama dengan username"

    else:

        for username in usernameData["username-list"]:
        
            if  username["username"] == body["username"]:
                print ("username sudah digunakan")
                isNotUsed=False
                message["username"] = body["username"]
                message["email"] = body["email"]
                message["status"] = "Username sudah digunakan"
                break
                
            elif username["email"] == body["email"]:
                print ("Email sudah digunakan")
                message["username"] = body["username"]
                message["email"] = body["email"]
                message["status"] = "Password sudah digunakan"
                isNotUsed=False
                break   

            else:
                print ("username tidak ada")
                isNotUsed=True

        if isNotUsed==True:
            
            shift = 4 
            body["password"] = encrypt(body["password"],shift)
            message["username"] = body["username"]
            message["email"] = body["email"]
            message["password"] = body["password"]
            message["status"] = "Berhasil Sign Up"

            with open(userFileLocation, 'w') as usernameFile:
                usernameData["username-list"].append(body)
                usernameFile.write(str(json.dumps(usernameData)))
            
    return jsonify(message)

@router.route('/signin', methods=["POST"])
def getSignIn():
    body = request.json
    usernameData = readFile(userFileLocation)
    isLogin = False
    shift = 4 
    body["password"] = encrypt(body["password"],shift)
    
    for username in usernameData["username-list"]:
        
        if  username["username"] != body["username"]:
            print (username["username"])
            print (body["username"])
            print ("username tidak terdaftar")
            isLogin = False
            body["message"] = "username tidak terdaftar"
            body["status"]= isLogin 
        
        elif  username["password"]  != body["password"]:
            print ("Password Salah")
            isLogin = False
            body["message"] = "Password Salah"
            body["status"]= isLogin 
    
        else:
            isLogin = True
            body["status"]= isLogin
            body["message"] = "Berhasil Sign In"
            body.pop("password")
            body["token"] = generateToken(body["username"])
            break

    return jsonify(body)

    

