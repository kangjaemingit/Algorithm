import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    note1 = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    note2 = list(map(int,sys.stdin.readline().split()))

    for j in range(M):
        if note2[j] in note1 :
            print("1")
        else :
            print("0")