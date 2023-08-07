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
    return


if __name__ == "__main__":
    tests = []

    while True:
        final = []
        n = inlt()
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                final.append(min(n[i], n[j]))
        final.sort()
        final = [str(x) for x in final]
        final = " ".join(final)
        print(len(n))
        print(final)