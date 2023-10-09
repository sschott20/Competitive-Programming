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

def solve(pots, t):
    pots = list(reversed(sorted(pots)))
    for i in range(0, len(pots)):
        
        if pots[i] <= t *(len(pots) - (i + 1)):
            # print(i, pots[i])
            return "NO"
    
    return "YES"


if __name__ == "__main__":
    tests = []
    N, T = inlt()
    pots = []
    for i in range(N):
        pots.append(inp())
    print(solve(pots, T))