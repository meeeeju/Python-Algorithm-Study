# 31256KB /	44ms
# 블로그 참고 / 질문 게시판 참고


import sys
input = sys.stdin.readline

T = int(input())
test_num = [None for _ in range(T)]
for i in range(T):
    test_num[i]= int(input())

max_num = max(test_num)     # 테스트 케이스 중에서 가장 큰 수

dp= [1 for _ in range(max_num+1)]     # 모든 숫자는 1로만 더해지는 방법을 다 가지고 있으니까 1로 초기화시키기


for i in range(2,max_num+1):    # 2를 적어도 하나를 포함하고 있는 모든 경우의 수 더해주기 (1,2 로 구성된 조합)
    dp[i] += dp[i-2]

for i in range(3,max_num+1):     # 3을 적어도 하나를 포함하고 있는 모든 경우의 수 더해주기 (1,2,3 으로 구성된 조합)
    dp[i] += dp[i-3]
    


for i in test_num:
    print(dp[i])
