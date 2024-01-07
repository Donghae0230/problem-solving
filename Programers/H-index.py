'''
-알고리즘 
1. 유형: 정렬
2. 문제: 프로그래머스 H-index
'''

def solution(citations):
    citations = sorted(citations, reverse=True)
    
    h_index = 0
    temp = citations[0]
    
    for c in citations:
        if c >= h_index:
            h_index += 1
            temp = c
        else:
            break
    return min([temp, h_index])
  