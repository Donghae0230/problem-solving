from collections import deque

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    
    while queue:
        v = queue.popleft()
        if not visited[v]:
            visited[v] = True
            for i in graph[v]:
                queue.append(i)
    
    # 방문한 노드의 개수 반환
    count = visited.count(True) 
    return count
    
def solution(n, wires):
    answer = -1
    result = []
    
    for i in range(len(wires)):
        temp = wires[0:i] + wires[i+1:]
        
        temp.sort(key=lambda x:x[0])
        start = temp[0][0]
        
        graph = [[] for _ in range(n+1)]
        for i in range(len(temp)):
            w1, w2 = temp[i][0], temp[i][1]
            graph[w1].append(w2)
            graph[w2].append(w1)
        
        visited = [False] * (n+1)
        count = bfs(graph, start, visited)
        
        # 방문한 노드와 방문하지 않은 노드의 개수 차이(절대값) 
        diff = abs(count-(n-count))
        result.append(diff)
    
    # 차이의 최솟값 반환
    answer = min(result)
    return answer

# solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])