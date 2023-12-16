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


if __name__ == "__main__":
    tests = []
    file = open("b.txt", "r")
    acc = 0
    translate = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    acc = 0
    for line in file.readlines():
        targets = {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "one": 0,
            "two": 0,
            "three": 0,
            "four": 0,
            "five": 0,
            "six": 0,
            "seven": 0,
            "eight": 0,
            "nine": 0,
        }
        for key in targets.keys():
            targets[key] = line.find(key)
        # get key of min value in targets greater than -1 :
        min_key = min(targets, key=lambda k: targets[k] if targets[k] > -1 else 100)

        if min_key.isnumeric():
            acc += int(min_key) * 10
        else:
            acc += int(translate[min_key]) * 10

        for key in targets.keys():
            targets[key] = line.rfind(key)
        max_key = max(targets, key=lambda k: targets[k] if targets[k] > -1 else -1)
        if max_key.isnumeric():
            acc += int(max_key)
        else:
            acc += int(translate[max_key])

    print(acc)
