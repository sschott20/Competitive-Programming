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
    n, k = test[0], test[1]
    a = test[2]
    b = test[3]
    prefix_sum = []
    prefix_max = []

    for i in range(n):
        if i == 0:
            prefix_sum.append(a[i])
            prefix_max.append(b[i])
        else:
            prefix_sum.append(prefix_sum[i - 1] + a[i])
            prefix_max.append(max(prefix_max[i - 1], b[i]))
    ret = []
    # print(a)
    # print(b)
    # print(prefix_sum)
    # print(prefix_max)
    for i in range(min(n, k)):
        # print(i, k - i)

        val = prefix_sum[i] + (k - i - 1) * prefix_max[i]
        ret.append(val)
    # print(ret)
    return max(ret)

    return


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        n, k = inlt()
        a = inlt()
        b = inlt()
        tests.append([n, k, a, b])
        continue
    for test in tests:
        print(solve(test))
