def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        temp = ''
        for i in tree:
            if i not in skill:
                continue
            else:
                temp += i
        if temp == skill[:len(temp)]:
            answer += 1
    return answer