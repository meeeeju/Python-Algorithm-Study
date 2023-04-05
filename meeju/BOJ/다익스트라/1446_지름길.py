# 31256kb /	44ms
import sys
input = sys.stdin.readline

''''5 150  N D
0 50 10
0 50 20
50 100 10
100 151 10
110 140 90'''

N, D = map(int,input().split())  # N : 지름길의 갯수 D : 고속도로의 길이
shortcut = [0 for _ in range(N)]



for i in range(N):
    shortcut[i] = tuple(map(int,input().split()))   # 0 50 10  0에서 50까지 10 만큼 걸림
shortcut.sort(key = lambda p: (p[0],p[1],p[2]))

dp = [i for i in range(D+1)]

for i in range(D+1):

    if dp[i] > dp[i-1]+1 and i !=0 :
        dp[i] = dp[i-1]+1

    for road in shortcut:
        if i < road[0]:
            break
        if i ==road[0]:
            v,w,dis = road
            if w <= D and v <= D :
                if (dp[w] > dp[v]+dis ):
                    dp[w] = dp[v] +dis
                    

print(dp[D])


