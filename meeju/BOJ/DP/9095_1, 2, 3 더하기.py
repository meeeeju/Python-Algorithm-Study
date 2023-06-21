# 31256	40

# 블로그 참고 -> 코드는 내가  
import sys
input = sys.stdin.readline

'''
3   # T (테스트케이스 수)
4
7
10

output
7
44
274'''

T = int(input())
n_list =[0 for _ in range(T)]
for i in range(T):
    n_list[i]=(int(input()))
max_n = max(n_list)

dp =[0 for _ in range(max_n+1)]
dp[1]=1
dp[2]=2
dp[3]=4

for i in range(4,max_n+1):
    dp[i]= dp[i-3]+dp[i-2]+dp[i-1]

for i in n_list:
    print(dp[i])




