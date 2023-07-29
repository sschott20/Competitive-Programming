t = inp()
solutions = []
for _ in range(t):
    n = inp()
    L = inlt()
    if max(L) == min(L) and max(L) == 0:
      solutions.append([])
      continue 
    ans = []
    M = 0
    Midx = 0

    if abs(max(L)) > abs(min(L)):
      M = max(L)
      Midx = L.index(M)
    else:
      M = min(L)
      Midx = L.index(M) 

    if M > 0:
      for i in range(1, n):
        while L[i] < L[i-1]:
          L[i] += M
          ans.append([i+1, Midx+1])
          if (L[i] > M):
            M = L[i]
            Midx = i
    else:
      for i in range(n-2, -1, -1):
        while L[i] > L[i+1]:
          L[i] += M
          ans.append([i+1, Midx+1])
          if (L[i] < M):
            M = L[i]
            Midx = i

    solutions.append(ans)


for sol in solutions:
    print(len(sol))
    for pair in sol:
      print(pair[0], pair[1])