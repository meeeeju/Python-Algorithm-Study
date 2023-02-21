# 79384 KB/ 812 ms 
import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    queue=deque()
    queue.append((1,color[1]))  # 루트는 무조건 1
    visited=[False for _ in range(N+1)] # 방문 여부
    visited[0]=True
    result=[0 for _ in range(N+1)] # 노드별 색깔 결과
    if color[1]!=0 : count=1 # 첫번째 노드인 1이 하얀색(0)이 아니라면 count=1
    else : count=0 
    while len(queue)!=0 and color != result:  # queue가 비었지 않고, color와 result가 같지 않을 때
        node,color_num = queue.popleft() # node : node 번호 , color_num = 색깔 번호
        visited[node]=True # queue에서 빠져나온 node를 방문했다고 초기화
        for g in graph[node]: # node와 연결되어 있는 다른 노드들을 꺼냄
            result[g]=color_num # node와 연결되어 있는 다른 노드들에 color_num을 저장
            if visited[g]!=True: # 만약 g를 방문하지 않았다면
                if color[g]!=result[g]: # g의 color색과 result 색이 다르다면 g에서 새로운 색깔로 새로 시작한 것! 
                    count+=1   # 따라서 count 증가 후, result[g] 를 color[g] 값으로 초기화해준다
                    result[g]=color[g]
                queue.append((g,color[g])) 
    return count
            


N=int(input())
count=0
color=[-1]+list(map(int,input().split()))
graph=[[] for _ in range(N+1)]


for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs())
    

