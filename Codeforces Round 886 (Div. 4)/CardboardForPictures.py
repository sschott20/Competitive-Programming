import sys
from math import sqrt

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


def calc_w(total, sizes):
    a, b, c = 0, 0, 0
    for painting in sizes:
        a += 4
        b += 4 * painting
        c += painting * painting
    c -= total

    roots = [
        (-b + sqrt(b * b - 4 * a * c)) / (2 * a),
        (-b - sqrt(b * b - 4 * a * c)) / (2 * a),
    ]
    return int(max(roots))


if __name__ == "__main__":
    num_tests = inp()
    tests = []

    for i in range(num_tests):
        n, c = inlt()
        sizes = inlt()
        tests.append([c, sizes])

    for test in tests:
        print(calc_w(test[0], test[1]))
