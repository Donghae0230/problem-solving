from itertools import permutations

def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))

def calculate(exp, op):
    for i in op:
        stack = []
        while len(exp)!=0:
            temp = exp.pop(0)
            if temp == i:
                stack.append(operation(stack.pop(), exp.pop(0), temp))
            else:
                stack.append(temp)
        exp = stack
    return abs(int(exp[0]))
 
def solution(expression):
    op = ['+', '-', '*']
    op_list = list(permutations(op, len(op)))

    exp_list = []
    temp = ''
    for i in expression:
        if i in op:
            exp_list.append(temp)
            exp_list.append(i)
            temp = ''
        else:
            temp += i
    exp_list.append(temp)
    
    max_val = 0
    for i in op_list:
        exp = exp_list.copy()
        max_val = max(calculate(exp, i), max_val)
    return max_val