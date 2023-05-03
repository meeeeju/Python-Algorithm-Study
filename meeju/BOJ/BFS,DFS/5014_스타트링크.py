# 46456KB /	2752ms
import sys
from queue import Queue
input = sys.stdin.readline

# bfs 사용하자

'''
F, S, G, U, D
10 1 10 2 1'''  
# F : 건물 층수, S : 강호의 현재 위치, G: 스타트링크가 있는 곳의 위치
# U: 위로 층, D: 밑으로 층

F, S, G, U, D = map(int,input().split()) 

def bfs(G,S):

    visited = [0 for _ in range(F+1)]
    q = Queue()
    visited[S]= 1
    q.put((S,0))

    while q.qsize()>0:

        x = q.get()
        if x[0]==G:
            return x[1]
        
        if 0 < (x[0] + U) <= F and not visited[x[0] + U]:
            nx = x[0] + U
            visited[nx] = 1
            q.put((nx,x[1]+1))
        if 0 < (x[0]-D) <= F and not visited[x[0]-D]:
            nx = x[0]-D
            visited[nx] = 1
            q.put((nx,x[1]+1))
    return "use the stairs"

print(bfs(G,S))









