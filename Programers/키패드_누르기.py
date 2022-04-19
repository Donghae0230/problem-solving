def solution(numbers, hand):
    hand = 'R' if hand == 'right' else 'L'
    
    pos = {1:(0, 0), 2:(1, 0), 3:(2, 0), 
           4:(0, 1), 5:(1, 1), 6:(2, 1),
           7:(0, 2), 8:(1, 2), 9:(2, 2),
           '*':(0, 3), 0:(1, 3), '#':(2, 3)}
    left = '*'
    right = '#'
    result = ''
    
    for num in numbers:
        if num in [1, 4, 7]:
            result += 'L'
            left = num
        elif num in [3, 6, 9]:
            result += 'R'
            right = num
        else:
            num_x, num_y = pos[num]
            left_x, left_y = pos[left]
            right_x, right_y = pos[right]
            
            num_to_left = abs(num_x - left_x) + abs(num_y - left_y)
            num_to_right = abs(num_x - right_x) + abs(num_y - right_y)
            
            if num_to_left < num_to_right:
                result += 'L'
                left = num
            elif num_to_left > num_to_right:
                result += 'R'
                right = num
            else:
                result += hand
                if hand == 'R':
                    right = num
                else:
                    left = num
    return result