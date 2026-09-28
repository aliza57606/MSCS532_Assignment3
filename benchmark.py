import sys
import random
import time

from randomized_quicksort import randomized_quicksort
from deterministic_quicksort import deterministic_quicksort
sys.setrecursionlimit(10000)
def measure_time(sort_function, arr):
    test_arr = arr.copy()

    start_time = time.perf_counter()
    sort_function(test_arr, 0, len(test_arr) - 1)
    end_time = time.perf_counter()

    return end_time - start_time

def generate_test_arrays(size):
    random_array = [random.randint(0, size) for _ in range(size)]

    sorted_array = list(range(size))

    reverse_sorted_array = list(range(size, 0, -1))

    repeated_array = [random.randint(0, 10) for _ in range(size)]

    return {
        "Random": random_array,
        "Sorted": sorted_array,
        "Reverse Sorted": reverse_sorted_array,
        "Repeated Elements": repeated_array
    }

sizes = [100, 500, 1000]

for size in sizes:
    print(f"\nArray Size: {size}")

    test_arrays = generate_test_arrays(size)

    for array_type, arr in test_arrays.items():
        randomized_time = measure_time(randomized_quicksort, arr)
        deterministic_time = measure_time(deterministic_quicksort, arr)

        print(f"{array_type}:")
        print(f"  Randomized Quicksort:    {randomized_time:.6f} seconds")
        print(f"  Deterministic Quicksort: {deterministic_time:.6f} seconds")