import requests
import os

API_KEY = os.environ.get('API_KEY')
API_URL = "http://www.omdbapi.com/"

def get_movie_data(query):
        param = {
            "apikey": API_KEY,
            "t": query["title"],
        }
        error = {}
        try:
            response = requests.get(f"{API_URL}", params=param)
            response.raise_for_status()
            if response.status_code == 200:
                response = response.json()
            else:
                error["error_message"] = f"There was a {response.status_code} error with your request."
                return error
        except (requests.ConnectionError, requests.HTTPError, requests.Timeout, requests.TooManyRedirects) as e:
            error["error_message"] = f"There was a '{str(e)}' error with your request."
            return error
        else:
            return response