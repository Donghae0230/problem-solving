import itertools

def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    p = list(itertools.permutations(dungeons, n))
    for i in range(len(p)):
        cnt = 0
        temp = k
        for j in p[i]:
            if temp < j[0]:
                break
            temp -= j[1]
            cnt += 1
        if cnt > answer:
            answer = cnt
    return answer