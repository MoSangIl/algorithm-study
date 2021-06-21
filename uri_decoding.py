import sys

rl = lambda: sys.stdin.readline().rstrip()

tc = int(rl())


def decodingURI(string):
    uri = ''
    checkn=0
    for i, s in enumerate(string):
        if s == '%':
            asc = string[i + 1:i + 3]
            s = chr(int(asc, 16))
            uri += s
            checkn = 1
        if checkn == 0:
            uri += string[i]
        elif checkn == 3:
            checkn = 0
        else:
            checkn += 1
    print(uri)

for _ in range(tc):
    string = rl()
    decodingURI(string)
