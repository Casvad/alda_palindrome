import unittest

from recursive.algorithm import recursive_pal
from utils.constants_test import arrays, expected


class AlgorithmTest(unittest.TestCase):
    def test_recursive_pal(self):
        for i in range(len(arrays)):
            result = recursive_pal(arrays[i])
            expectation = expected[i]
            self.assertEqual(result, expectation)


if __name__ == "__main__":
    unittest.main()
