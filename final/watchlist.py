from flask.views import MethodView
from flask import render_template, redirect, request, url_for
import ssmodel

class Watchlist(MethodView):
    """
    Class-based view for retrieving and storing movie information to model backend

    This view handles both GET and POST HTTP requests

    URL Endpoint: '/'
        HTTP Verb: GET
        Purpose: Retrieve movie information from database backend
        Parameter: None
        Returns: Rendered template "watchlist.html" with movie information object

        HTTP Verb: POST
        Purpose: Store movie information to database backend
        Parameter: None
        Returns: Redirect response object to template "watchlist.html"
    
    """
    def get(self):
        db = ssmodel.get_model()
        entities = db.select()
        return render_template("watchlist.html", movies=entities)

    def post(self):
        db = ssmodel.get_model()
        poster = request.form.get("poster")
        title = request.form.get("title")
        plot = request.form.get("plot")
        genre = request.form.get("genre")
        date = request.form.get("date")
        rated = request.form.get("rated")
        runtime = request.form.get("runtime")
        imdb_id = request.form.get("imdb_id")
        movie_info = {
            "poster" : poster,
            "title" : title,
            "plot" : plot,
            "genre": genre,
            "date" : date,
            "rated" : rated,
            "runtime" : runtime,
            "imdb_id" : imdb_id
        }
        db.insert(movie_info)
        return redirect(url_for("watchlist"))
