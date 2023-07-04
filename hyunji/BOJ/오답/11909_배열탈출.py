#다현이 방법 참고
n=int(input())
liist=[]
INF=1e8
dp=[[INF]*(n) for _ in range(n)]
dp[0][0]=0
for _ in range(n):
    liist.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        temp1=INF
        temp2=INF
        if 0<i<n:
            if liist[i-1][j]>liist[i][j]:
                temp1=dp[i-1][j]
            else:
                temp1=dp[i-1][j]+(liist[i][j]-liist[i-1][j])+1
        if 0<j<n:
            if liist[i][j-1]>liist[i][j]:
                temp2=dp[i][j-1]
            else:
                temp2=dp[i][j-1]+(liist[i][j]-liist[i][j-1])+1
        dp[i][j]=min(dp[i][j],temp1,temp2)
print(dp[n-1][n-1])
