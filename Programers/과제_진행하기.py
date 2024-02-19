def solution(plans):
    answer = []
    for i in range(len(plans)):
        hh, mm = map(int, plans[i][1].split(':'))
        plans[i][1] = hh*60 + mm
        plans[i][2] = int(plans[i][2])
        
    plans.sort(key = lambda x:x[1], reverse=True)

    temp = [plans.pop()]
    time = temp[0][1]
    
    while temp or plans:
        if temp:
            if temp[-1][2] == 0:
                task = temp.pop()
                answer.append(task[0])
        if plans:
            if time == plans[-1][1]:
                temp.append(plans.pop())  
        time += 1
        if temp:
            temp[-1][2] -= 1

    return answer