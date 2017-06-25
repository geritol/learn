MedianMaintainer = __import__('6_median_maintenance').MedianMaintainer

"""
to be tested with eg pytest or ptw (pytest-watch) (functions can also be called manually)
total test runtime ~ 45 secs
"""


def test():
    import random
    for i in range(100):
        random_list = [int(1000*random.random()) for _ in range(1000)]
        compare(random_list)


def test_pos_neg():
    import random
    for i in range(100):
        random_list = [random.randint(-100000000, 100000000) for _ in range(1000)]
        compare(random_list)


def compare(lst):
    from statistics import median
    m = MedianMaintainer()
    median_calculated = 0
    for number in lst:
        median_calculated = m.add(number)
    print(median_calculated)
    print(median(lst))
    assert median(lst) == median_calculated, lst

regression_set = [
[820, 257, 686, 674, 108, 626, 454, 12, 238, 69, 430, 92, 532, 331, 576, 316, 218, 333, 274, 263, 34, 916, 41, 211, 228, 63, 774, 538, 459, 743, 287, 187, 405, 371, 763, 158, 47, 263, 128, 871, 152, 571, 53, 487, 373, 724, 748, 303, 516, 380, 846, 718, 994, 209, 238, 734, 989, 68, 807, 597, 632, 208, 45, 563, 228, 892, 221, 633, 744, 64, 593, 758, 958, 703, 883, 715, 451, 605, 664, 718, 998, 139, 874, 563, 730, 793, 635, 126, 965, 376, 224, 871, 766, 970, 368, 772, 373, 972, 347, 77],
[963, 745, 754, 881, 380, 617, 504, 425, 139, 816, 810, 667, 713, 705, 825, 343, 808, 796, 225, 741, 907, 311, 416, 651, 389, 636, 395, 991, 135, 836, 624, 742, 565, 253, 689, 615, 473, 757, 902, 792, 585, 438, 409, 717, 700, 471, 145, 424, 724, 459, 618, 878, 32, 893, 679, 552, 616, 797, 923, 981, 140, 854, 758, 77, 502, 439, 642, 329, 337, 241, 59, 473, 713, 131, 658, 585, 65, 515, 494, 401, 371, 970, 107, 861, 275, 850, 461, 872, 16, 708, 219, 861, 794, 837, 392, 958, 194, 315, 995, 277]
]


def test_regression():
    for lst in regression_set:
        compare(lst)
