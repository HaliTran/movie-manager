from flask import render_template
from flask.views import MethodView
from ssmodel.model_sqlite3 import model

class Index(MethodView):
    def get(self):
        db = model()
        studySpaces = [dict(building=spaces[0], code=spaces[1], location=spaces[2], rating=spaces[3]) for spaces in db.select()]
        return render_template("index.html", studySpace = studySpaces)