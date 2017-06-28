# Josephus Problem
"""
Find the problem here: https://en.wikipedia.org/wiki/Josephus_problem
Here the value of k is 2 i.e. 2 steps.
"""
import math


def power_two(n):
    return int(math.log(n, 2))


n = int(input())
num = n - 2**power_two(n)
print((2 * num) + 1)
