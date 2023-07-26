# 48836KB / 500ms
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
lectureList = []
for _ in range(N):
    i, start, end = map(int, input().split())
    lectureList.append([start, end])
lectureList.sort()
lecture = []
# 필요한 강의실의 최소 개수는 같은 시간에 동시에 강의가 진행되는 최대 개수
ans = 1
for start, end in lectureList:
    while len(lecture) > 0 and lecture[0] <= start:
        heappop(lecture)
    heappush(lecture, end)
    ans = max(ans, len(lecture))
print(ans)