# 202500 KB / 1004 ms
# 블로그 참고 - dp로 푸는 건 줄 모르고 다익스트라로만 계속 풀다가 안되겠어서 블로그 참고 했엉 ㅠ
import sys
input = sys.stdin.readline
n= int(input())
nlist = [list(map(int,input().split())) for _ in range(n)]
dp =[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):  # 세로
    for j in range(n):  # 가로
        if i==0 and j==0: continue  # 시작점이면 pass
        prev_i,prev_j = int(1e7),int(1e7)
        if i>0:
            prev_i = dp[i-1][j] + (0 if nlist[i][j]<nlist[i-1][j] else nlist[i][j]-nlist[i-1][j]+1) # 위칸 값
        if j>0:
            prev_j = dp[i][j-1] + (0 if nlist[i][j]<nlist[i][j-1] else nlist[i][j]-nlist[i][j-1]+1) # 왼쪽 칸 값
        dp[i][j] = min(prev_i,prev_j) # 둘 중 더 작은 값으로 초기화
print(dp[n-1][n-1])
