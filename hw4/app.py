"""
A simple web application for listing campus study spaces

"""
import flask
from index import Index
from entry import Entry

app = flask.Flask(__name__)

app.add_url_rule('/', view_func=Index.as_view('index'), methods=["GET"])

app.add_url_rule('/entry', view_func=Entry.as_view('entry'), methods=["GET", "POST"])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)