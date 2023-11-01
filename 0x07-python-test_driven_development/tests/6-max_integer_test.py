#!/usr/bin/python3
"""
   Module to test functon that finds the max integer in a list
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class test_max_integer(unittest.TestCase):
    """
       using unittest subclass to test
    """

    # pass list of lists(matrix)
    def test_normaluse(self):
        """Testing normal use case"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_listWithFloat(self):
        """Test case: list with float components"""
        self.assertEqual(max_integer([1, 5.2, 3]), 5.2)

    def test_negativeElems(self):
        """Test case: List with negative numbers"""
        self.assertEqual(max_integer([1, +5.2, -2.2, -3]), 5.2)

    def test_None(self):
        """Test case:when None is passed"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_NoneAsElem(self):
        """Test case: test when None is passed a list member"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_nonints(self):
        """Test case: list with non numerical elems"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "one"])

    def test_samevals(self):
        """Test case: list with same values"""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_emptylist(self):
        """Test case: Empty list"""
        self.assertEqual(max_integer([]), None)

    def test_noArgs(self):
        """Test case: No argument passed"""
        self.assertEqual(max_integer(), None)

    def test_matrices(self):
        """Test case: Lists of list(matrices) passed as args"""
        with self.assertRaises(TypeError):
            max_integer([1, [2, 3], 4])

    def test_listOneElem(self):
        """Test case: List with only one element"""
        self.assertEqual(max_integer([2]), 2)

    def test_maxfirst(self):
        """Test case: Case when max int is at the 1st elem"""
        self.assertEqual(max_integer([5, 4, 3]), 5)


if __name__ == '__main__':
    unittest.main()
