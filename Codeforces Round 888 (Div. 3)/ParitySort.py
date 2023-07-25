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


def parity_sort(nums):
    sorted_nums = sorted(nums)
    for i in range(len(nums)):
        if nums[i] % 2 != sorted_nums[i] % 2:
            return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    num_tests = inp()
    tests = []
    for i in range(num_tests):
        n = inp()
        tests.append(inlt())
    for test in tests:
        print(parity_sort(test))