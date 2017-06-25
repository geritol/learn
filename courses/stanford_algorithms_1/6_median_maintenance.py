"""
MedianMaintainer

    maintaining the median of a stream of numbers,
    arriving one by one, using O(log(n))
    operations each step.

@author: Gergő Tolnai
"""


from heap import Heap


class MedianMaintainer:
    def __init__(self):
        self.highHeap = Heap('extract_min')
        self.lowHeap = Heap('extract_max')

    def add(self, value):
        low_max = self.lowHeap.get(0)
        high_min = self.highHeap.get(0)

        if not low_max or not high_min:
            self.highHeap.add(value)
        elif value > high_min:
            self.highHeap.add(value)
        else:
            self.lowHeap.add(value)

        self._balance()
        return self._median()

    def _balance(self):
        """
        if the highHeap or the lowHeap exeeds the other heap by more tha 1 element,
        transfer their first element to the other heap
        """
        high_heap_size = self.highHeap.size
        low_heap_size = self.lowHeap.size

        if high_heap_size > low_heap_size + 1:
            n = self.highHeap.extract_min()
            self.lowHeap.add(n)
        elif low_heap_size > high_heap_size + 1:
            n = self.lowHeap.extract_max()
            self.highHeap.add(n)

    def _median(self):
        high_heap_size = self.highHeap.size
        low_heap_size = self.lowHeap.size
        low_max = self.lowHeap.get(0)
        high_min = self.highHeap.get(0)

        if high_heap_size == 0 and low_heap_size == 0:
            return 0
        elif high_heap_size == low_heap_size:
            return (low_max + high_min) /2
        elif high_heap_size > low_heap_size:
            return high_min
        return low_max
