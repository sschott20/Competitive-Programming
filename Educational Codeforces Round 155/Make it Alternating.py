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

    mode = None
    if test[0] == "0":
        mode = 1
    else:
        mode = 0
    final = []
    for c in test:
        if c == '0' and mode == 1:
            final.append(1)
            mode = 0
        elif c == '1' and mode == 0:
            final.append(1)
            mode = 1
        else:
            final[-1] += 1
    n_acc = 0

    for f in final:
        if f != 1:
            n_acc += f - 1

    result = 1
    for x in final:
        result = result * x

    

    print(n_acc, (result * factorial(n_acc)) % 998244353)



if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        tests.append(insr())
        continue
    for test in tests:
        solve(test)