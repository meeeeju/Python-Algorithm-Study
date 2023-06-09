# 31348	40
import sys
input = sys.stdin.readline
'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000'''



N = int(input())    # 지도의 크기 N

building_map = [0 for _ in range(N)]
for i in range(N):
    building_map[i]=list(map(int,input()))

def dfs(x,y):
    global cnt
    building_map[x][y]=0
    cnt +=1

    dx =[-1,0,1,0]
    dy =[0,-1,0,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if building_map[nx][ny] ==0:
            continue
        
        dfs(nx,ny)

cnt = 0 
result =[]
for i in range(N):
    for j in range(N):
        if building_map[i][j] == 1:
            cnt = 0
            dfs(i,j)
            result.append(cnt)
        
print(len(result))
print(*sorted(result),sep='\n')



'''
파이썬에서 str은 immutable한 객체이므로 ['0110100', '0110101', '1110101', '0000111', '0100000', '0111110', '0111000'] 이런식으로
str으로 저장해줄시, 값을 변경 불가하다. 따라서 리스트를 가진 리스트로 저장시켜 이중 배열을 만들어주자'''