import sys
from math import *

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
    res = []
    n, l = test
    check = sorted(l)
    # print(check,l)
    d = dict()
    sumsmall = []
    sumbig = []
    acc = 0
    for i in check:
        sumsmall.append(acc)
        acc += i

    acc = 0
    for i in reversed(check):
        sumbig.append(acc)
        acc += i
    sumbig.reverse()

    for i in range(len(sumsmall)):
        d[check[i]] = [sumsmall[i], sumbig[i], i]

    for s in l:
        L, R, i = d[s]
        res.append(s * i - L + R - s * (n - i - 1) + n)
        # print(sumsmall, sumbig)
    res = [str(i) for i in res]
    res = " ".join(res)
    return res


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        tests.append([inp(), inlt()])
    
    for test in tests:
        print(solve(test))