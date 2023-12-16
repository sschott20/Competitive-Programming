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


def binarySearch(data, val):
    lo, hi = 0, len(data) - 1
    best_ind = lo
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if data[mid] < val:
            lo = mid + 1
        elif data[mid] > val:
            hi = mid - 1
        else:
            best_ind = mid
            break
        if abs(data[mid] - val) < abs(data[best_ind] - val):
            best_ind = mid
    return best_ind


def solve(test):
    k, arr = test
    if k >= 3:
        return 0
    if k == 1:
        sorted_list = sorted(arr)
        m = inf
        for i in range(len(sorted_list) - 1):
            m = min(m, abs(sorted_list[i + 1] - sorted_list[i]))
            # if abs(sorted_list[i + 1] - sorted_list[i]) < m:
            #     m = abs(sorted_list[i + 1] - sorted_list[i])
        m = min(m, min(sorted_list))
        return m
    if k == 2:
        sorted_list = sorted(arr)
        m = sorted_list[-1]
        for i in range(len(sorted_list)):
            for j in range(i + 1, len(sorted_list)):
                d = abs(sorted_list[j] - sorted_list[i])

                ind = binarySearch(sorted_list, d)
                m = min(m, abs(sorted_list[ind] - d), d)
                if m == 0:
                    return 0

        return m


if __name__ == "__main__":
    tests = []
    # n = [random.randint(1, 10000000000) for i in range(2000)]
    # print(" ".join(map(str, n)))
    num_tests = inp()
    for i in range(num_tests):
        n, k = inlt()
        arr = inlt()
        tests.append([k, arr])
    for test in tests:
        print(solve(test))
