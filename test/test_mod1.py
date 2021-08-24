import mod1
import unittest

class TestMod1(unittest.TestCase):

    def test_add_num(self):

        self.assertEqual(7, mod1.add_num(1, 6))