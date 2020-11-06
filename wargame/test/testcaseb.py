"""wargame.test.testcaseb

This module contains code to demonstrate unittest.TestSuite

This module is compatible with Python 2.7.9

:copyright: 2020, Jean Tardelli

:license: The MIT License (MIT). See LICENSE file for further details.
"""

import unittest

class MyUnitTestB(unittest.TestCase):
    """A Class to help illustrate how to use unitTest.TestSuite"""
    def test_b2(self):
        """
        Checks whether the two input arguments 4*4 and 15 are not equal.
        Otherwise an assertion error is raised.
        """
        print("MyUnitTestB.test_b2")
        self.assertNotEqual(4*4, 15)

    def test_b1(self):
        """
        Checks whether the argument expression 4+4 == 8 are equal.
        Otherwise an assertion error is raised.
        """
        print("MyUnitTestB.test_b1")
        self.assertTrue(4+4 == 8)

    def not_called_by_default(self):
        """
        This function just shows that, by default, the unittest framework
        does not call methods without _test_ as prefix.
        """
        print("MyUnitTestB: This method will not be called by default")
