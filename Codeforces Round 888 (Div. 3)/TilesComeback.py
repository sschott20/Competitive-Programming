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

def solve(vars, nums):
    n,k = vars
    start, final = nums[0], nums[-1]
    new = []
    for num in nums:
        if num == start:
            new.append(0)
        elif num == final:
            new.append(1)
    # need case for start == end
    rightsums = [sum(new)]
    for i in range(len(new)-1):
        rightsums.append(rightsums[-1] - new[i])
    if start != final:
        count = k
        for i in range(len(new)):
            if count == 0:
                if rightsums[i] >= k:
                    return "YES"
            elif new[i] == 0:
                count -= 1
    elif k <= len(new):
        return "YES"
    return "NO"


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        vars = inlt()
        nums = inlt()
        tests.append([vars,nums])
    for test in tests:
        print(solve(test[0],test[1]))