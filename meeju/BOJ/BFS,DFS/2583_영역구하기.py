# 	37112	116
# dfs 로 하면 왜 recursion error 나지?
import sys
from queue import Queue
input = sys.stdin.readline
sys.setrecursionlimit(10000)
'''
5 7 3 M(i) N(j) K
0 2 4 4
1 1 2 5
4 0 6 2'''


'''
1. 그래프 만들어주기
2. 영역에 해당하는 곳 전부 색칠해주기 (1로 처리해주기)
3. dfs Or bfs 돌려서 영역 구해주기

''' 

M , N , K = map(int,input().split()) # M : 세로(i==y), N : 가로(j==x), K(직사각형의 갯수)

paper = list( [0]*N for _ in range(M))

for _ in range(K):
    x1,y1,x2,y2= map(int,input().split())
    y1= M-y1
    y2= M-y2

    for i in range(y2,y1):
        for j in range(x1,x2):

            paper[i][j]=1

def bfs(x,y):

    area = 1
    dx =[-1,0,1,0]
    dy =[0,-1,0,1]

    q = Queue()
    q.put((x,y))
    paper[y][x] = 1 # 방문 처리해주기

    while q.qsize()>0:
        x,y = q.get()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if paper[ny][nx] ==1:
                continue
            q.put((nx,ny))
            paper[ny][nx]=1 # 방문 처리해주기
            area += 1
    return area

cnt = 0 
result =[]
for i in range(M):
    for j in range(N):
        if not paper[i][j]:
            cnt +=1
            result.append(bfs(j,i))            

print(cnt)
print(*sorted(result))


# def dfs(x,y):

#     global area
#     paper[y][x] = 1 # 방문 처리해주기
#     area += 1
#     dx =[-1,0,1,0]
#     dy =[0,-1,0,1]
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx < 0 or nx >= N or ny < 0 or ny >= M:
#             continue
#         if paper[ny][nx] ==1:
#             continue
#         dfs(nx,ny)
#     return

# area = 0

# for i in range(M):
#     for j in range(N):
#         if not paper[i][j]:
#             cnt +=1
#             area=0
#             dfs(j,i)
#             result.append(area)




