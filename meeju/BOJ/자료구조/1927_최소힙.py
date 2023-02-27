# 37180kb /	120ms
import heapq    # heappush(heap, x) - 힙에 원소 x 추가 heappop(heap) - 최솟값 내뱉기  heapify(heap) - 기존 리스트를 힙으로 변환
import sys
input = sys.stdin.readline

heap = [] # heapq를 사용해 최소 힙으로 다룰 리스트

N = int(input())

for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(heap,x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)