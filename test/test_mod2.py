import mod2
import unittest

class TestMod2(unittest.TestCase):

    def test_add_num(self):

        self.assertTrue(mod2.is_positive(1))
        self.assertFalse(mod2.is_positive(0))
        self.assertFalse(mod2.is_positive(-1))
