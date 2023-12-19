import sys
from math import *
import bisect

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


d = [0 for i in range(200)]


def solve(test):
    t, v = test
    if t == 1:
        d[v] += 1
        return
    else:
        bv = list(bin(v)[2:])
        bv.reverse()
        tmp = d.copy()
        for i in range(len(bv)):
            # print(tmp)
            # print(bv[i])
            if bv[i] == "1" and tmp[i] > 0:
                tmp[i] -= 1
                tmp[i + 1] += tmp[i] // 2
            elif bv[i] == "0":
                tmp[i + 1] += tmp[i] // 2
            elif bv[i] == "1" and tmp[i] == 0:
                return "NO"
    return "YES"


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        tests.append(inlt())
    for test in tests:
        ret = solve(test)
        if ret is not None:
            print(ret)
