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

# xor with a ^ b 
def solve(test):
    acc = 0
    for i in range(len(test)):
        


    return


if __name__ == "__main__":
    tests = []
    num_tests = inp()

    for i in range(num_tests):
        tests.append(inlt())
        continue
    for test in tests:
        print(solve(test))