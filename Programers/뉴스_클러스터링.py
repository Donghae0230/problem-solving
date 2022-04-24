import re
from collections import Counter

def get_str_list(s):
    # 모두 소문자로 변경
    s = s.lower()
    
    # 두 글자씩 끊어 다중집합 생성
    str_list = []
    for i in range(len(s)-1):
        # 영문으로 된 글자 쌍만 유효
        if s[i].isalpha() and s[i+1].isalpha():
            str_list.append(s[i] + s[i+1])
    return str_list

def solution(str1, str2):
    set1 = get_str_list(str1)
    set2 = get_str_list(str2)
    
    if set1 or set2:
        # 리스트 요소의 개수 확인
        cnt1 = Counter(set1)
        cnt2 = Counter(set2)

        # 교집합 및 합집합 리스트 구하기
        inter = list((cnt1 & cnt2).elements())
        union = list((cnt1 | cnt2).elements())
        return int((len(inter) / len(union)) * 65536)
    else:
        return 65536