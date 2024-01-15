import timeit
import random
from goit_algo_hw4_task1_methods import insertion_sort, merge_sort, timsort, timsorted


if __name__ == "__main__":
    l = [i for i in range(1000)]
    random.shuffle(l)
    print(f"Insertion sort: {timeit.timeit(lambda: insertion_sort(l), number=100)}")
    print(f"Merge sort: {timeit.timeit(lambda: merge_sort(l), number=100)}")
    print(f"Tim sort: {timeit.timeit(lambda: timsort(l), number=100)}")
    print(f"Tim sorted: {timeit.timeit(lambda: timsorted(l), number=100)}")
