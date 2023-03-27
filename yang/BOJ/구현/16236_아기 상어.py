# 37148KB / 100ms
import sys
from queue import Queue
input = sys.stdin.readline
N = int(input())
space = []
for k in range(N):
    col = list(map(int, input().split()))
    space.append(col)
    for s in range(N): # 아기상어 위치찾기
        if col[s]==9:
            x, y = k, s
            space[x][y] = 0
            break
def find_bfs(x, y, size):
    q = Queue()
    q.put((x, y, 0))
    dx = [-1, 0, 0, 1] # 상좌우하 => 우선순위 조건 충족
    dy = [0, -1, 1, 0]
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True
    ans = []
    check = [False, 0]
    while not q.empty():
        check_x, check_y, time = q.get()
        for i in range(4):
            mx, my = check_x+dx[i], check_y+dy[i]
            if 0<=mx<N and 0<=my<N and not visited[mx][my]:
                if 0<space[mx][my]<size: # 아기상어가 먹을 수 있음
                    if check[0] == False:
                        ans.append((mx, my, time+1)) 
                        check[0] = True
                        check[1] = time+1
                    else:
                        if check[1] == time+1:
                            ans.append((mx, my, time+1)) 
                        else:
                            ans.sort()
                            return ans[0]
                elif space[mx][my]==0 or space[mx][my]==size: # 아기상어가 지나갈 수 있으면
                    q.put((mx, my, time+1)) # 아기상어 이동
                    visited[mx][my] = True
    if len(ans) == 0:
        return -1, -1, -1 # 이동할 수 있는 곳이 없음.
    else:
        ans.sort()
        return ans[0]
        

size = 2
size_count = 0
time = 0
while True:
    move_x, move_y, move_t = find_bfs(x, y, size)
    if move_x > -1: # 먹을 수 있는 물고기로 이동
        x, y = move_x, move_y # 이동하고
        space[move_x][move_y] = 0 # 먹었당
        size_count += 1
        if size_count == size:
            size += 1
            size_count = 0
        time += move_t # 걸린시간
    else: # 이동 불가능
        break
print(time)