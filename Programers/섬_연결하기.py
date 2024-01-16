'''
1. 유형: 그리디
2. 문제: 섬 연결하기
3. 배운점: 노드간의 연결 여부를 확인할 때 그래프 탐색 알고리즘(BFS)을 쓸 수 있다.
'''

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
    return visited

def solution(n, costs):
    answer = 0
    
    costs = sorted(costs, key=lambda costs: costs[2])
    graph = [[] for _ in range(n)]
    visited = [False] * n
    
    for i in range(len(costs)):
        n1, n2 = costs[i][0], costs[i][1]

        # 1) 두 섬이 연결되어 있는 경우
        if visited[n1] and visited[n2]:
            continue
        # 2) 두 섬이 연결되어있지 않은 경우
        else:
            # 2-1) 인접 리스트에 추가
            graph[n2].append(n1)
            graph[n1].append(n2) 
        answer += costs[i][2]
        
        # visited 리스트 초기화 후 그래프 탐색
        visited = [False] * n
        visited = bfs(graph, n1, visited)

        if all(visited)==True:
            return answer
        else:
            continue
        
# solution(5, [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]])