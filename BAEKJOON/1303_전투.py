n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]
visited = [[0] * n for _ in range(m)]

def dfs(graph, visited, v, type):
    global cnt
    cnt += 1

    x, y = v
    visited[x][y] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < m and -1 < ny < n:
            if not visited[nx][ny] and graph[nx][ny] == type:
                dfs(graph, visited, (nx, ny), type)

w, b = 0, 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            cnt = 0
            if graph[i][j] == 'W':
                dfs(graph, visited, (i, j), 'W')
                w += cnt**2
            if graph[i][j] == 'B':
                dfs(graph, visited, (i, j), 'B')
                b += cnt**2

print(w, b)