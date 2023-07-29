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
    cnt = 0
    for i in range(len(test)):
        if test[i] == i + 1:
            cnt += 1
    if cnt % 2 == 0:
        return int(cnt / 2) 
    
    else: 
        return int(((cnt - 1) / 2) + 1)
    return


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        n = inp()
        tests.append(inlt())
        
    for test in tests:
        print(solve(test))