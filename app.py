import sys

from base.base import BaseSortingTimeGather
from binary.algorithm import binary_search
from linear.algorithm import linear_search
from ternary.algorithm import ternary_search

if __name__ == "__main__":
    base_gather = BaseSortingTimeGather([binary_search, linear_search, ternary_search])
    table = base_gather.take_execution_time(minimum_size=1000000, maximum_size=100000000, step=1000000, samples_by_size=5)
    for row in table:
        print(row)
