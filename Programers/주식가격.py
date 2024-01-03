'''
1. 유형: 스택큐
2. 특징: ADT(추상적 자료구조, 구조의 행동양식만 정의). 스택은 LIFO(예) 브라우저의 뒤로가기), 큐는 FIFO(예) 쇼핑몰 주문처리)   
3. 문제: 프로그래머스 주식가격
4. 배운점: deque는 내부적으로 linked list를 사용하기 때문에 i번째 데이터에 접근하려면 맨 앞/뒤부터 i번 순회가 필요하다.
(for price in prices가 아닌 for i in range(len(prices))로 하고 prices[i]로 접근하려 하면 시간초과 발생)
'''

from collections import deque

def solution(prices):
    answer = [0 for _ in range(len(prices))]

    # 1) deque로 큐 자료구조 사용
    prices = deque(prices)
    
    # 2) queue에 값이 있을 때 까지 반복
    idx = 0
    while prices:
        val = prices.popleft()
        time = 0
        for price in prices:
            time += 1
            if val > price:
                break
        answer[idx] = time
        idx += 1
    return answer