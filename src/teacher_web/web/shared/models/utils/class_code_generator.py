import string
import random

class ClassCodeGenerator:
    
    @classmethod
    def generate_class_code(cls, length):
        class_code = ""
        for n in range(length):
            class_code = class_code + random.choice(string.ascii_uppercase + "1234567890")
        return class_code
