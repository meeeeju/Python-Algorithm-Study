'''
# 34348 KB / 56 ms
import sys
import heapq
input = sys.stdin.readline
def bfs():
    queue=[(0,A)]
    visited=[False for _ in range(N+1)]
    visited[A]=True
    while queue:
        r,c = heapq.heappop(queue)
        for n in nlist[c]:
            if not visited[n]:
                visited[n]=True
                if distance[n]>r+1: 
                    distance[n]=r+1
                    heapq.heappush(queue,(r+1,n))
    
A,B = map(int,input().split())
N,M = map(int,input().split())
nlist = [[] for _ in range(N+1)]
distance=[1000000000000 for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    nlist[a].append(b)
    nlist[b].append(a)
if A==B : print(0);exit(0)
bfs()
if distance[B]==1000000000000: print(-1)
else: print(distance[B])
'''
# 32276 KB / 52 ms
import sys
input = sys.stdin.readline
def bfs():
    queue=[(0,A)]  # 움직인 거리, 현재 노드
    visited=[False for _ in range(N+1)]  # 방문여부 배열
    visited[A]=True
    while queue:
        r,c = queue.pop(0)
        for n in nlist[c]:  # 현재 노드와 연결되어 있는 노드들 방문
            if not visited[n]: # 이전에 방문하지 않았다면
                visited[n]=True
                if distance[n]>r+1: # n노드의 거리가 r+1보다 크다면, 
                    distance[n]=r+1 # 초기화 후, 
                    queue.append((r+1,n)) # queue에 append
    
A,B = map(int,input().split())
N,M = map(int,input().split())
nlist = [[] for _ in range(N+1)]
distance=[1000000000000 for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    nlist[a].append(b)  # a,b 양방향으로 저장
    nlist[b].append(a)
if A==B : print(0);exit(0)  # 만약, A -> A라면 0 출력후 종료
bfs()
if distance[B]==1000000000000: print(-1)  # B를 구할 수 있는 방향이 전혀 없다면 -1 출력
else: print(distance[B])  
