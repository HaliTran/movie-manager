from flask import render_template, request
from flask.views import MethodView
import os

API_KEY = os.environ.get('API_KEY')

class Index(MethodView):
    def get(self):
        return render_template("index.html")
    
    def post(self):
        movieTitle = request.form.get("movie-title")
        releaseYear = request.form.get("release-year")
        movieData = {
            "title": movieTitle,
            "year": releaseYear
        }

        return "Placeholder return value"