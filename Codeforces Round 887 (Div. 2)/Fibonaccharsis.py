import sys
import math

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


def num_fibb(n, k, a1, a2):
    if a1 < a2:
        return 0
    if k == 3 and a1 == 0:
        return 0
    if k == 3:
        return 1

    return num_fibb(a1, k - 1, a2, a1 - a2)


def get_num_fibb(test):
    n = test[0]
    k = test[1]
    num = 0
    for i in range(math.floor(n / 2), n + 1):
        num += num_fibb(n, k, i, n - i)
    return num


if __name__ == "__main__":
    num_tests = inp()
    tests = []
    for i in range(num_tests):
        tests.append(inlt())
    for test in tests:
        print(get_num_fibb(test))
