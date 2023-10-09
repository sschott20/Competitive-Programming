import sys
input = sys.stdin.readline

if __name__ == "__main__":
    len_k = int(input())
    k = []
    acc = 0 
    while True:
        new = input().split()
        acc += len(new)
        k += new
        if acc >= len_k:
            break

    k = [int(i) for i in k]
    for n in range(0, )        
