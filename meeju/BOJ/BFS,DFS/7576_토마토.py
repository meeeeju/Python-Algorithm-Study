# 99392	1176	

import sys
input = sys.stdin.readline

'''
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다
토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력
M : 상자의 가로칸 수 (j)
N : 상자의 세로칸 수 (i)
'''
'''
6 4 M N 
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1'''

'''
1. 일단 queue에 다 집어넣기 (한 loop 때마다 큐 다  비우기) 큐 말고 리스트에 넣어줘도 될듯?
2. 상하좌우로 가면서 0 인거  1 로 만들어주기
3. -1 은 무시
4. count 세주기
5. loop 끝났을때 전부 1로 바뀌었으면 count 출력 아니면 -1 출력
'''


M , N = map(int,input().split())
well_list =[]

garbage = [ 0 for _ in range(N)]
for i in range(N):
    garbage[i]= list(map(int,input().split()))

for i in range(N):
    for j in range(M):
        if garbage[i][j]==1:
            well_list.append((i,j))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
cnt = 0

def make_well(contents):

    temp = []

    while contents:

        x,y = contents.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M :
                continue
            if not garbage[nx][ny] :
                garbage[nx][ny]= 1 # 방문처리해주기
                temp.append((nx,ny))
    return temp

while well_list:
    cnt += 1    # 하루 증가하기
    well_list= make_well(well_list)


def check_empty():
    for i in range(N):
        for j in range(M):
            if garbage[i][j]==0:
                return 0
    return 1


if check_empty():
    print(cnt-1)
else:
    print(-1)



