# 101720KB / 1996ms
import sys
from queue import Queue
input = sys.stdin.readline
n = int(input())
ansColorList = [0] + list(map(int, input().split()))
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

child = [[] for _ in range(n+1)]
parent = [0] * (n+1)

def findChildAndParent():
    q = Queue() # 부모 및 자식 리스트 찾기 - 초기화
    visited = [False] * (n+1)
    q.put(1)
    visited[1] = True
    while not q.empty(): # 부모 및 자식 리스트 찾기 - BFS
        v = q.get()
        for k in adj[v]:
            if not visited[k]:
                visited[k] = True
                q.put(k)
                child[v].append(k)
                parent[k] = v
def color():
    q = Queue() # 색칠하기 - 초기화
    visited = [False] * (n+1)
    q.put(1)
    visited[1] = True
    colorCount = 0
    colorList = [0] * (n+1)
    if ansColorList[1] != 0:
        colorList[1] = ansColorList[1]
        colorCount += 1
    while not q.empty(): # 색칠하기 - BFS
        v = q.get()
        for k in adj[v]:
            if not visited[k]:
                visited[k] = True
                q.put(k)
                if colorList[parent[k]] != ansColorList[k]:
                    colorList[k] = ansColorList[k]
                    colorCount += 1
                else:
                    colorList[k] = colorList[parent[k]]
    print(colorCount)

findChildAndParent()
color()