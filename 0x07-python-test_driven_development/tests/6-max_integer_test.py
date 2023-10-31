#!/usr/bin/python3
"""
   Module to test functon that finds the max integer in a list
"""


import uniittest
class test_max_integer(unittest.TestCase):
    """
       using unittest subclass to test 
    """
    # Normal use case
    # Float
    # Negative int
    # None
    # Non integers
    # same values list
    # Empty list
    # pass list of lists(matrix)
    self.assertEqual(max_integer([1, 2, 3, 4]), 4)

 
if __name__ == '__main__':
    unittest.TestCase()
