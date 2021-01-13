import unittest
import math 

class TestCalc(unittest.TestCase):

    def test_square(self):
        self.assertEqual(math.square(3), 9, 'Shoul Return 9!')

if __name__ == '__main__':
    unittest.main()