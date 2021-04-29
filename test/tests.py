import unittest
from io import StringIO
from unittest.mock import patch

from src.q10 import Reverselter


class TestFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_q8(self):
        expected = [i*i for i in range (1,21)]
        actual=squareMap()
        self.assertEqual(expected,actual)
    
    def test_iterClass(self):
        expected =[]
        for ele in ReverseIter([i*i for i in range (1,21)]):
            expected.append(ele)
        actual = reversed([i*i for i in range(1,21)])
        self.assertEqual(liist(expected),list(acual))
    
    def tearDown(self):
        print("Testing completed")


if __name__ == '__main__':
    unittest.main()

