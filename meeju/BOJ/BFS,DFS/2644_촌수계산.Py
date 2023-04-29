#	37108kb / 92ms

import sys
from queue import Queue
input = sys.stdin.readline

'''
9   # 전체 사람의 수 
7 3 # 구해야하는 두 사람의 번호
7   # 부모 자식간의 관계의 갯수
1 2
1 3
2 7
2 8
2 9
4 5
4 6'''

n = int(input()) # 정점
a,b = map(int,input().split())
m = int(input())    # 간선

# 그래프 만들기
relative_graph = [[] for _ in range(n+1)]
for i in range(m):


    x,y = map(int,input().split())
    relative_graph[y].append(x)

def multi_bfs(a,b): 

    sca = -1    # shortest common ancestor
    sap_length = float('inf')

    a_visited = [-1 for _ in range(n+1)]
    b_visited = [-1 for _ in range(n+1)]

    q = Queue()
    q.put((1,a,0))  # (소속, 노드번호, 거리) a와 관련된 것들은 0 소속 
    a_visited[a]=0
    q.put((0,b,0))  # b 와 관련된 것들은 1 소속
    b_visited[b]=0
    
    while (q.qsize()>0):
        v = q.get()

        if v[2] > sap_length:
            break
        for w in relative_graph[v[1]]:
            if v[0]==1: # a로부터 온 경우라면
                if a_visited[w]<0:   # 아직 방문하지 않았더라면
                    q.put((1,w,v[2]+1))
                    a_visited[w]=v[2]+1
                    if b_visited[w]>=0:
                        distance =a_visited[w]+b_visited[w]
                        if distance < sap_length:
                            sca = w
                            sap_length = distance
            else:
                if b_visited[w]<0:
                    q.put((0,w,v[2]+1))
                    b_visited[w]=v[2]+1
                    if a_visited[w] >=0:
                        distance =a_visited[w]+b_visited[w]
                        if distance < sap_length:
                            sca = w
                            sap_length = distance
    if sca < 0 :
        return sca
    else:
        return sap_length
    
    
print(multi_bfs(a,b))
