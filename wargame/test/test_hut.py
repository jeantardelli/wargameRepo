"""wargame.test.test_hut

This module contains unit test for wargame.hut.Hut class.

This module is compatible with Python 3.6.x.

:copyright: 2020, Jean Tardelli

:license: The MIT License (MIT). See LICENSE file for further details.
"""

import sys
import unittest

from knight import Knight
from hut import Hut

# Add the top level directory wargame to sys.path
sys.path.append("../")

class TestHut(unittest.TestCase):
    """Contains unit tests for the game Attack of The Orcs.

    .. seealso::

        :py:meth: `wargame.hut.Hut.acquire`
    """
    def setUp(self):
        """Overrides the setUp fixture of the superclass.

        This method is called just before calling each unit test. Here, it
        creates instances of Knight for use by various unit tests.

        .. seealso:: :py:meth: `TestCase.tearDown`
        """
        self.knight = Knight()

    def test_acquire_hut(self):
        """Unittest to verify the hut occupant after it is acquired.

        Unit test ensure that when hut is 'acquired', the `hut.occupant` the
        `hut.occupant` is updated to the `Knight` instance.
        """
        hut = Hut(4, None)
        hut.acquire(self.knight)
        self.assertIs(hut.occupant, self.knight)


if __name__ == '__main__':
    unittest.main()
