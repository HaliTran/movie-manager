from flask import render_template, request
from flask.views import MethodView
import requests
import os

API_KEY = os.environ.get('API_KEY')
API_URL = "http://www.omdbapi.com/"


class Index(MethodView):
    def get(self):
        return render_template("index.html")
    
    def post(self):
        movie_title = request.form.get("movie_title")
        release_year = request.form.get("release_year")
        movie_data = {
            "title": movie_title,
            "year": release_year
        }
        movie_details = self.get_movie_data(movie_data)
        return "Placeholder return value"
    
    def get_movie_data(self, query):
        param = {
            "apikey": API_KEY,
            "t": query["title"],
            "y": query["year"]
        }
        error = {}
        try:
            response = requests.get(f"{API_URL}", params=param)
            response.raise_for_status()
            if response.status_code == 200:
                response = response.json()
            else:
                error["error_message"] = f"There was a {response.status_code} error with your requests"
                return error
        except requests.ConnectionError as e:
                error["error_message"] = f"There was a {str(e)} error with your requests"
                return error
        else:
            return response