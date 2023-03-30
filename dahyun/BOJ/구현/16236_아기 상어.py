# 31256 KB / 48 ms
# 계소 시간초과나서 풀었던 사람한테 조언받음 -> visited 처리
import sys
def bfs(baby_size,x,y):
    q=[(x,y,0)]   # y축 , x축 , total_time
    visited=[[False for _ in range(N)] for _ in range(N)]  # 방문 여부
    min_same=[]   # 먹을 수 있는 물고기 위치
    while q:
        nx,ny,time = q.pop(0)
        if min_same and min_same[0][2]<time+1: break
        for i in range(4):   # 상하좌우 모두 확인
            if 0<=nx+direction_x[i]<N and 0<=ny+direction_y[i]<N and not visited[nx+direction_x[i]][ny+direction_y[i]]:
                fish_size=sea[nx+direction_x[i]][ny+direction_y[i]]  # fish_size : 해당 칸에 있는 물고기의 크기
                if 0<=fish_size<=baby_size:    # 아기 상어가 갈 수 있는 칸
                    if fish_size<baby_size and fish_size!=0:  # 물고기 크기가 아기상어 크기보다 작을 때, 
                        min_same.append((nx+direction_x[i],ny+direction_y[i],time+1))
                    q.append((nx+direction_x[i],ny+direction_y[i],time+1))
                    visited[nx+direction_x[i]][ny+direction_y[i]]=True  # 방문했다고 표시
    if min_same:
        min_same.sort(key= lambda x : (x[2],x[0],x[1]))  # 시간 순, y축, x축 순으로 정렬
        return (min_same[0])  # 가장 위, 왼쪽에 있는 먹이 리턴
    return(-1,-1,-1)

sea=[]
direction_x=[-1,0,0,1]  # 상하좌우  , x: y축 , y: x축
direction_y=[0,-1,1,0]
N=int(sys.stdin.readline())
total_time=0   # 아기상어가 움직일 수 있는 총 시간
eat_fish=0  # 아기상어가 먹은 물고기 수
baby_size=2   # 아기 사이즈
for i in range(N):
    sea.append(list(map(int,sys.stdin.readline().split())))
    if 9 in sea[i]:
        sx=i
        sy=sea[i].index(9)
        sea[sx][sy]=0
while True:
    sx,sy,time=bfs(baby_size,sx,sy)
    if sx==-1 and sy==-1 and time==-1: break  # 더 이상 먹을 먹이가 없음
    sea[sx][sy]=0   # 해당 칸의 물고기는 없다 => 0으로 초기화
    eat_fish+=1  # 아기상어가 물고기를 먹음 
    total_time+=time
    if eat_fish==baby_size:  # 만약, 아기상어가 먹을 물고기 수가 아기상어크기와 같다면 
        eat_fish=0   # 아기상어가 먹은 물고기 소화시키고
        baby_size+=1  # 아기상어 크기 증가
    
print(total_time)
