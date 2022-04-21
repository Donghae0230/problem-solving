def solution(record):
    users = {}
    for log in record:
        log = log.split()
        if log[0] == 'Enter' or log[0] == 'Change':
            users[log[1]] = log[2]
    answer = []
    for log in record:
        log = log.split()   
        if log[0] == 'Enter':
            answer.append(f'{users.get(log[1])}님이 들어왔습니다.')
        if log[0] == 'Leave':
            answer.append(f'{users.get(log[1])}님이 나갔습니다.')
    return answer