import unittest
from ..src.factorial import (calculate_factorial)


class Test_factorial(unittest.TestCase):
    def test_0(self):
        self.assertEqual(calculate_factorial(0),1)
    def test_2(self):
        self.assertEqual(calculate_factorial(0),2)
    def test_6(self):
        self.assertEqual(calculate_factorial(0),720)
        
if __name__ =="__main__":
    unittest.main()