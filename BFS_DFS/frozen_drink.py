import sys
from collections import deque

rl = lambda: sys.stdin.readline().rstrip()

N, M = map(int, rl().split())

ice_form = []

for _ in range(N):
    row = list(map(int, rl().split()))
    ice_form.append(row)


def bfs_find_icecream(form, n, m):
    queue = deque([(n, m)])
    form[n][m] = 1
    while queue:
        pos = queue.popleft()
        row = pos[0]; col = pos[1]
        if row + 1 < N:
            if form[row + 1][col] == 0:
                queue.append((row + 1, col))
                form[row + 1][col] = 1
        if row - 1 >= 0:
            if form[row - 1][col] == 0:
                queue.append((row - 1, col))
                form[row - 1][col] = 1
        if col + 1 < M:
            if form[row][col + 1] == 0:
                queue.append((row, col + 1))
                form[row][col + 1] = 1
        if col - 1 >= 0:
            if form[row][col - 1] == 0:
                queue.append((row, col - 1))
                form[row][col - 1] = 1

def dfs_find_icecream(form, row, col):
    if row <= -1 or row >= N or col <= -1 or col  >= M:
        return False

    if form[row][col] == 0:
        form[row][col] = 1

        dfs_find_icecream(form, row - 1, col)
        dfs_find_icecream(form, row + 1, col)
        dfs_find_icecream(form, row, col - 1)
        dfs_find_icecream(form, row, col + 1)

        return True
    return False


count = 0

for row in range(N):
    for col in range(M):
        # bfs find the ice
        # if ice_form[row][col] == 0:
        #     count += 1
        #     bfs_find_icecream(ice_form, row, col)

        # dfs find the ice
        if dfs_find_icecream(ice_form, row, col):
            count += 1
print(count)
