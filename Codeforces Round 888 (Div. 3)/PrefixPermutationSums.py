import sys
import math

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

def solve(nums):
    # if len(nums) == 1:
    #     if nums[0] == 1 or nums[0] == 2:
    #         return "YES"
    #     else:
    #         return "NO"
    implied = [nums[0]]
    for i in range(1, len(nums)):
        implied.append(nums[i] - nums[i-1])
    implied = sorted(implied)
    
    missing = []

    extra = None
    setnums = set(implied)
    for i in range(len(implied)):
        if i + 1 not in setnums:
            missing.append(i+1)
        if i > 0 and implied[i] == implied[i-1]:
            if extra == None:
                extra = implied[i]
            else: 
                return "NO"
        if implied[i] > len(implied) + 1:
            if extra == None:
                extra = implied[i]
            else: 
                return "NO"
    if len(implied) + 1 not in setnums:
        missing.append(len(implied) + 1)
    # print("start")
    # print(nums)
    # print(implied)
    # print(missing)
    # print(extra)
    # print("done")
    
    if extra == sum(missing) and len(missing) == 2:
        return "YES"
    elif len(missing) == 1 and extra == None:
        return "YES"

    # return implied
    return "NO"

if __name__ == "__main__":
    tests = []
    num_tests = inp()
    
    for i in range(num_tests):
        n = inlt()
        tests.append(inlt())
    
    for test in tests:
        print(solve(test))