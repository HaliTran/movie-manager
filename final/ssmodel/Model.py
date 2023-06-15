"""
Abstract Model base class that can be extended to implement
different types of backend models for data storage and manipulation.

"""

class Model():
    def select(self):
        """
        Returns all entries in the database.
        
        Returns:
            List containing all rows in the database
        """
        pass
    def insert(self, movie_info):
        """
        Inserts into the database information regarding a movie
        
        Parameter:
            movie_info: dictionary object with details about a movie
            
        Key Required for movie_info dictionary
            poster: String (url of image location)
            title:  String
            plot: String
            year: String
            rated: String
            runtime: String
            imdb_id: String
            
        Raises database errors on connection and insertion
        """
        pass