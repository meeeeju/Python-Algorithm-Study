# 	116144	420
# 시간복잡도 : N^2 아닌가..? 그러면 2 ≤ N ≤ 40,000 이므로 16 * 10^8 
# dp 식 블로그 참고
import sys
input = sys.stdin.readline


N = int(input())

primes =[]
a = [0,0] + [1 for _ in range(N-1)]
def find_prime(N):
    
    for i in range(2,N+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i,N+1,i):
                a[j] = 0
    return 

find_prime(N)   

# 잘못된 DP 식
# for i in range(3,N+1):
#     for j in range(2,i//2+1):
#         if j == i-j :
#             a[i]+=1
#         else:
#             a[i] += a[j] + a[i-j]
    

dp = [0 for _ in range(N+1)]
dp[0] = 1
for p in primes:
    for i in range(p, N+1):
        dp[i] = (dp[i] + dp[i-p]) % 123456789
print(dp[N]) #(2,2,2,2) (3,5) (3,3,2)
