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
    zeros = 0
    test = [int(x) for x in str(test)]
    test.reverse()
    i = 0
    while i < len(test):
        if test[i] <= 4:
            i += 1
        elif test[i] >= 5:
            if i >= len(test) - 1:
                test.append(0)
                zeros = i + 1
            else:
                i += 1
                while test[i] == 9:
                    i += 1
                    if i >= len(test):
                        test.append(0)
                        zeros = i
                        break
                test[i] += 1
                zeros = i
    for i in range(0, zeros):
        test[i] = 0
    test.reverse()
    test = [str(x) for x in test]

    return int("".join(test))


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        tests.append(inp())
        continue
    for test in tests:
        print(solve(test))
