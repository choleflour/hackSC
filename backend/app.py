from flask import Flask, jsonify, request
from main import get_data
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# whenever someone goes to our server url's default endpoint, exec this fn and it'll return smth
@app.route('/')
def index():
    location = request.args.get('location')
    return jsonify(get_data(location).json())
