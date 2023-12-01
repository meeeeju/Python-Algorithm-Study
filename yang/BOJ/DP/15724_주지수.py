## PyPy로만 통과하는 코드(130644KB / 2232ms)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
territory = []
territorySubSum = []
for i in range(N):
    territory.append(list(map(int, input().split())))
    s = [0]
    sSum = 0
    for t in territory[i]:
        sSum += t
        s.append(sSum)
    territorySubSum.append(s)
K = int(input())
for _ in range(K):
    answer = 0
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1 - 1, x2): # x1 - 1 ~ x2 - 1
        answer += territorySubSum[x][y2] - territorySubSum[x][y1 - 1]
    print(answer)

## 고쳤는데 틀린코드
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
territory = []
territorySubSum = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
    territory.append(list(map(int, input().split())))
    for t in range(1, M+1):
        territorySubSum[i+1][t] = territorySubSum[i+1][t-1] + territorySubSum[i][t] - territorySubSum[i][t-1] + territory[i][t-1]
K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    answer = territorySubSum[x2][y2] - territorySubSum[x2 - 1][y1 - 1] - territorySubSum[x1 - 1][y2 - 1] + territorySubSum[x1 - 1][y1 - 1]
    print(answer)

## 이 코드 맞았는데 나랑 비슷
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = area[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(int(input())):
    x,y,i,j = map(int,input().split())
    print(dp[i][j] - dp[x-1][j] - dp[i][y-1] + dp[x-1][y-1])
