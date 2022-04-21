def solution(places):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    def check(i, j):
        cnt = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if nx > -1 and ny > -1 and nx < 5 and ny < 5:
                if place[nx][ny] == 'P':
                    cnt += 1
        return cnt
    
    answer = []
    temp = 1
    for place in places:
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    res = check(i, j)
                    if res:
                        temp = 0
                        break
                if place[i][j] == 'O':
                    res = check(i, j)
                    if res > 1:
                        temp = 0
                        break
        answer.append(temp)
        temp = 1
    return answer

'''
+++ BFS 풀이
from collections import deque

def bfs(graph, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((x, y))
    
    visited = [[0] * 5 for _ in range(5)]
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        if visited[x][y] > 2:   # 맨해튼 거리 
            break
        for i in range(4):
            nx = x + dx[i]  
            ny = y + dy[i]
            if nx < 5 and ny < 5 and nx > -1 and ny > -1:
                if visited[nx][ny]:
                    continue
                if graph[nx][ny] == 'P':
                    return False
                if graph[nx][ny] == 'O':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return True
                    
def solution(places):
    answer = []
    for place in places:
        graph = [list(place[i]) for i in range(5)]
        temp = 1
        
        for i in range(5):
            for j in range(5):
                if graph[i][j] == 'P':
                    if not bfs(graph, i, j):
                        temp = 0
        answer.append(temp)
    return answer
'''