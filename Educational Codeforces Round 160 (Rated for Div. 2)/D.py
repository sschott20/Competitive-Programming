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
    MOD = 998244353
    return count_reachable_arrays(len(test), test, MOD)


def count_reachable_arrays(n, p, MOD):
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one way to reach an empty array

    for i in range(1, n + 1):
        stack = []  # Stack to store pairs (element, dp value)
        for j in range(i, 0, -1):
            # Remove elements from the stack that are greater than p[j - 1]
            while stack and stack[-1][0] > p[j - 1]:
                stack.pop()
            if not stack:
                dp[i] = (dp[i] + dp[j - 1]) % MOD
            else:
                dp[i] = (dp[i] + dp[j - 1] - dp[stack[-1][1]] + MOD) % MOD
            stack.append((p[j - 1], j - 1))

    return dp[n]


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        tests.append(inlt())
    for test in tests:
        print(solve(test))
