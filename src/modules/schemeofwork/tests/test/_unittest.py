'''
import this file into test cases to ensure paths are included 
'''
from unittest import TestCase as CoreTestCase

import sys
sys.path.append('../')
sys.path.append('../../schemeofwork/modules')

class TestCase(CoreTestCase):
        pass