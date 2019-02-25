from flask import Flask, request, json, jsonify
import os
from . import router, baseLocation

quizzesFileLocation = baseLocation / "data" / "quizzes-file.json"
questionsFileLocation = baseLocation / "data" / "question-file.json"


#-------------------- Proses Create, Get, Update & Delete Quiz --------------------
@router.route('/quiz', methods=['POST'])
def createQuiz():
    body = json.dumps(request.json)

    quizData = {
        "totalQuizAvailable": 0,
        "quizzes": []
    }

    if os.path.exists(quizzesFileLocation):
        quizzesFile = open(quizzesFileLocation, 'r')
        quizData = json.load(quizzesFile)
    else:
        quizzesFile = open(quizzesFileLocation, 'x')

    quizData["totalQuizAvailable"] += 1
    quizData["quizzes"].append(body)

    quizzesFile = open(quizzesFileLocation, 'w')
    quizzesFile.write(str(json.dumps(quizData)))

    return str(quizData)

@router.route('/quizzes/<quizId>')
def getQuiz(quizId):
    # nyari quiznya
    quizzesFile = open(quizzesFileLocation)
    quizzesData = json.load(quizzesFile)

    for quiz in quizzesData["quizzes"]:
        quiz = json.loads(quiz)
        if quiz["quiz-id"] == int(quizId):
            quizData = quiz
            break

    # nyari soalnya
    questionsFile = open(questionsFileLocation)
    questionsData = json.load(questionsFile)

    for question in questionsData["questions"]:
        question = json.loads(question)
        if question["quiz-id"] == int(quizId):
            quizData["question-list"].append(question)

    return jsonify(quizData)

@router.route('/quizzes/<quizId>', methods=['PUT'])
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
            
        
    quizzesFile = open(quizzesFileLocation, 'w')
    quizzesFile.write(str(json.dumps(quizData)))

    return message

@router.route('/quizzes/<quizId>', methods=['DELETE'])
def deleteQuiz(quizId):
    # get data from question-file.json 
    quizzesFile = open(quizzesFileLocation)
    quizzesData = json.load(quizzesFile)

    questionFile = open(questionsFileLocation)
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

    quizzesFile = open(quizzesFileLocation, 'w')
    quizzesFile.write(str(json.dumps(quizData)))
    questionFile = open(questionsFileLocation, 'w')
    questionFile.write(str(json.dumps(questionUpdate)))



    return message
# minta data sebuah soal untuk kuis tertentu
@router.route('/quizzes/<quizId>/questions/<questionNumber>')
def getThatQuestion(quizId, questionNumber):
    quizData = getQuiz(int(quizId)).json

    for question in quizData["question-list"]:
        if question["question-number"] == int(questionNumber):
            return jsonify(question)