# 72212KB / 348ms
import sys
from queue import Queue

input = sys.stdin.readline
sys.setrecursionlimit(1000000) # 재귀 깊이 늘려주기 1000000번 재귀가 가능하도록

def bfs(s,graph,fromVertex):
    queue = Queue()
    queue.put(s)
    
    while(queue.qsize()> 0):
        v = queue.get()
        for w in graph[v]:
            if fromVertex[w] == None:
                queue.put(w)
                fromVertex[w]=v  
    return

def dfs(s,graph,fromVertex):

    def recur(v):
        for w in graph[v]:
            if fromVertex[w]==None:
                fromVertex[w]=v
                recur(w)
                
    fromVertex[s]=s
    recur(s)

    return 

def main():
    V = int(input()) # 정점 수
    E = V -1 # 간선 수
    tree = [[] for _ in range(V+1)]
    fromVertex = [None for _ in range(V+1)]

    for _ in range(E):
        v,w = map(int,input().split())
        tree[v].append(w)
        tree[w].append(v)
    
    # bfs(1,tree,fromVertex)
    dfs(1,tree,fromVertex)
    
    for i in fromVertex[2:]:
        print(i,sep='\n')

main()