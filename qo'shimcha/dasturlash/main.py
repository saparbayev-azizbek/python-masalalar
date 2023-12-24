import unittest
from funk import factorial, prg

class funkTest(unittest.TestCase):
    def test_funk(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(4), 24)

    def test_prg(self):
        self.assertEqual(prg(5), 15)
        self.assertEqual(prg(4), 10)


unittest.main()
