# 165300KB / 7092ms (PyPy3)
# 안되던 부분 블로그 참고 근데 왜인지 잘 모르겠당

import sys
input = sys.stdin.readline

def dp(i, j):
    if mem[i][j] != -1 : return mem[i][j]
    if i==j: return 0
    mem[i][j] = float('inf')
    s = subSum[j+1]-subSum[i]
    for p in range(i, j):
        mem[i][j] = min(mem[i][j], dp(i,p)+dp(p+1,j)+s)
    return mem[i][j]
T = int(input())
for _ in range(T):
    K = int(input())
    pages = list(map(int, input().split()))
    subSum = [0]
    sumValue = 0
    for s in pages:
        sumValue += s
        subSum.append(sumValue)
    mem = [[-1]*K for _ in range(K)] # mem[i][j] = i~j를 합치는 방법 중 가장 작은 방법
    # for i in range(K):
    #     mem[i][i] = pages[i]
    # for i in range(K-1):
    #     mem[i][i+1] = pages[i]+pages[i+1]
    #     mem[i+1][i] = pages[i]+pages[i+1]
    print(dp(0, K-1))