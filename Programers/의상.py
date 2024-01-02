'''
1. 유형: 해시
2. 특징: LIKE 전화번호부. 정수가 아닌 값(예) string)을 키로 가질 수 있어 배열로 담을 수 없는 정보를 담을 수 있다.
'''

def solution(clothes):
    answer = 1
    # 1) 의상의 종류를 key로, 의상의 개수를 value로 한 dict 생성
    dict = {}
    for i in clothes:
        if i[1] in dict:
            dict[i[1]] += 1
        else:
            dict[i[1]] = 1

    # print(dict)
    # {'headgear': 2, 'eyewear': 1}

    # 2) 의상의 개수를 곱해서 조합을 구하고 -1 (하나도 안입은 경우)
    for i in dict.values():
        answer *= (i + 1)
    return answer - 1