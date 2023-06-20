#메모리 :31256 시간 :48
import sys
input=sys.stdin.readline

n=int(input())

def rule(t):
    dp=[0 for _ in range(t+3)]
    dp[0]=0
    dp[1]=1
    dp[2]=2
    dp[3]=3
    
    liist=[0 for _ in range(t+3)]
    liist[0]=0
    liist[1]=1
    liist[2]=2
    liist[3]=4
    

    for i in range(4,t+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        liist[i]=liist[i-1]+dp[i-1]
    
    return liist[t]

for _ in range(n):
    t=int(input())
    print(rule(t))
