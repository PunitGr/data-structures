# Josephus Problem
"""
Find the problem here: https://en.wikipedia.org/wiki/Josephus_problem
It will work for any value of k(Steps).
"""

def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1


n, k = map(int, input().split())
print(josephus(n, k))
