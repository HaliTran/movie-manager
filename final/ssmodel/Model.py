"""
Abstract Model base class that can be extended to implement
different types of backend models for data storage and manipulation.

"""

class Model():
    def select(self):
        """
        Return all entries in the database
        :return: Tuple containing all rows in the database
        """
        pass
    def insert(self, movie_info):
        """
        Inserts into the database information regarding a movie
        :param movie_info: dictionary with details about a movie
        :key poster: String (url of img location)
        :key title: String
        :key plot: String
        :key year: String
        :key rated: String
        :key runtime: String
        :key imdb_id: String
        :raises: Database errors on connection and insertion
        """
        pass