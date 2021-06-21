import sys

rl = lambda: sys.stdin.readline().rstrip()

tc = int(rl())

Ns = []
for _ in range(tc):
    Ns.append(int(rl()))

def n_queen_puzzle(N):
    stack = []
    puzzle = [[0] * N for _ in range(N)]
    for col in range(N):
        stack.append((0, col))
        for row in range(1, N):

    return answer

for n in Ns:
    print(n_queen_puzzle(n))
