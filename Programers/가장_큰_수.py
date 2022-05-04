# permutations 사용 시 시간초과
def solution(numbers):
    numbers = list(map(str, numbers))
    
    # 원소 0 이상 1,000이하 => 3자리로 맞춤
    # 문자열 비교는 ASCII 값으로 치환되어 정렬
    numbers.sort(key = lambda x:x*3, reverse=True)
    
    # ex) 000을 처리하기 위해 int => str 변환
    res = int(''.join(numbers))
    return str(res)