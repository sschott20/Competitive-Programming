import sys
import math

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


def calc_desorted(test):
    min = None
    for i in range(0, len(test) - 1):
        diff = abs(test[i] - test[i + 1])
        steps = math.floor(diff / 2) + 1

        if min == None or steps < min:
            min = steps
        if test[i] > test[i + 1]:
            min = 0

    return min


if __name__ == "__main__":
    num_tests = inp()
    tests = []
    for i in range(num_tests):
        test_size = inp()
        tests.append(inlt())
    for test in tests:
        print(calc_desorted(test))
