import sys
from collections import deque
input = sys.stdin.readline

'''
3
0 0 0
0 0 0
0 9 0'''
# 0, 1, 2, 3, 4, 5, 6, 9(상어)
# bfs 는 가장 먼저 꺼내지는 것이 제일 가까운 것일까..?
# 배열은 global 이라고 명시 안해도됨?

N = int(input())

place = [0 for _ in range(N)]   # 공간
current_locate=(0,0)   # 상어의 현재 위치
eaten_fish= 0    # 먹은 물고기
level  = 2    # 상어의 크기(size) 
time = 0

dx =[-1,0,0,1]
dy =[0,-1,1,-1]


def hunting_fish(current):
    global level, time,eaten_fish

    queue=deque()
    queue.append((current[0],current[1],0)) # 상어의 현재 위치 넣어주기
    visited = [[0]*N for _ in range(N)]
    visited[current[0]][current[1]]= 1
    

    while queue:
        x,y,distance = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < -1 or ny < -1 or nx >= N or ny >= N:
                continue
            if not visited[nx][ny]:     # 방문이 안 된 곳이라면 
                visited[nx][ny] = 1     # 방문 처리
                if place[nx][ny] > level:   #  상어의 크기보다 물고기가 크다면 
                    continue
                if 0 < place[nx][ny] < level :   # 상어의 크기보다 물고기가 작다면
                    eaten_fish +=1
                    time += distance+1
                    if eaten_fish == level :
                        level+=1
                        eaten_fish=0
                    return (nx,ny)
                queue.append((nx,ny,distance+1))
    return (-1,-1)

for i in range(N):
    place[i]= list(map(int,input().split()))
    for j in range(N):      # 초기 상어의 위치 찾기
        if place[i][j]==9:
            current_locate=(i,j)

while True:
    current_locate = hunting_fish(current_locate)
    if current_locate == (-1,-1):
        break
    place[current_locate[0]][current_locate[1]]=0
    
print(time)




            

# def BFS(x,y):           
#     queue = [(x,y)]
#     matrix[x][y] = 0 # 방문처리

#     while queue:
#         x,y = queue.pop(0)

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= M or ny < 0 or ny >= N:
#                 continue

#             if matrix[nx][ny] == 1 :
#                 queue.append((nx,ny))
#                 matrix[nx][ny] = 0