# 최대층, 자리수, 바꾸는 횟수, 현재층
N, K, P, X = map(int, input().split())

# 0~9 : 위에서 아래로 - - - , 왼쪽에서 오른쪽으로 || ||
number = [[1,0,1,1,1,1,1],[0,0,0,0,1,0,1],[1,1,1,0,1,1,0],
          [1,1,1,0,1,0,1],[0,1,0,1,1,0,1],[1,1,1,1,0,0,1],
          [1,1,1,1,0,1,1],[1,0,0,0,1,0,1],[1,1,1,1,1,1,1],[1,1,1,1,1,0,1]]

# 바꾸는데 필요한 횟수
number_change = [[0]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        if i == j: continue
        count = 0
        for k in range(7):
            if number[i][k] != number[j][k]:
                count += 1
        number_change[i][j] = count

def find(k, change): # 자리수, 남은 바꿀수 있는 양
    if k == K or change == 0:
        if 1 <= int(''.join(sX)) <= N and change < P:
            global ans
            ans += 1
        return
    # k번째의 수 x를 변경
    x = int(sX[k])
    for j in range(10):
        if number_change[x][j]<=change:
            sX[k] = str(j)
            find(k+1, change-number_change[x][j])
            sX[k] = str(x)
ans = 0
sX = list(str(X).zfill(K))
find(0, P)
print(ans)