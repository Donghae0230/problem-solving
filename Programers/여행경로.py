'''
1. 유형: DFS/BFS
2. 풀이
- (1차 시도) 정렬 후 재귀를 사용해 풀었으나 항공권을 모두 사용하는 경로를 다 찾은 후 알파벳 순서가 앞서는 경로를 반환해야 하는 것 같다. 
'''

def dfs(val, temp, answer):
    if val in temp:
        for v in temp[val]:
            answer.append(v)
            temp[val].remove(v)
            dfs(v, temp, answer)
    return answer
        
def solution(tickets):       
    temp = {}
    n = len(tickets)
    
    for i in range(n):
        a, b = tickets[i]
        if a in temp:
            temp[a].append(b)
            temp[a] = sorted(temp[a])
        else:
            temp[a] = [b]
        
    answer = dfs('ICN', temp, ['ICN'])
    return answer
print(solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]))