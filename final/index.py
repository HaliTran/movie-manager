from flask import render_template, request
from flask.views import MethodView
from utils.utility import get_movie_data

class Index(MethodView):
    def get(self):
        return render_template("index.html")
    
    def post(self):
        movie_title = request.form.get("movie_title")
        movie_data = {
            "title": movie_title,
        }
        movie_details = get_movie_data(movie_data)
        return render_template("index.html", movie=movie_details)