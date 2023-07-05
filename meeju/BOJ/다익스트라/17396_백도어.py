#    120972   1124
import sys
import heapq
input = sys.stdin.readline

'''
5 7 N M
0 0 0 1 1 상대방의 시야에 보이는지 여부
0 1 7 a b t a에서 b 까지 가는데 t 시간만큼 걸린다.
0 2 2
1 2 4
1 3 3
1 4 6
2 3 2
3 4 1'''


N, M =map(int,input().split())

graph = [[] for _ in range(N) ]
disTo =[float('inf') for _ in range(N)]
edgeTo =[0 for _ in range(N)]

not_safe=list(map(int,input().split())) # not safe 가 1 이면 안전하지 않다는 뜻이다.


for i in range(M):
    a,b,t = map(int,input().split())
    graph[a].append((b,t))
    graph[b].append((a,t))



def do_backdoor(start):
    disTo[start]=0

    heap = [(0,start)]

    while heap:
        
        cost, v = heapq.heappop(heap)

        if cost > disTo[v]:
            continue
        
        for w,t in graph[v]:



            if not_safe[w] and w < N-1:
                continue

            if disTo[w] > disTo[v] + t:
                disTo[w]=disTo[v]+t
                edgeTo[w]=v
                heapq.heappush(heap,(disTo[w],w)) 
do_backdoor(0)

if disTo[N-1]==float('inf'):
    print(-1)
else:
    print(disTo[N-1])

# w=N-1
# while True:
#     print(edgeTo[w],'->')
#     w=edgeTo[w]
#     if w==0:
#         break