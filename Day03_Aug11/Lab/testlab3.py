import unittest
from lab3 import *

class labtest(unittest.TestCase):

    def test_shout(self):
        self.assertEqual(shout("Hello."), 'HELLO!')
        with self.assertRaises(Exception):
            shout(2)
    def test_reverse(self):
        self.assertEqual(reverse("Name"), "emaN")
        with self.assertRaises(Exception):
            reverse("Hello World")
        with self.assertRaises(Exception):
            reverse(2)
    def test_reversewords(self):
        self.assertEqual(reversewords("Hello world!"), "world! Hello")
        with self.assertRaises(Exception):
            reversewords(2)
    def test_reversewordletters(self):
        self.assertEqual(reversewordletters("Hello world!"), "!dlrow olleH")
        with self.assertRaises(Exception):
            reversewordletters(2)
            
if __name__ == '__main__':
        unittest.main()
