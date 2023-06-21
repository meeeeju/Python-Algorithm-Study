import sys
from queue import Queue
input = sys.stdin.readline

# 근데 circle 생기면 어떡함?
# 왜 30%에서 오류 나는 지 모르겠음 ㅜㅜ

'''
4 5 M(세로) N(가로) 
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
'''

# 초기화 시켜주기
M, N = map(int,input().split())

maps = [ 0 for _ in range(M)]
for i in range(M):
    maps[i]=list(map(int,input().split()))


dp = [[0]*N for _ in range(M)]
dp[0][0]=1


for i in range(M):  # 세로
    for j in range(N):  # 가로
        if i > 0:   # 위로부터 오는 경우 (나보다 높아야 나한테 올 수 있다)
            if maps[i][j] < maps[i-1][j]:   
                dp[i][j]+=dp[i-1][j] 

        if j > 0 :  # 왼쪽으로부터 오는 경우
            if maps[i][j] < maps[i][j-1]:
                dp[i][j]+=dp[i][j-1] 

    for j in range(N-1,0,-1):   # 오른쪽으로부터 오는 경우
        if i == 0 :
            continue
        if maps[i][j] > maps[i][j-1]:
            dp[i][j-1]+=dp[i][j]

    for j in range(N):  # 내 위치에서 위로 갈 수 있을 경우, 갈 수 있는 이전 위치의 경로 수 전부 다 업데이트 시켜주기 (단, 현재 내 위치 반경 안에 있는 경우)
    
        if i > 0 and maps[i][j] > maps[i-1][j]:
            y, x = i-1, j
            add_path = dp[i][j]

            dx = [0,0,-1,1]
            dy = [-1,1,0,0]

            q = Queue()
            q.put((x,y,dp[y][x]))
            dp[y][x] += add_path    # 방문 처리와 증가시키기

            while q.qsize()>0:

                x,y,prev_path = q.get() 

                if prev_path < dp[y][x]:    # 이미 방문 한 거임
                    continue 

                for i in range(4):
                    nx = x + dx[i]  # 가로
                    ny = y + dy[i]  # 세로
                
                    if nx < 0 or ny <= 0 or nx >= M or ny >= N : # 범위 벗어나는 경우
                        continue
                    if (nx > j and ny > i) or ny > i : # 시작 위치인 (j,i) 보다  벗어나는 경우
                        continue
                    
                    if maps[y][x] > maps[ny][nx]:   # 높 -> 낮 이동 가능하므로
                        q.put((nx,ny,dp[ny][nx]))
                        dp[ny][nx]+=add_path



# for i in range(1,M):  # 세로
#     for j in range(N):  # 가로
#         if j < N-1 :
#             if maps[i][j] < maps[i][j+1]:
#                 dp[i][j]+=dp[i][j+1]

print(dp[M-1][N-1])