'''
1. 유형: 스택큐
2. 특징: ADT(추상적 자료구조, 구조의 행동양식만 정의). 스택은 LIFO(예) 브라우저의 뒤로가기), 큐는 FIFO(예) 쇼핑몰 주문처리)   
3. 문제: 프로그래머스 프로세스
4. 배운점: zip()은 여러 개의 순회 가능한 객체를 인자로 받고, 각 객체의 원소를 튜플 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환한다.
'''

from collections import deque

def solution(priorities, location):
    answer = 0
    
    # 1) 최고 우선순위 구하기
    max_val = max(priorities)
    
    # 2) (우선순위, 위치) 리스트 만들기
    indices = [i for i in range(0, len(priorities))]
    pairs = list(zip(priorities, indices))
    
    # 3) 큐 생성 후 값이 없을 때 까지 반복
    queue = deque(pairs)
    while queue:
        val = queue.popleft()
        if val[0] < max_val:
            queue.append(val)
        else:
            # 최고 우선순위 갱신
            priorities[val[1]] = 0
            max_val = max(priorities)
            
            answer += 1
            if val[1] == location:
                return answer
    return answer