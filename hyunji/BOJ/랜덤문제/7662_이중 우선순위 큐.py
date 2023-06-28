#블로그 참고
import heapq
import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    q=int(input())
    minheap=[]
    maxheap=[]
    visited=[False]*q
    for i in range(q):
        a,b=input().split()
        if a=='I':
            heapq.heappush(minheap,(int(b),i))
            heapq.heappush(maxheap,(int(b),i))
            visited[i]=True
        else:
            if int(b)==1:
                while maxheap and not visited[maxheap[0][1]]:
                    heapq.heappop(maxheap)
                if maxheap:
                    visited[maxheap[0][1]]=False
                    heapq.heappop(maxheap)
            else:
                while minheap and not visited[minheap[0][1]]:
                    heapq.heappop(minheap)
                if minheap:
                    visited[minheap[0][1]]=False
                    heapq.heappop(minheap)

    while minheap and not visited[minheap[0][1]]:
        heapq.heappop(minheap)
    while maxheap and not visited[maxheap[0][1]]:
        heapq.heappop(maxheap)
                
    if not minheap or not maxheap:
        print("EMPTY")
    else:
        print(-maxheap[0][0],minheap[0][0])

