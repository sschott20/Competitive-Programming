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
    fancy = 0 
    m, k, a1, ak = test    
    total = 0

    fancy += max((m % k) - a1, 0) 
    a1 -= m % k 
    total += m % k
    # print(m, total, fancy, a1, ak)

    if total == m:
        return fancy
    
    m = m - total
    if a1 > 0:
        ak += a1 // k
    # print(m, total, fancy, a1, ak)

    fancy += max(m // k - ak, 0)

    ak -= m // k
    total += (m // k) * k
    # print(m, total, fancy, a1, ak)


    return fancy



if __name__ == "__main__":
    tests = []
    num_tests = inp()
    # for i in range(num_tests):
    #     print(solve(inlt()))
    for i in range(num_tests):
        tests.append(inlt())
        continue
    for test in tests:
        print(solve(test))