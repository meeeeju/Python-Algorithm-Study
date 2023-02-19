# 31256KB / 40ms
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
stack = []
count = 0
stack.append(1)
visited[1] = True
while len(stack)>0:
    v = stack.pop()
    for i in adj[v]:
        if not visited[i]:
            stack.append(i)
            visited[i] = True
            count += 1
print(count)