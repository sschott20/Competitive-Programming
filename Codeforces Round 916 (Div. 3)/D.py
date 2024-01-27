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


def get_3_largest_elements(a):
    # get the three largest elements and their original indicies
    ret = []
    for i in range(len(a)):
        ret.append([a[i], i])
    ret.sort()
    return ret[-3:]


def solve(test):
    a, b, c = test
    ap = get_3_largest_elements(a)
    bp = get_3_largest_elements(b)
    cp = get_3_largest_elements(c)
    ret = []
    for i in ap:
        for j in bp:
            for k in cp:
                if i[1] != j[1] and i[1] != k[1] and j[1] != k[1]:
                    ret.append(i[0] + j[0] + k[0])

    return max(ret)


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        a = inlt()
        b = inlt()
        c = inlt()
        tests.append([a, b, c])
    for test in tests:
        print(solve(test))
