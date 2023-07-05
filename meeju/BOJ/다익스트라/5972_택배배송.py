#    51604   260   
import sys
import heapq
input = sys.stdin.readline

'''
6 8 N(개의 헛간) M(양방향 길)
4 5 3 (A,B,C)
2 4 0
4 1 4
2 1 1
5 6 1
3 6 2
3 2 6
3 4 4
'''

N, M = map(int,input().split())
graph =[[] for _ in range(N+1)]
disTo=[float('inf') for _ in range(N+1)]



def dikstra(start):

    disTo[start]= 0
    heap=[(0,start)]    # dist : v까지 오는데 필요한 비용 , v 

    while heap:

        dist,v = heapq.heappop(heap)
        if dist > disTo[v]:
            continue

        for w in graph[v]: # w[0]: 헛간번호  , w[1]: v-w 간 거리비용
            
            if disTo[w[0]] > disTo[v] + w[1]:
                disTo[w[0]] = disTo[v] + w[1]
                heapq.heappush(heap,(disTo[w[0]],w[0]))
    

for _  in range(M):

    A,B,C= map(int,input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))

dikstra(1)

print(disTo[N])