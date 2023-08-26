import sys
from math import *

input = sys.stdin.readline

def findFirstOccurrence(target):
 
    (left, right) = (0, max(target, 100))
 
    result = -1
 
    while left <= right:
 
        mid = (left + right) // 2
        if target ==( mid * (mid - 1)) / 2:
            return mid
            
 
        elif target < ( mid * (mid - 1)) / 2:
            right = mid - 1
 
        else:
            left = mid + 1
 
    if result == -1:
        return left - 1
    else: 
        return result

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
    n = findFirstOccurrence(test)
    # print(n, test, n * (n - 1) // 2)


    return n + (test - (n * (n - 1) // 2))


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        tests.append(inp())
        
    for test in tests:
        print(solve(test))