"""
Heapsort

    O(nlog(n)) sorting thanks to the amazing heap data structure

@author: Gergő Tolnai
"""

from heap import Heap


def heapsort(lst):
    """
    :param lst: list to sort
    :return: sorted list
    """
    h = Heap('extract_min')
    result = []

    for num in lst:
        h.add(num)

    for _ in range(len(lst)):
        next_smallest = h.extract_min()
        result.append(next_smallest)

    return result

# for more extensive tests, see the tests fot the Heap class (heap_test.py)
unsorted = [1, 2, 3, 4, 0, -1, -12]
assert heapsort(unsorted) == sorted(unsorted)
