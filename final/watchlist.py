from flask.views import MethodView
from flask import render_template, redirect, request, url_for

class Watchlist(MethodView):
    def get(self):
        return render_template("watchlist.html")
