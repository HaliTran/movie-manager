from .Model import Model
from google.cloud import datastore

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cloud-tran-hali5')
    
    def select(self):
        query = self.client.query(kind = 'Movies')
        entities = list(query.fetch())
        if(len(entities) == 0):
            return None
        return entities
        
    def insert(self, movie_info):
        unique_id = movie_info["imdb_id"]
        key = self.client.key('Movies', unique_id)
        movie = datastore.Entity(key)
        movie.update( {
            "poster" : movie_info["poster"],
            "title" : movie_info["title"],
            "plot" : movie_info["plot"],
            "year" : movie_info["year"],
            "rated" : movie_info["rated"],
            "runtime" : movie_info["runtime"],
            "imdb_id" : movie_info["imdb_id"]
            })
        self.client.put(movie)
        return True
    
    def delete(self, imdb_id):
        key = self.client.key("Movies", imdb_id)
        self.client.delete(key)
        return True
        
