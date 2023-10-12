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


if __name__ == "__main__":
    n = inp()
    dp = [-1 for i in range(31)]
    dp[0] = 1
    dp[1] = 0
    dp[2] = 3
    dp[3] = 0
    dp[4] = 11
    res = []
    while n != -1:
        if n % 2 == 1:
            res.append(0) 
        elif dp[n] != -1:
            res.append(dp[n])
        else:
            for k in range(5, n + 1):
                if dp[k] != -1:
                    continue
                dp[k] = 3 * dp[k - 2]
                for j in range(k-4, -1, -2):
                    dp[k] += 2*dp[j]

            res.append(dp[n])
        n = inp()
    
    for d in res:
        print(d)
