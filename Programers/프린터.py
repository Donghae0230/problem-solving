from collections import deque

def solution(priorities, location):
    queue = deque([(idx, val) for idx, val in enumerate(priorities)])
    prior = max(priorities)
    res = []
    
    while queue:
        idx, temp = queue.popleft()
        if temp >= prior:
            res.append(idx)
            priorities.remove(temp)
            if priorities:
                prior = max(priorities)
        else:
            queue.append([idx, temp])
    return res.index(location) + 1 

'''
from collections import deque

def solution(priorities, location):
    queue = deque([(idx, val) for idx, val in enumerate(priorities)])
    answer = 0
    
    while queue:
        idx, val = queue.popleft()
        # any 사용하면 매번 max값 갱신하지 않아도 됨
        if any(val < q[1] for q in queue):
            queue.append((idx, val))
        else:
            answer += 1
            if idx == location:
                return answer
'''
