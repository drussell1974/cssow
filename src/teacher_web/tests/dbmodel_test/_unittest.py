'''
import this file into test cases to ensure paths are included 
'''
from unittest import TestCase as CoreTestCase, skip as CoreSkip
import mysql.connector
import sys

class TestCase(CoreTestCase):
        pass

class Cursor:
    def __init__(self):
        self.id = 0


    def cursor(self):
        pass


class FakeDb:

    def __init__(self):
        pass


    def __enter___(self):
        print("enter...")
        return Cursor()

    
    def __exit___(self,  type, value, traceback):
        print("exit...")
        pass

    def cursor(self):
        return Cursor()
    

    def connect(self):
        #self.cnx = mysql.connector.connect(user='drussell1974', password='password1.',
        #                      host='127.0.0.1',
        #                      database='cssow_api')
        pass

    
    def executesql(self, query):
        self.cursor = None #self.cnx.cursor()
        #self.cursor.execute(query)
        return self.cursor


    def close(self):
        #self.cursor.close()
        #self.cnx.close()
        pass


def contains_learning_objective(rows, id):
    for item in rows:
        if item.id == id:
            return True
    return False
