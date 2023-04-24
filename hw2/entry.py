from flask.views import MethodView
from flask import render_template, redirect, request, url_for
from ssmodel.model_sqlite3 import model

class Entry(MethodView):
    def get(self):
        return render_template("entry.html")
    
    def post(self):
        db = model()
        db.insert(request.form['building'], request.form['code'], request.form['location'], request.form['rating'])
        return redirect(url_for("index"))

