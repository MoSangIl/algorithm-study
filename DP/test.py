# import sys
# rl = lambda : sys.stdin.readline().rstrip()

# c = int(rl())
# ground = []

# def solve(c, r, n):
#     if c not in range(n) or r not in range(n):
#         return
#     if c <= n - 1 and r <= n - 1:
#         if ground[c][r] == -1:
#             return
#         distance = ground[c][r]
#         ground[c][r] = -1
#         solve(c + distance, r, n)
#         solve(c, r + distance, n)

# for _ in range(c):
#     n = int(rl())

#     ground.clear()

#     for row in range(n):
#         ground.append(list(map(int, rl().split())))

#     solve(0, 0, n)
#     if ground[n-1][n-1] == -1:
#         print("YES")
#     else:
#         print("NO")

import sys
rl = lambda : sys.stdin.readline().rstrip()

c = int(rl())
ground = []
cache = []

def solve(c, r, n):
    if c not in range(n) or r not in range(n):
        return 0
    if c == n - 1 and r == n - 1:
        return 1
    if cache[c][r] != -1:
        return cache[c][r]
    else:
        distance = ground[c][r]
        cache[c][r] = solve(c + distance, r, n) or solve(c, r + distance, n)
        return cache[c][r]

for _ in range(c):
    n = int(rl())

    ground.clear()
    cache.clear()

    for row in range(n):
        ground.append(list(map(int, rl().split())))
    cache = [[-1] * n for _ in range(n)]

    if solve(0, 0, n) != 0:
        print("YES")
    else:
        print("NO")
        print("----")
        print(cache)
# 2
# 7
# 2 5 1 6 1 4 1
# 6 1 1 2 2 9 3
# 7 2 3 2 1 3 1
# 1 1 3 1 7 1 2
# 4 1 2 3 4 1 2
# 3 3 1 2 3 4 1
# 1 5 2 9 4 7 0
# 7
# 2 5 1 6 1 4 1
# 6 1 1 2 2 9 3
# 7 2 3 2 1 3 1
# 1 1 3 1 7 1 2
# 4 1 2 3 4 1 3
# 3 3 1 2 3 4 1
# 1 5 2 9 4 7 0
