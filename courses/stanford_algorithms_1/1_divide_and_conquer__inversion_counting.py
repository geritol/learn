
def sort_and_count(lst):
    """
    Uses merge sort to sort the input integer list, and keeps track of inversions while doing this
    Used to find "similarity" between two rankings. Defines a measure that tells us how far the
    list is from being in ascending order.
    :param lst: list of unique ints
    :return: tuple with the sorted list at its first place, and the inversion count as the second
    """
    if len(lst) <= 1: return lst, 0

    split_at_index = len(lst)//2
    list_a, inversion_count = sort_and_count(lst[0:split_at_index])
    list_b, inversion_count_b = sort_and_count(lst[split_at_index:])

    inversion_count += inversion_count_b
    list_a_next_index = list_b_next_index = 0
    result = []

    for i in range(len(lst)):

        if list_a[list_a_next_index] < list_b[list_b_next_index]:
            result.append(list_a[list_a_next_index])
            list_a_next_index += 1
        elif list_a[list_a_next_index] > list_b[list_b_next_index]:
            result.append(list_b[list_b_next_index])
            list_b_next_index += 1
            inversion_count += len(list_a[list_a_next_index:])
        else:
            raise ValueError('The list contains two matching values.')

        if list_a_next_index == len(list_a) or list_b_next_index == len(list_b):
            result += list_a[list_a_next_index:] + list_b[list_b_next_index:]
            break

    return result, inversion_count


def calculate_inversion_count(lst):
    result, count = sort_and_count(lst)
    return count

assert calculate_inversion_count([1, 2, 3, 4]) == 0
assert calculate_inversion_count([1, 3, 5, 2, 4, 6]) == 3
