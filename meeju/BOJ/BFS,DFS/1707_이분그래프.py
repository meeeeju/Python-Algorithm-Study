# 블로그 참고
from queue import Queue
import sys
input = sys.stdin.readline

'''
이분그래프 : 인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프.
https://gmlwjd9405.github.io/2018/08/23/algorithm-bipartite-graph.html'''


'''
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2'''

# k = int(input())

# for _ in range(k):
#     V,E = map(int,input().split())


def bfs(s):
    q = Queue()
    q.put(s)
    visit[s] = 1
    while q.qsize()>0:
        x = q.get()
        for i in graph[x]:
            if visit[i] == 0:
                visit[i] = -visit[x]
                q.put(i)
            else:
                if visit[i] == visit[x]:
                    return False
    return True


k = int(input())
for i in range(k):
    v,e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visit = [0] * (v + 1)
    flag = 1
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,v+1):
        if visit[i] == 0:   # 아직 방문을 안했으면
            if not bfs(i):
                flag = -1
                break
    print('YES' if flag == 1 else 'NO')
