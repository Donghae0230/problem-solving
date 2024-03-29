# def solution(n, results):
#     answer = 0
    
#     lose = [[] for _ in range(n+1)]
#     win = [[] for _ in range(n+1)]

#     for i in range(len(results)):
#         a, b = results[i][0], results[i][1]
#         lose[b].append(a)
#         win[a].append(b)
        
#     for i in range(1, n+1):
#         for j in lose[i]:
#             for k in lose[j]:
#                 if k not in lose[i]:
#                     lose[i].append(k)

#     for i in range(1, n+1):
#         for j in win[i]:
#             for k in win[j]:
#                 if k not in win[i]:
#                     win[i].append(k)

#     for i in range(1, n+1):
#         if len(win[i])+len(lose[i]) == n-1:
#             answer += 1

#     return answer


def solution(n, results):
    answer = 0
    
    board = [[0] * (n) for _ in range(n)]
    for a, b in results:
        a, b = a-1, b-1
        board[a][b] = 1
        board[b][a] = -1
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if board[k][j] == 0:
                    if board[k][i] == 1 and board[i][j] == 1:
                        board[k][j] = 1
                    elif board[k][i] == -1 and board[i][j] == -1:
                        board[k][j] = -1

    for i in range(n):
        if board[i].count(0) == 1:
            answer += 1

    return answer

# print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
# print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5,6], [6,7]]), 4)
# print(solution(6, [[1,2], [2,3], [3,4], [4,5], [5,6]]), 6)
# print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]), 5)
# print(solution(5, [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]), 1)
# print(solution(3, [[1,2],[1,3]]), 1)
# print(solution(6, [[1,6],[2,6],[3,6],[4,6]]), 0)
# print(solution(8, [[1,2],[3,4],[5,6],[7,8]]),0)
# print(solution(9, [[1,2],[1,3],[1,4],[1,5],[6,1],[7,1],[8,1],[9,1]]), 1)
# print(solution(6, [[1,2],[2,3],[3,4],[4,5],[5,6],[2,4],[2,6]]), 6)
# print(solution(4, [[4,3],[4,2],[3,2],[3,1],[4,1], [2,1]]), 4)
# print(solution(3,[[3,2],[3,1]]), 1)
# print(solution(4, [[1,2],[1,3],[3,4]]), 1)