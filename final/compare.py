from flask.views import MethodView
from flask import render_template, url_for, request
from utils.utility import get_movie_data

class Compare(MethodView):
    """
    Class-based view for retrieving and displaying two movies to compare

    This view handles both GET and POST HTTP requests

    URL Endpoint: '/'
        HTTP Verb: GET
        Parameter: None
        Returns: Rendered template "compare.html" with movie information object

        HTTP Verb: POST
        Purpose: Retrieve movie information to compare
        Parameter: None
        Returns: Rendered template "compare.html" with two movie information object
    
    """
    def get(self):
        return render_template("compare.html")

    def post(self):
        movie_title1 = request.form.get("movie_title1")
        movie_title2 = request.form.get("movie_title2")
        movie_data1 = {
            "title": movie_title1,
        }
        movie_data2 = {
            "title": movie_title2
        }
        movie_details1 = get_movie_data(movie_data1)
        movie_details2 = get_movie_data(movie_data2)
        return render_template("compare.html", movie1=movie_details1, movie2=movie_details2)