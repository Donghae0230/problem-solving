from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque([0] * bridge_length)
    sec = 0
    total = 0   # 다리 위 트럭의 무게
    while truck_weights:
        total -= queue.popleft()
        # 트럭이 올라갈 수 있는 경우
        if total + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            queue.append(truck)
            total += truck
        else:
            queue.append(0)
        sec += 1
    return len(queue) + sec