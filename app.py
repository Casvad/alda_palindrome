from base.base import BaseSortingTimeGather
from iterative.algorithm import iterative_pal
from recursive.algorithm import recursive_pal
from reverse.algorithm import reverse_pal

if __name__ == "__main__":
    base_gather = BaseSortingTimeGather([iterative_pal, recursive_pal, reverse_pal])
    table = base_gather.take_execution_time(
        minimum_size=100000, maximum_size=1000000, step=50000, samples_by_size=5, probability=100
    )
    for row in table:
        print(row)
