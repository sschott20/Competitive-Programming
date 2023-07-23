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

def test_nums(test):
    for i in range(0, len(test)):
        for j in range(i + 1, len(test)):
            if test[i] + test[j] >= 10:
                return "YES"
    return "NO" 
    
if __name__ == "__main__":
    #  determine if you can choose any two digits to make a sum greater or equal to 10
    num_tests = inp()
    tests = []
    for i in range(0, num_tests):
        tests.append(inlt())

    for test in tests:
        print(test_nums(test))