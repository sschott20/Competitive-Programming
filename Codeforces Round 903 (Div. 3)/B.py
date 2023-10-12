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


def solve(a,b,c):
    target = min(a,b,c)
    if a == b and a == c:
        return "YES"
    acc = 0
    for i in range(0, 3):
        if a > target:
            a -= target
            acc += 1
        if b > target:
            b -= target
            acc += 1
        if c > target:
            c -= target
            acc += 1
    if a == b and a == c and acc <= 3:
        return "YES"

    
    return "NO"


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        a,b,c = inlt()
        tests.append([a,b,c])
    for test in tests:
        print(solve(test[0], test[1], test[2]))
