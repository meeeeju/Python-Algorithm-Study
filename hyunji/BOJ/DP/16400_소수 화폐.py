#블로그 참고
from itertools import combinations
n=int(input())
sosu=[]

for i in range(2,n+1):
    s_count=0
    for j in range(2,i):
        if i%j==0:
            s_count+=1
    if s_count==0:
        sosu.append(i)

dp=[0 for _ in range(n+1)]
dp[0]=1

for s in sosu:
    for i in range(s,n+1):
        dp[i]=(dp[i]+dp[i-s])%123456789
print(dp[n])

'''
count=0
for i in range(1,len(sosu)):
    liist=list(combinations(sosu,i))
    for j in range(len(liist)):
        for k in range()'''
