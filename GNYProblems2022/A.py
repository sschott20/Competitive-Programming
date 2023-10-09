import sys

input = sys.stdin.readline

if __name__ == "__main__":
    A = input().split()
    B = input().split()
    scoreA = 3 * int(A[0]) + int(A[1])
    scoreB = 3 * int(B[0]) + int(B[1])

    if scoreA > scoreB:
        print("1", scoreA - scoreB)
    elif scoreB > scoreA:
        print("2", scoreB - scoreA)
    else:
        print("NO SCORE")

    