# 블로그 참고
from collections import deque
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



def bfs(num):
    q = deque()
    q.append(num)
    visit[num] = 1
    while q:
        x = q.popleft()
        for i in board[x]:
            if visit[i] == 0:
                visit[i] = -visit[x]
                q.append(i)
            else:
                if visit[i] == visit[x]:
                    return False
    return True


num1 = int(input())
for i in range(num1):
    n,m = map(int, input().split())
    board = [[] for _ in range(n+1)]
    visit = [0] * (n + 1)
    flag = 1
    for _ in range(m):
        a,b = map(int,input().split())
        board[a].append(b)
        board[b].append(a)

    for i in range(1,n+1):
        if visit[i] == 0:
            if not bfs(i):
                flag = -1
                break
    print('YES' if flag == 1 else 'NO')
