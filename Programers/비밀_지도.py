# key word: python format binary leading zeros
def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        str = ''
        b_a1 = format(a1, f'0{n}b')
        b_a2 = format(a2, f'0{n}b')
        for b1, b2 in zip(b_a1, b_a2):
            if b1 == '1' or b2 == '1':
                str += '#'
            else:
                str += ' '
        answer.append(str)
    return answer