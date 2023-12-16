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
    tests = []
    file = open("a.txt", "r")
    acc = 0

    for line in file.readlines():
        for c in line:
            if c.isnumeric():
                acc += 10 * int(c)
                break
        for c in reversed(line):
            if c.isnumeric():
                acc += int(c)
                break
    print(acc)
