import sys

while True:
    val = sys.stdin.readline().rstrip()
    print(val)
    if val:
        print(sum(map(int, val.split())))
    else: break


    