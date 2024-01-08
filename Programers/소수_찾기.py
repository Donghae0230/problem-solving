'''
1. 유형: 완전탐색
2. 문제: 프로그래머스 소수 찾기
'''

from itertools import permutations
import math 

def is_prime(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    numbers = list(numbers)
    
    temp = []
    for i in range(1, len(numbers)+1):
        items = list(permutations(numbers, i))
        for item in items:
            item = int(''.join(item))
            if item not in temp:
                temp.append(item)
    
    for i in temp:
        if i > 1 and is_prime(i) == True:
            answer.append(i)
    return len(answer)