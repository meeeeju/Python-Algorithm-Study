#블로그보다 선아 코드가 더 와닿아서 선아코드 참고ㅎㅎ
#메모리 :31256 시간 :192
import sys
input=sys.stdin.readline

n=int(input())
liist=list(input().rstrip())

dp=[10000001]*n
dp[0]=0
nextstr={'B':'O','O':'J','J':'B'}

for i in range(n):
    for j in range(i+1,n):
        if liist[j]==nextstr[liist[i]]:
            dp[j]=min(dp[j],dp[i]+(j-i)**2)

if dp[n-1]==10000001:
    print(-1)
else:
    print(dp[n-1])
