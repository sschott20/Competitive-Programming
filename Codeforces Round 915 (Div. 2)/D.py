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


def prefix_mex(A, n):
    b = [False] * (n + 1)
    mex = 0
    result = [0] * n
    for i in range(n):
        b[A[i]] = True

        while b[mex]:
            mex += 1
        result[i] = mex
    return result


def mexsum(arr):
    return sum(prefix_mex(arr, len(arr)))


def solve(test):
    M = 0
    S = sum(test) / 2
    # print(S)
    for i in range(len(test)):
        tmp = test[i:] + test[:i]
        # print(mexsum(tmp), sum(tmp[: len(tmp) // 2]), tmp)
        if sum(tmp[: len(tmp) // 2]) <= S:
            M = max(M, mexsum(tmp))

    return M


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        tests.append(inlt())
    for test in tests:
        print(solve(test))
