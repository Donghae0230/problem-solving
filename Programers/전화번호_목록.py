'''
1. 유형: 해시
2. 특징: LIKE 전화번호부. 정수가 아닌 값(예) string)을 키로 가질 수 있어 배열로 담을 수 없는 정보를 담을 수 있다.
3. 문제: 프로그래머스 전화번호 목록
4. 배운점: 2-1 단계에서 for n in num, temp+=n과 같이 작성해 temp를 key와 비교할 수도 있다.
'''
def solution(phone_book):
    answer = True
    
    # 1) Dictionary Comprehesion으로 딕셔너리 생성
    dict = {num : 0 for num in phone_book}
    # print(dict)
    # {'119': 0, '97674223': 0, '1195524421': 0}
    
    # 2) 전체 전화번호부에서 반복
    # 2-1) 번호의 길이를 1에서 번호-1까지 자르고
    # 2-2) 값이 딕셔너리에 있으면 False 반환
    for num in phone_book: 
        for i in range(1, len(num)):
            if num[:i] in dict:
                answer = False
                return answer
    return answer

'''
1차 시도: 효율성 테스트 시간 초과로 실패
def solution(phone_book):
    answer = True
    for num1 in phone_book:
        for num2 in phone_book:
            if num1 == num2:
                continue
            else:
                if len(num1) < len(num2) and num2[:len(num1)] == num1:
                    answer = False
                    return answer
    return answer
'''
