import sys
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



# You are the author of a Codeforces round and have prepared n
#  problems you are going to set, problem i
#  having difficulty ai
# . You will do the following process:

# remove some (possibly zero) problems from the list;
# rearrange the remaining problems in any order you wish.
# A round is considered balanced if and only if the absolute difference between the difficulty of any two consecutive problems is at most k
#  (less or equal than k
# ).

# What is the minimum number of problems you have to remove so that an arrangement of problems is balanced?

# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.

# The first line of each test case contains two positive integers n
#  (1≤n≤2⋅105
# ) and k
#  (1≤k≤109
# ) — the number of problems, and the maximum allowed absolute difference between consecutive problems.

# The second line of each test case contains n
#  space-separated integers ai
#  (1≤ai≤109
# ) — the difficulty of each problem.

# Note that the sum of n
#  over all test cases doesn't exceed 2⋅105
# .

# Output
# For each test case, output a single integer — the minimum number of problems you have to remove so that an arrangement of problems is balanced.

def max_balanced(test, k):
    count = 0
    sublists = []
    lastbreak = 0
    for i in range(0, len(test) - 1):
        if test[i + 1] - test[i] > k:
            sublists.append(test[lastbreak: i + 1 ])
            lastbreak = i + 1
    sublists.append(test[lastbreak:])

    return len(test) - max([len(sublist) for sublist in sublists]) 

if __name__ == "__main__":
    numtests = inp()
    tests = []
    for i in range(numtests):
        n, k = inlt()
        test = inlt()
        tests.append([sorted(test), k])
    for test in tests:
        print(max_balanced(test[0], test[1]))
    
    