import heapq

def solution(n, works):
    heap = []
    for work in works:
        heapq.heappush(heap, (-work, work))
    while True:
        temp = heapq.heappop(heap)[1]
        if temp==0 or n==0:
            heapq.heappush(heap, (-temp,temp))
            break
        temp -= 1
        heapq.heappush(heap, (-temp,temp))
        n -= 1
    answer = sum([heapq.heappop(heap)[1]**2 for _ in range(len(works))])
    return answer
print(solution(	3, [1, 1]))