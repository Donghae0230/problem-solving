'''
-알고리즘 
1. 유형: 완전탐색
2. 문제: 프로그래머스 카펫
'''

def solution(brown, yellow):
    for h in range(1, yellow + 1):
        if yellow % h != 0:
            continue
        w = yellow // h
        temp = (h + 2) * (w + 2)
        if temp - (h * w) == brown:
            return [(w + 2), (h + 2)]