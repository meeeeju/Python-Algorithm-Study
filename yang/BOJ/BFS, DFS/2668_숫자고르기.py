# 블로그 참고
# 31256KB / 40ms
from sys import stdin
input = stdin.readline

def dfs(i):
    stack = [i]
    visited[i] = True
    while stack:
        x = stack.pop()
        for v in graph[x]:
            if not visited[v]:
                stack.append(v)
                visited[v] = True
            else:
                result.add(v)

# 입력받기
N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    graph[i].append(int(input()))

# 정답 구하기
result = set()
for i in range(1, N+1):
    visited = [False]*(N+1)
    dfs(i)

# 정답 출력
print(len(result))
print(*sorted(result))