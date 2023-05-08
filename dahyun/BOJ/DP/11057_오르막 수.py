# 31256 KB / 48 ms
N=int(input())

dp=[[i for i in range(10)] for _ in range(N+1)] # [길이][맨 앞자리]
for i in range(10):  # 길이 1 인 모든 수 전부 1로 초기화
    dp[1][i]=1
for i in range(2,N+1):  # 길이 2부터 N까지 구하기
    for j in range(10):  # 앞자리 수는 0~9까지 
        dp[i][j]=sum(dp[i-1][j:]) # 현재 길이의 앞자리 수가 j는 전 길이의 앞자리가 j부터 끝까지의 합
print(sum(dp[N])%10007)

'''
자기 자신 길이보다 더 작은데, 
오르막인 수들을 전부 다 더해줘야하므로 sum(dp[i-1][j:]) 
'''

