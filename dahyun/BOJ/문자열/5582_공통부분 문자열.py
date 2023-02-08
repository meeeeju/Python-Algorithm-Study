#시간초과나서 블로그 봤습니다.
import sys
input=sys.stdin.readline

s1=input().strip()
s2=input().strip()

result=0

dp=[[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]  # 이차원배열로 dp 초기화

for i in range(1,len(s1)+1):    # s1만큼 반복문 i
    for j in range(1,len(s2)+1):   # s2만큼 반복문 j
        if s1[i-1]==s2[j-1] : dp[i][j]= dp[i-1][j-1]+1  # 만약 s1[i]와 s2[j]가 같다면 바로 직전 문자열이 같은지 저장되어 있는 dp[i-1][j-1]에 +1 해준다
        if result<dp[i][j] : result=dp[i][j] # 가장 큰 값을 찾기 위해 max 함수 사용
        
print(result)
