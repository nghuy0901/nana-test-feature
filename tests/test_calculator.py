import unittest

from calculator import double


class DoubleTests(unittest.TestCase):
    def test_doubles_an_integer(self):
        self.assertEqual(double(3), 6)


if __name__ == "__main__":
    unittest.main()
