import sys

A, B = map(int, sys.stdin.readline().split())


while A != 0 and B != 0 :
    print(A + B)
    A, B = map(int, sys.stdin.readline().split())


# S = 1
# while True:
#     S = sum(map(int, sys.stdin.readline().split()))
#     if S == 0:
#         break
#     else:
#         print(S)