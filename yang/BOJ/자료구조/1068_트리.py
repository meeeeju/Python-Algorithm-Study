# 31256KB / 44ms
import sys
input = sys.stdin.readline
def solve1068():
    n = int(input())
    tree = list(map(int, input().split()))
    delNode = int(input())
    adj = [[] for _ in range(n)]
    for i in range(n):
        if tree[i]!=-1:
            adj[i].append(tree[i])
            adj[tree[i]].append(i)
        if tree[i] == -1: start = i
    queue = [start]
    visited = [False]*n
    leaf = [1]*n
    visited[start] = True
    leaf[delNode] = -1
    while queue:
        p = queue.pop(0)
        for i in adj[p]:
            if not visited[i]:
                if leaf[tree[i]] == -1: # 부모노드가 삭제될 노드면 자신도 삭제됨
                    leaf[i] = -1
                elif leaf[i] != -1: # 자기자신이 삭제될 노드가 아니면
                    leaf[tree[i]]= 0 # 자신의 부모 노드는 리프노드가 아님
                visited[i] = True
                queue.append(i)
    count = 0
    for l in leaf:
        if l==1: count += 1
    print(count)
solve1068()