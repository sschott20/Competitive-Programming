import sys
import math 
input = sys.stdin.readline

############ ---- Input Functions ---- ############

def inp():
  return(int(input()))
def inlt():
   return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

if __name__ == "__main__":
    numproblems = inp()
    count = 0
    for i in range(numproblems):
        a = inlt()
        if a[0] + a[1] + a[2] >= 2:
            count += 1
    print(count)
          