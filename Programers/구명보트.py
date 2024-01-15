'''
- 알고리즘
1. 유형: 그리디
2. 문제: 프로그래머스 구명보트
3. 배운점: 
- deque을 쓸때 pop(index)는 불가능하고 remove(item)는 가능
- 단 중간에서 값을 찾는 연산은 O(n)의 시간복잡도
= 양쪽 끝에서 빠른 삽입삭제를 필요로 하는 경우 사용
'''

from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))
    
    while people:
        min_p = people.pop()
        for i in range(len(people)):
            max_p = people.popleft()
            # 1) 둘이 탈 수 있는 경우
            if min_p + max_p <= limit:
                break
            # 2) 혼자 타야하는 경우
            else:
                answer += 1
        answer += 1
        
    return answer
