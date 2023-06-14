from flask.views import MethodView
from flask import render_template, url_for

class Compare(MethodView):
    def get(self):
        return render_template("compare.html")
