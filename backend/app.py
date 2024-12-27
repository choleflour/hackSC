from flask import Flask, jsonify, request
from main import get_data
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
# whenever someone goes to our server url's default endpoint, exec this fn and it'll return smth
@app.route('/')
def index():
    # city = request.args.get('city')
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    if not lat or not lng:
        return jsonify({"error": "Latitude and Longitude are required"}), 400

    response = get_data(lat, lng).json()
    return jsonify(response)
