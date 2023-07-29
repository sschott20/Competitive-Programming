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
 
    i = 1
    cnt = 0

    while i < max(test, 100):

        if test % i == 0:
            cnt += 1
        else:
            break
        
        i += 1
    
    return cnt



if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        tests.append(inp())
        
    for test in tests:
        print(solve(test))