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
    odd = 0
    for a in test:
        if a % 2 == 1:
            odd += 1
    
    if odd == 0 or odd % 2 == 0:
        return "YES"
    else: 
        return "NO"


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        tests.append(inlt())
        continue
    for test in tests:
        print(solve(test))