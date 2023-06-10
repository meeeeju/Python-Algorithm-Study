# 238328KB / 1236ms
# 블로그 참고
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
dp = [[float('inf')]*n for _ in range(n)]
dp[0][0] = 0
for i in range(n):
    for j in range(n):
        if 0<=j-1<n:
            if array[i][j] >= array[i][j-1]: cost = (array[i][j]-array[i][j-1])+1
            else: cost = 0
            dp[i][j] = min(dp[i][j-1]+cost, dp[i][j])
        if 0<=i-1<n:
            if array[i][j] >= array[i-1][j]: cost = (array[i][j]-array[i-1][j])+1
            else: cost = 0
            dp[i][j] = min(dp[i-1][j]+cost, dp[i][j])
print(dp[n-1][n-1])
'''
di = [1, 0]
dj = [0, 1]
visited = [[-1]*n for _ in range(n)]
pq = []  # (비용, i, j)
heappush(pq, (0, 0, 0))
visited[0][0] = 0
while pq:
    cost, i, j = heappop(pq)
    if i==n-1 and j==n-1:
        print(cost)
        break
    for k in range(2):
        next_i = i+di[k]
        next_j = j+dj[k]
        if 0<=next_i<n and 0<=next_j<n:
            if array[i][j] <= array[next_i][next_j]: next_cost = cost+(array[next_i][next_j]-array[i][j])+1
            else: next_cost = cost

            if visited[next_i][next_j]==-1 or visited[next_i][next_j]>next_cost:
                visited[next_i][next_j] = next_cost
                heappush(pq, (next_cost, next_i, next_j))
'''
