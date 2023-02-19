# 61568 KB / 564ms
import sys
import queue
input = sys.stdin.readline
n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
q = queue.Queue()
q.put(1)
parent = ["0"]*(n+1)
while not q.empty():
    v = q.get()
    for i in adj[v]:
        if parent[i] == "0":
            parent[i] = str(v)
            q.put(i)
print('\n'.join(parent[2:]))