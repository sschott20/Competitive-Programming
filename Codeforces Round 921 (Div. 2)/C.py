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
    n, k, m, s = test
    s = "".join(s)
    sub = set([chr(97 + i) for i in range(k)])
    chunk = set()

    num_chunks = 0
    for i in range(len(s)):
        if s[i] not in chunk:
            chunk.add(s[i])
        if len(chunk) == k:
            chunk = set()
            num_chunks += 1

    if num_chunks >= n:
        return "YES"

    ret = ""

    while n > 0:
        last = sub.difference(chunk).pop()
        ret = last + ret
        idx = s.rfind(last)
        s = s[:idx]
        n -= 1
        if n == 0:
            break
        chunk = set()
        num_chunks = 0
        for i in range(len(s)):
            if s[i] not in chunk:
                chunk.add(s[i])
            if len(chunk) == k:
                chunk = set()
                num_chunks += 1
        if num_chunks >= n:
            add = ["a" for i in range(n)]
            ret = "".join(add) + ret
            return "NO\n" + ret

    return "NO\n" + ret


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        n, k, m = inlt()
        s = insr()
        tests.append([n, k, m, s])
        continue
    for test in tests:
        print(solve(test))
