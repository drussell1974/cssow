import os
import requests
import time

class print_fnc_name():
    """ decorator for printing the name of the function """
    
    def __call__(self, func):
        """ the parent function """
        def inner(*args, **kwargs):
            print(func.__name__)
            # call decorated function
            return func(*args, **kwargs)
            
        print(func.__name__)         
        return inner
