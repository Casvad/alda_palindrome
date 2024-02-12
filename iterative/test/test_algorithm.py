import unittest

from ternary.algorithm import ternary_search
from utils.constants_test import arrays, expected


class AlgorithmTest(unittest.TestCase):
    def test_ternary_search(self):
        for i in range(len(arrays)):
            array = sorted(arrays[i][1])
            result = ternary_search(array, arrays[i][0])
            self.assertEqual(result, expected[i])


if __name__ == "__main__":
    unittest.main()
