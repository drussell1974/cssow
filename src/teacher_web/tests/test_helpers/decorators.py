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


class restore_demo_data():
    """ decorator for calling restore-data api service """
    
    def __call__(self, func, s=2):
        
        def inner(*args, **kwargs):
            # call decorated function
            return func(*args, **kwargs)
            

        uri = os.environ["TEST_URI"] + "/api/demo/restore-data"
        print(f"restoring demo data from {func.__name__}... calling {uri}...", end="")
        
        context = requests.get(uri)
        time.sleep(s)

        print(f"{context}... {context.content}")
        
        return inner
