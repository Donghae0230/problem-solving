def solution(name):
    temp = ['A', 'E', 'I', 'O', 'U']
    count = -1
    answer = 0
    
    def recursion(s, temp, target):
    	# 재귀함수 내에서 호출 횟수를 구하기위해 nonlocal 예약어 사용
        nonlocal count
        nonlocal answer
        count += 1

        if s == target:
            answer = count
            return
        
        if len(s) == len(temp):
            return
        
        for i in range(len(temp)):
            recursion(s + temp[i], temp, target)
        
    recursion('', temp, name)
    return answer