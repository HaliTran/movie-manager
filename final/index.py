from flask import render_template, request
from flask.views import MethodView
import os

API_KEY = os.environ.get('API_KEY')

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
        return "Placeholder return value"
    