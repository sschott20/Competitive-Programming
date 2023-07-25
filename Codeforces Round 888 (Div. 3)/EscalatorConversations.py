import sys

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

def calc_conv(vars, heights):
    n,m,k,h = vars
    heights = sorted(heights)
    count = 0
    for height in heights:
        diff = abs(h - height)
        if diff % k == 0 and diff != 0:
            if diff / k < m:
                count += 1
    return count




if __name__ == "__main__":
    num_tests = inp()
    tests = []
    for i in range(num_tests):
        vars = inlt()
        heights = inlt()
        tests.append([vars,heights])
    for test in tests:
        print(calc_conv(test[0],test[1]))