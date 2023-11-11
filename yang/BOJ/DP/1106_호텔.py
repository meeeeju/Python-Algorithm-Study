import sys
input = sys.stdin.readline

C, N = map(int,input.split())
city = []
max_people = 0
for i in range(N):
    cost,people = map(int,input.split())
    city.append((cost,people))
    max_people = max(max_people, people)

dp = [float('inf')] * (C+max_people + 1) # dp[i] = i명의 고객을 유치하는 데 드는 비용
dp[0] = 0

for cost, people in city:
    for i in range(people,C + max_people + 1):
        dp[i] = min(dp[i-people]+cost, dp[i]) # dp[i] = min(현재 도시에서 홍보했을 때의 비용, 현재까지 dp 값)

print(min(dp[C:])) # 최소 인원 C 이상일 때 dp 최솟값