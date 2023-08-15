#블로그 참고
import sys
from collections import deque
input = sys.stdin.readline
def bfs(x,y,z):  # 최단 경로이므로 bfs 사용
    queue=deque
    queue.append([(x,y,z)]) # x좌표,y좌표,벽파괴
    while queue:
        a,b,c=queue.popleft()
        if a==N-1 and b==M-1: return visited[a][b][c]
        for i in range(4):
            nx,ny = x+dir[i][0],y+dir[i][1]
            if 0<=nx<N and 0<=ny<M:
                # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
                if nlist[nx][ny]==1 and c==0:
                    visited[nx][ny][1]=visited[a][b][0]+1
                    queue.appendleft((nx,ny,1))
                #다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면 (최단경로야하므로 한 번 방문했으면 그냥 넘어감)
                elif nlist[nx][ny] == 0 and visited[nx][ny][c] == 0: 
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    queue.append((nx, ny, c))
    return -1
    
N,M = map(int,input().split())
dir = [(1,0),(-1,0),(0,1),(0,-1)]
nlist=[list(map(int,input())) for _ in range(N)]

# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

print(bfs(0,0,0))

'''
중간에 벽을 단 한번만 부술 수 있기 때문에 벽을 부쉈는지의 여부를 3차원 행렬로써 나타내면 된다.
벽 부수기 없이 나타낸다면 visit[x][y] 라고 표현할 수 있지만 z를 추가함으로써 0은 안부숨, 1은 부숨을 표현할 수 있다.
즉, visited[x][y][0]은 안부순 경로, visited[x][y][1]은 부순 경로.
'''
