def solution(places):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    def check(i, j):
        cnt = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if nx > -1 and ny > -1 and nx < 5 and ny < 5:
                if place[nx][ny] == 'P':
                    cnt += 1
        return cnt
    
    answer = []
    temp = 1
    for place in places:
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    res = check(i, j)
                    if res:
                        temp = 0
                        break
                if place[i][j] == 'O':
                    res = check(i, j)
                    if res > 1:
                        temp = 0
                        break
        answer.append(temp)
        temp = 1
    return answer