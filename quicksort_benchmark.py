import random
import time
from randomized_quicksort import randomized_quicksort
from deterministic_quicksort import deterministic_quicksort

# Increase the maximum recursion depth to allow quicksort to process larger arrays.
# This is necessary because deterministic quicksort on sorted or reverse-sorted input
# can result in deep recursion (up to n levels), which exceeds Python's default limit.
import sys
sys.setrecursionlimit(10000)

def time_sort(func, arr):
    """
    Returns time in seconds to sort arr using func.
    If RecursionError occurs, returns the string 'RecursionError'.
    """
    arr_copy = arr[:]
    try:
        import time
        start = time.time()
        func(arr_copy)
        end = time.time()
        return end - start
    except RecursionError:
        return "RecursionError"

def generate_arrays(size):
    return {
        "Random": [random.randint(0, size) for _ in range(size)],
        "Sorted": list(range(size)),
        "Reverse": list(range(size, 0, -1)),
        "Repeated": [random.choice([1, 2, 3, 4, 5]) for _ in range(size)],
    }

def run_all_tests():
    sizes = [1000, 5000, 10000, 50000]
    sorts = [("RandomizedQuicksort", randomized_quicksort),
             ("DeterministicQuicksort", deterministic_quicksort)]
    results = []

    for size in sizes:
        arrays = generate_arrays(size)
        for arr_name, arr in arrays.items():
            for sort_name, sort_func in sorts:
                times = [time_sort(sort_func, arr) for _ in range(3)]
                # Check if any run returned an error string
                if all(isinstance(t, float) for t in times):
                    avg_time = sum(times) / len(times)
                    print(f"{sort_name} | {arr_name} | n={size} | Avg Time: {avg_time:.5f}s")
                else:
                    avg_time = "RecursionError"
                    print(f"{sort_name} | {arr_name} | n={size} | Avg Time: {avg_time}")
                results.append((sort_name, arr_name, size, avg_time))
    return results

if __name__ == "__main__":
    run_all_tests()
