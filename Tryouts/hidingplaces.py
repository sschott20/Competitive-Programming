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


lookup_letter = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
lookup_number = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}
full_board = {(i, j) for i in range(1, 9) for j in range(1, 9)}


def all_moves(x, y):
    valid_moves = set()

    if x - 2 >= 1:
        if y - 1 >= 1:
            valid_moves.add((x - 2, y - 1))
        if y + 1 <= 8:
            valid_moves.add((x - 2, y + 1))

    if x + 2 <= 8:
        if y - 1 >= 1:
            valid_moves.add((x + 2, y - 1))
        if y + 1 <= 8:
            valid_moves.add((x + 2, y + 1))
    if y - 2 >= 1:
        if x - 1 >= 1:
            valid_moves.add((x - 1, y - 2))
        if x + 1 <= 8:
            valid_moves.add((x + 1, y - 2))
    if y + 2 <= 8:
        if x - 1 >= 1:
            valid_moves.add((x - 1, y + 2))
        if x + 1 <= 8:
            valid_moves.add((x + 1, y + 2))
    return valid_moves


def solve(x, y):
    tmp = set()
    tmp.add((x, y))
    moves = [tmp]

    while True:
        new_moves = moves[-1]
        for move in moves[-1]:
            new_moves = new_moves.union(all_moves(move[0], move[1]))
        moves.append(new_moves)
        # print("asdf")
        # print(moves[-1])

        if len(moves[-1]) == 64:
            break

    hiding = full_board.difference(moves[-2])
    hiding = sorted(hiding, key=lambda x: (-x[1], x[0]))
    out = ""
    out += str(len(moves) - 1)
    out += " "
    for s in hiding:
        out += lookup_number[s[0]] + str(s[1]) + " "
    print(out.strip())
    return None


if __name__ == "__main__":
    num_test = inp()
    tests = []
    for i in range(num_test):
        test = insr()
        x, y = (lookup_letter[test[0]], int(test[1]))
        tests.append([x, y])
    for t in tests:
        solve(t[0], t[1])