"""
Heap

    data structure that can be used to access and maintain min or max of values
    2 important supported operations:
        add         -> O(log n) # adds a simgle element
        extract_min -> O(log n) # or extract_max

    NOT IMPLEMENTED:
        heapify initialise a heap in linear time (opposed to n log n with individual inserts)

    usages: repeated minimum or maximum computations, sorting (see 7_heapsort.py), priority queues,
            median maintenance (see 6_median_maintenance.py)

@author: Gergő Tolnai
"""


class Heap:
    def __init__(self, supported_operation):
        self.supported_operations = ['extract_min', 'extract_max']
        if supported_operation not in self.supported_operations:
            raise ValueError('Heap should be initialised with one of the following supported operation {}.'
                             ' Got: {}'.format(self.supported_operations, supported_operation))
        self.supported_operation = supported_operation
        self.operator = '<' if(self.supported_operation == 'extract_min') else '>'
        self.repr = []

    def get(self, index):
        """
        gets an element by index
        returns None if not in the self.repr list
        """
        if index is None or index > len(self.repr) -1 or index < 0:
            return None
        return self.repr[index]

    def add(self, value):
        """
        add a value to the heap
        """
        self.repr.append(value)
        heap_length = len(self.repr)
        if heap_length > 1:
            self._bubble_up(heap_length - 1)

    def extract_min(self):
        """
        extracts the minimum value from the Heap
        :return: the extracted element
        """
        return self._extract('extract_min')

    def extract_max(self):
        """
        extracts the maximum value from the Heap
        :return: the extracted element
        """
        return self._extract('extract_max')

    @property
    def size(self):
        return len(self.repr)

    def _get_parent_index(self, elements_index):
        return (elements_index - 1) // 2

    def _get_children_indexes(self, elements_index):
        left_child_index = elements_index * 2 + 1
        right_child_index = elements_index *2 + 2
        max_index = len(self.repr) - 1
        left_child_index = left_child_index if left_child_index <= max_index else None
        right_child_index = right_child_index if right_child_index <= max_index else None
        return left_child_index, right_child_index

    def _compare(self, index1, index2):
        value1, value2 = self.get(index1), self.get(index2)
        if value1 is None and value2 is None:
            return None
        if value1 is None:
            return index2
        if value2 is None:
            return index1
        return index1 if eval('{}{}{}'.format(value1, self.operator, value2)) else index2

    def _bubble_up(self, elements_index):
        """
        bubbles up an element until parent elements are bigger/smaller depending on the supported operation
        if the heap supports extract_min operations the element is bubbled up until parent elements are bigger
        if the heap supports extract_max operations the element is bubbled up until parent elements are lower
        :param elements_index: the element's index to bubble up
        :return:
        """

        while True:
            element = self.repr[elements_index]
            parent_index = self._get_parent_index(elements_index)
            if parent_index < 0:
                break
            parent = self.repr[parent_index]
            comparison = eval('{}{}{}'.format(element, self.operator, parent))
            if not comparison:
                break

            # switch the elements
            self.repr[parent_index], self.repr[elements_index] = element, parent
            elements_index = parent_index

    def _bubble_down(self, elements_index):
        """
        bubbles down and deletes and element specified by index
        :param elements_index: the element's index to remove
        :return: the removed elements value
        """

        to_remove = self.repr[elements_index]
        to_be_removed_index = elements_index
        self.repr[elements_index] = self.repr[-1]
        self.repr.pop()

        while True:
            left_child_index, right_child_index = self._get_children_indexes(to_be_removed_index)
            min_child_index = self._compare(left_child_index, right_child_index)
            min_index = self._compare(min_child_index, to_be_removed_index)
            if not min_child_index or min_index == to_be_removed_index:
                break

            self.repr[to_be_removed_index], self.repr[min_child_index] = self.repr[min_child_index], self.repr[
                to_be_removed_index]
            to_be_removed_index = min_child_index
        return to_remove

    def _extract(self, operation):
        if self.supported_operation != operation:
            raise TypeError('{} heap does not support {} operations!'.format(self.supported_operation, operation))

        return self._bubble_down(0)
