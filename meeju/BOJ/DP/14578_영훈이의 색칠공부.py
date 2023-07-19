# 블로그 참조 
# 근데 왜 dp[2]=2 인데 dp[2]=1 로 하고 dp 해주는거야??
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
'''
3'''

N = int(input())
mod = 1000000007
dp=[0 for _ in range(N+1)]
dp[1]=0
dp[2]=1
fact =2

def factorial(n):

    if n == 1:
        return 1
    sums = factorial(n-1)*n

    return sums

if N > 2:
    for i in range(3, N+1):
        dp[i] =((i-1)*(dp[i-1]+dp[i-2])) % mod
        fact *=i
    print((fact *dp[N])%mod)
else :
    if N == 1:
        print(0)
    else :
        print(2)