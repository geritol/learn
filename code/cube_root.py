# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 20:10:45 2016

@author: geritol
"""


def cube_root(x):
    """
    calculates cube root of a num using binary search 
    """

    if x == 0: return 0

    isPositive = x > 0
    x = abs(x)

    counter = 0

    decimal_precision = 8

    integer_part = 0
    float_part = 0

    def cube_root_checker(num):
        nonlocal counter
        #check number
        counter += 1
        cube = exp(num, 3)
        if cube == x:
            return True
        elif cube > x:
            return 'lower'
        elif cube < x:
            return 'higher'

    def cube_root_float_checker(float_part):
        fl = float_part / 10**len(str(float_part))
        n = integer_part + fl
        return cube_root_checker(n)

    def exp(x, z):
        # calculates x**z
        if z == 0: return 1
        res = x
        for i in range(z-1):
            res *= x
        return res


    #init checker
    checker = cube_root_checker

    def int_binary(l, h, checker = checker):
        #does binary search, evaluates int options only
        low = l
        high = h
        num = None

        while True:
            mid = int((low + high) /2)
            check = checker(mid)
            if check == True or low == mid:
                num = mid
                break
            elif high == mid:
                num = low
                break
            elif check == 'lower':
                high = mid
            else:
                low = mid
        return num

    def float_lookup(digits, checker=cube_root_float_checker):
        #looks for the decimal digits of the solution
        low = 0
        hight = exp(10, digits)
        float_part = int_binary(low, hight, checker)
        return float_part / exp(10, len(str(float_part)))

    def int_lookup(checker = checker):
        digits = len(str(x))
        completeDigits = [0 for i in range(digits)]

        for i in range(digits):
            for j in range(1,11):
                testNum = j * exp(10, digits-1 - i)
                test = checker(testNum)
                if test == 'lower' and j == 1:
                    break
                elif test == 'lower':
                    completeDigits[i] = j -1
                    break
                elif test == True:
                    completeDigits[i] = j
                    break
        assembled = assemble(completeDigits, True)
        test = checker(assembled[0])
        return assembled[0] if test == True else int_binary(*assembled)

    def assemble(num_array, isUpLow = False):
        #assembles a num_array
        num = 0
        up = 0
        lenght = len(num_array)
        for i in range(lenght):
            if num_array[i] != 0:

                num += num_array[i] * exp(10,lenght-1-i)
                up += (num_array[i] + 1) * exp(10,lenght-1-i)

        return num if not isUpLow else num, up

    def result(integer_part, float_part = 0):
        num = integer_part + float_part
        numFinal = num if isPositive else -num

        print()
        print(counter)

        if integer_part > 1e16:
            return '%.15e' % numFinal
        return numFinal



    integer_part = int_lookup()
    test = checker(integer_part)
    if test == True:
        return result(integer_part)


    if integer_part > 1e16:
        return result(integer_part)

    float_part = float_lookup(decimal_precision)

    return result(integer_part, float_part)



big_number = 2674999999999999822364316059974953532218933105468753434564564564564564564564564564564564564564564555555555555555555555555555555555555555555555555555555555554564564564564565555
nums = [0,1,-512,100,0.1,0.5,0.57,1,123, 72563.48874662547, 12300000, big_number]
for number in nums:
    print(cube_root(number))
    print(number**(1/3))
