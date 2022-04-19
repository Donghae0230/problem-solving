def solution(board, moves):
    bucket = []
    count = 0
    for move in moves:
        move -= 1
        for b in board:
            if b[move]:     # 인형뽑기 기계에 인형이 있는 경우
                bucket.append(b[move])
                b[move] = 0     # 뽑아간 인형은 0으로 처리
                while len(bucket) > 1:
                    if bucket[-2] == bucket[-1]:
                        bucket.pop()
                        bucket.pop()
                        count += 2
                    else:
                        break
                break
    print(bucket)
    return count