'''
1. 유형: 해시
2. 특징: LIKE 전화번호부. 정수가 아닌 값(예) string)을 키로 가질 수 있어 배열로 담을 수 없는 정보를 담을 수 있다.
3. 문제: 프로그래머스 베스트앨범
4. 배운점: 
- dict에 items() 함수 사용시 {key: value}형태에서 [(key, value)] 형태로 변환
- dict 정렬 시 sorted(dict.items(), key=lambda x:x[1], reverse=True) 사용
'''

def solution(genres, plays):
    answer = []
    
    dict = {}
    n = len(genres)
    #1) 장르별 재생수 찾기
    for i in range(n):
        if genres[i] in dict:
            dict[genres[i]] += plays[i]
        else:
            dict[genres[i]] = plays[i]
    dict = sorted(dict.items(), key=lambda x:x[1], reverse=True)
    
    #2) 가장 높은 재생수의 장르 안에서
    for i in dict:
        # 2-1) 고유번호와 재생수를 찾기
        temp = {}
        for j in range(n):
            if genres[j] == i[0]:
                 temp[j] = plays[j]
        # 2-2) 재생수로 정렬 후 앞의 2개만 가져오기
        temp = sorted(temp.items(), key=lambda x:x[1], reverse=True)
        if len(temp) >= 2:
            answer.append(temp[0][0])
            answer.append(temp[1][0])
        else:
            answer.append(temp[0][0])
    return answer