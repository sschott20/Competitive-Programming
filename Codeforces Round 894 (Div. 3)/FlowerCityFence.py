import sys
from math import *

input = sys.stdin.readline

def findFirstOccurrence(nums, target):
 
    # search space is nums[left…right]
    (left, right) = (0, len(nums) - 1)
 
    # initialize the result by -1
    result = -1
 
    # loop till the search space is exhausted
    while left <= right:
 
        # find the mid-value in the search space and compares it with the target
        mid = (left + right) // 2
 
        # if the target is located, update the result and
        # search towards the left (lower indices)
        if target == nums[mid]:
            result = mid
            right = mid - 1
 
        # if the target is less than the middle element, discard the right half
        elif target < nums[mid]:
            right = mid - 1
 
        # if the target is more than the middle element, discard the left half
        else:
            left = mid + 1
 
    # return the leftmost index, or -1 if the element is not found
    if result == -1:
        return left
    else: 
        return result


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

def solve(test):
    stest = sorted(test)

    for i, n in enumerate(test):
        # print(i + 1, n, findFirstOccurrence(stest, i + 1))
        if len(test) - findFirstOccurrence(stest, i + 1) != n:
            return "NO"

    return "YES"


if __name__ == "__main__":
    tests = []
    num_tests = inp()
    for i in range(num_tests):
        inp()
        tests.append(inlt())
        
    for test in tests:
        print(solve(test))