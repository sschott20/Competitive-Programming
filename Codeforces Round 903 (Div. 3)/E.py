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

def rec(a):
    print(a)
    if len(a) == 0:
        return 0
    tmp = []
    for i in range(len(a)):
        tmp.append(i - a[i])
    

    return max(len(a), min(tmp)) + rec(a[tmp.index(min(i for i in tmp if i > 0)) + 1:])

def solve(test):
    test.reverse()
    
    return rec(test)

if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        tests.append(inlt())
    for test in tests:
        print(solve(test))