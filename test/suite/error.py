"""Only to try the prettier-unittest binary"""

import unittest


class FakeErrorTestCase(unittest.TestCase):
    def test_error(self):
        """Test nothing but show an error"""
        self.assertTrue(False)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(FakeErrorTestCase("test_error"))
    return suite
