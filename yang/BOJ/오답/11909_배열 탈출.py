# 202688KB / 1036ms (PyPy3)
import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))
MAX_DISTANCE = 222*N*N+1
distance = [[MAX_DISTANCE]*N for _ in range(N)]
distance[0][0] = 0
for i in range(N):
    for j in range(N):
        if i-1>=0:
            d = 0 if array[i][j]<array[i-1][j] else array[i][j]-array[i-1][j]+1
            distance[i][j] = min(distance[i][j], distance[i-1][j]+d)
        if j-1>=0:
            d = 0 if array[i][j]<array[i][j-1] else array[i][j]-array[i][j-1]+1
            distance[i][j] = min(distance[i][j], distance[i][j-1]+d)
print(distance[-1][-1])