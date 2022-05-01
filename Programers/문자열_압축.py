def solution(s):
    length = len(s)
    shortest = len(s)
    
    for step in range(1, int(length // 2) + 1):
        '''
        start, end = 0, step
        while True:
            if end >= length:
                words.append(s[start:])
                break
            words.append(s[start:end])
            start += step
            end += step
        '''
        # 자른 문자열 for문으로 구현
        words = [s[i:i+step] for i in range(0, length, step)]

        res = str(words[0])
        count = 1

        if len(words) > 1:
            for i in range(1, len(words)):
                if words[i] == words[i-1]:
                    count += 1
                else:
                    if count > 1:
                        res += str(count)
                        res += words[i]
                    else:
                        res += words[i]
                    count = 1
            if count > 1:
                res += str(count)
        shortest = min(shortest, len(res))
    return shortest