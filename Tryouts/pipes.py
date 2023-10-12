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
    return

def solve(N, A, pipes, ltry):
    adj = {}
    for i in range(N):
        if pipes[i] == -1:
            continue
        if pipes[i] not in adj:
            adj[pipes[i]] = [i]
        adj[pipes[i]].append(i)
        adj[pipes[i]].sort()

    for i in range(A):
        cur_loc = ltry[i]
        while pipes[cur_loc] != -1:
            cur_loc = pipes[cur_loc]
        coin = cur_loc

        queue = []
        queue.append(coin)
        depth = 0
        while len(queue) != 0:
            qs = len(queue)
            while qs != 0:
                cur = queue.pop(0)
                if cur in adj:
                    if len(adj[cur]) == 0:
                        return cur
                    for n in adj[cur]:
                        queue.append(n)
                qs -= 1
            depth += 1

if __name__ == "__main__":
    N = inp()
    pipes = inlt()
    A = inp()
    ltry = inlt()
    print(solve(N, A, pipes, ltry))

