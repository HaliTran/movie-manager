"""
A simple web application for users to search
and manage their favorite movies and T.V. shows

"""
from flask import Flask, request, url_for, redirect
from index import Index
from watchlist import Watchlist
from compare import Compare
import ssmodel

app = Flask(__name__)

app.add_url_rule('/', view_func=Index.as_view('index'), methods=["GET", "POST"])

app.add_url_rule('/watchlist', view_func=Watchlist.as_view('watchlist'), methods=["GET", "POST"])

app.add_url_rule('/compare', view_func=Compare.as_view('compare'), methods=["GET"])

@app.route('/watchlist/delete', methods=["POST"])
def delete_movie():
    imdb_id = request.form.get("imdb_id")
    db = ssmodel.get_model()
    db.delete(imdb_id)
    return redirect(url_for('watchlist'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)