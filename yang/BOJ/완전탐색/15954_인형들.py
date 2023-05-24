# 116180KB / 308ms
N, K = map(int, input().split())
value = list(map(int, input().split()))
ans = float('inf')
for i in range(K, N+1): # 개수
    for j in range(N-K+1): # 시작점
        if i+j-1 >= N:
            continue
        m = sum(value[j:i+j])/i
        variance = 0
        for a in range(j, i+j):
            variance += (value[a]-m)**2
        variance = variance/i
        ans = min(variance, ans)
print(ans**0.5)