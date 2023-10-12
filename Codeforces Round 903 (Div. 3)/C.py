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


def solve(a):
    b = [[i[j] for i in a] for j in range(len(a))]
    # print(a)
    # print(b)
    acc = 0
    for i in range(len(a)):
        # row 1 == row - 1 == col 1 == col - 1
        for j in range(i, len(a) - i - 1):
            tmp = []
            tmp.append(ord(a[i][j]))
            tmp.append(ord(b[-i - 1][j]))
            tmp.append(ord(a[-i - 1][-j - 1]))
            tmp.append(ord(b[i][- j- 1]))
            # p = [chr(x) for x in tmp]
            # print(p)
            
            m = max(tmp)
            tmp = [m - x for x in tmp]
            acc += sum(tmp)
            # print(tmp)

    return acc


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        arr = []
        size = inp()
        for j in range(size):
            arr.append(insr())
        tests.append(arr)
    for test in tests:
        print(solve(test))
