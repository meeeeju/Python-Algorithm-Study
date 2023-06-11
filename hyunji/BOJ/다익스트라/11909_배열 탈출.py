#블로그참고
n = int(input())
array = []
dp = [[0] * n for _ in range(n)]


for _ in range(n):
    array.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if 0 <= j - 1 < n:
            if array[i][j] >= array[i][j - 1]:
                count = (array[i][j] - array[i][j - 1]) + 1
            else:
                count = 0
            dp[i][j] = min(dp[i][j - 1] + count, dp[i][j])

        if 0 <= i - 1 < n:
            if array[i][j] >= array[i - 1][j]:
                count = (array[i][j] - array[i - 1][j]) + 1
            else:
                count = 0
            dp[i][j] = min(dp[i - 1][j] + count, dp[i][j])

print(dp[n - 1][n - 1])
