import sys
from math import *
from collections import *
from heapq import *

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


def calc_pair(head, adj):
    if head not in adj:
        return [0, 1]
    ret = []
    for i in adj[head]:
        ret.append(calc_pair(i, adj))
    pairs = []
    unpaired = []

    for i in range(len(ret)):
        heappush(pairs, ret[i][0])
        heappush(unpaired, (-1 * (ret[i][1] + 2 * ret[i][0]), i))

    acc = 0
    while True:
        if len(unpaired) < 2:
            break
        mx = heappop(unpaired)
        mx2 = heappop(unpaired)
        if mx[0] < 0 and mx2[0] < 0:
            heappush(unpaired, (mx[0] + 1, mx[1]))
            heappush(unpaired, (mx2[0] + 1, mx2[1]))
            acc += 1
        else:
            heappush(unpaired, (mx[0], mx[1]))
            heappush(unpaired, (mx2[0], mx2[1]))
            break
    for i in range(len(unpaired)):
        p = pairs[unpaired[i][1]]
        u = unpaired[i][0]
        if u >= 2 * p:
            unpaired[i] = (-1 * unpaired[i][0] - 2 * p, unpaired[i][1])
            acc += p
        else:
            acc += (-1 * u) // 2
            unpaired[i] = ((-1 * u) % 2, unpaired[i][1])
    up = 0
    for u in unpaired:
        up += u[0]
    return [acc, up + 1]


def solve(test):
    adj = {}
    for i in range(len(test)):
        ind = i + 2
        if test[i] in adj:
            adj[test[i]].append(ind)
        else:
            adj[test[i]] = [ind]
    return calc_pair(1, adj)[0]


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        tests.append(inlt())
    for test in tests:
        print(solve(test))
