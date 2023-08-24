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

    t = ['(' for i in test] + [')' for i in test]
    t = "".join(t)
    t2 = ["()" for i in test]
    t2 = "".join(t2)
    if "".join(test) not in t:
        print("YES")
        print(t)
        return
    if "".join(test) in t2:
        print("NO")
        return
    else:
        print("YES")
        print(t2)
        return 
    


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        tests.append(insr())
        continue
    for test in tests:
        solve(test)