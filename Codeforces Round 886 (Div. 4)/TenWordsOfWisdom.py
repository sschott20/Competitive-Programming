import sys

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


def determine_winner(test):
    max = [0, 0]
    for i in range(len(test)):
        if test[i][1] > max[0] and test[i][0] <= 10:
            max[0] = test[i][1]
            max[1] = i
    return max[1] + 1


if __name__ == "__main__":
    numtests = inp()
    tests = []
    for i in range(numtests):
        testlen = inp()
        test = []
        for j in range(testlen):
            test.append(inlt())
        tests.append(test)

    for test in tests:
        print(determine_winner(test))
