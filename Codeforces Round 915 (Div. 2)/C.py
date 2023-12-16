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
    a = [ord(i) for i in test]
    # s_a = sorted(a)
    # if a == s_a:
    #     return 0
    ind = [len(a) - 1]
    subseq = [a[-1]]
    for i in range(len(a) - 2, -1, -1):
        if a[i] >= subseq[-1]:
            subseq.append(a[i])
            ind.append(i)

    acc = -1
    M = max(subseq)
    for i in range(len(subseq)):
        if subseq[i] == M:
            acc += 1

    for index in ind:
        nxt = subseq.pop()
        a[index] = nxt
    s_a = sorted(a)

    if a == s_a:
        return len(ind) - 1 - acc
    else:
        return -1


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        tests.append(insr())
    for test in tests:
        print(solve(test))
