# 37052KB /	100ms

import sys
from queue import Queue
input = sys.stdin.readline

def bfs(s,graph,visited):
    
    queue = Queue()
    queue.put(s)
    visited[s]= True
    virus_count = 0

    while(queue.qsize() > 0):
        v = queue.get()
        for w in graph[v]:
            if visited[w] == False:
                visited[w] = True
                virus_count +=1
                queue.put(w)
    return virus_count
    
def main():
    V = int(input())
    E = int(input())
    
    graph = [[] for _ in range(V+1)]
    visited= [ False for _ in range(V+1)]

    for _ in range(E):
        v,w= map(int,input().split())
        graph[v].append(w)
        graph[w].append(v)

    print(bfs(1,graph,visited))

main()

'''
7   #컴퓨터수
6   #간선 수
1 2
2 3
1 5
5 2
5 6
4 7
'''