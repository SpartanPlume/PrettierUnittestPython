"""Only to try the prettier-unittest binary"""

import unittest


class FakeTestCase(unittest.TestCase):
    def test_nothing(self):
        """Test nothing"""
        pass


def suite():
    suite = unittest.TestSuite()
    suite.addTest(FakeTestCase("test_nothing"))
    return suite
