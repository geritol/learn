"""
Cube root approximation using Newton's method (also known as the Newton–Raphson method)
More on it: https://en.wikipedia.org/wiki/Newton%27s_method
The goal is to approximate the cube root of a number using only basic arithmetic operators (+,-,*,/)
precision: 8 decimal places
"""

import random

def approximate(x, goal):
    def f(x): return x*x*x - goal
    def fd(x): return 3*x*x
    precision = 1e-08 if goal < 1000 else 1e-04

    if abs(f(x)) < precision: return x

    return approximate(x-f(x)/fd(x), goal)


def test(x):
    approx = approximate(x, x)
    real = x ** (1 / 3)
    assert abs(approx - real) <= 1e-08, 'for {}, approximate() calculated {} as root, while root is {}'.format(x, approx, real)


for num in [0, 0.1, 0.5, 2**(1/2), 2, 3, 11, 250]:
    test(num)

for i in range(10000):
    x = random.uniform(0, 100000000000)
    test(x)

for i in range(10000):
    x = random.randint(0, 100000000000)
    test(x)