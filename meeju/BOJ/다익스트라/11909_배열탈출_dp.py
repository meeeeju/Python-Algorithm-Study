# dp 로 풀자,,블로그 참고
import sys
input = sys.stdin.readline

N = int(input()) 
graph =[0 for _ in range(N+1)]

graph[0]=[0] * (N+1)
for i in range(1,N+1):
    graph[i]= [0]+ list(map(int,input().split()))

cost_save = [ [0 for _ in range(N+1)] for _ in range(N+1) ]

for i in range(1,N+1) : # 왼쪽이랑 위만 검사하면 됨 
    for j in range(1,N+1) : 
        cost_up = int(1e9)
        cost_left = int(1e9)

        if i == 1 and j== 1:    # 처음 값 생략
            continue

        if i >=2:   # 위를 볼 수 있는 경우만
            cost_up = cost_save[i-1][j]
            if graph[i][j] >= graph[i-1][j] :
                cost_up += graph[i][j]-graph[i-1][j]+1
                
        if j >=2:   # 왼쪽을 볼 수 있는 경우만
            cost_left = cost_save[i][j-1]
            if graph[i][j] >= graph[i][j-1] : 
                cost_left+=(graph[i][j]-graph[i][j-1])+1
                
        # 둘 중 더 작은 값 가져오기
        cost_save[i][j] = min(cost_up, cost_left)

print(cost_save[N][N])
