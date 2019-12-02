# create db connection
import mysql.connector
class FakeDb:

    def connect(self):
        self.cnx = mysql.connector.connect(user='drussell1974', password='password',
                              host='127.0.0.1',
                              database='cssow_api')

    def executesql(self, query):
        self.cursor = self.cnx.cursor()
        self.cursor.execute(query)
        return self.cursor


    def close(self):
        self.cursor.close()
        self.cnx.close()

def contains_learning_objective(rows, id):
    for item in rows:
        if item.id == id:
            return True
    return False
