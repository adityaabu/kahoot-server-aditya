from flask import Flask
app = Flask(__name__)
 
@app.route('/12')
def landing():
    return 'hello world'