def solution(rows, columns, queries):
    # 1) rows, columns로 2차원 리스트 만들기
    lst = [[i + j*columns for i in range(1, columns+1)] for j in range(rows)]
    answer = []
    
    for query in queries:
        # 2) 인덱스 맞추기(-1) 
        for i in range(4):
            query[i] -= 1
        x1, y1, x2, y2 = query
        
        # 3) 오른쪽 위 값을 임시로 저장
        temp = lst[x1][y2]
        
        # 4) 최솟값을 임시값으로 설정
        min_val = temp
        
        # 5) 화전하는 값 위치 변경 및 최솟값 확인
        for i in range(y2-1, y1-1, -1): 
            min_val = min(min_val, lst[x1][i])
            lst[x1][i+1] = lst[x1][i]
            
        for i in range(x1+1, x2+1):
            min_val = min(min_val, lst[i][y1])
            lst[i-1][y1] = lst[i][y1]
            
        for i in range(y1+1, y2+1):
            min_val = min(min_val, lst[x2][i])
            lst[x2][i-1] = lst[x2][i]
            
        for i in range(x2-1, x1, -1):
            min_val = min(min_val, lst[i][y2])
            lst[i+1][y2] = lst[i][y2]
        lst[x1+1][y2] = temp
        
        answer.append(min_val)
    return answer