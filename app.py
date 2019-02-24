from flask import Flask, request, json, jsonify
from random import randint
import requests
import os
app = Flask(__name__)


#-------------------- Proses Create, Get, Update & Delete Quiz --------------------
@app.route('/quiz', methods=['POST'])
def createQuiz():
    body = json.dumps(request.json)

    quizData = {
        "totalQuizAvailable": 0,
        "quizzes": []
    }

    if os.path.exists('./quizzes-file.json'):
        quizzesFile = open('./quizzes-file.json', 'r')
        quizData = json.load(quizzesFile)
    else:
        quizzesFile = open('./quizzes-file.json', 'x')

    quizData["totalQuizAvailable"] += 1
    quizData["quizzes"].append(body)

    quizzesFile = open('./quizzes-file.json', 'w')
    quizzesFile.write(str(json.dumps(quizData)))

    return str(quizData)

@app.route('/quizzes/<quizId>')
def getQuiz(quizId):
    # nyari quiznya
    quizzesFile = open('./quizzes-file.json')
    quizzesData = json.load(quizzesFile)

    for quiz in quizzesData["quizzes"]:
        quiz = json.loads(quiz)
        if quiz["quiz-id"] == int(quizId):
            quizData = quiz
            break

    # nyari soalnya
    questionsFile = open('./question-file.json')
    questionsData = json.load(questionsFile)

    for question in questionsData["questions"]:
        question = json.loads(question)
        if question["quiz-id"] == int(quizId):
            quizData["question-list"].append(question)

    return jsonify(quizData)

@app.route('/quizzes/<quizId>', methods=['PUT'])
def updateQuiz(quizId):
    body = json.dumps(request.json)

    # get data from question-file.json 
    quizzesFile = open("./quizzes-file.json")
    quizzesData = json.load(quizzesFile)
    quizData = {
        "totalQuizAvailable": quizzesData["totalQuizAvailable"],
        "quizzes": []
    }
    message = "Quiz-id gagal di update " + quizId
    for quiz in quizzesData["quizzes"]:
        quiz = json.loads(quiz)
        if quiz["quiz-id"] == int(quizId):
            quizData["quizzes"].append(body)
            message = "Quiz-id berhasil di update " + quizId
        else:
            quiz = json.dumps(quiz)
            quizData["quizzes"].append(quiz)
            
        
    quizzesFile = open('./quizzes-file.json', 'w')
    quizzesFile.write(str(json.dumps(quizData)))

    return message

@app.route('/quizzes/<quizId>', methods=['DELETE'])
def deleteQuiz(quizId):
    # get data from question-file.json 
    quizzesFile = open("./quizzes-file.json")
    quizzesData = json.load(quizzesFile)

    questionFile = open("./question-file.json")
    questionData = json.load(questionFile)

    quizData = {
        "totalQuizAvailable": 0,
        "quizzes": []
    }

    questionUpdate = {
        "questions": []
    }

    message = "Quiz-id : " + quizId +"gagal di hapus "

    for quiz in quizzesData["quizzes"]:
        quiz = json.loads(quiz)
        if quiz["quiz-id"] == int(quizId):
            message = "Quiz-id : " + quizId +" berhasil di hapus "
            pass
        else:
            quiz = json.dumps(quiz)
            quizData["totalQuizAvailable"] += 1
            quizData["quizzes"].append(quiz)
            
    for question in questionData["questions"]:
        question = json.loads(question)
        if question["quiz-id"] == int(quizId):
            pass
        else:
            question = json.dumps(question)
            questionUpdate["questions"].append(question)

    quizzesFile = open('./quizzes-file.json', 'w')
    quizzesFile.write(str(json.dumps(quizData)))
    questionFile = open('./question-file.json', 'w')
    questionFile.write(str(json.dumps(questionUpdate)))



    return message

#-------------------- Proses Create, Get, Update & Delete Question --------------------
@app.route('/question', methods=['POST'])
def createQuestion():
    body = json.dumps(request.json)

    questionData = {
        "questions": []
    }

    if os.path.exists('./question-file.json'):
        questionFile = open('./question-file.json', 'r')
        print("File ada")
        questionData = json.load(questionFile)
    else:
        questionFile = open('./question-file.json', 'x')
        print("file ga ada") 

    questionFile = open('./question-file.json', 'w')
    questionData["questions"].append(body)
    questionFile.write(str(json.dumps(questionData)))

    return str(questionData)

@app.route('/quizzes/<quizId>/questions/<questionNumber>', methods=['PUT'])
def updateQuestion(quizId, questionNumber):
    body = json.dumps(request.json)

    # get data from question-file.json 
    questionFile = open("./question-file.json")
    questionData = json.load(questionFile)

    questionUpdate = {
        "questions": []
    }
    message = "Question no. "+ questionNumber + " dengan quiz-id: " + quizId + " gagal di update."
    for question in questionData["questions"]:
        question = json.loads(question)
        if question["quiz-id"] == int(quizId) and question["question-number"] == int(questionNumber):
            questionUpdate["questions"].append(body)
            message = "Question no. "+ questionNumber + " dengan quiz-id: " + quizId + " berhasil di update."
        else:
            question = json.dumps(question)
            questionUpdate["questions"].append(question)
            
        
    questionFile = open('./question-file.json', 'w')
    questionFile.write(str(json.dumps(questionUpdate)))

    return message

@app.route('/quizzes/<quizId>/questions/<questionNumber>', methods=['DELETE'])
def deleteQuestion(quizId, questionNumber):

    # get data from question-file.json 
    questionFile = open("./question-file.json")
    questionData = json.load(questionFile)

    questionUpdate = {
        "questions": []
    }
    message = "Question no. "+ questionNumber + " dengan quiz-id: " + quizId + " gagal di update."

    for question in questionData["questions"]:
        question = json.loads(question)
        if question["quiz-id"] == int(quizId) and question["question-number"] == int(questionNumber):
            message = "Question no. "+ questionNumber + " dengan quiz-id: " + quizId + " berhasil di update."
            pass
        else:
            question = json.dumps(question)
            questionUpdate["questions"].append(question)
            
        
    questionFile = open('./question-file.json', 'w')
    questionFile.write(str(json.dumps(questionUpdate)))

    return message

# minta data sebuah soal untuk kuis tertentu
@app.route('/quizzes/<quizId>/questions/<questionNumber>')
def getThatQuestion(quizId, questionNumber):
    quizData = getQuiz(int(quizId)).json

    for question in quizData["question-list"]:
        if question["question-number"] == int(questionNumber):
            return jsonify(question)


#-------------------- Proses Create, Join, Answer & Leaderboard Game --------------------

@app.route('/game', methods=["POST"])
def createGame():
    body = request.json

    # dapetin info quiz
    quizzesFile = open('./quizzes-file.json')
    quizzesData = json.load(quizzesFile)

    for quiz in quizzesData["quizzes"]:
        quiz = json.loads(quiz)

        if quiz["quiz-id"] == int(body["quiz-id"]):
            gameInfo = quiz

    gameInfo["game-pin"] = randint(100000, 999999)
    gameInfo["user-list"] = []
    gameInfo["leaderboard"] = []


    # create skeleton for list of game buat nulis 
    # kalau belum pernah main game sama sekali
    gamesData = {
        "game-list": []
    }

    # simpen data game nya
    if os.path.exists('./games-file.json'):
        gamesFile = open('./games-file.json', 'r')
        gamesData = json.load(gamesFile)
    else:
        gamesFile = open('./games-file.json', 'x')

    with open('./games-file.json', 'w') as gamesFile:
        gamesData["game-list"].append(gameInfo)
        gamesFile.write(str(json.dumps(gamesData)))

    return jsonify(gameInfo)


@app.route('/game/join', methods=["POST"])
def joinGame():
    body = request.json

    # get data from games-file.json 
    gamesFile = open('./games-file.json')
    gamesData = json.load(gamesFile)

    position = 0
    for i in range(len(gamesData["game-list"])):
        game = gamesData["game-list"][i]

        if game["game-pin"] == int(body["game-pin"]):
            if body["username"] not in game["user-list"]:
                game["user-list"].append(body["username"])
                game["leaderboard"].append({
                    "username": body["username"],
                    "score": 0
                })

                gameInfo = game
                position = i
                break
            # TODO: error kalau usernya udah dipake

    with open('./games-file.json', 'w') as gamesFile:
        gamesData["game-list"][position] = gameInfo
        gamesFile.write(str(json.dumps(gamesData)))

    return jsonify(request.json)


@app.route('/game/answer', methods=["POST"])
def submitAnswer():
    isTrue = False
    body = request.json

    # buka file question
    questionsFile = open('./question-file.json')
    questionsData = json.load(questionsFile)

    for question in questionsData["questions"]:
        question = json.loads(question)

        if question["quiz-id"] == int(body["quiz-id"]) and question["question-number"] == int(body["question-number"]):
            if question["answer"] == body["answer"]:
                isTrue = True


    # TODO: update skor/leaderboard
    gamesFile = open('./games-file.json')
    gamesData = json.load(gamesFile)

    gamePosition = 0
    for i in range(len(gamesData["game-list"])):
        game = gamesData["game-list"][i]

        if game["game-pin"] == body["game-pin"]:
            if isTrue:
                userPosition = 0
                for j in range(len(game["leaderboard"])): 
                    userData = game["leaderboard"][j]

                    if userData["username"] == body["username"]:
                        userData["score"] += 100

                        userInfo = userData
                        userPosition = j
                        break
                
                game["leaderboard"][userPosition] = userInfo
                gameInfo = game
                gamePosition = i
                break

    with open('./games-file.json', 'w') as gamesFile:
        gamesData["game-list"][gamePosition] = gameInfo
        gamesFile.write(str(json.dumps(gamesData)))
    

    return jsonify(request.json)

@app.route('/game/leaderboard', methods=["POST"])
def getLeaderboard():
    body = request.json

    gamesFile = open('./games-file.json')
    gamesData = json.load(gamesFile)

    for game in gamesData["game-list"]:
        if game["game-pin"] == body["game-pin"]:
            # TODO: sorting dari yang paling gede ke kecil
            return jsonify(game["leaderboard"])

#-------------------- Proses Sign Up, Sign In & Enkripsi dengan Caesar Cipher --------------------
@app.route('/signup', methods=["POST"])
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

    if os.path.exists('./username-file.json'):
        usernameFile = open('./username-file.json', 'r')
        usernameData = json.load(usernameFile)
    else:
        usernameFile = open('./username-file.json', 'x')

    with open('./username-file.json', 'w') as usernameFile:
        usernameData["username-list"].append(body)
        usernameFile.write(str(json.dumps(usernameData)))

    return jsonify(request.json)

# Proses Sign Up #
@app.route('/signin', methods=["POST"])
def getSignIn():
    body = request.json
    usernameFile = open('./username-file.json')
    usernameData = json.load(usernameFile)
    
    # <proses enkripsi password>
    
    shift = 4 
    body["password"] = encrypt(body["password"],shift)
    
    #</proses encripsi password>

    for username in usernameData["username-list"]:
        if  username["username"] != body["username"]:
            return "username tidak terdaftar"
        
        elif  username["username"]  == body["username"] and username["password"] == body["password"]:
            return "password dan username benar"
        elif  username["username"]  == body["username"] and username["password"] != body["password"]:
            return "password tidak benar"

# Proses enkripsi password
def encrypt(password,shift): 
    encryptPassword = "" 

    for i in range(len(password)): 
        char = password[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            encryptPassword += chr((ord(char) + shift - 65) % 26 + 65) 
        # Encrypt lowercase characters 
        else: 
            encryptPassword += chr((ord(char) + shift - 97) % 26 + 97) 
  
    return encryptPassword
