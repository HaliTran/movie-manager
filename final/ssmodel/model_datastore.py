from .Model import Model
from google.cloud import datastore

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cloud-tran-hali5')

    def insert(self, movie_info):
        key = self.client.key('Movies')
        movie = datastore.Entity(key)
        movie.update( {
            "poster" : movie_info["poster"],
            "title" : movie_info["title"],
            "plot" : movie_info["plot"],
            "year" : movie_info["year"],
            "rated" : movie_info["rated"],
            "runtime" : movie_info["runtime"],
            "imdbID" : movie_info["imdb_id"]
            })
        self.client.put(movie)
        return True
