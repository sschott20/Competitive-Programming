import sys

input = sys.stdin.readline

if __name__ == "__main__":
    p = float(input())
    l = []
    
    for N in range(2, 17):
        P = (1- p) ** N
        l.append([(P + N * (1 - P)) / N, N])
    # print(l)
    M = [99999999999999999,0]

    for i in l:
        if i[0] < M[0]:
            M = i
    # print(M)
    if M[0] >= 1:
        print(1)
    else:
        print(M[1])
