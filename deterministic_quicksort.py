import random
from typing import List, Any

def deterministic_quicksort(arr: List[Any]) -> List[Any]:
    """
    Sorts the array in ascending order using Deterministic Quicksort.
    Always selects the first element as pivot.

    Args:
        arr (List[Any]): The list to be sorted.

    Returns:
        List[Any]: The sorted list.

    Time Complexity: O(n log n) average, O(n^2) worst-case.
    Space Complexity: O(log n) due to recursion stack.
    """
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[0]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return deterministic_quicksort(less) + equal + deterministic_quicksort(greater)

# Example usage
if __name__ == "__main__":
    test = [3, 5, 1, 2, 5, 4, 1]
    print(deterministic_quicksort(test))
