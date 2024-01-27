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
    top, left, bottom, right = 0, 0, 0, 0
    for point in test:
        x = point[0]
        y = point[1]
        if x > 0:
            right += 1
        elif x < 0:
            left += 1
        if y > 0:
            top += 1
        elif y < 0:
            bottom += 1
    if top == 0 or bottom == 0 or left == 0 or right == 0:
        return "YES"
    return "NO"


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        n = inp()
        test = []
        for i in range(n):
            test.append(inlt())
        tests.append(test)
    for test in tests:
        print(solve(test))
