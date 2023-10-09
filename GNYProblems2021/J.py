# encode morse code

import sys

m = {
    "A": "01",
    "B": "1000",
    "C": "1010",
    "D": "100",
    "E": "0",
    "F": "0010",
    "G": "110",
    "H": "0000",
    "I": "00",
    "J": "0111",
    "K": "101",
    "L": "0100",
    "M": "11",
    "N": "10",
    "O": "111",
    "P": "0110",
    "Q": "1101",
    "R": "010",
    "S": "000",
    "T": "1",
    "U": "001",
    "V": "0001",
    "W": "011",
    "X": "1001",
    "Y": "1011",
    "Z": "1100",
    "0": "11111",
    "1": "01111",
    "2": "00111",
    "3": "00011",
    "4": "00001",
    "5": "00000",
    "6": "10000",
    "7": "11000",
    "8": "11100",
    "9": "11110",
}


def main():
    input = sys.stdin.readline()

    input = [m.get(c, "") for c in input.upper()[:-1]]

    input = "".join(input)

    if input == "":
        print("NO")
        return

    l, r = 0, len(input) - 1

    while l < r:
        if input[l] != input[r]:
            print("NO")
            return

        l += 1
        r -= 1

    print("YES")
    return


if __name__ == "__main__":
    main()
