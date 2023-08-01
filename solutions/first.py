"""
Solution to the first exercise.
"""

from collections import Counter
from typing import List


def find_duplicate_elements(lst: List[str]) -> List[str]:
    """
    Find duplicate elements in a list. Create a Counter object from the list 
    and return the keys with values greater than 1.
    The implementation ensures only one pass over the list.

    Time complexity: O(n), where n is the length if the input list.
    Space complexity: O(u), where u is the number of unique elements in the input list.

    Args:
        lst (List[str]): List of strings.

    Returns:
        List[str]: List of duplicate elements.

    Examples:
        >>> find_duplicate_elements(["b", "a", "c", "c", "e", "a", "c", "d", "c", "d"])
        ["a", "c", "d"]
    """
    # Note: the Counter library is used for style purposes, but it is very easy to replicate fully natively as follows:
    # counter = {}
    # for c in lst:
    #     if c not in counter:
    #         counter[c] = 1
    #     else:
    #         counter[c] += 1
    # We can also use defaultdict for this.
    counter = Counter(lst)
    return [key for key, value in counter.items() if value > 1]
