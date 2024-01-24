'''
1. 유형: 다이나믹 프로그래밍(DP)
2. 특징: 
- 메모리를 사용해 중복 연산을 줄이고 속도를 개선
3. 풀이
- (1차 시도) 재귀를 사용해 풀었으나 효율성 테스트에서 시간초과 발생
- (2차 시도) 시작점을 미리 1로 채운 후 반복문 실행 > 성공
'''

'''
1차 시도)
def finder(table, m, n, i, j):
    if i > n or j > m:
        return
    if table[i][j] == -1:
        return 
    table[i][j] += 1 
    
    finder(table, m, n, i+1, j)
    finder(table, m, n, i, j+1)
    return table
    

def solution(m, n, puddles):
    answer = 0
    
    table = [[0] * (m+1) for _ in range(n+1)]
    for p in puddles:
        table[p[1]][p[0]] = -1
    
    table = finder(table, m, n, 1, 1)
    answer = table[n][m] % 1000000007
    return answer

'''
# 2차 시도)
def solution(m, n, puddles):
    answer = 0
    
    table = [[0] * (m+1) for _ in range(n+1)]
    for p in puddles:
        table[p[1]][p[0]] = -1
    
    # 시작점 채우기
    for j in range(1, m+1):
        if table[1][j] == -1:
            break
        table[1][j] = 1
    
    for i in range(1, n+1):
        if table[i][1] == -1:
            break
        table[i][1] = 1

    # 길찾기
    for i in range(2, n+1):
        for j in range(2, m+1):
            # 1) 지역이 물에 잠긴 경우
            if table[i][j] == -1:
                continue

            # 2) 지역이 물에 잠기지 않은 경우
            if table[i][j-1] != -1:
                table[i][j] += table[i][j-1]
            if table[i-1][j] != -1:
                table[i][j] += table[i-1][j]
    answer = table[n][m] % 1000000007
    return answer

# print(solution(2, 2, []), 2)
# print(solution(3, 3, []), 6)
# print(solution(3, 3, [[2, 2]]), 2)
# print(solution(3, 3, [[2, 3]]), 3)
# print(solution(3, 3, [[1, 3]]), 5)
# print(solution(3, 3, [[1, 3], [3, 1]]), 4)
# print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
# print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
# print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0) 
# print(solution(4, 4, [[3, 2], [2, 4]]), 7)
# print(solution(100, 100, []), 690285631)