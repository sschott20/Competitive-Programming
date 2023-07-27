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
    n,k = test[0]
    
    health = test[1]

    health = [ i % k if i % k != 0 else k for i in health]
    health = sorted(list(zip(health,range(1, len(health) + 1))), key = lambda x: (-1 * x[0], x[1]))
    health = list(zip(*health))[1]
    
    return " ".join(str(i) for i in health)


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        tests.append([inlt(), inlt()])
        continue
    for test in tests:
        print(solve(test))