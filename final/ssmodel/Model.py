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
    def insert(self, building, buildingCode, floor, rating):
        """
        Inserts into the database information regarding campus study spaces
        :param building: String
        :param buildingCode: String
        :param location: String
        :param rating: Number
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass