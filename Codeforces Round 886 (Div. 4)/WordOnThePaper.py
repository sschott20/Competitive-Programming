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

def find_word(test):
    srow, scol = find_start(test)
    word = []
    for row in range(srow, 8):
        if test[row][scol] == ".":
            break
        else:
            word.append(test[row][scol])
    return word
        
        

def find_start(test):
    for row in range(0, 8):
        for col in range(0, 8):
            if test[row][col] != ".":      
                return  row, col
    


if __name__ == "__main__":
    numtests = inp()
    tests = []
    for i in range(numtests):
        test = []
        for j in range(0, 8):
            test.append(insr())
        tests.append(test)
    for test in tests:
        print("".join(find_word(test)))
    