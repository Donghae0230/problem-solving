'''
1. 유형: 힙
2. 특징: 
- 우선순위 큐 자료구조를 힙으로 구현
- 완전 이진 트리의 일종으로 항상 루트 노드를 삭제
- 삽입/삭제는 O(logN)(트리 길이)만큼, 정렬은 요소 개수를 곱해서 O(NlogN)만큼 소요. 
3. 문제: 프로그래머스 더 맵게
'''

import heapq

def solution(scoville, K):
    answer = 0
    
    # 1) soville 리스트를 힙 자료구조로 변경
    heapq.heapify(scoville)
    
    # 2) 스코빌 지수가 가장 낮은 음식 꺼내기 반복
    while scoville:
        item = heapq.heappop(scoville)
        # 2-1) 음식을 섞을 필요가 없는 경우
        if item >= K:
            return answer
        # 2-2) 음식을 섞어야 하는 경우
        else:
            if not scoville:
                return -1
            else:
                answer += 1
                next_item = heapq.heappop(scoville)
                item = item + (next_item * 2)
                heapq.heappush(scoville, item)
    return answer
