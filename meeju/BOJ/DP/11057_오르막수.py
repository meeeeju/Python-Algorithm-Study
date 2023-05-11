# 블로그 참고 https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-11057-%EC%98%A4%EB%A5%B4%EB%A7%89-%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
# 오답하기,, (dp 의 경우 규칙을 잘 찾자)
# 규칙을 찾기 -> 자신의 것과 근접한 것들의 관계 파악하기,,아님 전체로라도 
# 메모리제이션하기

n = int(input())
dp = [1]*10
for i in range(1,n) :
    for j in range(1,10) :
        dp[j] += dp[j-1]

print(sum(dp)%10007)
