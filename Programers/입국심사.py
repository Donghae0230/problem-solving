'''
1. 유형: 이분탐색
2. 특징: 
- 가운데 값을 기준으로 target 찾기 > 재귀함수 또는 while 반복문을 사용
- 이때 가운데 값을 기준으로 앞은 모두 0 뒤는 모두 1이라는 조건을 만족해야야 한다
'''
def binary_search(start, end, n, times):
    # 종료조건
    if start >= end:
        return start 
    
    mid = (start + end) // 2
    cnt = 0
    for i in range(len(times)):
        cnt += mid // times[i]
    
    if cnt >= n:
        return binary_search(start, mid, n, times) 
    else: 
        return binary_search(mid+1, end, n, times) 
        

def solution(n, times):
    start = 0
    end = max(times) * n
    
    answer = binary_search(start, end, n, times)
    return answer

print(solution(6, [7, 10]))