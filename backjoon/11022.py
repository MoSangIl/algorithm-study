# A + B - 7
import sys

rl = lambda: sys.stdin.readline().rstrip()

T = int(rl())

for i in range(1, T + 1):
    A, B = map(int, rl().split())
    print(f"Case #{i}: {A} + {B} = {A + B}")