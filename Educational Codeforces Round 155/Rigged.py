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
    strength = test[0][0]
    endurence = test[0][1]

    for i in range(1, len(test)):
        if test[i][0] >= strength and test[i][1] >= endurence:
            return -1
    return strength

if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        test = []
        num_ath = inp()

        for j in range(num_ath):
            test.append(inlt())
        tests.append(test)

    for test in tests:
        print(solve(test))
