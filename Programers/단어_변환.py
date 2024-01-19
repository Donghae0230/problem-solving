import copy

def dfs(begin, target, words, count, result):
    for i in range(len(words)):
        temp = 0
        for w1, w2 in zip(begin, words[i]):
            if w1 != w2:
                temp += 1
        if temp == 1:
            new_words = copy.deepcopy(words)
            answer = new_words.pop(i)
            if answer == target:
                result.append(count+1)
            else:
                dfs(words[i], target, new_words, count+1, result)
    return result

def solution(begin, target, words):
    if target not in words:
        return 0
    result = dfs(begin, target, words, 0, [])
    return min(result)

# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))