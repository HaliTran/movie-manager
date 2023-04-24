"""

The data will be stored in a SQLite database.

"""

from .Model import Model
import sqlite3
DB_FILE = 'campus.db'    # file for our database


class model(Model):
    def __init__(self):
        # Check if our db exist, if not then create it.
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT COUNT(*) FROM studyspace;")
        except sqlite3.OperationalError:
            cursor.execute("CREATE TABLE studyspace (building text, buildingCode text, location text, rating int);")

        cursor.close()
        connection.commit()
        connection.close()
    
    def select(self):
        """
        Query for all the rows in the study space table of the database
        Each rows data includes: building name, building code, location of study space, rating.

        :return: List of tuples of the result. E.g [(colum1, colum2, colum3), (column1, etc...)]
        """
        
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM studyspace;")
        result = cursor.fetchall()

        cursor.close()
        connection.close()
        return result

    def insert(self, building, buildingCode, location, rating):
        """
        Insert into the studyspace table of the campus database

        :param building: String
        :param buildinCode: String
        :param location: String
        :param rating: Int
        :return: True
        :raises: Database errors on connection and insertion
        """

        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()

        param = {"building": building, "code": buildingCode, "location": location, "rating": rating}
        cursor.execute("INSERT INTO studyspace VALUES (:building, :code, :location, :rating)", param)

        cursor.close()
        connection.commit()
        connection.close()
        return True