# 37600	104

import sys
from queue import Queue
input = sys.stdin.readline


'''
1 2  (문자 a 와 b)
4 4  ( 전체 문자의 수 N, 치환 가능한 문자쌍의 수 M)
1 3
1 4
3 2
4 2

output 최소치환횟수'''

a,b  = map(int,input().split())

N,M  = map(int,input().split())

graph =[[] for i in range(N+1)]
visited=[0 for _ in range(N+1)]

for _ in range(M):
    v,w = map(int,input().split())
    graph[v].append(w)
    graph[w].append(v)


def bfs(s):
    q = Queue()
    q.put(s)
    while q.qsize() > 0:
        v = q.get()
        for w in graph[v]:
            if w == b :
                return visited[v]+1
            if not visited[w]:
                visited[w]=visited[v]+1
                q.put(w)

    return -1


if a==b:
    print(0)
else:
    print(bfs(a))



'''
항상 예외사항을 까먹지 말고 고려하기 !! '''