from flask import Flask, request, json, jsonify
import os
from . import router, baseLocation
from ..utils.auth import verifySignIn

questionsFileLocation = baseLocation / "data" / "question-file.json"

#-------------------- Proses Create, Get, Update & Delete Question --------------------
@router.route('/question', methods=['POST'])
@verifySignIn
def createQuestion():
    body = json.dumps(request.json)

    questionData = {
        "questions": []
    }

    if os.path.exists(questionsFileLocation):
        questionFile = open(questionsFileLocation, 'r')
        print("File ada")
        questionData = json.load(questionFile)
    else:
        questionFile = open(questionsFileLocation, 'x')
        print("file ga ada") 

    questionFile = open(questionsFileLocation, 'w')
    questionData["questions"].append(body)
    questionFile.write(str(json.dumps(questionData)))

    return str(questionData)

@router.route('/quizzes/<quizId>/questions/<questionNumber>', methods=['PUT'])
@verifySignIn
def updateQuestion(quizId, questionNumber):
    body = json.dumps(request.json)

    # get data from question-file.json 
    questionFile = open(questionsFileLocation)
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
            
        
    questionFile = open(questionsFileLocation, 'w')
    questionFile.write(str(json.dumps(questionUpdate)))

    return message

@router.route('/quizzes/<quizId>/questions/<questionNumber>', methods=['DELETE'])
@verifySignIn
def deleteQuestion(quizId, questionNumber):

    # get data from question-file.json 
    questionFile = open("./question-file.json")
    questionData = json.load(questionFile)

    questionUpdate = {
        "questions": []
    }
    message = "Question no. "+ questionNumber + " dengan quiz-id: " + quizId + " gagal di delete."

    for question in questionData["questions"]:
        question = json.loads(question)
        if question["quiz-id"] == int(quizId) and question["question-number"] == int(questionNumber):
            message = "Question no. "+ questionNumber + " dengan quiz-id: " + quizId + " berhasil di delete."
            pass
        else:
            question = json.dumps(question)
            questionUpdate["questions"].append(question)
            
        
    questionFile = open(questionsFileLocation, 'w')
    questionFile.write(str(json.dumps(questionUpdate)))

    return message


