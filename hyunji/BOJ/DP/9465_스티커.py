#메모리 :48200 시간 :900
import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    liist=[]
    for _ in range(2):
        liist.append(list(map(int,input().split())))
    dp=[[0 for _ in range(n)] for _ in range(2)]
    dp[0][0]=liist[0][0]
    dp[1][0]=liist[1][0]
    
    if n==1:
        print(max(dp[0][0],dp[1][0]))
    else:
        dp[0][1]=liist[1][0]+liist[0][1]
        dp[1][1]=liist[0][0]+liist[1][1]
        
        for i in range(2,n):
            dp[0][i]=max(liist[0][i]+dp[1][i-1],liist[0][i]+dp[1][i-2])
            dp[1][i]=max(liist[1][i]+dp[0][i-1],liist[1][i]+dp[0][i-2])
            
        print(max(dp[0][-1],dp[1][-1]))
