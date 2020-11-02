"""wargame.test.testcasea

This module contains code to demonstrate unittest.TestSuite

This module is compatible with Python 2.7.9

:copyright: 2020, Jean Tardelli

:license: The MIT License (MIT). See LICENSE file for further details.
"""
import unittest

class MyUnitTestA(unittest.TestCase):
    """A class to help illustrate how to use unitTest.TestSuite"""

    def test_a2(self):
        """
        Checks whether the two input arguments 1+1 and 3 are not equal.
        Otherwise an assertion error is raised.
        """
        print("MyUnitTestA.test_a2")
        self.assertNotEqual(1 + 1, 3)

    def test_a1(self):
        """
        Checks whether the expression argument 1+1 == 2 are equal.
        Otherwise an assertion error is raised.
        """
        print("MyUnitTestA.test_a1")
        self.assertTrue(1 + 1 == 2)

    def not_called_by_defaul(self):
        """
        This function just shows that, by default, the unittest framework
        does not call methods without _test_ as prefix.
        """
        print("MyUnitTestA: This method will not be called by default")
