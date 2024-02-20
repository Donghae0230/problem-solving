def solution(dirs):
    answer = 0
    
    tmp = []
    x, y = 5, 5
    
    for i in range(len(dirs)):
        tmp_x, tmp_y = -1, -1
        if dirs[i] == 'U':
            tmp_x, tmp_y = x, y+1
        elif dirs[i] == 'D':
            tmp_x, tmp_y = x, y-1
        elif dirs[i] == 'R':
            tmp_x, tmp_y = x+1, y
        else:
            tmp_x, tmp_y = x-1, y
        
        if (0 <= tmp_x <= 10) and (0 <= tmp_y <= 10):
            forward = [[x, y], [tmp_x, tmp_y]]
            backward = [[tmp_x, tmp_y], [x, y]]
            x, y = tmp_x, tmp_y

            if forward in tmp or backward in tmp:
                continue
            else:
                tmp.append(forward)
                answer += 1
                x, y = tmp_x, tmp_y
    
    return answer
print(solution("ULURRDLLU"))
