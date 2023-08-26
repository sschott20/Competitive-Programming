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
    n,m,d  = test[0]
    a = test[1]
    print(n,m,d,a)

    table = [[0 for i in range(len(a))] for j in range(m)]
  

    return


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        
        n,m,d = inlt()
        tests.append([(n,m,d), inlt()])
    for test in tests:
        print(solve(test))