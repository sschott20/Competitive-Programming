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
    b,c,h = test
    fill = c + h
    if fill - 1 > b - 2 :
        return 2 + (2 * (b - 2)) + 1
    else: 
        return 2 + ( 2 * fill) - 1


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        tests.append(inlt())
        continue
    for test in tests:
        print(solve(test))