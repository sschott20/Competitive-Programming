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
    letters = ['v', 'i', 'k', 'a']
    count = 0
    for i in range(len(test[0])):
        for j in range(len(test)):
            if test[j][i] == letters[count]:
                count += 1
                break
        if count > 3:
            return 'YES'
    return 'NO'
    


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        test = []
        n = inlt()[0]
        for i in range(n):
            test.append(insr())
        tests.append(test)
        
    for test in tests:
        print(solve(test))