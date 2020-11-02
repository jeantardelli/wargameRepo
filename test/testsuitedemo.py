"""wargame.test.testsuitedemo

This module contains code to demonstrate the unittest.TestSuite.

This module is compatible with Python 2.7.9.

:copyright: 2020, Jean Carlo

:license: The MIT License (MIT). See LICENSE file for further details.
"""
import unittest
from testcasea import MyUnitTestA
from testcaseb import MyUnitTestB

def suite():
    """ Return a composite testsuite that aggregates two testsuits.

    These sub-testsuites, in turn, aggregate all the tests in classes
    `MyUnitTestA` and `MyUnitTestB`.

    :return: Instance of `unittest.TestSuite`
    """

    # Create a test suite by collecting all test cases defined in MyUnitTestA.
    # By default it only looks for methods starting with test*
    suite_a = unittest.makeSuite(MyUnitTestA)

    # Similarly, create suite_b using testcases from MyUnitTestB
    suite_b = unittest.makeSuite(MyUnitTestB)

    # Add a new testcase to suite_b.
    suite_b.addTest(MyUnitTestB("not_called_by_default"))

    # Return a composite test suite containing suite_a and suite_b
    return unittest.TestSuite((suite_a, suite_b))

if __name__ == '__main__':

    # Run the tests
    unittest.main(defaultTest='suite')
