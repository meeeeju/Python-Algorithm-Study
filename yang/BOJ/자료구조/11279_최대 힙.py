# 37180KB / 128ms
# python heap 라이브러리 블로그 참고
import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print("0")
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)