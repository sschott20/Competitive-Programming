import sys
from math import *

input = sys.stdin.readline


if __name__ == "__main__":
    # n = str(input()).split()
    s = input()
    s = list(s[: len(s) - 1])
    f = 3 / 2
    acc = 0
    s.reverse()

    for i in range(0, len(s)):
        acc += int(s[i]) * pow(f, i)
    # print((acc - int(acc)).as_integer_ratio())
    frac = (acc - int(acc)).as_integer_ratio()
    if (acc - int(acc) == 0):
        print(str(int(acc)))
    else:
        print(str(int(acc)) + " " + str(frac[0]) + "/" + str(frac[1]))


