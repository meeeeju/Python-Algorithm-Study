#블로그 참고
#메모리 :168868 시간 :2716
import sys
input=sys.stdin.readline

n=int(input())
day=[]
money=[]
dp=[0]*(n+1)

for i in range(n):
    t,p=map(int,input().split())
    day.append(t)
    money.append(p)

maxx=0
for i in range(n):
    maxx=max(maxx,dp[i])
    if i+day[i]<=n:
        dp[i+day[i]]=max(maxx+money[i],dp[i+day[i]])

print(max(dp))
