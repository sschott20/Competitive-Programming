import sys 

input = sys.stdin.readline


if __name__ == "__main__":
    bangs = input().split("!")
    skips = {}

    for i in range(len(bangs)):
        skips[bangs[i].lower()] = i
    final = []
    i = 0
    done = False
    while i < len(bangs):
        final.append(bangs[i])
        if skips[bangs[i].lower()] > i:
            i = skips[bangs[i].lower()]
        i += 1
    print("!".join(final))
    # print(skips)
    # print(bangs)