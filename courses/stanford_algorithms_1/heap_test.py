import math
from heap import Heap

# to be tested with eg. pytest (functions can also be called manually)
# takes ~20-30 secs to run


def test():
    x = Heap('extract_min')
    x.add(5)
    assert x.repr[0] == 5
    x.add(4)
    assert x.repr[0] == 4
    x.add(7)
    assert x.repr[0] == 4
    assert x.repr[2] == 7
    x.add(2)
    assert x.repr[0] == 2
    x.add(3)
    assert x.repr[0] == 2


def test_extract_min():
    x = Heap('extract_min')
    x.add(2)
    x.add(1)
    assert x.repr[0] == 1
    x.extract_min()
    assert x.repr[0] == 2


def test_extract_max():

    x = Heap('extract_max')
    x.add(1)
    x.add(2)
    assert x.repr[0] == 2
    x.extract_max()
    assert x.repr[0] == 1


def check(arr):
    x = Heap('extract_min')

    for num in arr:
        x.add(num)

    # sort the array (this is heapsort)
    sorted_arr = []
    while len(x.repr) > 0:
        sorted_arr.append(x.extract_min())

    # check if the list is sorted
    last_seen = - math.inf
    for num in sorted_arr:
        assert last_seen <= num
        last_seen = num


def test_long():
    import random
    for _ in range(1000):
        lst = [int(1000*random.random()) for _ in range(100)]
        check(lst)


def test_pos_neg():
    import random
    for _ in range(10):
        lst = [random.randint(-100000000, 100000000) for _ in range(1000)]
        check(lst)

regression_set = [
[72, 954, 480, 345, 331, 712, 117, 913, 224, 417, 925, 429, 751, 693, 831, 595, 682, 709, 700, 577, 578, 988, 739, 500, 285, 761, 822, 0, 358, 685, 849, 748, 308, 0, 410, 246, 174, 477, 776, 829, 457, 338, 699, 726, 308, 380, 350, 407, 418, 966, 364, 796, 295, 849, 30, 641, 992, 91, 808, 347, 720, 474, 583, 803, 784, 483, 971, 895, 899, 796, 685, 627, 311, 666, 690, 213, 445, 765, 826, 449, 397, 375, 418, 76, 367, 345, 328, 439, 951, 691, 175, 935, 22, 676, 481, 751, 727, 65, 451, 720]
]


def test_regression():
    for lst in regression_set:
        for i in range(0,len(lst)):
            check(lst[0:i])
