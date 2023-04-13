# 주니온 유튜브 참고gㅎㅋㅋㅋ
# 55712KB / 328ms
import sys
sys.setrecursionlimit(1000*7)
input = sys.stdin.readline

S1 = input().strip()
S2 = input().strip()
def lcs(x, y):
    x, y = ' '+x, ' '+y
    m, n = len(x), len(y)
    c = [[0]*n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])
    return c[m-1][n-1]
    # return c

print(lcs(S1, S2))
