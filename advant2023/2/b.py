import sys
from math import *
import re

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


def solve(line):
    d = {
        "blue": 0,
        "red": 0,
        "green": 0,
    }
    id, draws = line.split(":")
    # extract a whole number from the string using regex
    id = int(re.search(r"\d+", id).group())
    draws = draws.split(";")

    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    # Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    # Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    # Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    # Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

    for draw in draws:
        draw = draw.split(",")

        for pull in draw:
            pull = pull.strip().split(" ")
            d[pull[1]] = max(d[pull[1]], int(pull[0]))
    acc = 1
    for val in d.values():
        acc *= val
    return acc


if __name__ == "__main__":
    file = open("b.txt", "r")
    acc = 0
    for line in file.readlines():
        acc += solve(line)
    print(acc)
