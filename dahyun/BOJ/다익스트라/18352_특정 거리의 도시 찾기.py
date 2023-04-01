#BaekJoon 18352 특정 거리의 도시 찾기
# 98804 KB / 1468 ms (python)
# 155752 KB / 1044 ms (pypy)
import sys
input = sys.stdin.readline
    
def bfs():
    queue=[(X,0)]  # 시작지점 , 거리
    visited=[False for _ in range(N+1)]  # 방문 여부
    visited[X]=True
    while queue:
        x,count = queue.pop(0)
        if count>K: return   # 만약, 거리가 K보다 커지며 바로 종료 
        if count==K:   # 거리가 K와 같다면, result에 추가
            result.append(x)
        for i in graph[x]:
            if not visited[i]:
                visited[i]=True
                queue.append((i,count+1))
            
            
N,M,K,X = map(int,input().split())  # 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
graph=[[] for i in range(N+1)]
result=[]
for i in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)

bfs()
if not result : print(-1)
else:
    for r in sorted(result):
        print(r)
