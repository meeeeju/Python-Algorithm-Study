# 시간초과 나서 블로그 보고 짰습니다
# https://lmcoa15.tistory.com/73

S = input()
T = input()
m = 0
dp = [[0]*len(T) for _ in range(len(S))]
for i in range(len(S)):
    for k in range(len(T)):
        if S[i]==T[k]:
            if i>0 and k>0:
                dp[i][k] = dp[i-1][k-1]+1
            else:
                dp[i][k] = 1
            m = max(m, dp[i][k])
print(m)