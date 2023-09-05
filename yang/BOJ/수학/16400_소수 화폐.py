# 블로그 참고

N = int(input())
MOD = 123456789

# 1. 에라토스테네스의 체로 MAX 까지의 소수 판별
is_prime = [True]*(N+1)
primes = []
is_prime[0], is_prime[1] = False, False
for i in range(2, N+1):
    if not is_prime[i]: continue
    primes.append(i)
    j = 2*i
    while j <= N:
        is_prime[j] = False
        j += i

# 2. dp로 정답 구하기
dp = [0]*(N+1)
dp[0] = 1
for p in primes:
    for i in range(p, N+1):
        dp[i] += dp[i-p]
        dp[i] %= MOD

# 출력
print(dp[N])