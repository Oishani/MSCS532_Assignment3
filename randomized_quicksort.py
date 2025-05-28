import random
from typing import List, Any

def randomized_quicksort(arr: List[Any]) -> List[Any]:
    """
    Sorts the array in ascending order using Randomized Quicksort.
    The pivot is chosen randomly to avoid worst-case time complexity
    on sorted or repeated input.

    Args:
        arr (List[Any]): The list to be sorted.

    Returns:
        List[Any]: The sorted list.

    Time Complexity: O(n log n) average, O(n^2) worst-case.
    Space Complexity: O(log n) due to recursion stack (in-place sorting).
    """

    # Base case: an empty or single-element array is already sorted
    if len(arr) <= 1:
        return arr[:]
    
    # Randomly select a pivot and partition the array
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    
    # Partition step: create three lists for <, =, > pivot
    less = []
    equal = []
    greater = []

    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    
    # Recursive sort and combine
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

# ----- Example Usage and Test Cases -----

if __name__ == "__main__":
    # Edge Cases
    test_cases = [
        [],                      # empty array
        [1],                     # single element
        [2, 2, 2],               # all elements equal
        [3, 2, 1],               # descending
        [1, 2, 3],               # already sorted
        [5, 1, 8, 3, 7, 9, 2],   # random order
        [3, 5, 3, 1, 2, 2, 1],   # repeated elements
    ]
    
    for i, test in enumerate(test_cases):
        print(f"Test case {i+1}: Input: {test}")
        sorted_arr = randomized_quicksort(test)
        print(f"           Sorted: {sorted_arr}\n")
