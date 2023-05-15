# 74428KB / 828ms

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
timeline = []
for _ in range(N):
    s, t = map(int, input().split())
    heappush(timeline, (s, +1))
    heappush(timeline, (t, -1))
ans = 0
now = 0
while timeline:
    c, t = heappop(timeline) # 강의실 / +1 or -1여부
    now += t
    ans = max(now, ans)
print(ans)
