from flask import json
import os
def writeFile(fileLocation,theData):
    theFile = open(fileLocation, 'w')
    theFile.write(str(json.dumps(theData)))

def readFile(fileLocation):
    theFile = open(fileLocation)
    return json.load(theFile)

def checkFile(fileLocation, theData):
    if os.path.exists(fileLocation):
        theFile = open(fileLocation, 'r')
        theData = json.load(theFile)
        return theData