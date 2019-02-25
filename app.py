from flask import Flask, request, json, jsonify
# import requests
import os
from src.routes import router
app = Flask(__name__)
app.register_blueprint(router)