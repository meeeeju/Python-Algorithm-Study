# 블로그 코드
import sys
import heapq
input = sys.stdin.readline
n = int(input())
problems = []
for _ in range(n):
    deadline, ramen = map(int, input().split())
    problems.append((deadline, ramen))
problems.sort()

queue = []
for d, r in problems:
    heapq.heappush(queue, r)
    if d < len(queue):
        heapq.heappop(queue)
    
print(sum(queue))