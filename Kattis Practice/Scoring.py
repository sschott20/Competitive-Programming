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
    # print(test)
    ranking = {}
    test = sorted(test, key=lambda x: (-x[1], x[2], x[3]))
    for i in range(len(test)):
        t = test[i]
        ranking[t[0]] = i
    print(test)

    return


if __name__ == "__main__":
    tests = []
    num_contest = inp()
    contestants = []
    
    for i in range(num_contest):
        contestants.append([i] + inlt())
    print(solve(contestants))