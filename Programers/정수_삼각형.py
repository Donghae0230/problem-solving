'''
1. 유형: 다이나믹 프로그래밍(DP)
2. 특징: 
- 메모리를 사용해 중복 연산을 줄이고 속도를 개선
2-1) DFS/BFS로도 풀수있지만 경우의 수가 너무 많은 경우 사용
2-2) 경우의 수에 중복 연산이 많은 경우 사용
'''


def solution(triangle):
    n = len(triangle)
    
    table = [[0] * len(triangle[-1]) for _ in range(n)]
    table[0][0] = triangle[0][0]
    
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j==0:
                table[i][j] = triangle[i][j] + table[i-1][0]
            else:
                table[i][j] = triangle[i][j] + max(table[i-1][j-1], table[i-1][j])
    
    answer = max(table[-1])
    return answer
# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))