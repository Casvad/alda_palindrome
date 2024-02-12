import unittest

from iterative.algorithm import iterative_pal
from utils.constants_test import arrays, expected


class AlgorithmTest(unittest.TestCase):
    def test_iterative_pal(self):
        for i in range(len(arrays)):
            result = iterative_pal(arrays[i])
            expectation = expected[i]
            self.assertEqual(result, expectation)


if __name__ == "__main__":
    unittest.main()
