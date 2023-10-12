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


def solve(s):
    for i in range(len(s)):
        if i + 1 < len(s):
            if s[i] == "s" and s[i + 1] == "s":
                print("hiss")
                return
    print("no hiss")
        


if __name__ == "__main__":
    s = insr()
    solve(s)
