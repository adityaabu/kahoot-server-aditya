from flask import Flask, request, json, jsonify, g
import os
from . import router, baseLocation
from ..utils.file import readFile, writeFile, checkFile
from ..utils.auth import verifySignIn

quizzesFileLocation = baseLocation / "data" / "quizzes-file.json"
questionsFileLocation = baseLocation / "data" / "question-file.json"

try:
    quizzesData = readFile(quizzesFileLocation)
except: 
    print ("Quizzes file not found")

try:
    questionsData = readFile(questionsFileLocation)
except:
    print ("Question file not found")

# questionsData = readFile(questionsFileLocation)
# quizzesData = readFile(quizzesFileLocation)


#-------------------- Proses Create, Get, Update & Delete Quiz --------------------
@router.route('/quiz', methods=['POST'])
@verifySignIn
def createQuiz():
    # body = json.dumps(request.json)
    body = request.json
    print ("quuz", g.username)
    quizData = {
        "totalQuizAvailable": 0,
        "quizzes": []
    }
    message={}

    quizData = checkFile(quizzesFileLocation)
   
    isNotUsed = False
    for quiz in quizzesData["quizzes"]:
        if quiz["quiz-id"] == body["quiz-id"]:
            isNotUsed = False
            message["error"]= "quiz-id sudah ada"
        else:
            isNotUsed = True


    if isNotUsed == True :
        quizData["totalQuizAvailable"] += 1
        quizData["quizzes"].append(body)
        writeFile(quizzesFileLocation,quizData)
        message["status"] = "Quiz berhasil di buat."

    return jsonify(message)

@router.route('/quizzes/<quizId>')
@verifySignIn
def getQuiz(quizId):
    
    for quiz in quizzesData["quizzes"]:
        if quiz["quiz-id"] == int(quizId):
            quizData = quiz
            break

    for question in questionsData["questions"]:
        if question["quiz-id"] == int(quizId):
            quizData["question-list"].append(question)

    return jsonify(quizData)

@router.route('/quizzes/<quizId>', methods=['PUT'])
@verifySignIn
def updateQuiz(quizId):
    body = request.json

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
            
        
    quizzesFile = open(quizzesFileLocation, 'w')
    quizzesFile.write(str(json.dumps(quizData)))
    

    return message

@router.route('/quizzes/<quizId>', methods=['DELETE'])
@verifySignIn
def deleteQuiz(quizId):

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
            
    for question in questionsData["questions"]:
        question = json.loads(question)
        if question["quiz-id"] == int(quizId):
            pass
        else:
            question = json.dumps(question)
            questionUpdate["questions"].append(question)

    quizzesFile = open(quizzesFileLocation, 'w')
    quizzesFile.write(str(json.dumps(quizData)))
    questionFile = open(questionsFileLocation, 'w')
    questionFile.write(str(json.dumps(questionUpdate)))

    return message
# minta data sebuah soal untuk kuis tertentu
@router.route('/quizzes/<quizId>/questions/<questionNumber>')
@verifySignIn
def getThatQuestion(quizId, questionNumber):
    quizData = getQuiz(int(quizId)).json

    for question in quizData["question-list"]:
        if question["question-number"] == int(questionNumber):
            return jsonify(question)
