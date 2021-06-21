import sys
from collections import deque
rl = lambda: sys.stdin.readline().rstrip()


ROW, COL = map(int, input())
maze = []
for _ in range(ROW):
    maze.append(list(map(int, input())))

def bfs_find_way(maze):
    queue = deque([(0, 0)])

    while queue:
        pos = queue.popleft()
        r = pos[0]; c = pos[1]

        for way in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r_way = r + way[0]
            c_way = c + way[1]
            if 0 <= r_way < ROW and 0 <= c_way < COL:
                if maze[r_way][c_way] == 1:
                    queue.append((r_way, c_way))

                    if maze[r_way][c_way] == 1:
                        maze[r_way][c_way] += maze[r][c]
                    else:
                        maze[r_way][c_way] = min(maze[r_way][c_way], maze[r][c] + 1)
    return maze[ROW - 1][COL - 1]

# print(bfs_find_way(maze))

print(ROW, COL)
print(maze)
