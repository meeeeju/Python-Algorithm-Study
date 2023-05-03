# 36988kb /	144ms
import sys
from queue import Queue
input = sys.stdin.readline
'''
'W'
모든 정점에 대해 for 문을 돈다.
돌면서 같은 W이면 갯수를 셈

'B'
모든 정점에 대해 for 문을 돈다.
돌면서 같은 B 면 갯수를 셈

계산해서 더 큰 값이 이김
'''
N, M = map(int,input().split()) # N : 가로 / M : 세로

war =[0 for _ in range(M)]
for i in range(M):
    war[i]= input().rstrip()

W_visited = [[0] * N for _ in range(M)]
B_visited = [[0] * N for _ in range(M)]
group=[]

def bfs(a,b,my):

    dx=[0,0,1,-1]
    dy=[-1,1,0,0]
    count =0
    q = Queue()
    q.put((a,b))

    while q.qsize()>0:
        x,y = q.get()
        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny <0 or ny >= N:
                continue
            if war[nx][ny] == my:
                if my == 'W' and not W_visited[nx][ny]:
                    count +=1
                    W_visited[nx][ny]=1
                    q.put((nx,ny))
                if my =='B' and not B_visited[nx][ny]:
                    count +=1
                    B_visited[nx][ny]=1
                    q.put((nx,ny))
    if count == 0 :
        count =1
    group.append((my,count))

for i in range(M):
    for j in range(N):
        if war[i][j]=='W':
            if not W_visited[i][j]: 
                bfs(i,j,'W')
        else:
            if not B_visited[i][j]:
                bfs(i,j,'B')
w_score = 0
b_score = 0 
for score in group:
    if score[0]=='W':
        w_score += pow(score[1],2)
    else:
        b_score += pow(score[1],2)
print(w_score, b_score)


