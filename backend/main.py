import requests
from dotenv import load_dotenv
import os

def get_data(lat, lng):
    load_dotenv()
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    querystring = {"location": f"{lat},{lng}","keyword":"hiking","key": os.getenv('API_KEY'),"radius":"50000"}

    payload = ""
    headers = {
        "User-Agent": "insomnia/10.1.1",
        "Authorization": f"Bearer {os.getenv('auth')}"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)


    for place in response['results']:
        if 'photos' in place:
            
            photo_reference = place['photos'][0]['photo_reference']
            place['image'] = f"https://maps.googleapis.com/maps/api/place/photo?key={os.getenv('API_KEY')}&photo_reference={photo_reference}&maxwidth=400"


    return response
