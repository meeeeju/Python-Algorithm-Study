# 블로그참고
import math
def is_prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
N=int(input())
prime=[]

for i in range(2,N+1):
    if is_prime(i): prime.append(i)

dp=[0 for _ in range(N+1)]
dp[0]=1
for p in prime:
    for i in range(p,N+1):
        dp[i]=(dp[i]+dp[i-p])%123456789
print(dp[N])
