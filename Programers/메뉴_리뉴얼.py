from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        menu = {}
        for o in orders:
            o = list(o)
            # 단품 메뉴가 코스요리 구성보다 같거나 많은 경우
            if len(o) >= c:     
                combi = list(combinations(o, c))    # 조합 계산
                for cb in combi:
                    cb = ''.join(cb)                # 조합 정렬 (tuple -> str -> list -> str)
                    cb = ''.join(sorted(cb))
                    if menu.get(cb):
                        menu[cb] += 1
                    else:
                        menu[cb] = 1
        # 최소 2명이상, 가장 많이 주문한 단품메뉴
        answer += [k for k, v in menu.items() if v > 1 and v == max(menu.values())]
    answer.sort()
    return answer

'''
다른 풀이) Counter 사용
from itertools import combinations
import collections

def solution(orders, course):
    answer = []
    
    for c in course:
        combi = []
        for o in orders:
            # 단품 메뉴가 코스요리 구성보다 같거나 많은 경우
            if len(o) >= c:     
                combi += list(combinations(sorted(o), c))   
        
        # most_common: 데이터가 많은 순으로 정렬된 배열 반환
        most_order = collections.Counter(combi).most_common()
    
        # 최소 2명이상, 가장 많이 주문한 단품메뉴
        answer += [''.join(k) for k, v in most_order if v > 1 and v == most_order[0][1]]
    answer.sort()
    return answer
'''