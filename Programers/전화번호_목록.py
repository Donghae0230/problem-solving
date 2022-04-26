def solution(phone_book):
    phone_book.sort()
    n = len(phone_book)
    
    for idx in range(n-1):
        l = len(phone_book[idx])
        if l < len(phone_book[idx+1]):
            if phone_book[idx] == phone_book[idx+1][:l]:
                return False
    return True

'''
해시를 사용한 방법

def solution(phone_book):
    hash_map = {}
    
    for phone in phone_book:
        hash_map[phone] = 1
        
    for phone in phone_book:
        temp = ''
        for num in phone:
            temp += num
            if (temp in hash_map) and (temp != phone):
                return False
    return True
'''

'''
for문 2개 사용 시 시간초과 > sort() 함수 사용 시 길이와 값 둘 다 정렬되는 것 사용

def solution(phone_book):
    phone_book.sort()
    n = len(phone_book)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            length = len(phone_book[i])
            if phone_book[j][:length] == phone_book[i]:
                return False
    return True
'''
