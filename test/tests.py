import unittest
from unittest.mock import patch
from io import StringIO
from src.q8 import q8

class TestFunctions(unittest.TestCase):

    def swtUp(self):
        pass

    def test_q8(self):
        expected = [i*i for i in range (1,21)]
        actual=squareMap()
        self.asserteual(expected,actual)
    
    def tearDown(self):
        print("Testing completed")

