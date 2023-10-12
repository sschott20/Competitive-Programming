import sys
from math import *


def primeFactors(n):
    acc = [1]
    while n % 2 == 0:
        acc.append(2)
        n = n // 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            acc.append(i)
            n = n // i
    if n > 2:
        acc.append(n)
    return acc

input = sys.stdin.readline


############ ---- Input Functions ---- ############
def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


def solve(test):
    a = []
    for t in test:
        a.append(primeFactors(t))
    # print(a)
    d = {}
    for t in a:
        for f in t:
            if f in d:
                d[f] += 1
            else:
                d[f] = 1

    val = d.values()
    # print(d)
    # print(val)
    for v in val:
        if v % len(test) != 0:
            return "NO"
    return "YES"


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        tests.append(inlt())
    for test in tests:
        print(solve(test))
