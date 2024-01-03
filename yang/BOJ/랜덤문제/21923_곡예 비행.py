# 150136KB / 3152ms

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MIN_SCORE = float('-inf')
scores = []
for _ in range(N):
    scores.append(list(map(int, input().split())))

# 상승 비행
dp_up = [[MIN_SCORE]*M for _ in range(N)]
dp_up[N-1][0] = scores[N-1][0]
for n in range(N):
    i = N - n - 1 # 맨 밑에서부터
    for m in range(M):
        if i + 1 < N and dp_up[i + 1][m] != MIN_SCORE:
            dp_up[i][m] = max(dp_up[i + 1][m] + scores[i][m], dp_up[i][m])
        if m - 1 >= 0 and dp_up[i][m - 1] != MIN_SCORE:
            dp_up[i][m] = max(dp_up[i][m - 1] + scores[i][m], dp_up[i][m])

# 하강 비행
dp_down = [[MIN_SCORE]*M for _ in range(N)]
dp_down[N-1][M-1] = scores[N-1][M-1]
for n in range(N):
    i = N - n - 1 # 맨 밑에서부터
    for m in range(M):
        j = M - m - 1 # 맨 오른쪽에서부터 왼쪽으로
        if i + 1 < N and dp_down[i + 1][j] != MIN_SCORE:
            dp_down[i][j] = max(dp_down[i + 1][j] + scores[i][j], dp_down[i][j])
        if j + 1 < M and dp_down[i][j + 1] != MIN_SCORE:
            dp_down[i][j] = max(dp_down[i][j + 1] + scores[i][j], dp_down[i][j])

# 정답 구하기
ans = MIN_SCORE
for n in range(N):
    for m in range(M):
        ans = max(dp_up[n][m] + dp_down[n][m], ans)
print(ans)