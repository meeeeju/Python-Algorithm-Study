import heapq
import sys
input=sys.stdin.readline

heap=[]
liist=[]
N=int(input())
for i in range(N):
    n=int(input())
    if n==0:
        if not heap:
            print(0)
        else:
            print(-1*(heapq.heappop(heap)))
    else:
        heapq.heappush(heap, -n)
