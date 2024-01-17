def solution(routes):
    answer = 1
    
    n = len(routes)
    if n == 1:
        return answer
    
    # 먼저 진입한 차량부터 정렬
    routes.sort(key=lambda x:(x[0], x[1]))
    
    start, end = routes[0][0], routes[0][1]
    
    for i in range(1, n):
        t1, t2 = routes[i][0], routes[i][1]
        
        # 1) 이전 경로에 속해있는 경우
        if start <= t1 and t2 <= end:
            start, end = t1, t2

        # 2) 이전 경로와 겹치는 경로가 있는 경우
        elif end >= t1 and t2 > end:
            start = t1
        
        # 3) 경로가 아예 다른 경우
        else:
            start, end = t1, t2
            answer += 1

    return answer
# print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]]))