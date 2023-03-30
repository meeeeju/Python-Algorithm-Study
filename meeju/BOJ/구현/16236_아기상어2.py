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
# 뭐가 잘못인지 모르겟슴 ㅜㅜ

N = int(input())

place = [0 for _ in range(N)]   # 공간
current_locate=(0,0)   # 상어의 현재 위치
eaten_fish= 0    # 먹은 물고기
level  = 2    # 상어의 크기(level) 
result = 0

dx =[-1,0,0,1]
dy =[0,-1,1,0]


def hunting_fish(current):


    visited = [[0]*N for _ in range(N)]
    visited[current[0]][current[1]]= 1  
    temp = []
    queue=deque()
    queue.append((current[0],current[1],0)) # 상어의 현재 위치 넣어주기

    while queue:
        x,y,distance = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < -1 or ny < -1 or nx >= N or ny >= N:
                continue
            if not visited[nx][ny]:     # 방문이 안 된 곳이라면 
                visited[nx][ny] = 1     # 방문 처리

                if place[nx][ny] <= level:
                    queue.append((nx,ny,distance+1))
                    if place[nx][ny] != level:
                        temp.append((nx,ny,distance+1))
    return sorted(temp,key=lambda x: (-x[2],-x[0],-x[1]))   # 거리 순, x 순, y 순

for i in range(N):
    place[i]= list(map(int,input().split()))
    for j in range(N):      # 초기 상어의 위치 찾기
        if place[i][j]==9:
            current_locate=(i,j)

while True:
    fishes = hunting_fish(current_locate)
    print(fishes)

    if len(fishes)==0:      # 더 이상 먹을 것이 없으면 break
        break
    
    nx,ny,dis = fishes[0]    # 가장 첫번째에 있는 값 꺼내주기
    current_locate=(nx,ny)   # 상어의 현재 위치 업데이트 하기
    place[nx][ny]=0          # 먹은 물고기는 0 으로 바꿔주기

    result += dis            # 결과 더해주기
    eaten_fish +=1           # 먹은 갯수 더 해주기
    if eaten_fish == level:   # 레벨 업 시켜주기
        level +=1
        eaten_fish = 0       

print(result)

