"""
A simple web application for users to search
and manage their favorite movies and T.V. shows

"""
import flask
from index import Index
from watchlist import Watchlist

app = flask.Flask(__name__)

app.add_url_rule('/', view_func=Index.as_view('index'), methods=["GET", "POST"])

app.add_url_rule('/watchlist', view_func=Watchlist.as_view('watchlist'), methods=["GET", "POST"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)