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
    dp = {}
    prefix = []
    acc = 0
    sorted_list = sorted(test)

    for i in sorted_list:
        if len(prefix) == 0:
            prefix.append(i)
        else:
            prefix.append(prefix[-1] + i)
    # iterate backwards through the sorted list
    for i in range(len(sorted_list) - 1, -1, -1):
        if i == len(sorted_list) - 1:
            dp[sorted_list[i]] = len(sorted_list) - 1
        else:
            pre = prefix[i]
            val = sorted_list[i]
            nxt = sorted_list[i + 1]
            if pre >= nxt:
                dp[val] = dp[nxt]
            else:
                dp[val] = i

    ret = []
    for i in test:
        ret.append(dp[i])

    return " ".join(map(str, ret))


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        n = inp()
        tests.append(inlt())
        continue
    for test in tests:
        print(solve(test))
