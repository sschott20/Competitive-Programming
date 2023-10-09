import sys
from math import *

input = sys.stdin.readline


def inp():
    return int(input())


if __name__ == "__main__":
    ips = []
    num_ips = inp()
    first_val = 0
    shared_val = 0
    for i in range(num_ips):
        str_ip = str(input())
        arr = str_ip.split(".")
        final_val = 0
        final_val += int(arr[0]) << 24
        final_val += int(arr[1]) << 16
        final_val += int(arr[2]) << 8
        final_val += int(arr[3])
        if i == 0:
            first_val = final_val
            shared_val = final_val
        else:
            shared_val = final_val & shared_val

    first_val_string = "{:032b}".format(first_val)
    second_val_string = "{:032b}".format(shared_val)
    print(first_val_string)
    print(second_val_string)
    shared = 0
    for c, d in zip(first_val_string, second_val_string):
        if c == d:
            shared += 1
        else:
            break

    if shared == 0:
        print(str(32))
    else:
        print(str(shared))
