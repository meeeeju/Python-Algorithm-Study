#메모리 :31388 시간 :40
import sys
input=sys.stdin.readline

t=int(input())
dp=[1,1,1,2,2,3]
liist=[]
for _ in range(t):
    liist.append(int(input()))

for i in range(6,max(liist)+1):
    dp.append(dp[i-1]+dp[i-5])

for i in range(t):
    print(dp[liist[i]-1])
