import sys


def main():
    ans = sys.stdin.readline()[:-1]
    lets = set([c for c in ans])

    guesses = []

    for i in range(7):
        guesses.append(sys.stdin.readline()[:-1])

    for i, g in enumerate(guesses):
        if g == ans:
            print("WINNER")
            return

        if i == 6:
            break

        p = ""
        for i in range(5):
            p += "X" if g[i] not in lets else "G" if g[i] == ans[i] else "Y"

        print(p)

    print("LOSER")
    return


if __name__ == "__main__":
    main()
