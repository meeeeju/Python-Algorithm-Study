# 34160 KB / 64 ms
import sys
from collections import deque

def bfs():
    if rm==root : return 0  # 루트 노드를 지울 경우 0
    queue=deque()
    queue.append(root) # 루트 노드를 queue에 넣어주기 (시작점)
    count=0
    while queue:
        q = queue.popleft()
        # 만약 q의 자식노드가 하나이고 + 그 자식노드가 비어있거나, 지워지는 노드일 경우 => 해당 노드가 리프 노드가 되므로 count+=1
        if len(graph[q])==1 and ((not graph[graph[q][0]]) or (graph[q][0])==rm): count+=1 
        else:
            for g in graph[q]: 
                if g==rm : continue # 자식노드가 지워지는 노드이면 continue
                elif not graph[g] : count+=1 # 자식노드와 연결된 자식들이 없을 경우 자식노드가 리프노드가 되므로 count+=1
                else : queue.append(g) # 자식노드가 지워지지도 않고, 연결된 자식이 있을 경우 queue에 넣어준다
    return count
                
    
N= int(sys.stdin.readline())
graph=[[] for _ in range(N)] # 연결된 노드들
fromVertex = list(map(int,sys.stdin.readline().split())) # 부모 노드
rm = int(sys.stdin.readline()) # 지워지는 노드
# 연결되어 있는 노드들을 graph에 저장  및  root 노드 찾아주기
for i in range(N):
    if fromVertex[i]==-1: root=i
    else: graph[fromVertex[i]].append(i)
print(bfs())


