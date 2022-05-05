import heapq
import sys 

input = sys.stdin.readline

n = int(input())
lectures = []
for _ in range(n):
    start, end = map(int, input().split())
    lectures.append([start, end])

lectures.sort()

room = []
heapq.heappush(room, lectures[0][1])
for i in range(1, len(lectures)):
    if lectures[i][0] < room[0]:
        heapq.heappush(room, lectures[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, lectures[i][1])
print(len(room))