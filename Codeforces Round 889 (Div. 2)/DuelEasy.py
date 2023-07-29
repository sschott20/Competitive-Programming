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
    moves = []
    m = 0
    srt = sorted(test)

    if abs(max(test)) > abs(min(test)):
        srt = sorted(test)

        while srt != test:
            if len(moves) > 50:
                # print("FAILFAIL")
                break
            for i in range(0, len(test) - 1):
                if test[i + 1] < test[i]:
                    diff = test[i ] - test[i + 1]
                    tmp = False
                    for s in srt:
                        if s >= diff:
                            tmp = True
                            moves.append([i + 1 + 1, test.index(s) + 1])
                            test[i + 1] += s
                            srt = sorted(test)
                            break
                    if not tmp:
                            moves.append([i + 1+ 1, test.index(max(srt)) + 1])
                            test[i + 1] += max(srt)
                            srt = sorted(test)
        
    else:
        while sorted(test) != test:
            # if srt.reverse() == test:
            #     break
            # print(test)
            # print(srt)
            if len(moves) > 50:
                # print("FAILFAIL")
                break
            for i in range(1, len(test)):
                if test[i] < test[i - 1]:
                    tmp = False
                    for s in srt:
                        if s + test[i - 1] <= test[i]:
                            tmp = True
                            moves.append([i, test.index(s) + 1])
                            test[i - 1] += s
                            srt = sorted(test, reverse=True)
                            break
                    if not tmp:
                            moves.append([i, test.index(min(srt)) + 1])
                            test[i - 1] += min(srt)
                            srt = sorted(test, reverse=True)
            srt = sorted(test, reverse=True)


        
                
    print(len(moves))
    if (len(moves) > 50):
        print(test)
        print("FAILFAIL")
    for move in moves:
        print(move[0], move[1])
    # print(test)
    # return len(moves)


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        tests.append(inlt())
        continue
    for test in tests:
        solve(test)