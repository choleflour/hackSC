import requests
def get_data():
    url = "https://api.yelp.com/v3/businesses/search"

    querystring = {"location":"losangeles","categories":"hiking"}

    payload = ""
    headers = {
        "User-Agent": "insomnia/10.1.1",
        "Authorization": "Bearer AxZmESTbmKUy6VeLEaStDvnZBp5iRnBXB0vXs7nZxXxBNayNvdDw0DaLq6nXHOnJTzWqjWPb30aKYAgB_n4C8WgC4wDXw_YVVfpJKQAtIDjb9gFSl7SaeTY9MgEvZ3Yx"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    return response