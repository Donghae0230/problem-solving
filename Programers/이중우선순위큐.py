'''
1. 유형: 힙
2. 특징: 
- 힙은 완전 이진트리 자료구조의 일종으로 항상 루트노드를 삭제. 
- 루트 노드가 가장 작으면 min heap, 가장 크면 max heap
- 값의 비교는 부모와 자식간에만 하고 형제간에는 X
- 파이썬의 heapq는 기본적으로 min heap으로 동작하며 값을 삽입할때 -를 사용하면 max heap 구현 가능
3. 문제: 프로그래머스 이중우선순위큐
4. 배운점: 힙정렬(O(NlogN), 요소의 개수 N 완전 이진트리 높이 logN)을 사용해 이중우선순위큐를 구현할 수 있다.
'''

import heapq

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

def solution(operations):
    answer = [0, 0]
    temp = []
    
    for op in operations:
        op = op.split(' ')
        if op[0] == 'I':
            temp.append(int(op[1]))
            temp = heapsort(temp)
        else:
            if not temp:
                continue
            else:
                if op[1] == '1':
                    del temp[-1]
                else:
                    del temp[0]

    if not temp:
        return answer
    else:
        answer[0] = temp[-1]
        answer[1] = temp[0]
        return answer
