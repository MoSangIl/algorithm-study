# 빠른 A+B
import sys

rl = lambda: sys.stdin.readline().rstrip()

T = int(rl())

for _ in range(T):
    a, b = map(int, rl().split())
    print((a+b))