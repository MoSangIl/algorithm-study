from collections import deque

def bfs(graph, x, visited):
    queue = deque([x])

    visited[x] = True

    while queue:
        target = queue.popleft()
        print(target, end=' ')
        for i in graph[target]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
