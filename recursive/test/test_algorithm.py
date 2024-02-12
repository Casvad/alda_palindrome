import unittest

from binary.algorithm import binary_search
from utils.constants_test import arrays, expected


class AlgorithmTest(unittest.TestCase):
    def test_binary_search(self):
        for i in range(len(arrays)):
            array = sorted(arrays[i][1])
            result = binary_search(array, arrays[i][0])
            self.assertEqual(result, expected[i])


if __name__ == "__main__":
    unittest.main()
