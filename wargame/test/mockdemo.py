"""wargame.test.mockdemo

This module contains a demo for Mock class.

This module is compatible with Python 3.6.x.

:copyright: 2020, Jean Tardelli

:license: The MIT license (MIT). See LICENSE file for further details.
"""
import unittest
from unittest.mock import Mock, call

class MyClassA:
    """Class for mock demo"""

    def foo(self):
        """Return a number.

        Created to illustrate the use of Mock objects.
        """
        # Assume it does some lenghty computation here.
        # (not shown in this trivial example)
        return 120

    def foo2(self, num):
        """Return a number.

        Creates to illustrate the use of Mock objects.
        """
        # Assume it does some lengthy computation here.
        # (not shown in this trivial example)
        return num + 50

    def compute(self):
        """Demonstrate the use of Mock objects"""
        val1 = self.foo()
        val2 = self.foo2(val1)
        print("val1 = {0}, val2 = {1}".format(val1, val2))
        result = val2 + val1
        print("In MyClassA.compute, result: val1 + val2 = {0}".format(result))
        return result


class TestA(unittest.TestCase):
    """Write test cases for methods from class MyClassA"""

    def test_compute(self):
        """Unit test for MyClassA.compute"""
        myobj = MyClassA()

        # Create a mock object and mock methods of MyClassA
        mockobj = Mock()
        myobj.foo = mockobj.foo
        myobj.foo2 = mockobj.foo2

        # Assuming you know the return values, set those for the mocks
        myobj.foo.return_value = 120
        myobj.foo2.return_value = 170

        # Run the computation. Calls to foo and foo2 in compute method are
        # now replaced with mock object calls that return the desired values
        result = myobj.compute()

        # Verify the results
        self.assertEqual(result, 290)

        # Get info on how the mock objects are actually called by compute
        test_call_list = mockobj.mock_calls
        print("test_call_list = {0}".format(test_call_list))

        # Compare it against some reference calling order
        reference_call_list = [call.foo(), call.foo2(120)]
        self.assertEqual(test_call_list, reference_call_list)

    def test_compute_with_patch(self):
        """Unit test for MyClassA.compute using mock.patch"""
        print("Running test_compute_with_patch...")
        with unittest.mock.patch(__name__+'.MyClassA.foo', new=Mock(return_value=1)):
            myobj = MyClassA()
            result = myobj.compute()

            # Verify the results. The test is expected to fail since we are
            # using a return value of 1 using MyClassA.foo!
            self.assertEqual(result, 270)

    def test_compute_with_patch_alternate(self):
        """Unit test for MyClassA.compute, using mock.patch

        .. note:: This uses `mock.patch` but does not use the `new` argument.
        """
        print("Running test_compute_with_patch_alternate...")
        with unittest.mock.patch(__name__+'.MyClassA.foo') as foo_patch:
            foo_patch.return_value = 1
            myobj = MyClassA()
            result = myobj.compute()

            # Verify the results. The test is expected to fails since we are
            # using a return value of 1 using MyClassA.foo!
            self.assertEqual(result, 270)

if __name__ == '__main__':
    unittest.main()
