def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    elif s % n == 0:
        return [(s // n) for _ in range(n)]
    else:
        while n:
            temp = s // n
            answer.append(temp)
            s -= temp
            n -= 1     
    return answer