import sys

input = sys.stdin.readline


if __name__ == "__main__":
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    score1 = 6 * l1[0] + 3 * l1[1] + 2 * l1[2] + l1[3] + 2 * l1[4]
    score2 = 6 * l2[0] + 3 * l2[1] + 2 * l2[2] + l2[3] + 2 * l2[4]
    print(score1, score2)